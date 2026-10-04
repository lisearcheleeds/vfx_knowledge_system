---
schema_version: 0.1.0
id: technique/volume-density
kind: technique
title: 内部密度で形を作る体積描画
summary: 境界Meshを描く代わりに、内部の密度・吸収・発光を積分し、侵食された炎や煙の塊を作る。
status: draft
revision: 1
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
  reason: 密度の粗密、侵食、座標変位を再現する。
- target: rendering/emission-and-opacity
  type: requires
  reason: 発光と吸収を同時に扱い、暗い煙を加算だけで消さない。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明体積と不透明物・別体積の遮蔽を確認する。
- target: technique/mesh-core
  type: alternative
  reason: 硬い核を伝えたい場合は面の輪郭を持つMeshが適する。
  role: core
  when: 流体の塊より固体・魔法球の外形を優先する場合。
- target: adapter/unity-urp-noise-density
  type: implemented_by
  reason: Unity URPでの密度積分と粒子入力の制作例。
evidence:
- evidence/organic-fire-volume-preview
superseded_by: []
---

# 内部密度で形を作る体積描画

## 採用する理由

「燃えている物体」と「炎そのもの」を区別する。炎の塊に球Meshの連続した外縁が出る場合、表面の柄を増やしても、固体の印象が残る。形状を支えるMeshは描画範囲の境界とし、見える形を内部密度で作る候補を比較する。これは物理的な流体シミュレーションやメタボール計算を必須にする指示ではない。

## 主形状から作る

前方の大きな房、後方へ伸びる房、揺れる小さな先端を柔らかい密度場で重ねる。大きな輪郭が成立した後に、周期ノイズの粗密、座標変位、セル距離による侵食を足す。境界直前で密度を減らし、箱の切断面を露出させない。

進行方向・上方向・後方を明示する。密度の模様は前方から後方へ流し、軸周りの一様回転で代用しない。細部が動いても全体が常に完全な球なら、大きな房の配置・伸長・侵食から見直す。熱い領域は内部密度と色へ統合し、独立した明るい球で硬い輪郭を復活させない。

## 積分と合成

視線と境界の交差区間を取り、手前から奥へ密度をサンプリングする。各区間の不透明度を吸収量から求め、未吸収分に発光色と不透明度を累積する。区間長を式へ含め、サンプル数変更で見え方が大きく変わらないか比較する。

密度を色や透明度と同一視しない。高温の発光、低温の赤、暗い煙を寿命で遷移させる。Premultiplied Alphaを返す場合は対応するBlendを選ぶ。通常alphaや加算との混在では別の積分・合成契約が必要。

## 着弾と煙への展開

複数の房に固定Seed・位置・寸法・速度・寿命の差を与え、一度の解放から膨張、減速、冷却へつなぐ。毎フレーム新しい乱数を引かない。密度場を共用しても、飛翔・射出・着弾・煙の時間と熱履歴は役割ごとに持つ。

## 限界と削減

費用は画面上の面積×積分サンプル数×体積の重なりに依存する。大きな粒子を増やすだけで高品質・高速になると判断しない。品質基準ができた後にサンプル数・房数・解像度・表示距離を一つずつ比較する。軽量化で必要な輪郭まで失う場合は、別技法も比較する。

[面の核](mesh-core.md)は固体形状の代替候補。[Unity Adapter](../../adapters/unity-urp-noise-density.md)の現在の例は透視投影・粒子回転なしの条件で試作しており、遮蔽・拡縮・密集時の保証はない。

## 根拠と状態

[実行記録](../../evidence/organic-fire-volume-preview.md)は少数のPreviewでの見た目と撮影結果を扱う。内部構造・実ゲーム接続・性能の合格を意味せず、この技法はdraft。
