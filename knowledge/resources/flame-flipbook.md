---
schema_version: "0.1.0"
id: "resource/flame-flipbook"
kind: "resource"
title: "方向性を持つ火炎Flipbook"
summary: "炎の舌と膨張する炎塊を64フレームの素材で設計する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["resource","fire"]
scope: "engine-neutral"
relations: []
evidence: []
superseded_by: []
---

# 方向性を持つ火炎Flipbook

## 主案
1024×1024、8×8セルの64フレーム。RGBAのstraight alpha。RGBは表示色としてsRGB、アルファは線形で扱い、読み込み時のMaterial側の規約と合わせる。プリマルチプライ済みの素材を同じ設定で混ぜない。

## 内容
細長い炎舌のループ用と、立ち上がり・膨張・侵食の単発用を別シートにする。同じ役割のセル配置・原点・余白を揃える。炎の根元は太く、先端は二つ程度の大きな舌に絞る。

## 色・密度
小さな淡黄の芯、橙の中間、暗赤の縁。全面を白にしない。透明余白はマスク拡張したRGBを持たせ、黒い縁を防ぐ。Loop用は先頭と末尾の形状・明度を接続する。

## 検証・状態
単体連番と任意Seedの同時表示を確認する。シートが煙や写真ノイズだけで輪郭を失わないことを見る。素材の制作仕様であり、実画像・エンジン再生は未実施。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
