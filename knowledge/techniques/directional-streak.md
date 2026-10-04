---
schema_version: "0.1.0"
id: "technique/directional-streak"
kind: "technique"
title: "攻撃軸の針と短い放射筋"
summary: "細長いメッシュで突きの前進と命中の方向を保持する。"
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
  - target: "resource/effect-mask-atlas"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/uv-dissolve"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 攻撃軸の針と短い放射筋

## 主案
先細りの針メッシュと少数の細い筋を攻撃ベクトルに揃える。突きの線は根元から伸ばし、接触後は先端側から短く侵食する。命中の筋は法線方向に出し、全方向の丸い爆発にしない。

## 形
核の一本を最も太くし、補助筋は幅と明度を下げる。攻撃が短ければ針も短くする。入力の物理長さとActor幅を分け、画面サイズだけで武器射程を延長しない。

## 時間・弱点
20〜40msの立上り、80〜160msの残留を制作基準にする。細い線が遠距離で消える場合は芯の幅と短い接触ピークで補う。白い線を重ねて一本の塊にしない。

## 検証
前・横・斜めから方向が読めるか、移動Actorへ追従しすぎないかを確認する。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [technique/uv-dissolve](uv-dissolve.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
