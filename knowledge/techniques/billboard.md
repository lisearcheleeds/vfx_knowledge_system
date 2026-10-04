---
schema_version: "0.1.0"
id: technique/billboard
kind: technique
title: ビルボード
summary: カメラに向けた板と素材で核や外周を描く候補。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [ビルボード, billboard, カメラ向きの板]
tags: [billboard, readable-silhouette]
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
---

# ビルボード

## 原理と採用条件

カメラへ向ける板の形状とテクスチャ等の素材で見た目を設計する。想定する投影・距離・視点で核の輪郭が読める場合の候補。Particle、Flipbook、加算合成を一括して必須にする名称ではない。

## 素材・能力要件

板の向きを制御する機能、寸法・原点を定めた板、輪郭や透明度を表す素材、描画方法が必要。素材のチャンネル、アルファ方式、色空間は実装計画で明示する。対応するResource・Rendering・Adapterは追加候補であり未登録。

## 弱点・代替・性能

カメラ移動時の向き、近距離での平面感、交差・ソート、背景による飽和を確認する。立体形状が必要ならメッシュ核と比較する。透明面積や重なりの負荷は対象環境で測定する。

## 状態

設計上の仮説。実装・再現・性能測定は未実施。代替関係の逆方向は索引から取得し、本文側で重複管理しない。
