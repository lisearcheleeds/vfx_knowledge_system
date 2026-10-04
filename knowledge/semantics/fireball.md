---
schema_version: "0.1.0"
id: semantic/fireball
kind: semantic
title: ファイアボール
summary: 火炎属性を持ち、飛翔方向と着弾を伝える投射体の視覚要件。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [ファイアボール, fireball, 火炎弾]
tags: [projectile, fire]
scope: engine-neutral
relations:
  - target: composition/projectile
    type: candidate
    reason: 発射・飛翔・着弾・終了の役割を整理する入口となる。
  - target: recipe/fireball-readable-core
    type: candidate
    reason: 核の輪郭と火炎属性を分けて設計する構成案。
evidence: []
superseded_by: []
---

# ファイアボール

## 意味と視覚要件

火炎属性の投射体であること、飛翔方向、着弾の瞬間を伝える。核の大きさとゲーム側の当たり判定の関係はProfileで定める。

火炎の揺らぎと主要な輪郭を別の役割として考え、カメラ・背景・画面占有率に合わせて構成する。色だけで属性が伝わるかは検証する。

## 誤解と構成候補

輪郭の拡散による範囲の誤認、尾の遅延による位置の誤認、着弾前のフラッシュに注意する。[投射体の役割構造](../compositions/projectile.md)と[輪郭重視の構成案](../recipes/fireball-readable-core.md)を比較の入口にする。

## 根拠と状態

設計上の要求案。エンジン上での制作・再現・性能測定は未実施。
