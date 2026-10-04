---
schema_version: "0.1.0"
id: "recipe/self-regeneration"
kind: "recipe"
title: "自己再生：身体を巡る柔らかな回復"
summary: "少数の葉が身体外縁を昇り、実回復刻みで小さく輝く自己再生。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["自己再生：身体を巡る柔らかな回復","self-regeneration"]
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
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "regen-apply"
    reason: "胸から肩へ淡いミントの縁を滑らかに上げる。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "spiral-rise"
    reason: "葉6個が身体の外縁を半周しながら0.5H上昇。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "active"
    reason: "ミントの葉二枚を静かな上昇位相で周回。"
  - target: "technique/event-pulse"
    type: "composes"
    requirement: "required"
    role: "regen-tick"
    reason: "葉のパルスと小さな光点二個の上昇。"
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

# 自己再生：身体を巡る柔らかな回復

## 推奨する主案

再生は身体に沿う柔らかな螺旋で内側から戻る感覚を作る。ポーションの直線上昇と区別し、毎秒の大きな環や全身点灯を繰り返さない。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| regen-apply | `technique/body-shell` | 胸から肩へ淡いミントの縁を滑らかに上げる。 | applyで0.24秒。 |
| spiral-rise | `technique/particle-emission` | 葉6個が身体の外縁を半周しながら0.5H上昇。 | 付与一回、寿命0.50秒。 |
| active | `technique/orbit-glyphs` | ミントの葉二枚を静かな上昇位相で周回。 | 実状態の有効期間。 |
| regen-tick | `technique/event-pulse` | 葉のパルスと小さな光点二個の上昇。 | 実回復刻みイベント。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

HPカテゴリの継続と刻みはポーション/休憩と共用候補。付与の半周上昇が再生の固有差分。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

付与は一回、継続は小さく、refreshは位相を維持する。実tickと更新後の期限、同カテゴリ集約、解除・消失後の残留を確認する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/restoration](../../semantics/restoration.md)
- [composition/refreshable-status](../../compositions/refreshable-status.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [technique/event-pulse](../../techniques/event-pulse.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
