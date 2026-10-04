---
schema_version: "0.1.0"
id: "recipe/self-regeneration-cast"
kind: "recipe"
title: "再生：自分を巡る柔らかな回復"
summary: "身体へ収束する薄い緑の流れから、実回復刻みの小さな上昇へ引き継ぐ。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["再生：自分を巡る柔らかな回復","regeneration"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/restoration"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/targeted-activation"
    type: "composes"
    requirement: "required"
    role: "lifecycle"
    reason: "この推奨構成の時間・空間・発動と終了の契約。"
  - target: "composition/combat-readability"
    type: "composes"
    requirement: "required"
    role: "visual-hierarchy"
    reason: "主形状・接触・状態の明度と面積を整理する。"
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "self-gather"
    reason: "自分の胸へミント色の点6個を集める。"
  - target: "recipe/self-regeneration"
    type: "composes"
    requirement: "required"
    role: "regeneration-state"
    reason: "身体に沿う緩い上昇と小さな回復刻み。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 再生：自分を巡る柔らかな回復

## 推奨する主案

再生は爆発的な回復より、身体の中から巡る柔らかい流れを主役にする。毎秒のフル付与を避け、対象自身の輪郭を読める密度に保つ。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| self-gather | `technique/converge-motes` | 自分の胸へミント色の点6個を集める。 | 準備の入力進捗。 |
| regeneration-state | `recipe/self-regeneration` | 身体に沿う緩い上昇と小さな回復刻み。 | 自分への実状態適用、実tick、refresh/remove。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

対象状態のRecipeへ引き継ぎ、スキル側と状態側の二重ループを作らない。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

ヒールの単発上昇と再生の継続が区別され、tickと実回復が一致する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/restoration](../../semantics/restoration.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [recipe/self-regeneration](../states/self-regeneration.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
