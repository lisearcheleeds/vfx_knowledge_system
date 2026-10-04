---
schema_version: "0.1.0"
id: "semantic/protein-food"
kind: "semantic"
title: "肉・魚・卵等の食材"
summary: "食材の柔らかな栄養感を、少数の丸い光点や短い暖色の上昇で示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["semantic","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/food-consumption"
    type: "candidate"
    reason: "上位の摂取表現として参照する。分類の関係であり、ゲーム効果の必須依存ではない。"
evidence: []
superseded_by: []
---

# 肉・魚・卵等の食材

## 視覚的な意味

肉、魚、卵等の食材の摂取。柔らかい白黄の丸点、暖白の短い上昇、淡い銀の欠片から、画面で食品の輪郭を読む一つを選ぶ。血や生々しい脂の散乱を標準にせず、回復や副作用は採用先の効果指定に従う。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/food-consumption](food-consumption.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
