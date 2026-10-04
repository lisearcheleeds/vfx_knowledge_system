---
schema_version: "0.1.0"
id: "composition/targeted-activation"
kind: "composition"
title: "使用者の準備と対象への発動"
summary: "詠唱する使用者と、回復・呪い等を受け取る対象を別の発生位置として扱う。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["combat","magic","lifecycle"]
scope: "engine-neutral"
relations: []
evidence: []
superseded_by: []
---

# 使用者の準備と対象への発動

## 主案
使用者の手・武器・口等の発生点で準備を見せ、target-effect-appliedの実際の対象に発動を表示する。距離のある二地点を一つの原点や一つの長寿命Particle Systemに閉じ込めない。

## 契約
cast-start、cast-progress、cast-complete、target-effect-applied、cancelを意味上の入力とする。cast-progressはゲーム側の実時間から得る。開始時に対象を固定できるとは限らないため、効果対象は適用イベントの対象IDを使う。

## 時間
準備の収束は詠唱進捗に追従し、発動のピークは適用イベントに合わせる。中断した詠唱で対象への成功演出を出さない。投射物が定義されていない効果に、ダメージを運ぶ飛翔弾を追加しない。

## 運用
使用者と対象の消失を独立に処理する。状態の継続表示は状態ハンドラへ引き継ぎ、詠唱の再生尺から期限を計算しない。

## 評価
別対象への切替、中断、対象消失、同時詠唱で原点と発動先が混ざらないことを確認する。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
