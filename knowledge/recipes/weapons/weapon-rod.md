---
schema_version: "0.1.0"
id: "recipe/weapon-rod"
kind: "recipe"
title: "棒：しなる後流と面の打撃"
summary: "棒先の灰白の後流を短くつなぎ、接触で幅広い衝撃へ切り替える。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["棒：しなる後流と面の打撃","rod"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/blunt-impact"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/melee-strike"
    type: "composes"
    requirement: "required"
    role: "lifecycle"
    reason: "この推奨構成の時間・空間・発動と終了の契約。"
  - target: "composition/combat-readability"
    type: "composes"
    requirement: "required"
    role: "visual-hierarchy"
    reason: "主形状・接触・状態の明度と面積を整理する。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "rod-wake"
    reason: "棒の先端側二点から薄い灰白の帯。武器幅の2〜3倍に留める。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "幅広い接触星と圧縮環。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 棒：しなる後流と面の打撃

## 推奨する主案

武器の実運動を後流で拾い、当たった瞬間だけ放射形へ切り替える。棒に剣の刃のような連続した高明度の弧を付けない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| rod-wake | `technique/history-ribbon` | 棒の先端側二点から薄い灰白の帯。武器幅の2〜3倍に留める。 | 履歴0.07秒、終端後0.15秒減衰。 |
| hit | `recipe/impact-blunt` | 幅広い接触星と圧縮環。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

後流は拳・大盾の小さな運動にも流用可能。接触は打撃共通。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

振りの準備と接触が分かれ、棒を斬撃と取り違えない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
