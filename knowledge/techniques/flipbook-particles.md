---
schema_version: "0.1.0"
id: "technique/flipbook-particles"
kind: "technique"
title: "連番素材で形を保つ炎・煙の粒子"
summary: "板上の連番素材を寿命で再生し、炎舌や煙房の形状を維持する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "technique/particle-emission"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/billboard"
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

# 連番素材で形を保つ炎・煙の粒子

## 主案
素材内の形状と時間変化を活かす少数の板粒子を使う。炎は方向に伸ばした板、煙は大きな房を持つ板とし、発生源に沿う輪郭を先に決める。必要な炎/煙Resourceは採用Recipeが指定する。

## 時間
フレーム番号は粒子の正規化寿命または明示した炎ループ位相へ対応付ける。burstの立上りを固定のシート速度に任せず、発生瞬間を発動へ合わせる。煙はピーク後の余韻とする。

## 配置
横から薄くなる炎は角度の異なる二枚の板で厚みを補う。全員の炎を常にカメラの同じ平面に置かない。連番の二重輪郭と境界の黒縁を避ける。

## 評価
フレームの継ぎ目、近距離、前後視点、密集時の透明面積を確認する。流体シミュレーションを必須にしない。

## 接続する知識

- [technique/particle-emission](particle-emission.md)
- [technique/billboard](billboard.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
