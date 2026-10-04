---
schema_version: "0.1.0"
id: "recipe/rest-health-and-mana"
kind: "recipe"
title: "休息回復：静かなHP・MPの識別"
summary: "葉と結晶を小さく並べ、実回復刻みだけに柔らかな脈動を付ける。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["休息回復：静かなHP・MPの識別","rest-health-and-mana"]
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
    role: "rest-apply"
    reason: "胸に低明度の真珠色の薄い縁。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "hp-active"
    reason: "身体外縁のミントの葉二枚。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "mp-active"
    reason: "別の高さに淡青の結晶二枚。葉と同一面に重ねない。"
  - target: "technique/event-pulse"
    type: "composes"
    requirement: "required"
    role: "rest-tick"
    reason: "葉と結晶を同じ実刻みに短く点灯。常時の新しい粒子は出さない。"
  - target: "evaluation/status-refresh-and-overlap"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 休息回復：静かなHP・MPの識別

## 推奨する主案

休憩は戦闘の解放ではなく、静かな二つの識別形で作る。実状態期間の光柱や眠りのZ字、未定義の睡眠状態を追加しない。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| rest-apply | `technique/body-shell` | 胸に低明度の真珠色の薄い縁。 | applyで0.20秒。 |
| hp-active | `technique/orbit-glyphs` | 身体外縁のミントの葉二枚。 | 実HP回復状態中。 |
| mp-active | `technique/orbit-glyphs` | 別の高さに淡青の結晶二枚。葉と同一面に重ねない。 | 実MP回復状態中。 |
| rest-tick | `technique/event-pulse` | 葉と結晶を同じ実刻みに短く点灯。常時の新しい粒子は出さない。 | 実回復刻みのHP/MP回復イベント。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

HPは葉、MPは結晶の共通カテゴリを参照し、他の回復元と同時でも一組ずつへ集約する。

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
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [technique/event-pulse](../../techniques/event-pulse.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
