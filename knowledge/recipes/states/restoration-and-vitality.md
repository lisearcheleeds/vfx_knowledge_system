---
schema_version: "0.1.0"
id: "recipe/restoration-and-vitality"
kind: "recipe"
title: "回復と活力：独立した二つの状態表示"
summary: "緑の回復と暖金の強化を同時に付与し、実状態期間は強化だけを残す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["回復と活力：独立した二つの状態表示","restoration-and-vitality"]
tags: ["recipe","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/restoration"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/refreshable-status"
    type: "composes"
    requirement: "required"
    role: "lifecycle"
    reason: "この推奨構成の時間・空間・発動と終了の契約。"
  - target: "composition/combat-readability"
    type: "composes"
    requirement: "required"
    role: "visual-hierarchy"
    reason: "主形状・接触・状態の明度と面積を整理する。"
  - target: "semantic/attack-buff"
    type: "expresses"
    reason: "複合構成で伝えるもう一つの意味。"
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "dish-apply"
    reason: "胸にミントの縁、その外へ薄い暖金を一度上昇。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "nourish-rise"
    reason: "葉4個と穀粒4個を分けた二色の短い上昇。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "hp-active"
    reason: "ミントの葉二枚、HPカテゴリ。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "attack-active"
    reason: "暖金の上向き山形二枚、攻撃強化カテゴリ。"
  - target: "technique/event-pulse"
    type: "composes"
    requirement: "required"
    role: "recovery-event"
    reason: "実HP回復が届いた時だけ葉を脈動。"
  - target: "evaluation/status-refresh-and-overlap"
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

# 回復と活力：独立した二つの状態表示

## 推奨する主案

二つの効能を色と形で分け、短い回復が終わったあとに活力だけ残る構造にする。一つの実状態期間オーラに緑を焼き込んで回復が続くように見せない。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| dish-apply | `technique/body-shell` | 胸にミントの縁、その外へ薄い暖金を一度上昇。 | applyで0.22秒。 |
| nourish-rise | `technique/particle-emission` | 葉4個と穀粒4個を分けた二色の短い上昇。 | 0.40秒。 |
| hp-active | `technique/orbit-glyphs` | ミントの葉二枚、HPカテゴリ。 | 実HP機能の有効区間、実状態期間。 |
| attack-active | `technique/orbit-glyphs` | 暖金の上向き山形二枚、攻撃強化カテゴリ。 | 実強化の有効区間、実状態期間。 |
| recovery-event | `technique/event-pulse` | 実HP回復が届いた時だけ葉を脈動。 | 実tickのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

HP表示は栄養/ポーション、強化表示は食事/号令とカテゴリ集約する。料理の二色の付与は固有差分。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

付与は一回、継続は小さく、refreshは位相を維持する。実tickと更新後の期限、同カテゴリ集約、解除・消失後の残留を確認する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/restoration](../../semantics/restoration.md)
- [composition/refreshable-status](../../compositions/refreshable-status.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [semantic/attack-buff](../../semantics/attack-buff.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [technique/event-pulse](../../techniques/event-pulse.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
