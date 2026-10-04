---
schema_version: "0.1.0"
id: "recipe/wide-weapon-sweep"
kind: "recipe"
title: "広域なぎ払い：横へ押し抜く主弧"
summary: "拡張射程の大きな前方弧を一枚で見せ、広い振り抜きを保持する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["なぎ払い：横へ押し抜く入力角度θの主弧","wide-sweep"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/slash"
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
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "sweep-load"
    reason: "武器の手元へ灰白の筋を短く集める。"
  - target: "technique/arc-sweep"
    type: "composes"
    requirement: "required"
    role: "wide-front-arc"
    reason: "入力角度θ、外半径は入力された拡張された実射程R。外縁は象牙白、内面は薄い灰青。幅0.07R。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "weapon-wake"
    reason: "刃の実軌道へ暗い後流。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "前方に当たった対象だけ小さな切断反応。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 広域なぎ払い：横へ押し抜く主弧

## 推奨する主案

拡張射程の一枚の弧を主役にし、武器から外縁まで連続する内面でなぎ払いの到達を見せる。円形の旋風や複数方向の小弧へ分散しない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| sweep-load | `technique/converge-motes` | 武器の手元へ灰白の筋を短く集める。 | 準備の入力進捗。 |
| wide-front-arc | `technique/arc-sweep` | 入力角度θ、外半径は入力された拡張された実射程R。外縁は象牙白、内面は薄い灰青。幅0.07R。 | attack-activeの振りへ同期、主形保持0.07秒、残留0.24秒。 |
| weapon-wake | `technique/history-ribbon` | 刃の実軌道へ暗い後流。 | 履歴0.10秒。 |
| hit | `recipe/impact-cut` | 前方に当たった対象だけ小さな切断反応。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

剣・斧の弧原理を共用し、入力角度θの広い内面・拡張R・遅い後端を専用差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

背後へ攻撃があるように見せず、外縁がゲームの到達範囲と一致する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/arc-sweep](../../techniques/arc-sweep.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-cut](../impacts/impact-cut.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
