---
schema_version: "0.1.0"
id: "technique/uv-dissolve"
kind: "technique"
title: "方向性を持つマスク展開と侵食"
summary: "U/Vと低周波ノイズで主形状を解放し、大きな裂け目から消す。"
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
evidence: []
superseded_by: []
---

# 方向性を持つマスク展開と侵食

## 主案
進行方向の線形マスクと低周波ノイズを別に制御する。展開で先頭が前進し、後端は少し遅れて侵食する。粒状の高周波ノイズを輪郭全体へ均一に散らさない。

## 入力・素材
normalized-phase、展開方向、先頭の鋭さ、侵食の大きさ、縁幅、色を受け取る。Maskの線形値と色を混同しない。縁の発光は細く、主面が消えた後に巨大な光だけ残さない。

## 時間
最初のピークまで形を保ち、残留の後半から形を切る。中断は別の短い減衰へ移り、途中から発動ピークへ跳ばない。

## 評価
縮小、時間倍率、左右反転、半透明の重なりで形が読めるかを確認する。具体的なShader実装はAdapterに分離する。

## 接続する知識

- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
