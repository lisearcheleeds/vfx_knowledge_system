---
schema_version: 0.1.0
id: adapter/unity-urp-noise-density
kind: adapter
title: Unity URP：粒子の密度体積・方向流れ・煙
summary: ParticleSystemの個体入力と共有ノイズで、密度体積、侵食Mesh面、熱から煙へ変わる尾を作るPreview実装例。
status: draft
revision: 2
updated_at: '2026-10-04'
aliases: []
tags:
- rendering
- mesh
- fire
scope: engine-specific
relations:
- target: resource/periodic-density-noise
  type: requires
  reason: 体積と面で共用する周期ノイズを用意する。
- target: rendering/emission-and-opacity
  type: requires
  reason: 体積と面の異なるalpha方式を守る。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 通常透明Queueと奥行き設定の適用範囲を確認する。
- target: technique/surface-density-core
  type: candidate
  reason: 面上密度の固定Mesh描画を実行した候補。
  role: core
- target: technique/folded-axial-billboard
  type: candidate
  reason: 進行軸と支点UVを使う向きの候補。
  role: orientation
evidence:
- evidence/organic-fire-volume-preview
- evidence/quality-baseline-to-core-only
superseded_by: []
engine: unity
compatibility:
  engine_version: 6000.3.14f1
  renderer: URP 17.3.0 / DX12
  platforms:
  - Windows Editor
  verification: engine-tested
---


# Unity URP：粒子の密度体積・方向流れ・煙

## 実行した範囲

Unity 6000.3.14f1 / URP 17.3.0 / Windows Editor / DX12で、隔離PreviewSceneのParticleSystemを手動Simulateして撮影した。`engine-tested`はこの条件での実描画を示す。Adapter全体はdraft。完成ゲーム・他API・Webビルド・GPU予算・コード構造の独立レビューは未確認。

## 共用するネイティブ素材

- Texture3D：周期的なRの3段Value noise、GのWorley/Voronoi距離、Bの低周波変位、Aの定数を線形UNormで保存する。試作はRGBA32、Repeat、Bilinear、Mipなし。寸法と周波数は制作記録の採用値を参照する。
- 体積Mesh：中心原点の単位Cube、座標±0.5、外向き三角形。Meshの面は炎の外形にしない。
- 流れ面：根元→先端のUVを持つ分割Mesh。法線と必要な頂点を用意する。
- Material：高温、冷却する爆発、低温煙、短い射出の共有プリセット。粒子ごとに複製せず、Seed・寿命・サイズは粒子入力へ置く。今回GPU Instancingは使用していない。

## ParticleSystemから体積座標を復元する

体積RendererをMesh、alignmentをLocalにする。この実装例では粒子の3D回転を無効にし、姿勢はPrefabで与える。Custom1.xを0→1の寿命曲線、Custom1.yを生成時の固定乱数にする。

`SetActiveVertexStreams`の順序とShaderの入力をセットで保存する。

| Stream順 | Shaderの受け取り |
| --- | --- |
| Position | POSITION |
| Color | COLOR |
| UV → Custom1XY | TEXCOORD0.xy=UV、zw=寿命進捗/Seed |
| Center → SizeXYZ | TEXCOORD1.xyz=world-space Center、w=Size.x、TEXCOORD2.xy=Size.yz |

Centerはworld-spaceである。これを`TransformWorldToObject`し、Mesh頂点とカメラ位置から粒子中心を引き、現在Size.xyzで割って単位Cube内の座標を得る。CustomDataを足しただけでは入力が合わないので、Stream順、生成したMesh、実際のShader入力を確認する。

## 密度・熱・吸収のShader

URP Core.hlslとTexture3Dを使う。透視カメラからCubeへ視線を通し、slab法で入口・出口を取り、手前から奥へ一定区間で積分する。初稿は複数の柔らかい房に座標の歪みと2周波数の侵食を加えた。Cube端で密度を減らす。

`alpha = 1 - exp(-density * stepLength * absorptionScale)`とし、累積RGBとalphaに`1 - accumulatedAlpha`を掛けて加える。RGBはalphaを掛けた値として返す。`Blend One OneMinusSrcAlpha`、`ZWrite Off`、`ZTest LEqual`、`Cull Front`、通常のTransparent Queueを使用した。これは不透明物との交差が完全に解決したという保証ではない。

前方をローカル+Zとした体積では、`samplePosition.z + time * flowSpeed`で可視模様が-Zへ流れる。熱い房と後方の房をずらして伸長し、Noiseで輪郭を崩す。熱履歴は初期熱と寿命冷却で制御し、淡黄→橙→赤→暗い煙へ変える。独立した球形の熱核で外形を上書きしない。

## 流れ面のShader

面用のStreamはPosition / Normal / Color / UV / Custom1XY。TEXCOORD0.zwに寿命とSeedを渡す。UV.y=0の前方から1の後方へ伸ばした面では、`uv.y - time * flowSpeed`が後方へ模様を流す。法線方向の低周波変位をUV.yで増やす。

幅の揺れ、セル距離の侵食、先細り、色面のUV変位を分ける。面の角度・長さ・Seedを変える。面は`Cull Off`、通常alphaの`Blend SrcAlpha OneMinusSrcAlpha`とし、体積Shaderのpremultiplied出力をそのまま流用しない。

## 尾と煙の連続性

native Trailsはworld-spaceの履歴を残し、幅を先細りに、色を黄橙→橙→赤→暗い煙色へ変える。ParticleSystem TrailsのLifetimeは粒子寿命への倍率として扱い、必要履歴秒数/粒子寿命を設定する。尾長の目安は移動速度×履歴秒数。停止時に粒子を消す場合はTrail残留との関係も確認する。

World-spaceの体積粒子を後方へ発生させ、成長・漂流・冷却を加える。粒子の発生間隔による距離は`speed / emissionRate`。見える房の幅がこの距離を覆うかを動画で見る。Meshの箱寸法ではなく、侵食後の実際の密度領域を基準にする。疎な高温粒子は光る点列になるため、発生密度・初期サイズ・初期熱を一緒に比較する。

## 時間・終了・Preview

Shaderは`_Time`を読まず、粒子進捗とMaterialのCycleSecondsから時間を得る。これは制作時の手動Simulateに同期する方法。寿命をランダム化した粒子ではCycleSecondsが実寿命と一致しない場合があり、正確な秒同期が必要なら実寿命も渡す経路を別途設計する。製品のゲーム時計接続は未実装。

Previewは隔離SceneとPreviewRenderUtilityで実粒子をSimulateし、移動を小刻みに進めて履歴を残す。射出・飛翔・着弾は別の区間と撮影時刻を持ち、単一の共通尺へ揃えない。明暗背景と複数視点で静止画・動画を撮り、開始・ピーク・膨張・冷却・消失を確認する。

Clear後の再生で粒子数と初期見た目を比較する。ただしPreviewのClear確認は製品Poolの再利用やimpact停止契約の確認を代替しない。核・外炎の終了、煙・Trailの残留、teleportの切断、階層切替復元は統合側で検証する。

## 保存と再現

Unity起動中のnativeアセットはUnity Editor APIで生成・変更する。今回のPrefab更新はアセット本体の変更→SavePrefabAsset→SaveAssets→ForceUpdateで保存し、git差分とディスク上の参照も確認した。一時生成コードは実行後に削除し、生成条件と決定的なSeedを記録へ残した。未保存編集がある間は再インポートやcompileを実行しない。

## 既知の適用制限・次の検証

- 粒子単位の回転を復元していない。回転を有効にするには座標変換の実装・再撮影が必要。
- カメラ原点を使う透視投影の実装。正射影、非単位親Scale、カメラが体積内にあるケースは未確認。
- Scene Depthを参照せず、Cube裏面のZTestを使っている。不透明物との交差・複数体積の並べ替えは実ゲームで要確認。
- 密度64ステップと重なる煙は品質基準版の費用。性能測定、密集試験、圧縮・Mip・サンプル削減は未実施。
- 汎用化・Shader/Materialの責務・ハードコードされた熱色や房の構成・内部構造の独立レビューは未実施。

## 根拠

[実行記録](../evidence/organic-fire-volume-preview.md)に実装版、撮影条件、観察、未実施項目を保存した。見た目の成功を他条件の保証へ拡張しない。


## 品質基準版から固定Meshへの変換

上記の体積・粒子構成は品質基準版の実行例。後続では[面上密度](../knowledge/techniques/surface-density-core.md)と[折り曲げ式ビルボード](../knowledge/techniques/folded-axial-billboard.md)を実装し、飛翔をCoreだけへ削減した。射出・着弾の体積粒子は維持した。

固定描画にはMeshFilter/MeshRendererを使い、MaterialPropertyBlockへ経過秒・固定Seed・Tintを渡す。実装側のWorldEffectMeshViewは入力を受けるだけで、自身のUpdate時計を持たない。Editor Previewが粒子とMeshへ同じ経過時間を渡し、粒子なしでもSeekと再生を行う。単にSceneへ配置してPlayした場合は時間の接続がなく、UVは動かない。ゲーム側時計の接続は未実施。

折り曲げMeshはUV0に描画UV、UV2に支点のlocal長さ座標と外端フラグを持たせる。ShaderのTEXCOORD1へ読み、進行軸・カメラ方向・支点から各頂点を配置する。GetWorldSpaceNormalizeViewDirで透視と平行投影を区別し、軸と視線の一致には基準方向を設ける。Boundsには変形後の範囲を入れる。

UnityEngine.Objectの欠損・破棄判定はUnityのnull比較で行う。欠損ParticleSystemにC#のnull条件演算子を使うと実行時にアクセスする例を検出し、明示的な判定へ修正した。共有MaterialとPropertyBlockで個体入力を渡しても、SRP Batcher成立やGPU費用の低減を保証しない。

[実行Evidence](../evidence/quality-baseline-to-core-only.md)ではRenderer1・ParticleSystem0、時計・シーク、透視/平行投影、既存粒子Previewを確認。ゲームへの接続・製品実機・密集負荷は未測定。
