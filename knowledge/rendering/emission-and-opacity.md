---
schema_version: 0.1.0
id: rendering/emission-and-opacity
kind: rendering
title: 発光の芯と色の面を分ける合成
summary: 小さな加算の芯と、輪郭を保つ色のアルファ面を分ける描画判断。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases: []
tags:
- rendering
- readable-silhouette
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
---

# 発光の芯と色の面を分ける合成

## 主案
主形状は色と不透明度を持つアルファ面、熱い芯・火花は狭い加算面、煙は低明度のアルファ面に分ける。RGBとalphaを独立に制御し、透明度だけを下げて色が白へ飽和する運用を避ける。

## 時間
ピークでは芯の幅だけ一度強め、面の輪郭を維持する。減衰では彩度・面積・侵食を制御し、全レイヤーを同じ明度曲線で消さない。

## 契約・失敗
straight alpha素材を基本とする。エンジンのBlend設定と色空間はAdapterで対応付ける。Bloomなしでも核が読める形を作る。HDR発光値をこの文書で全エンジン共通の数値に固定しない。

## 評価
白黒表示、白い床・黒い床、重なり、Bloom有無で輪郭を確認する。場面の飽和はMaterial設定と面積から修正する。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。

## 輪郭と立上りを色面から分ける

金属の刃や火花を示す場合は美術指定に従った色を面に残す。主面まで一様に薄くして発光で補わず、不透明寄りの領域と端の透明グラデーションを作る。輪郭coverage、全体opacity、RGB、内部流れを独立にする。フェードアウトのalphaだけでは切り取る境界の形や移動方向を作れない。

部分修正時も立上り、色、面の濃さ、流れ、消える順序、終端を維持一覧で確認する。透明Queueの選択と主面のopacityは別の判断。
