---
schema_version: "0.1.0"
id: "technique/orbit-glyphs"
kind: "technique"
title: "小さな周回記号による継続状態"
summary: "身体の外縁に小さな識別形状を配置し、長寿命状態を低密度で示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "resource/effect-mask-atlas"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/world-depth-and-transparency"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 小さな周回記号による継続状態

## 主案
Actor幅Wの0.08〜0.14倍の記号2〜3枚を、腰から肩の外縁へ置く。HPは葉/滴、MPは結晶、攻撃強化は上向き山形、弱体は欠けた下向き山形とする。色だけで識別しない。

## 動き
4秒程度の緩い周回・上下動を美術上の位相として使う。回復刻みや残り時間の正本にしない。頭上のUIと重ならない高さへ置き、周回半径は最大0.65Wの制作初期値とする。

## 更新・集約
状態のapply/refresh/removeへ追従する。複数の元状態はカテゴリごとに集約し、最も強い表示を一組にまとめる。単純にEmitterを追加して記号を増殖させない。

## 削減・評価
小粒子を省いても識別記号を保つ。5分の再生、画面外復帰、装備差、複数カテゴリの重なり、消失後の残留を確認する。

## 接続する知識

- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
