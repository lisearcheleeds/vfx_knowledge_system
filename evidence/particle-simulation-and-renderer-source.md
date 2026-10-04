---
schema_version: "0.1.0"
id: "evidence/particle-simulation-and-renderer-source"
kind: "evidence"
title: "粒子シミュレーションと描画方法の分離に関する一次資料"
summary: "Niagaraの公式説明で、一つのEmitterのシミュレーションを複数の描画方法へ対応付けられる例を確認。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["evidence","technique"]
scope: "engine-neutral"
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: "official-documentation"
  claims:
    - target: "technique/particle-emission"
      statement: "粒子のシミュレーションとSprite/Ribbon等の描画は別の軸として扱う。"
  conditions: "Epic GamesのNiagara Overview、参照版4.27の説明を確認。利用対象エンジンの版は未確定。"
  result: "発生・シミュレーションと描画方法を分けて技法ノードを設計する根拠にした。"
  limitations: "Unrealの既知の説明例であり、Unity/Godotへの互換性、???????????での再現、性能を証明しない。"
  sources: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-overview?application_version=4.27"]
  checked_at: "2026-10-04"
---

# 粒子シミュレーションと描画方法の分離に関する一次資料

## 確認内容
公式資料のEmitter説明に、同じシミュレーションをSpriteとRibbonで描画する例がある。粒子の発生・運動と、板・帯・メッシュの描画を別の軸で設計する判断に利用する。

## 限界
参照した説明の版は4.27であり、採用するゲームエンジンの版を4.27に決めたものではない。実際の設定・互換性・性能はAdapterと実行Evidenceで別途確認する。

## 接続する知識

- [technique/particle-emission](../knowledge/techniques/particle-emission.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
