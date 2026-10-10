---
schema_version: 0.1.0
id: recipe/metal-contact-sparks
kind: recipe
title: 金属の接触火花と一瞬の閃き
summary: 接触点から一方向へ数本の伸びた火花を短く飛ばし、白い閃きを添える命中演出。斬撃・打撃・刺突のContactに汎用で使える。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases:
- 接触火花
- contact sparks
- ヒットの火花
- 金属の火花
tags:
- recipe
- combat
- melee
scope: engine-neutral
relations:
- target: technique/particle-emission
  type: composes
  requirement: required
  role: sparks
  reason: 少数の伸びた粒子を一方向の円錐へ短く飛ばす。
- target: technique/billboard
  type: composes
  requirement: optional
  role: glint
  reason: 接触の瞬間の小さな星形の閃き。
- target: semantic/slash
  type: expresses
  reason: 刃が金属・硬い物に当たった手応え。
- target: evaluation/combat-shape-and-events
  type: evaluated_by
  reason: 実命中の位置・方向・回数で確認する。
evidence:
- evidence/sword-slash-analytic-crescent-preview
superseded_by: []
---

# 金属の接触火花と一瞬の閃き

## 位置づけ

斬撃の残像の一部として作り、残像の中では「何の火花か分からない」と評価された。一方で、命中の演出として見ると非常に良いとユーザーが評価した（ヒットエフェクトとして98点）。**接触点・攻撃方向が分かっている命中（Contact）の演出として使う。** 攻撃の残像・振り・範囲表示に混ぜない（命中していない位置に目標がいるように読める）。

## 構成

| 役割 | 形と運動 | 時間 |
| --- | --- | --- |
| 火花 | 伸びた（Stretched）粒子 8〜10個。接触点から攻撃の接線と外向きの間の一方向へ、開き角20度前後の円錐で飛ばす。初速は速くばらつかせ（例 4〜9 m/s）、強い減速（drag）で急に止める。少し重力を掛ける | 開始は接触の直後（0.01秒）。寿命0.09〜0.17秒の短いばらつき |
| 色 | 白に近い淡黄 → 橙 → 赤橙へ冷める。alphaは後半で落とす。加算 | 寿命の中で冷める |
| 大きさ | 細い（0.035〜0.06m）。速度で伸ばし（速度倍率の伸び）、寿命の終わりに0.3倍まで細る | 速度の減少と一緒に短くなる |
| 閃き（任意） | 接触点に十字＋斜めの弱い光条の星形を1つ。大きさは小さく、最初の1/4で最大 | 0.02秒から約0.07秒 |

## なぜ良く見えるか（観察）

- 本数が少なく、一方向にまとまっているので、方向と勢いが読める（丸い爆発にならない）。
- 速い初速と強い減速で「弾けて止まる」運動になり、金属の硬さが出る。
- 速度で伸ばした細い線が冷めながら短くなるので、熱い金属片らしく見える。

## 採用時の入力

接触点、攻撃方向（または接線）、接触面の外向き。実際のhit-confirmedだけで発生させ、振りの時刻から推定しない。複数対象に当たったら接触点ごとに小さく出す。

## 限界

斬撃の基準版の中で作り、単独の命中演出としての実ゲーム接続・連打・複数対象・明るい背景は未確認。数値は一つの制作例の値で、普遍値ではない。
