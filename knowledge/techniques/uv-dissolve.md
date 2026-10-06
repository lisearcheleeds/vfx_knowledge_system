---
schema_version: 0.1.0
id: technique/uv-dissolve
kind: technique
title: 方向性を持つマスク展開と侵食
summary: U/Vとノイズで展開・侵食する候補。曲線残像の内側抜きや立上り中の消失を一様ワイプへ置き換えない。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases: []
tags:
- technique
- combat
scope: engine-neutral
relations:
- target: resource/effect-mask-atlas
  type: requires
  reason: この技法の採用時に必要な素材・処理・描画規約。
- target: technique/completed-arc-afterimage
  type: candidate
  reason: 判定後に表示する残像の分岐。
  role: afterimage
evidence: []
superseded_by: []
---

# 方向性を持つマスク展開と侵食

## 主案
進行方向の線形マスクと低周波ノイズを別に制御する。展開で先頭が前進し、後端は少し遅れて侵食する。粒状の高周波ノイズを輪郭全体へ均一に散らさない。

## 入力・素材
normalized-phase、展開方向、先頭の鋭さ、侵食の大きさ、縁幅、色を受け取る。Maskの線形値と色を混同しない。縁の発光は細く、主面が消えた後に巨大な光だけ残さない。

## 時間
動作中の展開ではピークまで形を保つ案を比較する。判定後の残像へこの待ち時間を自動適用しない。中断は別の短い減衰へ移り、途中から発動ピークへ跳ばない。

## 評価
縮小、時間倍率、左右反転、半透明の重なりで形が読めるかを確認する。具体的なShader実装はAdapterに分離する。

## 接続する知識

- [resource/effect-mask-atlas](../resources/effect-mask-atlas.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。

## 発火時点で表現を選ぶ

動作中の刃と、判定後に残った空間は別の時間契約。[完成弧の残像](../techniques/completed-arc-afterimage.md)では外側を初めから完成させ、内部流れと方向の読める消失を動かす。立上りopacityと消失時計は独立にし、直列再生を既定にしない。意味が異なる既存の展開・履歴方式は削除せず、用途を分けて保持する。
