---
schema_version: "0.1.0"
id: "recipe/weakening-thrust"
kind: "recipe"
title: "急所突き：一点の赤金の刺突と弱体の刻印"
summary: "短い収束、鋭い刺突、接触から沈む弱体記号で急所を伝える。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["急所突き：一点の赤金の刺突と弱体の刻印","vital-thrust"]
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
  - target: "semantic/attack-debuff"
    type: "expresses"
    reason: "複合構成で伝えるもう一つの意味。"
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "point-focus"
    reason: "刃先へ赤金の点4個を短く集める。"
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "vital-axis"
    reason: "通常刺突より締まった針。長さ0.55L、白芯と赤金の縁。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "急所の接触針を少し長くし、放射を増やさない。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "debuff-mark"
    reason: "対象の外縁に欠けた下向き記号。状態ハンドラが通常/強の形を選ぶ。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "recipe/attack-reduction"
    type: "candidate"
    role: "debuff-state"
    when: "採用先がこの強度の攻撃低下を実際に付与する場合。"
    reason: "通常/強の継続表現を比較して一つ選ぶ。自動採用しない。"
  - target: "recipe/strong-attack-reduction"
    type: "candidate"
    role: "debuff-state"
    when: "採用先がこの強度の攻撃低下を実際に付与する場合。"
    reason: "通常/強の継続表現を比較して一つ選ぶ。自動採用しない。"
evidence: []
superseded_by: []
---

# 急所突き：一点の赤金の刺突と弱体の刻印

## 推奨する主案

一点の精度を主役にし、赤金の接触から暗紫の下降記号へ切り替えて、物理命中と攻撃低下を別に読む。丸い爆発や長い拘束を付け足さない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| point-focus | `technique/converge-motes` | 刃先へ赤金の点4個を短く集める。 | 準備の入力進捗。 |
| vital-axis | `technique/directional-streak` | 通常刺突より締まった針。長さ0.55L、白芯と赤金の縁。 | attack-active、接触ピーク0.04秒、0.12秒侵食。 |
| hit | `recipe/impact-pierce` | 急所の接触針を少し長くし、放射を増やさない。 | 実hit-confirmed。 |
| debuff-mark | `technique/orbit-glyphs` | 対象の外縁に欠けた下向き記号。状態ハンドラが通常/強の形を選ぶ。 | 実effect-appliedで開始、更新後の期限とremoveへ追従。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

刺突接触と弱体継続の部品を共有する。急所の細い赤金と短い準備を固有差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

命中したが弱体が適用されない場合に記号を出さず、弱体延長で表示が早く消えない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [semantic/attack-debuff](../../semantics/attack-debuff.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [recipe/attack-reduction](../states/attack-reduction.md)
- [recipe/strong-attack-reduction](../states/strong-attack-reduction.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
