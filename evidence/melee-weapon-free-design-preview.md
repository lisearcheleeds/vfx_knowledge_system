---
schema_version: 0.1.0
id: evidence/melee-weapon-free-design-preview
kind: evidence
title: 斧・大鎌・鉄扇・棒を武器から一から作ったPreview記録
summary: 剣の作り方を土台にした版が「Swordに引っ張られすぎ」と評価された後、武器から推測して一から作った版が75〜90点と評価された記録。
status: reviewed
revision: 1
updated_at: '2026-10-07'
aliases: []
tags:
- combat
- evidence
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: first-party-experiment
  claims:
  - target: recipe/melee-weapon-afterimages
    statement: 剣の三日月を土台にした版は武器の差が出ず、武器から推測して一から作った版は斧80・大鎌90・鉄扇85・棒75点と評価された。
  - target: technique/crumbling-heavy-wedge
    statement: 斧のくさびと崩れは80点。振り終わりの辺が1→0で切れて見える点を指摘され、グラデーションを足した。
  - target: technique/rotating-sweep-trails
    statement: 最初から見える範囲の円盤と、順番に現れて回る3本の刃の組み合わせが90点。粒子の公転の向きが逆で逆回転に見えた。
  - target: technique/fan-rib-reveal
    statement: 扇と濃い骨が85点。前へ飛ぶ風の筋は何か分からないと指摘され、弧に沿って流れる筋と完成した外側の弧の線に替えた。
  - target: technique/blunt-motion-smear
    statement: 棒のぼけた帯は75点。帯の幅を打撃部に合わせて半分に、衝突の輪と土煙は削除するよう指摘された。
  - target: adapter/unity-urp-baseline-sheet-particles
    statement: 汎用のシートShaderと粒子の層を一つの生成スクリプトで組み、粒子の回転の向きを位置の読み取りで確かめた。
  conditions: 専用Prefab Preview。暗い背景、45度俯瞰と真上。ユーザーがライブPreviewで評価。前任・剣の版のアセットは参照していない。
  result: 斧80・大鎌90・鉄扇85・棒75点（版1）。指摘を直した版2は評価待ち。
  limitations: 一つのカメラ条件・一つのプロジェクトの例。評価点はユーザーの主観。ゲーム接続・性能は未確認。
  sources: []
  checked_at: '2026-10-07'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview
    executed_at: '2026-10-07'
    procedure: 生成スクリプトで面と粒子の層を作り、連番の一覧画像で確認・修正してからユーザーが評価した。粒子の回転の向きは位置を2時刻読んで確かめた。
    artifacts:
    - projects/dungeon-inn/runs/melee-weapon-free-design-2026-10-07.md
---

# 斧・大鎌・鉄扇・棒を武器から一から作ったPreview記録

## 経緯

剣の残像の因子（片側の長さ・時間配分・剣圧）とユーザーの助言から、斧・大鎌・鉄扇・棒を剣の三日月の変形として作った版は「応用はまだ難しいですか？Swordのエフェクトに引っ張られすぎです」と評価された。剣を一旦忘れ、エフェクト名から武器を推測し、技術スタックを制限せずに一から作り直した。

## 判定

武器の性格（攻撃部位・鋭さ・重さ・動き方）から技法を選ぶと、武器ごとに別の表現になり評価が上がった。指摘は役割の分担（衝突はContact、前へ飛ぶものは飛び道具）と仕上げ（端のグラデーション、回転の向き）に集中した。
