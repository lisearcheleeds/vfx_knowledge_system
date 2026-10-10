---
schema_version: 0.1.0
id: technique/ignition-burst
kind: technique
title: 着火・炎の命中は、全方位へ一瞬広がってから上へ昇る
summary: 炎が当たる・燃え上がる瞬間は、最初から上へ向かわせず、全方位へ一瞬だけ広がってすぐ止まり、その後に熱で上へ昇らせる。コンロに着火した時の「ボッ」の動き。
status: draft
revision: 1
updated_at: '2026-10-10'
aliases:
- 着火
- 熱接触
- 燃え上がり
- ボッ
tags:
- fire
- combat
- technique
scope: engine-neutral
relations:
- target: recipe/impact-fire-contact
  type: enhances
  reason: 炎の命中の炎の動き方。
evidence:
- evidence/skill-baselines-preview
superseded_by: []
---

# 着火・炎の命中は、全方位へ一瞬広がってから上へ昇る

## 何を伝えるか

炎は燃え広がる瞬間に一度全方向へ膨らみ、その後に熱で上へ流れる。最初から上へだけ向かう炎は、燃え上がる焚き火や上向きの噴射に見え、当たった瞬間の破裂感が出ない。

## 作り方

- 炎の粒を接触点から全方向へ速く出し、強い抵抗ですぐ止める。その後は浮力（上向きの力）で昇らせる。
- 炎は炎の形を描いた板にしない。柔らかい丸を動きの向きに引き伸ばす（形の板は小さな三角の記号に見える）。
- 火の粉は外へ弾けてから上へ漂わせる。煙は遅れて薄く昇らせる。

## 確認

接触の直後の数フレームで、炎が全方向へ開いているか、その後に上へ流れが変わるかを見る。
