---
schema_version: 0.1.0
id: technique/crumbling-heavy-wedge
kind: technique
title: 焼けた縁から崩れ落ちる重いくさび
summary: 振り終わりへ向かって厚く重くなるくさびの面を、荒れた外縁と焼けた縁を残す溶解で崩して消す。重く叩き割る武器（斧）の残像。
status: draft
revision: 1
updated_at: '2026-10-07'
aliases:
- 斧
- 叩き割る
- 重いくさび
- 崩れる残像
tags:
- combat
- melee
- technique
- mesh
scope: engine-neutral
relations:
- target: rendering/emission-and-opacity
  type: requires
  reason: 焼けた縁の発光と面の不透明度の配分。
- target: technique/uv-dissolve
  type: enhances
  reason: 崩れて消える溶解の一般形。
- target: adapter/unity-urp-baseline-sheet-particles
  type: implemented_by
  reason: Unityで実行した実装。
evidence:
- evidence/melee-weapon-free-design-preview
superseded_by: []
---

# 焼けた縁から崩れ落ちる重いくさび

## 伝えること

鋭さではなく、重さと叩き割る力。刃が大きく、研ぎ澄まされていない。

## 形

- 弧の帯の面で、厚みを振り始めの約半分から振り終わりでほぼ全幅へ増やす（くさび）。三日月のように両端を尖らせない。
- 外縁を弧に沿ってわずかにがたつかせる（研いでいない刃の荒れ）。
- 色は熱い橙の外縁から暗い赤褐色の内側へ。内側を暗く不透明に残すと重く見える。
- **端は少しでもグラデーションで落とす**。振り終わりの辺が1→0で切れていると途切れて見える（弧の1割ほど）。

## 時間

立上りの直後から、ノイズの溶解で崩し始める。振り始め側と内側を先に消す偏りを付け、境界に焼けた明るい縁を残す。全体は剣より長め。

## 補助

土埃は振り終わり側の低い位置にだけ少し。弧全体に多く出すと主役を覆う。

## 限界

一つの例（評価80点）。色・厚みの値は採用先の美術で調整する。
