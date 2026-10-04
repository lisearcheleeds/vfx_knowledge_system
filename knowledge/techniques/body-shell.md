---
schema_version: "0.1.0"
id: "technique/body-shell"
kind: "technique"
title: "小さな身体表面の発動パルス"
summary: "対象の身体に短い色面と輪郭のパルスを置き、付与の瞬間を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/world-depth-and-transparency"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 小さな身体表面の発動パルス

## 主案
身体表面の薄いMaterialオーバーレイを一度だけ点灯し、縁に沿って畳む。主役は身体のシルエットで、全身を不透明な発光球に包まない。Material対応がない場合は胴体に沿う小さなメッシュ殻へ置換する。

## 色・時間
色面は低不透明度、縁のピークは60〜100ms、全体は180〜300msを制作初期値とする。長時間状態ではこのパルスをapplyにだけ使い、継続識別を別形状にする。

## 必要能力
身体Materialの一時パラメータまたは追従メッシュが必要。Shaderの種類・描画Pipelineを共通知識で固定しない。別の点滅やダメージ表示とパラメータを共有して上書きしない。

## 評価
武器、装備差分、同時状態、薄い身体、透明装備、解除時の復元を確認する。

## 接続する知識

- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
