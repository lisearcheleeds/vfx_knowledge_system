---
schema_version: "0.1.0"
id: "semantic/crispy-food"
kind: "semantic"
title: "衣・乾いた食感のある食品"
summary: "短い角片で軽い歯触りを見せ、身体側の演出へ素早く引き継ぐ。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["semantic","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/prepared-food"
    type: "candidate"
    reason: "上位の摂取表現として参照する。分類の関係であり、ゲーム効果の必須依存ではない。"
evidence: []
superseded_by: []
---

# 衣・乾いた食感のある食品

## 視覚的な意味

衣、揚げ物、焼いた乾いた表面の摂取表現。小さな暖金の角片を四個、一度だけ弾いて消す。大きな破砕や大量の食べこぼしを避ける。焼成・揚げの有無は実食品の指定に従い、曖昧な芋の品目を一律に揚げ物へ分類しない。

## 採用時の境界

食材の分類は形・質感を選ぶ判断材料。ゲーム効果、適用対象、効果量、期間を決める根拠にしない。

## 接続する知識

- [semantic/prepared-food](prepared-food.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
