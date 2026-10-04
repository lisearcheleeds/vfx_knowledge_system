---
schema_version: "0.1.0"
id: "semantic/beverage"
kind: "semantic"
title: "飲料・飲用"
summary: "滴や泡の短い抜けで、飲用の成立と口当たりを表す。"
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

# 飲料・飲用

## 視覚的な意味

飲料の摂取表現。透明感のある滴、泡の小さな上昇、口元から身体へ寄る収束を使う。泡のある飲料ではクリームの丸点を三個、琥珀の小弧を主案にする。泡・色は飲料の見た目に対応し、アルコール、酩酊、MP回復の意味を自動で付けない。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/food-consumption](food-consumption.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
