---
schema_version: "0.1.0"
id: evaluation/projectile-readability
kind: evaluation
title: 投射体の視認性とライフサイクルの評価
summary: 核・飛翔・着弾・終了を、背景・視点・同時表示・運用条件で確認する評価案。
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: [投射体評価, projectile readability]
tags: [projectile, evaluation, lifecycle]
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
---

# 投射体の評価

## 目的と入力条件

核の位置・飛翔方向・着弾を読み取れ、ゲーム側のイベントと同期し、停止・再利用が成立するかを確認する。Profile、Brief、参照知識版、カメラ、背景、対象端末、同時表示条件、Seedを事前に固定する。

## 操作と観察

1. 発射から飛翔・着弾・終了まで動画を撮る。
2. 明暗の背景、想定する近遠距離・視点、地面・遮蔽、単体・重なりで主要情報を確認する。
3. stop、連続発射、再利用、追従対象の消失を用途に応じて確認する。
4. 対象環境でCPU/GPUを測り、エフェクト有無または変更前後を同条件で比較する。

## 判定と証拠

合格条件と性能予算はProfile/Briefの値を使う。未定なら未判定として記録し、構造検証の成功で代用しない。動画・画像・ログ・測定環境・操作手順・未解決事項を制作記録に残す。

## 状態

評価手順の提案。実際の撮影・観察・計測は未実施。
