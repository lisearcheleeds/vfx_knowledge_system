---
schema_version: "0.1.0"
id: "rendering/emission-and-opacity"
kind: "rendering"
title: "発光の芯と色の面を分ける合成"
summary: "小さな加算の芯と、輪郭を保つ色のアルファ面を分ける描画判断。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["rendering","readable-silhouette"]
scope: "engine-neutral"
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
