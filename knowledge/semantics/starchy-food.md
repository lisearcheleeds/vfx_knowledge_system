---
schema_version: "0.1.0"
id: "semantic/starchy-food"
kind: "semantic"
title: "芋・でんぷん質の食事"
summary: "丸みのある淡い光点で素朴なでんぷん質の摂取を表す。"
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

# 芋・でんぷん質の食事

## 視覚的な意味

芋等の素朴な食事。主案は淡い暖白の丸点二個が低く上昇してまとまる形。実物の調理法が未指定でも使用できる。揚げた衣、穀粒、湯気は調理・形状が確認できた場合に別レシピから選び、未知の食品形状を決めつけない。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/food-consumption](food-consumption.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
