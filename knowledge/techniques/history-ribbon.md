---
schema_version: 0.1.0
id: technique/history-ribbon
kind: technique
title: 移動履歴の先細り帯
summary: 武器や投射体の実移動から、長さ・厚さ・色を制御した帯を生成する。
status: draft
revision: 2
updated_at: '2026-10-04'
aliases: []
tags:
- technique
- combat
scope: engine-neutral
relations:
- target: resource/unit-effect-mesh-kit
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: resource/effect-mask-atlas
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: rendering/emission-and-opacity
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
evidence:
- evidence/organic-fire-volume-preview
superseded_by: []
---

# 移動履歴の先細り帯

## 主案
武器の二点または投射体中心の位置履歴を帯へ結ぶ。主役に沿う一本の帯を使い、根元に厚さ、末尾に先細りと透明度を持たせる。投射体の視認用尾は速度と履歴秒数で長さを定める。

## 契約
world-spaceの履歴を保存し、発生元が止まっても過去点を巻き戻さない。teleport、Pool再利用、追従先変更では帯を切る。急旋回ではサンプル距離を上げる前に捻れと帯の法線を確認する。

## UV・停止
Uは蓄積距離、Vは幅としてスクロールの速度と伸長を分離する。impact/stopで新規点を止め、残留の寿命だけで消す。VFXが投射体の移動・命中位置を決めない。

## 熱と煙の遷移

炎の尾は距離/履歴年齢に従い、黄橙→橙→赤→暗い煙色へ冷却する候補がある。加算だけでは暗い煙が出ないため、色とalpha・合成を分けて確認する。world-spaceの煙粒子を併用する場合、発生間隔の距離は速度/発生率。侵食後の見える房がこの距離を覆うかを動画で見る。単に色を黒くする、位相を変えるだけで連続性を保証しない。

## 性能・評価
点列数、同時帯数、透明面積で評価する。曲線の滑らかさを過剰な点列で解決しない。細長い帯のちらつき、曲がり角、前後からの視点、停止後の残留を確認する。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

[実行記録](../../evidence/organic-fire-volume-preview.md)にUnityの手動Simulateによる暖色→煙色の履歴例を保存した。teleport・製品Pool・実ゲーム停止と性能は未検証。この技法はdraft。
