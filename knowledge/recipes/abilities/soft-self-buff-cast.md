---
schema_version: "0.1.0"
id: "recipe/soft-self-buff-cast"
kind: "recipe"
title: "鼓舞：短い上昇の鼓動と自己強化"
summary: "短い暖金の上昇で自分を強化し、小さな継続記号へ畳む。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["鼓舞：短い上昇の鼓動と自己強化","encourage"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/attack-buff"
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
    role: "resolve"
    reason: "胸へ暖金の点4個を集める。"
  - target: "recipe/soft-self-empowerment"
    type: "composes"
    requirement: "required"
    role: "encourage-state"
    reason: "小さな身体パルスと上向き記号。号令より軽く短い付与。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 鼓舞：短い上昇の鼓動と自己強化

## 推奨する主案

号令より短い上昇と柔らかな明度で鼓舞を作る。パーティ全体のオーラではなく、自身の動きと力の上向きの読みを主役にする。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| resolve | `technique/converge-motes` | 胸へ暖金の点4個を集める。 | 準備の入力進捗。 |
| encourage-state | `recipe/soft-self-empowerment` | 小さな身体パルスと上向き記号。号令より軽く短い付与。 | 自分への実状態適用・更新・解除。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

攻撃強化の継続カテゴリは号令と共有候補。準備と付与の明度曲線を鼓舞の差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

自己強化として読め、号令との違いが準備の長さと付与形の柔らかさで分かる。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-buff](../../semantics/attack-buff.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [recipe/soft-self-empowerment](../states/soft-self-empowerment.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
