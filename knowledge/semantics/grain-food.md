---
schema_version: "0.1.0"
id: "semantic/grain-food"
kind: "semantic"
title: "米・穀物の食事"
summary: "小さな長円の穀粒の束で、米・穀物の摂取を表す。"
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

# 米・穀物の食事

## 視覚的な意味

米、麦、穀物の粒を使った食事の概念。主案は象牙白の長円三粒が上昇し、胸へ一束で収束する形。粒が見える食事に向き、パンや粥では形状を粉・湯気へ調整する。米の分類からHP回復・攻撃強化を必須にしない。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/food-consumption](food-consumption.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
