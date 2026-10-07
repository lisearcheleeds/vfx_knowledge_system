---
schema_version: 0.1.0
id: technique/fan-rib-reveal
kind: technique
title: 骨が開く扇と完成した外側の弧
summary: 扇で斬りつける攻撃を、濃い骨と薄い面の扇が片側から開く形で見せ、判定済みを表す完成した弧の線と、弧に沿って流れる筋を添える。
status: draft
revision: 1
updated_at: '2026-10-07'
aliases:
- 鉄扇
- 扇
- 開く
- fan
tags:
- combat
- melee
- technique
- mesh
scope: engine-neutral
relations:
- target: rendering/emission-and-opacity
  type: requires
  reason: 骨の明るさと面の薄さの配分。
- target: technique/completed-arc-afterimage
  type: enhances
  reason: 外側の弧の線は、判定後の完成した残像の考え方。
- target: adapter/unity-urp-baseline-sheet-particles
  type: implemented_by
  reason: Unityで実行した実装。
evidence:
- evidence/melee-weapon-free-design-preview
superseded_by: []
---

# 骨が開く扇と完成した外側の弧

## 伝えること

扇という武器（濃い骨と薄い面）と、その縁で斬りつけた向き。

## 構成

1. **扇**: 扇形の面に、等間隔の濃い骨の線と、骨の間の薄い面。片側から短い時間（例 0.06秒）で扇形に開く。外縁に明部。骨が濃いことが扇らしさを作る（評価85点）。
2. **完成した弧の線**: 再生開始の時点でダメージ判定は済んでいる。扇を開くアニメーションにするなら、**扇の外縁に沿った弧の線を最初から完成した形で**置き、斬った弧を先に示す。振り終わり側を太く。
3. **流れる筋**: 粒子を使うなら、**斬りつける向き（振り始め → 振り終わり）に扇の弧に沿って曲がって流れる**筋にする（公転の速度で曲げる）。

## 入れないもの

扇の縁から前へ飛ぶ風の筋。斬りつける武器で先端から何かが飛ぶと、別の武器（飛び道具・扇の風の術）に見える。

## 限界

一つの例。骨の本数・開く速さは採用先の扇の造形に合わせる。
