---
schema_version: "0.1.0"
id: "recipe/instant-fire-cone"
kind: "recipe"
title: "瞬間火炎コーン：太い炎筋と短い残留"
summary: "半径R・入力角度θの前方形状を発動時に一度解放し、太い炎筋と短い残留で仕上げる。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["火炎の息：入力角度θの瞬間的な炎の解放","fire-breath"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/fire-burst"
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
    role: "mouth-load"
    reason: "口元へ橙の点6個と淡黄の小さな核を集める。"
  - target: "technique/cone-burst"
    type: "composes"
    requirement: "required"
    role: "fan-volume"
    reason: "実範囲R・入力角度θへ一致する円錐殻。根元を締め、遠端を5本の炎舌に分ける。"
  - target: "technique/flipbook-particles"
    type: "composes"
    requirement: "required"
    role: "flame-tongues"
    reason: "口から扇の中へ向きの異なる炎板6枚。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "actual-sector"
    reason: "ゲームの範囲中心・前方から半径R/入力角度θの細い地面境界。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "embers"
    reason: "炎筋の後端から火の粉8個。薄い煙2房は扇内の低い余韻。"
  - target: "recipe/impact-fire-contact"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "実対象の小さな熱接触。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "resource/flame-flipbook"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "resource/smoke-flipbook"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "????????????????????????"
evidence: []
superseded_by: []
---

# 瞬間火炎コーン：太い炎筋と短い残留

## 推奨する主案

瞬間ブレスは持続Emitterではなく、方向の強い一回の形の解放にする。円錐殻で範囲を読み、少数の大きな炎舌で生きた炎を作る。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| mouth-load | `technique/converge-motes` | 口元へ橙の点6個と淡黄の小さな核を集める。 | 準備の入力進捗、最後に口の輪郭だけ明るくする。 |
| fan-volume | `technique/cone-burst` | 実範囲R・入力角度θへ一致する円錐殻。根元を締め、遠端を5本の炎舌に分ける。 | 発動時に全体を表示、主ピーク0.04秒、0.25秒で侵食。 |
| flame-tongues | `technique/flipbook-particles` | 口から扇の中へ向きの異なる炎板6枚。 | 一回のBurst、0.18〜0.38秒。長時間の発生をしない。 |
| actual-sector | `technique/surface-sigil` | ゲームの範囲中心・前方から半径R/入力角度θの細い地面境界。 | 発動時に全体表示、0.25秒終了。 |
| embers | `technique/particle-emission` | 炎筋の後端から火の粉8個。薄い煙2房は扇内の低い余韻。 | 火の粉0.45秒、煙0.55秒まで。 |
| hit | `recipe/impact-fire-contact` | 実対象の小さな熱接触。 | 実hit-confirmedのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

火球の炎・煙素材と熱接触は共有候補。円錐と扇境界はブレス専用の主形状。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

発動フレームで扇全体が読め、半径R/入力角度θが正確。残留が継続ブレスや床の火傷に見えない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/fire-burst](../../semantics/fire-burst.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/cone-burst](../../techniques/cone-burst.md)
- [technique/flipbook-particles](../../techniques/flipbook-particles.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [recipe/impact-fire-contact](../impacts/impact-fire-contact.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [resource/flame-flipbook](../../resources/flame-flipbook.md)
- [resource/smoke-flipbook](../../resources/smoke-flipbook.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
