---
schema_version: 0.1.0
id: recipe/melee-weapon-afterimages
kind: recipe
title: 近接武器の残像：武器から推測して技法を選ぶ入口
summary: 近接攻撃の残像を作る前に、武器の攻撃部位・鋭さ・重さ・動き方を推測し、それに合う技法を選ぶ。既存の別の武器のレシピを出発点にしない。
status: draft
revision: 1
updated_at: '2026-10-07'
aliases:
- 近接武器
- 通常攻撃の残像
- 武器から推測
- melee afterimage
tags:
- recipe
- combat
- melee
scope: engine-neutral
relations:
- target: composition/melee-strike
  type: composes
  requirement: required
  role: lifecycle
  reason: 残像と命中（Contact）の役割の分担と、発火時点の契約。
- target: recipe/completed-slash-afterimage
  type: candidate
  reason: 研いだ刃で斬る武器（剣・短剣・大剣）。
- target: technique/crumbling-heavy-wedge
  type: candidate
  reason: 重く叩き割る武器（斧）。
- target: technique/rotating-sweep-trails
  type: candidate
  reason: 回転して周りを薙ぎ払う武器（大鎌・回転斬り）。
- target: technique/fan-rib-reveal
  type: candidate
  reason: 開いて縁で斬る武器（鉄扇）。
- target: technique/blunt-motion-smear
  type: candidate
  reason: 鋭くない打撃の武器（棒）。
- target: evaluation/combat-shape-and-events
  type: evaluated_by
  reason: 形・向き・発火時点を確かめる。
evidence:
- evidence/melee-weapon-free-design-preview
superseded_by: []
---

# 近接武器の残像：武器から推測して技法を選ぶ入口

## 最初にすること

**別の武器のレシピ（特に剣の三日月）を出発点にしない。** 剣の作り方を土台に他の武器を作ると、すべてが剣の変形に見える（斧・大鎌・鉄扇・棒を剣の三日月から作った版は「Swordに引っ張られすぎ」と評価された。武器から一から考えた版は75〜90点）。

エフェクト名と武器から、次の問いに答えてから技法を選ぶ。

| 問い | 何を決めるか |
| --- | --- |
| 攻撃部位はどこで、どれくらいの大きさか | 帯の幅・位置（棒は先端の小さい打撃部だけ、斧は大きい刃） |
| 研いだ刃か、鈍いか | 細い明部と尖った端（鋭い）か、厚い端・ぼけ・崩れ（鈍い・重い）か |
| 重さ・速さ | 尺、太い部分を保つ時間、崩れ方 |
| どう動くか | 一方向の振り／回転／開く／突く。回転は範囲と回る向き、開くは開く動き |
| 何が「その武器らしさ」か | 扇の骨、斧の荒れた刃、鎌の円など、形の手がかり |

## 武器と技法の例

| 武器 | 推測した性格 | 技法 |
| --- | --- | --- |
| 剣・短剣・大剣 | 研いだ刃で斬る | `recipe/completed-slash-afterimage`（因子の表） |
| 斧 | 大きく鈍い刃・重く叩き割る | [焼けた縁から崩れ落ちる重いくさび](../../techniques/crumbling-heavy-wedge.md) |
| 大鎌 | 一回転して周りを刈る | [範囲の円盤と順番に回る刃の軌跡](../../techniques/rotating-sweep-trails.md) |
| 鉄扇 | 開いて縁で斬る | [骨が開く扇と完成した外側の弧](../../techniques/fan-rib-reveal.md) |
| 棒 | 小さい打撃部・鋭くない | [打撃部の幅だけのぼけた振りの帯](../../techniques/blunt-motion-smear.md) |

## 共通の規則

- 残像の再生開始の時点で、ダメージ判定は済んでいる。開く・回る等のアニメーションを付けるなら、判定済みを示す完成した形（外側の弧の線、範囲の円盤）を最初から置く。
- **衝突・命中の表現（衝撃の輪・土煙・火花）は残像に入れない。** それは命中の演出（Contact）の仕事。入れると何を表すのか分からなくなる。
- **攻撃部位から何かが前へ飛ぶ表現は、飛び道具や術に見える。** 粒子は斬る・振る向きに沿わせる（弧に沿って曲げる）。
- 端は少しでもグラデーションで落とす。1→0で切れた辺は途切れて見える。
- 粒子の回転の向きは、刃の向きと合っているかを数値で確かめる。

## 限界

剣・短剣・大剣・斧・大鎌・鉄扇・棒の例から作った入口。槍・爪・拳・盾などは同じ問いから考え、結果を追加する。
