---
schema_version: 0.1.0
id: technique/arc-sweep
kind: technique
title: 弧状メッシュの展開による斬撃
summary: 動作中の刃を角度・曲率・幅を持つ弧の展開で見せる候補。判定後の完成残像とは用途を分ける。
status: draft
revision: 2
updated_at: '2026-10-06'
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
- target: technique/uv-dissolve
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: rendering/emission-and-opacity
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: technique/completed-arc-afterimage
  type: candidate
  reason: 判定後に表示する残像の分岐。
  role: afterimage
evidence: []
superseded_by: []
---

# 弧状メッシュの展開による斬撃

## 主案
弧状帯のU方向へ先頭マスクを進め、後端を遅れて侵食する。固定扇形の主輪郭はこの方法で作り、粒子の分布へ委ねない。外縁に細い高明度線、内側に厚薄のある色面を置く。

## 調整
中心、運動面、半径、開始角、終端角、横断幅、進行位相を入力する。攻撃の有効範囲を示す部分はゲームのRと角度を使う。装飾の弧は武器の軌道面に置き、斬撃の水平・斜めを取り違えない。

## 時間
アニメーションの振りに位相を合わせ、展開の先頭と刃先を接続する。外縁は短く強く、後端は大きな裂け目で消す。開始角を反転した左右攻撃ではUVの進行も反転する。

## 弱点・検証
薄い平面は視点で消えるため、湾曲断面を持たせる。背面からの見え方、反転、画面占有率、ソートを検査する。必要時の代替は履歴帯だが、判定扇形の輪郭を一律に置換しない。

## 接続する知識

- [resource/unit-effect-mesh-kit](../resources/unit-effect-mesh-kit.md)
- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)
- [technique/uv-dissolve](uv-dissolve.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)
- [rendering/world-depth-and-transparency](../rendering/world-depth-and-transparency.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。

## 発火時点で表現を選ぶ

動作中の刃と、判定後に残った空間は別の時間契約。[完成弧の残像](../techniques/completed-arc-afterimage.md)では外側を初めから完成させ、内部流れと方向の読める消失を動かす。立上りopacityと消失時計は独立にし、直列再生を既定にしない。意味が異なる既存の展開・履歴方式は削除せず、用途を分けて保持する。
