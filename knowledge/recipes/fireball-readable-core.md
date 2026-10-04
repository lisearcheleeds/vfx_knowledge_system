---
schema_version: "0.1.0"
id: recipe/fireball-readable-core
kind: recipe
title: 輪郭を重視したファイアボール
summary: 火炎弾の核・外周・着弾を役割として分け、核の技法を条件に応じて選ぶ。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [輪郭重視の火炎弾, readable fireball]
tags: [projectile, fire, readable-silhouette]
scope: engine-neutral
relations:
  - target: semantic/fireball
    type: expresses
    reason: 火炎属性・飛翔方向・着弾の意味を表現する。
  - target: composition/projectile
    type: composes
    requirement: required
    role: lifecycle
    reason: 発射・飛翔・着弾・終了の役割構造を利用する。
  - target: technique/mesh-core
    type: candidate
    role: core
    when: 複数方向で安定した立体的な輪郭が必要。
    reason: 核の形状を外周の揺らぎから分離する候補。
  - target: technique/billboard
    type: candidate
    role: core
    when: 想定するカメラと背景で板の輪郭が成立する。
    reason: 核を素材で構成する代替候補。
  - target: evaluation/projectile-readability
    type: evaluated_by
    reason: 核・飛翔・着弾の視認性とライフサイクルを確認する。
evidence: []
superseded_by: []
---

# 輪郭を重視したファイアボール

## 適用条件と不向きな条件

火炎弾の核を読み取る要求に対する構成案。炎全体を不定形の主役にする美術方針では、安定した核の必要性から見直す。対象カメラ・性能予算はProfileで確認する。

## 役割と候補選択

[投射体のライフサイクル](../compositions/projectile.md)を必須構成として利用する。核の候補は[メッシュ核](../techniques/mesh-core.md)と[ビルボード](../techniques/billboard.md)であり、両方の採用を要求しない。[ファイアボールの視覚要件](../semantics/fireball.md)に合う理由と、棄却理由をBrief・仕様に残す。

火炎外周・尾・着弾素材の具体的な技法は未選定。これらの追加候補は実装前に設計し、必要なResource・Renderingを整備する。現時点でこのRecipeだけでは実装計画は完結しない。

## 時間・削減・失敗の仮説

核はゲーム側の飛翔位置に追従し、着弾表示はimpactに同期する。削減時も核と着弾情報を維持する。外周の飽和で核が消える、尾で位置を誤認する、stop後に残留する可能性を検証する。実際に観測した失敗記録ではない。

## 評価と状態

[投射体の評価](../evaluation/projectile-readability.md)を実施する。エンジンでの制作・撮影・評価・性能測定は未実施。共有Techniqueと候補選択の構造確認に使う `draft` であり、完成アセットを再現するRecipeではない。
