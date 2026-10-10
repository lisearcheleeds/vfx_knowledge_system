---
schema_version: "0.1.0"
id: "recipe/weapon-axe"
kind: "recipe"
title: "斧：先端の重い扇状の振り抜き"
summary: "先端が厚い弧と遅れる重い残留で、斧の刃重と振り抜きを見せる。"
status: "draft"
revision: 2
updated_at: "2026-10-07"
aliases: ["斧：先端の重い入力角度θの振り抜き","axe"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "technique/crumbling-heavy-wedge"
    type: "candidate"
    reason: "判定後の残像を作る場合の、武器から推測して作った新しい技法（評価80点）。"
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
    role: "weighted-arc"
    reason: "入力角度θの弧。内側は灰褐色、外縁は暖白。幅0.12L、終端側を太くする。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "head-wake"
    reason: "斧頭の軌跡だけを厚い先端・細い後端でつなぐ。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "標準切断の線幅1.4倍、接触片は短く重い方向。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 斧：先端の重い扇状の振り抜き

## 推奨する主案

斧頭の質量を、弧の外側の厚さと終端に残る形で表す。剣を単純に拡大せず、内側の暗い面と遅れる外縁で重さを作る。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| weighted-arc | `technique/arc-sweep` | 入力角度θの弧。内側は灰褐色、外縁は暖白。幅0.12L、終端側を太くする。 | 振りに追従、終端で0.06秒の形を保持し0.22秒で消す。 |
| head-wake | `technique/history-ribbon` | 斧頭の軌跡だけを厚い先端・細い後端でつなぐ。 | 履歴0.09秒、白い帯にしない。 |
| hit | `recipe/impact-cut` | 標準切断の線幅1.4倍、接触片は短く重い方向。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

弧・履歴・切断命中は共有候補。終端の厚みと持続を斧の固有調整にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

剣より重く読め、暗い面が対象を隠さない。

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

## 判定後の残像（2026-10-07）

このレシピは振りの位相を見せる初期案。判定後に発火する残像は recipe/melee-weapon-afterimages の入口から作る（この武器では technique/crumbling-heavy-wedge）。
