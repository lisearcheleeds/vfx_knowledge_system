---
schema_version: "0.1.0"
id: technique/mesh-core
kind: technique
title: メッシュによる核
summary: 独立した立体形状で投射体の核の輪郭を設計する候補。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [メッシュ核, mesh core]
tags: [mesh, readable-silhouette]
scope: engine-neutral
relations:
  - target: technique/billboard
    type: alternative
    role: core
    when: 限定した画角で板の見え方が成立する場合。
    reason: 同じ核の役割に対し、形状と素材の負担を変える代替候補。
evidence: []
superseded_by: []
---

# メッシュによる核

## 原理と採用条件

単一または少数のメッシュの輪郭を核として設計する。複数方向から形を読む要求がある場合の候補とする。立体形状だけで視認性が保証されるわけではなく、素材・合成・背景の組合せを確認する。

## 素材・能力要件

核の寸法・原点・向きを定義したメッシュと、描画に必要なMaterialが必要。具体的なアセット仕様、合成方法、エンジン上の作成手順は採用時に決める。未登録の素材・描画ノードは追加候補として扱う。

## 弱点・代替・性能

形状の硬さ、背景との明度不足、スケールと遮蔽による読み取りの変化を検証する。[ビルボード](billboard.md)を同じ核の代替候補として比較する。描画負荷は面積・Material・同時表示・対象環境に依存し、低負荷と断定しない。

## 状態

設計上の仮説。実装・複数視点の再現・性能測定は未実施。エンジン用Adapterは未作成。
