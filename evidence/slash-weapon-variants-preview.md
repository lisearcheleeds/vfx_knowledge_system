---
schema_version: 0.1.0
id: evidence/slash-weapon-variants-preview
kind: evidence
title: 解析式の三日月を短剣・大剣へ展開した再現記録
summary: 剣の知見だけで短剣・大剣の残像を作り、指摘の往復から刃渡り・重さ・破壊力の読ませ方を確かめた記録。
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
  - target: recipe/completed-slash-afterimage
    statement: 改訂2の優先する作り方を、値だけ変えて短剣・大剣へ適用でき、初回で短剣80点・大剣70点と評価された。
  - target: technique/arc-reach-asymmetry
    statement: 振り始め側を短くした短剣は「薙刀の射程の長い斬撃」に見え70点に下がった。振り終わり側を短くする必要があった。
  - target: technique/afterimage-weight-timing
    statement: 大剣で細い外縁だけの時間を削り太い本体へ回すと、重い振りとして80点に上がった。
  - target: technique/slash-pressure-haze
    statement: 大剣の外に置いた薄く広い柔らかな霞が、剣との差（破壊力）として受け入れられた。離れた細い帯は二本目の線に見えた。
  - target: technique/analytic-crescent-uv
    statement: 内縁の裂けを厚みに比例させると、細い楕円では暗い切れ目、幅広い刃では大きな歯になった。
  - target: adapter/unity-urp-analytic-crescent
    statement: 同じShaderで値と弧の範囲・楕円の倍率だけを変えて二種を作った。既存Meshの上書きの不具合を回避した。
  conditions: 専用Prefab Preview。暗い背景、45度俯瞰と真上。ユーザーがライブPreviewで評価。前任の短剣・大剣のアセットは参照していない。
  result: 初回 短剣80点・大剣70点。修正後 大剣80点。短剣は短くする端を取り違えて70点、端を入れ替えた版3は評価待ち。
  limitations: 一つのカメラ条件・一つのプロジェクトの例。評価点はユーザーの主観。ゲーム接続・性能は未確認。
  sources: []
  checked_at: '2026-10-07'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview
    executed_at: '2026-10-07'
    procedure: 設定値だけを変える生成スクリプトで二種を作り、連番の一覧画像で確認・修正してからユーザーが評価した。指摘ごとに作り直して再評価した。
    artifacts:
    - projects/dungeon-inn/runs/slash-weapon-variants-2026-10-07.md
---

# 解析式の三日月を短剣・大剣へ展開した再現記録

## 目的

剣の作り直し（85点）で得た知見だけで、別の武器の残像が作れるか（再現性）を確かめた。

## 往復の要点

- 短剣（初回80点）: 剣と差別化できていない。刃渡りの短さを、振り終わり側（尾）を短くした片側の短い三日月で見せたい。
  → 版2で振り始め側を短くしてしまい、薙刀の射程の長い斬撃に見えて70点。→ 版3で振り終わり側を短くし、長い振り始め側を早く縮めた。
- 大剣（初回70点）: 振り速度が遅い代わりに重く強いことを見せたい。細い外縁だけの時間（鋭さ）を短くして振り全体へ回し、剣には無い剣圧をごくわずかに外へ出したい。
  → 時間配分の変更と剣圧の霞で80点。

## 判定

形と時間の作り方は武器をまたいで再現した。武器の性格は「片側の長さ」「時間配分」「剣圧」の三つの因子で読み分けられる。
