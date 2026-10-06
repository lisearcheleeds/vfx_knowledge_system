---
schema_version: 0.1.0
id: semantic/slash
kind: semantic
title: 斬撃
summary: 弧または帯の移動と接触によって切断方向を伝える。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases: []
tags:
- combat
scope: engine-neutral
relations:
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
