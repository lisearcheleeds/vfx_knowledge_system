---
schema_version: 0.1.0
id: technique/blunt-motion-smear
kind: technique
title: 打撃部の幅だけのぼけた振りの帯
summary: 鋭くない打撃武器（棒）の振りを、打撃部が通った幅だけの、縁の無いぼけた帯と振り方向の平行な筋で見せる。衝突は入れない。
status: draft
revision: 1
updated_at: '2026-10-07'
aliases:
- 棒
- 打撃
- モーションブラー
- ぶれ
- smear
tags:
- combat
- melee
- technique
scope: engine-neutral
relations:
- target: rendering/emission-and-opacity
  type: requires
  reason: 縁の無い半透明の帯の明度。
- target: adapter/unity-urp-baseline-sheet-particles
  type: implemented_by
  reason: Unityで実行した実装。
evidence:
- evidence/melee-weapon-free-design-preview
superseded_by: []
---

# 打撃部の幅だけのぼけた振りの帯

## 伝えること

鋭くない、もっとも単純な打撃の振り。

## 形

- **帯の幅は打撃部（攻撃部位）の大きさに合わせる**。棒は先端の打撃部が小さいので、振りの扇全体ではなく、先端が通った外側の半分ほどの幅にする（全幅だと面で打つ武器に見える）。
- 縁を作らず、内外とも柔らかく透明へ落とす（円柱が速く動いたぶれ）。
- 振り方向に平行な細い筋を流し、動きのぶれを出す。
- 消えるときも焼けた縁を作らず、煙のように薄れる。

## 入れないもの

振り終わりの衝撃の輪や土煙。衝突は命中の演出（Contact）の仕事で、振りの残像に入れると何を表すのか分からなくなる。

## 限界

一つの例（版1は75点。幅と衝突の要素を直した版は評価待ち）。
