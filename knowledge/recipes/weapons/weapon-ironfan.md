---
schema_version: "0.1.0"
id: "recipe/weapon-ironfan"
kind: "recipe"
title: "鉄扇：薄い三筋の切り返し"
summary: "扇の外縁から短い三筋を出し、軽い金属の切り返しを見せる。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["鉄扇：薄い三筋の切り返し","ironfan"]
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
    role: "fan-wake"
    reason: "扇の外縁を薄い帯で追う。幅0.025L、銀灰。"
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "fan-rays"
    reason: "扇の接線へ三本の短い筋。長さ0.35L、中央だけ白芯。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "薄い接触星、小さな圧縮環。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 鉄扇：薄い三筋の切り返し

## 推奨する主案

軽い金属の外縁と扇の切り返しを、薄い線の組で表す。見た目が扇でも、マスタの直接攻撃を入力角度θ等の範囲攻撃として描かない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| fan-wake | `technique/history-ribbon` | 扇の外縁を薄い帯で追う。幅0.025L、銀灰。 | 履歴0.045秒、0.10秒減衰。 |
| fan-rays | `technique/directional-streak` | 扇の接線へ三本の短い筋。長さ0.35L、中央だけ白芯。 | 振りの終端0.07秒。 |
| hit | `recipe/impact-blunt` | 薄い接触星、小さな圧縮環。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

細帯と筋の技法を共用し、扇の外縁の三筋が識別点。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

扇の形を残し、画面上の装飾線が遠隔攻撃に見えない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
