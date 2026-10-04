---
schema_version: "0.1.0"
id: recipe/magic-orb-readable-core
kind: recipe
title: 輪郭を重視した魔法弾
summary: 魔法弾の核と着弾を優先し、共有Techniqueから核の描画方法を選ぶ。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [魔法弾の核, readable magic orb]
tags: [projectile, magic, readable-silhouette]
scope: engine-neutral
relations:
  - target: semantic/magic-orb
    type: expresses
    reason: 球状の魔法投射体・方向・着弾を表現する。
  - target: composition/projectile
    type: composes
    requirement: required
    role: lifecycle
    reason: 火炎弾と共通の投射体ライフサイクルを利用する。
  - target: technique/mesh-core
    type: candidate
    role: core
    when: カメラ移動と遮蔽に対して立体的な核が必要。
    reason: 共通のメッシュ核を魔法弾にも利用する候補。
  - target: technique/billboard
    type: candidate
    role: core
    when: 限定した画角と素材による核が美術上成立する。
    reason: 同じ核の役割を板と素材で構成する候補。
  - target: evaluation/projectile-readability
    type: evaluated_by
    reason: 飛翔・着弾・終了の共通評価を使う。
evidence: []
superseded_by: []
---

# 輪郭を重視した魔法弾

## 適用条件と不向きな条件

[魔法弾の意味](../semantics/magic-orb.md)と核の位置・着弾を読み取る要求に対する構成案。球状の主役が不要なビームや面状の攻撃へ、そのまま適用しない。属性・色・質感はBriefで指定する。

## 役割と候補選択

[投射体の役割構造](../compositions/projectile.md)を利用し、核には[メッシュ核](../techniques/mesh-core.md)または[ビルボード](../techniques/billboard.md)を比較する。どちらも火炎弾と共有するTechniqueである。属性名を理由に技法を固定せず、今回のカメラ・形状・背景に対する選択理由を残す。

任意の尾・表面装飾と着弾表示の素材・合成・具体的な技法は未選定であり、実装計画に進む前に整備する。

## 時間・削減・失敗の仮説

ゲーム側の飛翔位置とimpact/stopイベントに従う。装飾を減らす場合も核と必要な着弾情報を維持する。明るい装飾による輪郭の消失、画角による見え方の変化、停止後の残留を検証する。実際の失敗記録ではない。

## 評価と状態

[共通評価項目](../evaluation/projectile-readability.md)を使用する設計案。エンジン上での制作・再現・性能測定は未実施。知識の共有と選択を確認する `draft`。
