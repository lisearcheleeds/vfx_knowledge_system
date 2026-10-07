---
schema_version: "0.1.0"
id: "recipe/weapon-spear"
kind: "recipe"
title: "槍：長い軸を通す刺突"
summary: "槍先から伸びる細い軸と二本の短い側筋で、直線的な到達を見せる。"
status: "draft"
revision: 3
updated_at: '2026-10-08'
aliases: ["槍：長い軸を通す刺突","spear"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/piercing"
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
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "spear-axis"
    reason: "槍先の運動に沿う細い針と、暗い二本の側筋。針長0.35L。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "tip-wake"
    reason: "槍先の細い履歴帯。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "攻撃軸へ長さ1.3倍の接触針。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/axial-thrust-cone"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# 槍：長い軸を通す刺突

## 推奨する主案

槍の長い軸を崩さず、先端の動きと一点の接触に光を置く。太い円錐や剣の扇で前方範囲を広く見せない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| spear-axis | `technique/directional-streak` | 槍先の運動に沿う細い針と、暗い二本の側筋。針長0.35L。 | 前進の終端で明度を上げ、0.12秒で侵食。 |
| tip-wake | `technique/history-ribbon` | 槍先の細い履歴帯。 | 履歴0.05秒。 |
| hit | `recipe/impact-pierce` | 攻撃軸へ長さ1.3倍の接触針。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

短剣と刺突命中・針を共有し、長さ・側筋・短い軌跡で差を出す。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

真横だけでなく斜めの視点でも到達方向が読める。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- 突きは斬撃の帯の変形でなく、伸びる円錐で作る。（[technique/axial-thrust-cone](../../techniques/axial-thrust-cone.md)）

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
