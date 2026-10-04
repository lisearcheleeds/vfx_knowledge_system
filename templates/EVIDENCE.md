---
schema_version: "0.1.0"
id: evidence/replace-with-observation
kind: evidence
title: "対象の判断を支える記録"
summary: "観察・仮説・結果・限界を分けた根拠の要約。"
status: draft
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: []
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: hypothesis
  claims:
    - target: technique/replace-with-concept
      statement: "根拠の対象となる主張"
  conditions: "対象条件は未確定。"
  result: "未確認。"
  limitations: "実際の再現結果はない。"
  sources: []
  checked_at: null
---

# Evidence作成用テンプレート

知識登録対象外。対象ID・主張・根拠の種類・条件へ置き換える。

## 観察・仮説・結果

それぞれを分ける。出典で確認した仕様と、実機の再現結果を混同しない。

## 未検証範囲

対象外のカメラ・環境・性能等を記録する。

## 実行記録を追加する場合

実際のエンジン実行がある場合だけ、evidence_details.executionにengine、engine_version、renderer、environment、executed_at、procedure、artifactsを記録する。値・画像・動画・ログの所在を創作しない。
