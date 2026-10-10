---
schema_version: 0.1.0
id: evidence/sword-slash-analytic-crescent-preview
kind: evidence
title: 剣の斬撃残像を解析式の三日月で作り直したPreview記録
summary: 前任の版（ユーザー評価65点）を参照せずに作り直し、85点と評価された基準版の記録。火花は命中演出として98点と評価された。
status: reviewed
revision: 1
updated_at: '2026-10-06'
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
  - target: technique/analytic-crescent-uv
    statement: 弧帯UV上の解析式で描いた非対称の三日月・模様・消え方が、ユーザーに「とてもいい」と評価された（基準版全体で85点）。
  - target: recipe/completed-slash-afterimage
    statement: 解析式の三日月を主役にした版が、内側SDF版（65点）より高く評価された。
  - target: recipe/metal-contact-sparks
    statement: 斬撃の中では意味が不明とされた火花が、命中演出として見ると98点と評価された。
  - target: adapter/unity-urp-analytic-crescent
    statement: Unityの専用Prefab Previewで、外部経過秒による描画と連番の撮影を行った。
  conditions: 専用Prefab Preview。暗い背景と明るい背景、45度俯瞰（yaw -135）と真上。ユーザーがライブPreviewで評価。ゲーム用削減・統合前の基準版。
  result: ユーザー評価85点（前任版65点）。残りの差は三日月の消失アニメーションの時間カーブ（0.1秒単位の調整）。火花はContact系に転用する。
  limitations: ゲーム統合・実機性能・他エンジンは未実施。消失カーブは未調整。明るい背景で淡くなる弱点は未解決。数値評価はユーザーの主観。
  sources: []
  checked_at: '2026-10-06'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview（WorldEffectPrefabPreviewWindow）
    executed_at: '2026-10-06'
    procedure: Editorスクリプトでテクスチャ・Mesh・Material・Prefabを生成し、Previewの時計で連番を書き出して一覧画像で評価・修正を4回繰り返した後、ユーザーがライブPreviewで評価した。
    artifacts:
    - projects/dungeon-inn/runs/sword-slash-2-2026-10-06.md
---

# 剣の斬撃残像を解析式の三日月で作り直したPreview記録

## 経緯

ユーザーの指示で、前任の剣の斬撃（内側SDF版。ユーザー評価65点）のアセットを参照せず、最新のナレッジから作り直した。ナレッジは補助輪で表現を規制しない、コストは度外視（家庭用PCで動く範囲）という条件。

## 観察と判定

制作担当（AI）が連番の一覧画像で4回評価・修正した。初稿は色が茶色く沈む、帯が細い、内縁の裂けが櫛状、補助の風圧が二重線、最後の外縁が暗い、という弱点があった。真上からの撮影で「深い三日月ではなく幅の揃った帯」になっていることが分かり、内縁の透明化の範囲と抜きの進み方を直した。

ユーザーの評価: 予想以上に良い品質で85点。三日月メッシュの模様・消え方がとても良い。残り15点は三日月の消失アニメーションの時間カーブ（今は詰めない）。火花は何の火花か不明（目標は三日月の正面にいるのに、振り終わりの地点に目標がいるように読める）。ただし命中演出として見ると98点で、Contact系に使える。

## 限界

一つの武器・一つのカメラ条件の基準版。性能は未計測。評価点はユーザーの主観で、他の演出の合格基準ではない。
