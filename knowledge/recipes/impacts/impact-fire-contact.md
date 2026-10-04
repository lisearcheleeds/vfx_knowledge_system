---
schema_version: "0.1.0"
id: "recipe/impact-fire-contact"
kind: "recipe"
title: "火炎が触れた対象の小さな熱反応"
summary: "局所の橙の熱い縁と少数の火の粉で、火炎の接触を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["火炎が触れた対象の小さな熱反応","impact-fire-contact"]
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
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "heat-contact"
    reason: "接触側に橙の短い縁、芯は淡黄。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "embers"
    reason: "接触点から上へ火の粉4個。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "????????????????????????"
evidence: []
superseded_by: []
---

# 火炎が触れた対象の小さな熱反応

## 推奨する主案

大きな火炎の本体に対し、各対象の接触は小さく締める。対象ごとに火球爆発を複製せず、炎上状態が定義されていない対象を長時間燃やさない。

## 採用先が渡す入力

実際の命中だけに応答する。継続火傷、追加ダメージ刻み、燃焼ループは作らない。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| heat-contact | `technique/body-shell` | 接触側に橙の短い縁、芯は淡黄。 | hit-confirmedで0.04秒ピーク、0.18秒終了。 |
| embers | `technique/particle-emission` | 接触点から上へ火の粉4個。 | 0.18〜0.32秒、0.25W以内。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

火球爆発・瞬間ブレスの各対象への接触で共用候補。本体の爆発は発生中心で一回だけ作る。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

範囲本体と接触の関係が読め、接触の終了後に炎上状態と誤認させる残留がない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/fire-burst](../../semantics/fire-burst.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
