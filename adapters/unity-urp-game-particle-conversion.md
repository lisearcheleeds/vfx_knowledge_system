---
schema_version: 0.1.0
id: adapter/unity-urp-game-particle-conversion
kind: adapter
title: Unity URP：基準版の帯と粒子を共有素材の粒子へ変換するときのエンジンの事実
summary: 最高品質の基準版（帯のMeshRendererと粒子）を、共有素材2つの粒子だけで描くゲーム用版へ機械的に変換したときに確かめた、ParticleSystemのメッシュ粒子・頂点ストリーム・Texture Sheet Animation・トレイルの挙動と、その回避。
status: draft
revision: 2
updated_at: '2026-10-10'
aliases:
- ゲーム用変換
- Custom Vertex Streams
- メッシュ粒子
tags:
- mesh
- billboard
scope: engine-specific
relations:
- target: rendering/lightweight-vfx-catalog
  type: enhances
  reason: カタログの技法（LW-C3・D1・D2・F2・F5）をUnityの粒子で実装するときの前提。
- target: adapter/unity-urp-baseline-sheet-particles
  type: enhances
  reason: 変換元の基準版の構成。
evidence:
- evidence/game-effect-conversion-preview
superseded_by: []
engine: unity
compatibility:
  engine_version: 6000.3.14f1
  renderer: URP 17.3.0
  platforms:
  - Windows Editor
  verification: engine-tested
---

# Unity URP：基準版の帯と粒子を共有素材の粒子へ変換するときのエンジンの事実

## 実行範囲

Unity 6000.3.14f1 / URP 17.3.0 / Windows Editor の専用Prefab Previewで実描画して確かめた。対象機種での性能は未計測。

## 確かめた事実と回避

| 事実 | 症状 | 回避 |
| --- | --- | --- |
| メッシュ粒子の頂点色は8bitとして読まれる | floatのColorで保存したメッシュの色がずれる | メッシュの頂点色は Color32 で保存する |
| 粒子の頂点ストリームの UV2 はフリップブックの次のコマのUVで、メッシュのUV2ではない | メッシュのUV2に詰めた値が届かない | 層ごとの値はメッシュのUVやCustom Dataに詰める |
| メッシュ粒子の法線は変換で正規化される（値を10倍しても見た目が同じ） | 法線に詰めた縮尺・強さが失われ、ノイズが極端に粗くなる | 法線を値の運搬に使わない。UVの整数部に層ごとの定数を、小数部（×0.998）に位置を詰め、シェーダで floor と小数部に分ける |
| スクリプトの Texture Sheet Animation の startFrame は全コマに対する比（0〜1） | コマ番号を入れると別のタイル（多くは最後のコマ）になる | (コマ番号＋0.5)／コマ数 を入れる |
| メッシュ粒子のUVには Texture Sheet Animation のタイルが効かない（アトラス全体を引く） | 立体の粒子が薄く、別のタイルの断片が出る | メッシュのUVをタイルの範囲へ焼き直し、Texture Sheet Animation を切る |
| メッシュ粒子は毎フレームCPUで頂点を展開する | 細かい格子のメッシュ（数千三角形）を粒子にすると、同時数に比例して重い | 長さ・周の格子を間引く（見た目が変わらない範囲で1/3・1/2） |
| 半透明の立体メッシュ粒子は、基準版が両面で描いていると表と裏が重なって濃く見える | 片面で描くと薄く見える | 基準版に合わせて Cull Off。ビルボードは常に表を向くので費用は変わらない |
| トレイルの寿命は粒子の寿命に対する比 | 寿命の長い本体に秒で入れると、尾が何十メートルにもなる | 尾の秒数／本体の寿命 を入れる |
| トレイルにはCustom Dataが渡らない | 発光の倍率・加算の割合を粒子ごとに渡せない | トレイルは別素材にし、明るさは色と不透明度で作る |
| Velocity over Lifetime の x・y・z の曲線のモードが違うと動かない | 一部の軸の動きが消える | 3軸のモードをそろえる |
| 大きな粒子は既定で画面の半分に制限される | 大きな面が途中で止まる | ParticleSystemRenderer の maxParticleSize を上げる |
| 焼き込みで時刻ごとに `Simulate(t, restart=true)` し直すと、Shape の Arc を Loop で回す発生位置などが模擬の刻みに依存し、同じ粒でも時刻ごとに出る位置が変わって軌跡が飛ぶ | 焼いた粒の位置・向きが元と合わない | 0 秒から一度だけ始め、小さな刻み（1/120 秒以下）で順に進めながら記録する。比較する元の Preview も同じ順進めにそろえる |
| 縦のビルボード（VerticalBillboard）は世界の上を保ったまま**カメラの位置**の方を向き（カメラの面ではない）、回転は**板の面の中**（板の法線が軸）。rotation が正のとき u の辺が下がる | 焼き込みの Shader で、カメラの右を水平に倒した向きや、カメラの前を軸の回転を使うと傾きが合わない | 右＝カメラの位置への水平な向きと上の外積、回転は右と上の 2 軸の面内で行う |
| ParticleSystem は系 1 つごとに更新と頂点の生成の固定費がある（100 個・65 種の同時再生で主スレッド約 26 ms 増。粒を減らしても系の数が同じなら時間がほぼ変わらない） | 粒・画素を減らしても軽くならない | 多用する演出は焼き込みのインスタンス描画にする（カタログ LW-D8）。メッシュ粒子に VAT を載せても頂点の生成の固定費は残るので、系をやめて MeshRenderer／インスタンス描画で描く |
| 粒子の色（GetCurrentColor）は sRGB の 8bit。線形の色空間では Shader に届く前に線形へ変換される | 焼いた色が白っぽくなる | 焼くときに線形へ変換して記録する |
| 再生基盤・Previewはルートの ParticleSystem を起点に進める | 帯だけの基準版を変換するとルートに系が無く再生されない | 発生しない空の系をルートに足し、子の系の duration をそろえる |

## 限界

startFrame が比であること・メッシュ粒子にタイルが効かないことは、このバージョンでの観察で、公式文書では確認していない。
