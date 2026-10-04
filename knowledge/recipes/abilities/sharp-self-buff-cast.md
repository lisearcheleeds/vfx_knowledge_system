---
schema_version: "0.1.0"
id: "recipe/sharp-self-buff-cast"
kind: "recipe"
title: "号令：自分を押し上げる強化の解放"
summary: "使用者自身の胸から上向きの形を解放し、攻撃強化の小さな記号へ畳む。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["号令：自分を押し上げる強化の解放","command"]
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
    role: "chest-gather"
    reason: "自分の胸/武器へ暖金の点6個を引き込む。"
  - target: "recipe/sharp-self-empowerment"
    type: "composes"
    requirement: "required"
    role: "self-status"
    reason: "胸の短いパルスと上向き山形の解放、その後は小さな強化記号。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 号令：自分を押し上げる強化の解放

## 推奨する主案

胸から上へ押し上げる動きで号令の意思と力を表す。自分の周囲へ大きな同心円を広げて味方へ作用するように見せない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| chest-gather | `technique/converge-motes` | 自分の胸/武器へ暖金の点6個を引き込む。 | 準備の入力進捗。 |
| self-status | `recipe/sharp-self-empowerment` | 胸の短いパルスと上向き山形の解放、その後は小さな強化記号。 | 自分への実状態適用に同期。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

継続の強化カテゴリは鼓舞・食事と共用候補。号令の準備と鋭い上向き解放は専用。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

使用者だけが強化される読みになり、隣のActorへ強化の波が渡らない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-buff](../../semantics/attack-buff.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [recipe/sharp-self-empowerment](../states/sharp-self-empowerment.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
