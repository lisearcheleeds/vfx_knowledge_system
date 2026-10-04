---
schema_version: "0.1.0"
id: "technique/event-pulse"
kind: "technique"
title: "ゲームイベント同期の小さな脈動"
summary: "実際の回復刻みや付与更新を、既存の表示の短い明度変化へ変換する。"
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
evidence: []
superseded_by: []
---

# ゲームイベント同期の小さな脈動

## 主案
回復やrefreshイベントを受けて、既存記号の明度とサイズを短く上げる。毎秒の新しいフル付与や大きな地面環は作らない。立上り30ms、減衰120ms、サイズ最大1.12倍を初期値とする。

## 契約
イベント種、Actor、カテゴリ、発生時刻、強度を入力する。ローカルループで回復が起きたと推測しない。UI数値の生成をVFX側から行わない。

## 重複
同一時刻・同一カテゴリの視覚パルスは一つにまとめる。ゲーム効果の集計・スタックはゲーム側に残す。回復とMP回復の両方がある場合は異なる記号の明度を上げる。

## 評価
イベント欠落、同時刻の複数元、停止直後のtick、再利用先への誤配送を確認する。

## 接続する知識

- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
