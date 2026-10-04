---
schema_version: "0.1.0"
id: "recipe/targeted-healing-cast"
kind: "recipe"
title: "ヒール：使用者の収束と対象の上昇回復"
summary: "詠唱の小さな環から、対象の回復パルスと上昇する葉へ接続する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["ヒール：使用者の収束と対象の上昇回復","heal"]
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
    role: "healer-cast"
    reason: "使用者の手元へミント色の光点6個を収束。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "healer-seal"
    reason: "手元の小さな輪を0.24Wへ絞る。"
  - target: "recipe/targeted-restoration-burst"
    type: "composes"
    requirement: "required"
    role: "target-heal"
    reason: "対象の身体パルスと葉の上昇は状態適用の一回として再生。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# ヒール：使用者の収束と対象の上昇回復

## 推奨する主案

使用者の準備と対象の回復を別原点にし、対象には明瞭な上昇の形を渡す。長い天上の光柱や未定義の回復弾を追加せず、身体・足元・上昇葉の短い組合せで完成させる。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| healer-cast | `technique/converge-motes` | 使用者の手元へミント色の光点6個を収束。 | 詠唱の入力進捗、終盤に小さな白芯。 |
| healer-seal | `technique/surface-sigil` | 手元の小さな輪を0.24Wへ絞る。 | 詠唱中、cancelで畳む。 |
| target-heal | `recipe/targeted-restoration-burst` | 対象の身体パルスと葉の上昇は状態適用の一回として再生。 | target-effect-applied→実際の状態終了。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

対象側の短い回復Recipeを参照し、詠唱側と状態側から二重の回復Burstを発生させない。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

別Actorの詠唱/対象が区別でき、詠唱中断で対象の回復が点灯しない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/restoration](../../semantics/restoration.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [recipe/targeted-restoration-burst](../states/targeted-restoration-burst.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
