---
schema_version: "0.1.0"
id: composition/projectile
kind: composition
title: 投射体のライフサイクル
summary: 発射・飛翔・着弾・終了の役割と、ゲームイベントによる同期を定義する。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [投射体, projectile]
tags: [projectile, lifecycle]
scope: engine-neutral
relations:
  - target: evaluation/projectile-readability
    type: evaluated_by
    reason: 飛翔・着弾・停止の読み取りと運用を確認する。
evidence: []
superseded_by: []
---

# 投射体のライフサイクル

## 役割と優先順位

| 役割 | 必須性 | 契約 |
| --- | --- | --- |
| 核 | 必須 | ゲーム側の投射体位置に追従し、主要な位置・形状を伝える |
| 着弾表示 | 着弾がある用途で必須 | ゲーム側のimpactイベントと位置・法線を起点にする |
| 尾・発射装飾 | 任意 | 方向性や強度を補助する。性能・画面密度に応じて省く |
| 終了処理 | 必須 | stopまたはimpactで発生を止め、残留要素の終了をcompleteとして扱う |

必須の役割は、必須の技法ノードを意味しない。核の技法などはRecipeで候補比較後に選ぶ。削減時も核、必要な着弾情報、終了処理を維持する。

## 時間・空間の関係

飛翔位置・当たり判定・ダメージはゲーム側が決める。着弾を再生開始からの固定秒数で代用しない。尾の発生停止と残留の減衰を分け、再利用時に前回の履歴・パラメータを残さない。

## 評価と状態

[投射体の評価項目](../evaluation/projectile-readability.md)を使用する設計案。実際のイベント同期と停止・再利用は未検証。
