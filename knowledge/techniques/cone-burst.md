---
schema_version: "0.1.0"
id: "technique/cone-burst"
kind: "technique"
title: "瞬間範囲を埋める円錐状の解放"
summary: "円錐メッシュと扇状の炎筋で前方範囲を一度に見せる。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "resource/unit-effect-mesh-kit"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/uv-dissolve"
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

# 瞬間範囲を埋める円錐状の解放

## 主案
根元から広がる薄い円錐殻と、異なる角度の数枚の筋を重ねる。主形状の到達距離・扇角はゲーム入力を使い、少数の粒子だけで扇の境界を作らない。

## 瞬間攻撃
範囲攻撃の発動イベントで全体の主形状を表示する。長い発生ループや前進する見た目の先端にダメージを結び付けない。粒子は解放後の減衰に用いる。

## 形・弱点
根元は締め、遠端は3〜5本の大きな舌へ分かれる。全幅の一枚板でカメラを向かせない。先端の装飾を実範囲の延長と読ませない。

## 評価
発動フレーム、真横、上方、遮蔽、近接対象が炎面で消えないことを確認する。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [technique/uv-dissolve](uv-dissolve.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
