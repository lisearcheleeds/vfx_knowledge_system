---
schema_version: 0.1.0
id: technique/completed-arc-afterimage
kind: technique
title: 判定後の完成した斬撃残像
summary: 刃が通過済みの空間を静止した完成弧として置き、色面の流れと方向の読める消失を重ねる。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases:
- completed slash
- 斬撃の残像
- 振り終わり
- 剣閃
tags:
- combat
- technique
scope: engine-neutral
relations:
- target: technique/inner-cut-sdf
  type: candidate
  reason: 曲線状の内側境界で残像を薄くする候補。
  role: contour
- target: semantic/slash
  type: expresses
  reason: 刃の通過方向を伝える。
evidence:
- evidence/completed-slash-inner-cut-preview
superseded_by: []
---

# 判定後の完成した斬撃残像

## 適用条件

発火時点で振りとダメージが完了し、通過した空間の残像を見せる場合に選ぶ。現在の刃先に追従するTrailや、振りに同期して弧を伸ばす展開とは時間の意味が違う。武器名から発火時点を推測しない。実運動の履歴が必要なら従来の方式を選ぶ。

## 構成と時間

外側の弧と全体位置は初めから完成している。見えるまでの短いopacity立上り、内部模様のUV流れ、輪郭の消失を独立した関数として外部経過秒で駆動する。フェードインと消失は並列に開始できる。フェードイン終了を消失時計の原点にするのは、明示的に要求された場合だけ。

方向は形が消える順序にも残す。一様なalpha減衰では位置と濃さしか変わらない。直線ワイプや角度ワイプで根元が先に切れるなら、参照の曲線に沿う内側の抜き、厚み、終端の短縮を別々に設計する。振り始めの端点を武器の回転中心と混同しない。

## 形と差分

三日月の外形、内側の食い込み、帯の厚み、全体縦横比を区別する。短い刃物の細い帯は、全体を小さくするだけでは得られない。深く食い込む内側形と長く鋭い奥行きを両立させる。大きい刃物は基準の弧を保ち、帯を広げ残留を少し長くする。別の戻り残像や二回目の攻撃を、切り返しという言葉だけで追加しない。

## 選択と限界

固定Meshで必要な形が成立すれば粒子やVATを必須にしない。[内側の抜きSDF](inner-cut-sdf.md)は輪郭変化の候補。補助層や命中反応は独立に採否を決める。見た目承認をゲーム時計・判定同期・実機負荷の合格へ拡張しない。
