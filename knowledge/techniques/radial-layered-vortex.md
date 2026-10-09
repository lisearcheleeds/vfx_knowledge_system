---
schema_version: 0.1.0
id: technique/radial-layered-vortex
kind: technique
title: 渦・竜巻は半径で層を棲み分ける
summary: 渦を巻く溜め・竜巻は、中央のコイル、外周の流れる風、最外周の舞うほこりと、半径ごとに役割の違う層に分けると、風感と渦巻き感が出る。
status: draft
revision: 1
updated_at: '2026-10-10'
aliases:
- 竜巻
- 渦巻き
- 旋風
- 風感
tags:
- combat
- technique
scope: engine-neutral
relations:
- target: technique/rotation-overshoot
  type: enhances
  reason: 各層の回転量と端の消し方。
evidence:
- evidence/skill-baselines-preview
superseded_by: []
---

# 渦・竜巻は半径で層を棲み分ける

## 何を伝えるか

同じ半径に輪や筋を重ねると、風ではなく線の束に見える。半径ごとに役割を分けると、中心へ巻き込む力と、まわりの空気が流れる風と、巻き上げられたほこりが読み分けられる。

| 半径 | 層 | 形 |
| --- | --- | --- |
| 中央 | コイル | 細い弧が回りながら締まる |
| 外周 | 風 | 高さの違う薄い帯を数段。全周の輪にせず、回る窓で一部（半周ほど）だけ見せ、筋の模様を回る向きへ流す |
| 最外周 | ほこり | 小さな粒が公転しながら舞い上がる |

## 作り方

- 全周の帯を何段も重ねると、止まった輪（ばね）に見える。外周の風は必ず一部だけを見せて回す。
- すべての層を同じ向きに回す。粒子の公転の向きは数値で確かめる。

## 確認

斜め上から等倍で再生し、中心・外周・最外周がそれぞれ別のものとして読めるかを見る。
