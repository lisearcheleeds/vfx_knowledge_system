---
schema_version: "0.1.0"
id: "recipe/attack-reduction"
kind: "recipe"
title: "攻撃低下：欠けた下降記号"
summary: "暗紫の短い付与と、欠けた下向き山形二枚で攻撃低下を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["攻撃低下：欠けた下降記号","attack-reduction"]
tags: ["recipe","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/attack-debuff"
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
    role: "weaken-apply"
    reason: "身体の紫の細い縁が上から下へ沈む。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "broken-mark"
    reason: "短い紫の欠片4個を胸から下へ散らす。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "active"
    reason: "欠けた下向き山形二枚。暗い面と薄い紫の縁。"
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

# 攻撃低下：欠けた下降記号

## 推奨する主案

減少は下降と欠けた形で読む。毒の液滴、麻痺の電撃、拘束の鎖を標準に使わず、攻撃低下の意味へ絞る。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| weaken-apply | `technique/body-shell` | 身体の紫の細い縁が上から下へ沈む。 | applyで0.18秒。 |
| broken-mark | `technique/particle-emission` | 短い紫の欠片4個を胸から下へ散らす。 | 寿命0.25秒、床へ長く残さない。 |
| active | `technique/orbit-glyphs` | 欠けた下向き山形二枚。暗い面と薄い紫の縁。 | 実弱体期間、実状態期間。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

強い弱体と下降記号・付与の原理を共有候補。通常は薄い二枚を維持する。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

付与は一回、継続は小さく、refreshは位相を維持する。実tickと更新後の期限、同カテゴリ集約、解除・消失後の残留を確認する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-debuff](../../semantics/attack-debuff.md)
- [composition/refreshable-status](../../compositions/refreshable-status.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
