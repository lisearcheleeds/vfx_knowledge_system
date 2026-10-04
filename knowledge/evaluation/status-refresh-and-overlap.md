---
schema_version: "0.1.0"
id: "evaluation/status-refresh-and-overlap"
kind: "evaluation"
title: "状態の更新・複合時間・重複表示の評価"
summary: "付与・実際のtick・延長・解除へ追従し、長時間の重なりと表示残留を確認する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["evaluation","status"]
scope: "engine-neutral"
relations: []
evidence: []
superseded_by: []
---

# 状態の更新・複合時間・重複表示の評価

## 操作
各state-idのapply、実tick、refresh、removeを記録して再生する。元期限の直前に再付与し、更新後期限まで継続することを確認する。複数元のHP/MP回復・強化・弱体を同時に適用する。

## 採用条件
tickの視覚パルスは実tickと一致し、固定ローカルタイマーで偽の回復を表示しない。5秒HP回復/60秒強化では5秒側だけ終了する。300秒の状態がフル演出を繰り返さず、対象の動作とUIを覆わない。同カテゴリが一組へ集約され、元の一つが終了しても残りの状態を消さない。

## 強弱・解除
通常と強い弱体を形でも区別する。refreshは継続位相を維持し、remove、死亡、Actor消失、Pool再利用で表示・参照が残らない。画面外復帰でも時間の正本へ追従する。

## 証拠
付与元・state-id・実期限・tick時刻・動画・ログ・測定条件を残す。実行・結果は未取得。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
