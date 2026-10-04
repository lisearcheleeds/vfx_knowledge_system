---
schema_version: "0.1.0"
id: "technique/oriented-projectile-core"
kind: "technique"
title: "前方を保つ投射体の実体"
summary: "矢・ボルト・魔法核を実位置・実速度方向へ向けて飛翔の主役とする。"
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
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/world-depth-and-transparency"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 前方を保つ投射体の実体

## 主案
矢は細い軸と鏃、ボルトは短く硬い紡錘、魔法弾は球/滴を主役にする。位置・姿勢はゲーム側の投射体入力へ追従し、VFXの粒子速度で本体を二重移動させない。

## 生成
可視の投射体アセットがゲーム側にある場合は、それを核として使い素体を重複生成しない。発光は小さな縁・先端に置く。速度と投射距離に依らず不自然に巨大な球へ置換しない。

## イベント
launchで核を有効化、impactで核を消し着弾へ引き継ぐ。stop/消失は成功着弾と分けて扱う。入力位置が跳ぶ場合は尾も切る。

## 評価
高速飛翔、接近するカメラ、前後、壁の遮蔽、impactフレームでの二重核を確認する。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
