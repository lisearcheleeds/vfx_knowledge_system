---
schema_version: "0.1.0"
id: "recipe/meal-vitality"
kind: "recipe"
title: "食事由来の活力：暖かな攻撃強化"
summary: "穀粒の上昇と暖金の小さな上向き記号で、食事由来の活力を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["食事由来の活力：暖かな攻撃強化","meal-vitality"]
tags: ["recipe","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/attack-buff"
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
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "apply"
    reason: "胸の薄い暖金のパルス。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "grain-rise"
    reason: "丸い穀粒と短い上向き形を合わせた光点5個。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "active"
    reason: "暖金の小さな上向き山形二枚。粒子の常時放出はしない。"
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

# 食事由来の活力：暖かな攻撃強化

## 推奨する主案

長時間の攻撃強化は、付与の一回を豊かにし、継続は小さな上向き形へ畳む。暖かな色と丸い穀粒で食事由来を伝え、戦闘的な鋭い自己強化と出所を読み分ける。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| apply | `technique/body-shell` | 胸の薄い暖金のパルス。 | applyで0.24秒。 |
| grain-rise | `technique/particle-emission` | 丸い穀粒と短い上向き形を合わせた光点5個。 | 0.45秒の上昇。 |
| active | `technique/orbit-glyphs` | 暖金の小さな上向き山形二枚。粒子の常時放出はしない。 | 更新後の実期限まで。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

攻撃強化の継続形は鋭い/柔らかな自己強化と共用候補にする。食物の摂取表現と効果を分離し、実際に攻撃強化を付与する採用先で使う。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

付与は一回、継続は小さく、refreshは位相を維持する。実tickと更新後の期限、同カテゴリ集約、解除・消失後の残留を確認する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-buff](../../semantics/attack-buff.md)
- [composition/refreshable-status](../../compositions/refreshable-status.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
