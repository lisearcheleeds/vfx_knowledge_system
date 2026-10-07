---
schema_version: 0.1.0
id: semantic/slash
kind: semantic
title: 斬撃
summary: 弧または帯の移動と接触によって切断方向を伝える。
status: draft
revision: 3
updated_at: '2026-10-07'
aliases: []
tags:
- combat
scope: engine-neutral
relations:
- target: technique/arc-reach-asymmetry
  type: candidate
  reason: 刃渡り・射程の長さを、残像の片側の長さで伝える。
- target: technique/afterimage-weight-timing
  type: candidate
  reason: 武器の速さ・重さ・鋭さを、残像の時間配分で伝える。
- target: technique/slash-pressure-haze
  type: candidate
  reason: 重い武器の破壊力を、外側の薄い霞で伝える。
- target: technique/completed-arc-afterimage
  type: candidate
  reason: 判定後に表示する残像の分岐。
  role: afterimage
evidence: []
superseded_by: []
---

# 斬撃

## 意味・視覚上の要求
斬撃の主情報は刃の通過方向・長さ・曲率。剣は細い弧、斧は先端が重い弧、大剣は長く厚い弧、鎌は連続した円周、爪は平行した短い切り線に分ける。範囲とヒット回数はゲームから受け取り、線の本数でダメージ回数を推測させない。

## 構成判断
弧または帯の移動と接触によって切断方向を伝える。 主役の形を先に読み取れるよう、補助粒子の密度と明度を抑える。カメラと画面密度に対する成功条件は制作Profileで指定する。

## 状態
意味と美術判断の定義。ゲームエンジンでの再現記録ではない。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。

## 発火時点で表現を選ぶ

動作中の刃と、判定後に残った空間は別の時間契約。[完成弧の残像](../techniques/completed-arc-afterimage.md)では外側を初めから完成させ、内部流れと方向の読める消失を動かす。立上りopacityと消失時計は独立にし、直列再生を既定にしない。意味が異なる既存の展開・履歴方式は削除せず、用途を分けて保持する。

## 武器の性格を読ませる因子

形の種類（細い弧・重い弧など）に加えて、同じ三日月でも次の因子で武器の性格が読み分けられる。

- 刃渡り・射程: [残像の片側の長さ](../techniques/arc-reach-asymmetry.md)。振り終わり側が短いと短い刃、振り始め側が長いと長い射程。
- 速さ・重さ・鋭さ: [残像の時間配分](../techniques/afterimage-weight-timing.md)。細い外縁だけの時間は鋭さ、太い本体の時間は重さ。
- 破壊力: [剣圧の霞](../techniques/slash-pressure-haze.md)。重い武器だけにごく薄く。
