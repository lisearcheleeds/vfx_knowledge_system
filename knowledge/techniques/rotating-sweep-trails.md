---
schema_version: 0.1.0
id: technique/rotating-sweep-trails
kind: technique
title: 範囲の円盤と順番に回る刃の軌跡
summary: 回転して周りを薙ぎ払う攻撃を、最初から見える範囲の円盤と、半径と速さの違う複数の刃の軌跡が順番に現れて回る形で見せる。
status: draft
revision: 1
updated_at: '2026-10-07'
aliases:
- 大鎌
- 回転斬り
- 薙ぎ払い
- sweep
- 旋風
tags:
- combat
- melee
- technique
- area
scope: engine-neutral
relations:
- target: rendering/emission-and-opacity
  type: requires
  reason: 薄い円盤と明るい刃の軌跡の明度の差。
- target: technique/particle-emission
  type: enhances
  reason: 刈った切れ端を回転の向きに飛ばす。
- target: adapter/unity-urp-baseline-sheet-particles
  type: implemented_by
  reason: Unityで実行した実装。
evidence:
- evidence/melee-weapon-free-design-preview
superseded_by: []
---

# 範囲の円盤と順番に回る刃の軌跡

## 伝えること

周り全部を刈った範囲と、回った向き。

## 構成

1. **範囲**: 刈った範囲を表すごく薄い渦巻く円環（または円盤）を、**最初から**表示する。回転方向へ流れる筋の模様。中心から崩れて消す。灰色の雲のように濃くしない。
2. **方向**: 半径と速さの違う細い刃の軌跡を3本ほど、**少しずつ遅れて順番に**現れさせ、円環の上を回す。先頭を厚く明るく、後ろを細く消す。順番と回転で向きが読める。
3. **補助**: 刈った切れ端を外へ飛ばす。細く少なく（太い切れ端はマッチ棒に見える）。

範囲（円盤）と方向（回る刃）の組み合わせが表現の核（評価90点）。

## 粒子の回転

- 粒子の公転は**刃と同じ向き**にする。設定の符号はエンジンの座標系で逆になりうるので、粒子の位置を2時刻読んで向きを数値で確かめる（逆向きに設定して等倍再生で逆回転に見えた例がある）。
- 速さは等倍で目で追える程度（例 約0.5回転/秒、60fpsで1フレーム数度）。速すぎると車輪の錯覚で逆回転に見える。

## 限界

一つの例。回転の速さ・本数は採用先の攻撃の尺に合わせる。
