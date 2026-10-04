---
schema_version: "0.1.0"
id: "technique/radial-wave"
kind: "technique"
title: "接地した膨張環と圧縮波"
summary: "薄い環状メッシュで衝撃の伝播を見せ、実範囲境界と分離する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "resource/unit-effect-mesh-kit"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/uv-dissolve"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/world-depth-and-transparency"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 接地した膨張環と圧縮波

## 主案
薄い環を接触点・接地点の法線へ置き、半径と帯幅を別々に変化させる。中心の圧縮から速く外へ解放し、末尾は侵食する。正確な攻撃範囲は別の固定境界を使う。

## 時間・空間
単発範囲攻撃では全体の有効範囲を発動時に示し、膨張環を遅いダメージ波として扱わない。壁・斜面を貫く完全な輪は、接地可能な面に限って表示する。

## 弱点・削減
厚い白い輪は他Actorを遮る。高さ・発光・透明面積を抑え、輪の先頭を読みやすくする。軽量化では補助の二重輪を省き、主波一枚を保つ。

## 評価
実範囲との区別、中心の破綻、地面交差、残留時間を確認する。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [technique/uv-dissolve](uv-dissolve.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
