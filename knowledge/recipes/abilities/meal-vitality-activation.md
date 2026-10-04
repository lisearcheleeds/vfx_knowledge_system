---
schema_version: "0.1.0"
id: "recipe/meal-vitality-activation"
kind: "recipe"
title: "食事による活力付与：暖かな収束と小さな継続表示"
summary: "対象の胸へ穀粒の形を収束し、暖金の上昇から小さな長寿命の活力表示へ移る。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["まかない料理：暖かな活力の付与","staff-meal"]
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
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "warm-application"
    reason: "対象の胸の薄い暖金のパルス。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "grain-rise"
    reason: "柔らかな穀粒/葉の光点5個が胸から上へ昇る。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "vitality-state"
    reason: "小さな暖金の上向き山形二枚。常時の大きな足元環を作らない。"
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

# 食事による活力付与：暖かな収束と小さな継続表示

## 推奨する主案

食事・施設サービスの付与が成立した対象へ、小さな穀粒の収束と暖金の上昇を一回再生する。攻撃強化が実際に存在する採用先では上向き記号へ接続し、長い光柱を常時維持しない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| warm-application | `technique/body-shell` | 対象の胸の薄い暖金のパルス。 | 施設サービスの実effect-appliedで0.22秒。 |
| grain-rise | `technique/particle-emission` | 柔らかな穀粒/葉の光点5個が胸から上へ昇る。 | 寿命0.45秒、0.5H以内。 |
| vitality-state | `technique/orbit-glyphs` | 小さな暖金の上向き山形二枚。常時の大きな足元環を作らない。 | 実強化のapply/refresh/removeへ追従、更新後の実期限。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

食事の活力と攻撃強化の継続形を共有候補にする。料理の穀粒・暖かな付与は独自差分。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

サービス対象にだけ付与され、5分経過・再付与・移動でも表示が増殖しない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-buff](../../semantics/attack-buff.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
