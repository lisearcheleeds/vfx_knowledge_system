---
schema_version: "0.1.0"
id: semantic/magic-orb
kind: semantic
title: 魔法弾
summary: 特定の元素属性を固定せず、球状の核・飛翔方向・着弾を伝える魔法投射体。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [魔法弾, magic orb]
tags: [projectile, magic]
scope: engine-neutral
relations:
  - target: composition/projectile
    type: candidate
    reason: 投射体のライフサイクルを共有できる。
  - target: recipe/magic-orb-readable-core
    type: candidate
    reason: 魔法弾の主要情報を核と着弾に割り当てる構成案。
evidence: []
superseded_by: []
---

# 魔法弾

## 意味と視覚要件

ゲーム側から渡される位置・方向・着弾イベントに従う魔法投射体。球状にまとまった主役と飛翔方向、着弾の瞬間を伝える。色・質感・属性・強度はProfileとBriefで定める。

## 誤解と構成候補

装飾の明るさによって主役が消えたり、視覚範囲と当たり判定を混同したりしないか確認する。[投射体の役割構造](../compositions/projectile.md)と[魔法弾の構成案](../recipes/magic-orb-readable-core.md)を参照する。球状の核を特定の描画技法に固定しない。

## 根拠と状態

設計上の要求案。エンジン上での制作・再現・性能測定は未実施。
