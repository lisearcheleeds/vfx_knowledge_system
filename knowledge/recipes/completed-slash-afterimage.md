---
schema_version: 0.1.0
id: recipe/completed-slash-afterimage
kind: recipe
title: 完成した三日月の斬撃残像
summary: 判定後に発火する剣・短剣・大型刃の残像。固定外形、内側SDF、色面の流れ、並列の立上りと消失を採用する。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases:
- SwordSlash
- DaggerThrust
- GreatswordSlash
- 剣の残像
- 短剣の三日月
tags:
- combat
- recipe
scope: engine-neutral
relations:
- target: technique/completed-arc-afterimage
  type: composes
  reason: 判定後の固定空間に残像を置く。
  requirement: required
  role: afterimage
- target: technique/inner-cut-sdf
  type: composes
  reason: 固定外形から曲線状の穴を拡げる。
  requirement: required
  role: contour
- target: semantic/slash
  type: expresses
  reason: 刃の通過方向と形を伝える。
- target: evaluation/combat-shape-and-events
  type: evaluated_by
  reason: 発火時点と時間を含めて確認する。
- target: adapter/unity-urp-inner-cut-afterimage
  type: implemented_by
  reason: Unityで実行した候補。
evidence:
- evidence/completed-slash-inner-cut-preview
superseded_by: []
---

# 完成した三日月の斬撃残像

## 採用契約

刃が通過済みの空間を見せる場合の主案。現在の刃の動きを追うレシピへ無条件に適用しない。攻撃方向、運動面、発火イベント、参照形状、秒単位の尺を採用先から受け取る。見た目からダメージや射程を作らない。

## 主役

[完成弧の残像](../techniques/completed-arc-afterimage.md)に[内側SDF](../techniques/inner-cut-sdf.md)を組み合わせる。外形を覆う静止Mesh、色面のUV流れ、内側穴の変化、細い明部で構成する。立上りと輪郭消失は同じ経過秒から並列に進む。色のある面のopacityは十分に保ち、端だけグラデーションで透明へ落とす。

## 個体差と補助

基準形を共有しても、内側の深さ、帯幅、縦横比、残留を独立にする。細い刃は深い内側抜きと鋭い奥行き、大型刃は幅広い面と少し長い残留で差を出す。前後の残像、履歴Trail、Contact、スパークはこの主案の必須依存に含めない。各役割が必要な場合に選択記録へ追加する。

## 修正・承認

形、色、opacity、立上り、UV流れ、消失方向、終端、既存補助層の維持一覧を作る。部分指摘を直すために他の成立済み要素を削除しない。主役だけ・補助だけ・合成後、通常速度と代表時刻で比較する。内側の抜きを動かしただけで方向性が合うと決めない。

Previewでの実行例はあるが、ゲーム用削減、ゲーム接続、製品端末負荷の合格は別段階。一般化したこのレシピはdraftを維持する。
