---
schema_version: 0.1.0
id: technique/directional-flow-surface
kind: technique
title: 進行方向に流れる侵食Mesh面
summary: 固定MeshのUVと頂点をノイズで変化させ、根元から後方へ流れる炎舌や薄い後流を作る。
status: draft
revision: 2
updated_at: '2026-10-04'
aliases: []
tags:
- technique
- mesh
- fire
scope: engine-neutral
relations:
- target: resource/periodic-density-noise
  type: requires
  reason: 幅の揺れ、穴、頂点変位を独立に制御する。
- target: resource/unit-effect-mesh-kit
  type: requires
  reason: 向きとUVを定義した分割面を用意する。
- target: rendering/emission-and-opacity
  type: requires
  reason: 色面と侵食された輪郭を分けて制御する。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 面の重なり・裏面・奥行きによる消失を確認する。
- target: technique/flipbook-particles
  type: alternative
  reason: 連番画像も同じ炎舌の役割の候補になる。
  role: flame-shell
  when: 限定画角で連番の形と反復が許容でき、体積・変位の費用を減らしたい場合。
- target: adapter/unity-urp-noise-density
  type: implemented_by
  reason: Unity URPでUV流れ、頂点変位、侵食を組み合わせた制作例。
evidence:
- evidence/organic-fire-volume-preview
- evidence/quality-baseline-to-core-only
superseded_by: []
---

# 進行方向に流れる侵食Mesh面

## 面の役割

主形状の外側へ流れる薄い炎舌を置く。Meshは滑らかな変位ができる分割面とし、固定した形をノイズ・UV・色で動かす。面を追加する前に、根元・先端・UVの向き・裏面の描画を決める。

UVの一軸を前方の根元から後方の先端へ割り当てる。サンプリング座標 `uv - velocity * time` の模様はUVの正方向へ動く。オブジェクトの座標軸とUV軸の向きが違う場合もあるため、UVの基準点を実描画で追って符号を確認する。

## ノイズの分担

低周波の値で中心線と頂点をゆっくり変位させ、根元側の変位を抑える。セル距離で炎の大きな幅と裂け目、別周波数で小さい侵食を作る。色面のUVも同じ流れ方向へ動かし、輪郭と模様の運動が矛盾しないようにする。

先端の幅は細くし、根元・先端の透明度で矩形を隠す。輪郭が規則的な三角形のままなら、色の情報量より幅・侵食・変位を見直す。頂点不足による折れは分割数、細かすぎる変位は周波数から比較する。

## 繰り返しの隠し方

同じ素材の位相だけを変えると、同じ輪郭が並ぶ場合がある。長さ・幅・配置角・Seed・侵食・時間の差を役割に沿って組み合わせる。進行方向の周囲へ固定して配置し、意味のないY軸回転を炎の運動にしない。反対側の視点で板が消える、十字に見える、重なりが急に変わることも確認する。

## 動画で残った矩形境界と次の切り分け

実行例では、静止画で目立たない四角い面や、何もない位置から突然炎が現れる辺が動画で指摘された。密度体積の改善を、この面の完成と同一視しない。

面単独を灰色背景で再生し、UV四辺、変位前後、侵食なし/あり、重なりなし/ありを固定Seedで比較する。原因候補はMesh端による切断、侵食の閾値・流れ、変位で浮き出る面、複数面の重なり。現時点で支配的な原因は未確定。

対策候補は、最終alphaへ四辺からの滑らかな距離マスクを掛ける、周囲に未描画の余白を作って変位を端で弱める、侵食の周波数と時間変化を滑らかにする、面の形状や密度体積への置換を比較すること。上下のFadeだけで左右・変位後の境界も隠れると判断しない。対策は未実施で、動画と反対視点の確認前に成功として記録しない。

## 時間と状態

時間は呼び出し側の時計か粒子寿命から渡す。停止・速度変更・再利用の際にUVと粒子だけが別々に進まないかを見る。個体Seedは生成時に固定する。材質の個体複製ではなく、共通Materialと粒子入力で差を出す候補を優先する。

## 根拠と限界

[Unity Adapter](../../adapters/unity-urp-noise-density.md)と[実行記録](../../evidence/organic-fire-volume-preview.md)に少数の実装例がある。全画角・任意のMesh・実機負荷は未確認。軽量代替として[連番粒子](flipbook-particles.md)を比較できるが、自動採用はしない。この技法はdraft。


## 削減時に判明した輪郭と価値

後続の[削減例](../../evidence/quality-baseline-to-core-only.md)では、開始フェードを広げるだけでは三角形の底辺の角が残った。前端の幅を半楕円で立ち上げ、侵食とは別の輪郭マスクで角の再表示を防いだ。その後も主役への寄与が小さく、外炎は削除された。前節の「対策未実施」は品質基準版時点の記録であり、この例の最終採用ではない。

形の問題は輪郭マスク、端の露出は元UVの端マスク、連続運動は参照座標の流れとして切り分ける。完成した層でも合成に不要なら残す理由にはならない。固定した面に1粒子を使う必然性はなく、MeshRendererと外部時間入力を候補にする。
