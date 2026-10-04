---
schema_version: "0.1.0"
id: "recipe/weapon-scythe"
kind: "recipe"
title: "鎌：途切れない円形の薙ぎ"
summary: "細い円周を刃先に沿って一周展開し、円形攻撃の流れを保つ。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["鎌：途切れない円形の薙ぎ","scythe"]
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
  - target: "technique/arc-sweep"
    type: "composes"
    requirement: "required"
    role: "circular-cut"
    reason: "360度の細い帯。外縁を淡青白、内側を灰緑。幅0.05R。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "scythe-tip-wake"
    reason: "刃先を追う短い細帯。後流が円全体を二重に埋めない。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "各対象の接触線を円の接線に合わせる。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 鎌：途切れない円形の薙ぎ

## 推奨する主案

円形のまとまりと鎌の連続性を一本の細い円周で表す。太い全画面トーラスや複数の同心円を主役にしない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| circular-cut | `technique/arc-sweep` | 360度の細い帯。外縁を淡青白、内側を灰緑。幅0.05R。 | attack-active内で一周を展開し、実有効期間の有効区間へ同期。 |
| scythe-tip-wake | `technique/history-ribbon` | 刃先を追う短い細帯。後流が円全体を二重に埋めない。 | 履歴0.08秒、終了後0.14秒減衰。 |
| hit | `recipe/impact-cut` | 各対象の接触線を円の接線に合わせる。 | ゲームの各hit-confirmedに従う。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

旋風斬と円形弧の原理を共有するが、鎌は細く持続区間に追従する。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

円周の切れ目とUV継ぎ目が目立たず、各対象の実命中が読める。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/arc-sweep](../../techniques/arc-sweep.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-cut](../impacts/impact-cut.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
