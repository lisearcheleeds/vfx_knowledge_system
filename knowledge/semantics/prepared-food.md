---
schema_version: "0.1.0"
id: "semantic/prepared-food"
kind: "semantic"
title: "料理・調理された食事"
summary: "調理の温かさとまとまりを、低い湯気と暖色の小さな上昇で表す。"
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

# 料理・調理された食事

## 視覚的な意味

料理、焼き物、温かい汁物の摂取表現。白い低い湯気と小さな暖金の点を主案にする。冷たい料理では湯気を外し、丸い点のまとまりへ差し替える。料理であることと回復・能力強化の有無は分離する。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/food-consumption](food-consumption.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
