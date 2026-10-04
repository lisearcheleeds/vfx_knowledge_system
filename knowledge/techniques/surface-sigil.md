---
schema_version: "0.1.0"
id: "technique/surface-sigil"
kind: "technique"
title: "面に沿う輪・扇・記号の展開"
summary: "地面や手元の面に記号を置き、範囲と発動方向を明示する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "resource/effect-mask-atlas"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "resource/unit-effect-mesh-kit"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/ground-footprint"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 面に沿う輪・扇・記号の展開

## 主案
地面の範囲境界は正確な輪/扇、詠唱の手元は小さな収束環にする。地面法線と前方を入力し、扇の中心・角度を実判定と合わせる。装飾の文字や細いルーンより外周の形を優先する。

## 面と時間
境界と塗りを分け、短い発動時は輪郭を先に全体表示する。予兆がゲームにある場合だけ進捗で明度を上げる。発動後は中心から侵食して輪の残留を短くする。

## 実装候補
地面投影を主案にし、機能がない場合は追従メッシュへ置換する。一つの面に両方を重ねない。手元の面は実オブジェクトの姿勢へ追従する。

## 評価
斜面・段差・遠距離、扇の反転、確定していない着弾点への誤表示を確認する。

## 接続する知識

- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [rendering/ground-footprint](../rendering/ground-footprint.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
