---
schema_version: "0.1.0"
id: "recipe/weapon-fang"
kind: "recipe"
title: "牙：内へ閉じる二点の噛みつき"
summary: "上下の短い針と内向きの圧縮で、噛みつきの締まりを示す。"
status: "draft"
revision: 3
updated_at: '2026-10-08'
aliases: ["牙：内へ閉じる二点の噛みつき","fang"]
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
    role: "jaw-pinch"
    reason: "上下の二本の短い針を口の軸へ寄せる。長さ0.22W。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "接触環を外へ広げず内側へ一度締める。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/articulated-closing-parts"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
  - target: "technique/volumetric-object-proxy"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# 牙：内へ閉じる二点の噛みつき

## 推奨する主案

外へ裂く爪と逆に、内へ閉じる動きを主役にして噛みつきを識別する。血しぶきに依存せず口の位置と接触の圧縮で成立させる。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| jaw-pinch | `technique/directional-streak` | 上下の二本の短い針を口の軸へ寄せる。長さ0.22W。 | 顎の閉じる位相に同期、0.09秒で侵食。 |
| hit | `recipe/impact-pierce` | 接触環を外へ広げず内側へ一度締める。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

刺突の接触を共用し、二点の閉じる形と圧縮方向を差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

対象の外へ針が飛翔するように見えず、口元と接触位置が一致する。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- 噛みつきは実物の噛み合わせの到達状態と、顎の回転で作る。（[technique/articulated-closing-parts](../../techniques/articulated-closing-parts.md)）
- 牙は根元が太く反る立体。（[technique/volumetric-object-proxy](../../techniques/volumetric-object-proxy.md)）
- 噛みつきの命中は受けた側から外へ飛ぶ。（[composition/melee-strike](../../compositions/melee-strike.md)）

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
