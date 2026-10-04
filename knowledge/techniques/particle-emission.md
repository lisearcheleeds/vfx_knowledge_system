---
schema_version: "0.1.0"
id: "technique/particle-emission"
kind: "technique"
title: "役割を限定した粒子の発生と運動"
summary: "火花・破片・葉・光点を、数・方向・寿命を決めて補助として発生させる。"
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
  - target: "rendering/world-depth-and-transparency"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: ["evidence/particle-simulation-and-renderer-source"]
superseded_by: []
---

# 役割を限定した粒子の発生と運動

## 原理・主案
粒子は発生・寿命・速度・回転・サイズ変化を制御する仕組みとして扱い、描画形状は別に選ぶ。命中の放射、回復の上昇、詠唱の収束で運動を分ける。主形状の輪郭を粒子のランダムな分布に任せない。

## 制作
一回のBurstまたは状態のtickイベント起点を使う。各Recipeで指定する個数は制作初期値であり、性能合格の閾値ではない。速度ベクトル、重力、抗力、Seed、ローカル/ワールド空間を明示する。

## 描画・弱点
光点や火花は板、立体片はメッシュを選ぶ。Billboard/Flipbook/加算は同義ではない。粒子のランダム性で核を失わないよう、役割と面積を制限する。

## 運用・評価
停止で発生を止め、残留だけ消す。再利用時は粒子・Seed・座標を初期化する。多重発生と透明面積を実機計測する。

## 接続する知識

- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)
- [evidence/particle-simulation-and-renderer-source](../../evidence/particle-simulation-and-renderer-source.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
