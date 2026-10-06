---
schema_version: 0.1.0
id: technique/inner-cut-sdf
kind: technique
title: 固定外形から内側だけをSDFで抜く
summary: 外側の弧を保ち、距離場の中心・半径・終端制御で内側から三日月の厚みを消す。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases:
- SDF
- 三日月の内側
- inner cut
- 円SDF
tags:
- combat
- technique
scope: engine-neutral
relations:
- target: resource/signed-distance-mask
  type: requires
  reason: 内側境界の符号付き距離を使う。
- target: rendering/emission-and-opacity
  type: requires
  reason: 色面・縁coverage・全体opacityを分離する。
evidence:
- evidence/completed-slash-inner-cut-preview
superseded_by: []
---

# 固定外形から内側だけをSDFで抜く

## 原理

完成した外形のcoverageから内側の穴を引く。SDFは内側境界の滑らかな輪郭とアンチエイリアスに使い、斬撃全体を一様なしきい値で縮めない。色面用のUVを流しても、穴を決める座標は同じ流れへ巻き込まない。

単一の距離場を座標変換して中心・半径を変え、内側境界を外側へ近づける。終端の戻り側を別の曲線制御で短くする。初期の完成形から薄い外縁まで、残す端と連続した弧が維持されるように合わせる。しきい値だけ、X方向だけ、角度だけという一変数への置換が参照と同じ運動になるとは限らない。

## 必要素材と成立条件

[距離マスク](../resources/signed-distance-mask.md)を使う。同じ円・楕円等のプリミティブと変換で、参照の内側曲線群を近似できるなら一枚を共有できる。任意の四枚の輪郭を一枚の円SDFで再現できる保証はない。別の場、合成、Mesh形状等を必要に応じて比較する。

## ラスタライズと縁

Meshが初期穴の位置で終わっていると、後から変わるSDF輪郭に必要なfragmentが発生しない。必要な描画領域を覆う静的な支持面とBoundsを用意し、外側coverageで見える形を制限する。支持面を広げる処理は、時間で頂点を動かすアニメーションとは区別する。

外形のcoverage、穴のcoverage、端の透明化、全体の立上り、色・発光を独立に確認する。色のある不透明寄りの面を確保し、縁のみ滑らかに透明へ落とす。透明素材を選んだことと全面を薄くすることは別。

## 評価

初期・中間・後半・最後の細い外縁を参照と照合する。曲線の接続、根元の残り方、反対端の短縮、薄い終端の欠け、背景透過、Boundsを確認し、通常速度でも方向が読めることを人間が判断する。単調な画素数減少だけでは合格にしない。
