---
schema_version: "0.1.0"
id: "recipe/foamy-beverage-consumption"
kind: "recipe"
title: "泡のある飲料：短い泡抜けと琥珀の弧"
summary: "クリームの丸点三個と薄い琥珀の小弧を、一度だけ口元から上昇して消す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["泡のある飲料：短い泡抜けと琥珀の弧"]
tags: ["recipe","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/beverage"
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
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "source-accent"
    reason: "クリーム色の小さな丸点三個と薄い琥珀色の弧。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "recipe/food-health-restoration"
    type: "candidate"
    role: "target-effect"
    when: "採用先の実効果にこの意味がある場合。"
    reason: "摂取の見た目とゲーム効果を分離する。食品の分類から状態を必須にしない。"
  - target: "recipe/meal-vitality"
    type: "candidate"
    role: "target-effect"
    when: "採用先の実効果にこの意味がある場合。"
    reason: "摂取の見た目とゲーム効果を分離する。食品の分類から状態を必須にしない。"
  - target: "recipe/restoration-and-vitality"
    type: "candidate"
    role: "target-effect"
    when: "採用先の実効果にこの意味がある場合。"
    reason: "摂取の見た目とゲーム効果を分離する。食品の分類から状態を必須にしない。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "????????????????????????"
evidence: []
superseded_by: []
---

# 泡のある飲料：短い泡抜けと琥珀の弧

## 推奨する主案

クリームの丸点三個と薄い琥珀の小弧を、一度だけ口元から上昇して消す。泡と飲用の満足感を表し、酔い・ふらつきの意味は別途選択する。

## 採用先が渡す入力

摂取の成立、口元/手元の位置、実際に付与された状態を独立した入力にする。失敗・中断で成功の反応を出さない。身体側の状態表示は採用先が選んだ別レシピへ委ね、一回の適用を二重再生しない。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| source-accent | `technique/particle-emission` | クリーム色の小さな丸点三個と薄い琥珀色の弧。 | 実摂取成立時0.18秒で口元から昇って消える。0.15W以内。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

形・色・個数・短い動きはカテゴリ内の調整値。食品名・ItemId・効果時間は採用先の対応表に置く。満腹度、HP回復、攻撃強化等は食品の分類から自動採用しない。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

食品側の短い形と身体側の応答が区別できる。遠景では小さなまとまりを保ち、密集時は光点を増殖させない。実摂取と実状態適用に同期し、再付与で表示を増やさない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/beverage](../../semantics/beverage.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [recipe/food-health-restoration](../states/food-health-restoration.md)
- [recipe/meal-vitality](../states/meal-vitality.md)
- [recipe/restoration-and-vitality](../states/restoration-and-vitality.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
