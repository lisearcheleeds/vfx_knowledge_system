---
schema_version: "0.1.0"
id: "recipe/impact-cut"
kind: "recipe"
title: "切断方向を保つ斬撃の命中"
summary: "短い切り線・接触の小さな白芯・法線方向の少数片で切断の瞬間を示す。"
status: "draft"
revision: 2
updated_at: "2026-10-06"
aliases: ["切断方向を保つ斬撃の命中","impact-cut"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/slash"
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
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "contact-line"
    reason: "命中位置に攻撃接線へ沿う細い切り線。長さ0.45W、幅0.025W。"
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "contact-peak"
    reason: "接触側の縁だけ淡い象牙色で一度点灯。対象全身を白くしない。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "cut-fragments"
    reason: "白金色の筋状片4個を法線と攻撃方向の間へ散らす。血や肉片は標準にしない。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "recipe/metal-contact-sparks"
    type: "candidate"
    reason: "金属・硬い対象への命中。少数の伸びた火花と閃き。ユーザー評価の高い実例がある。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "????????????????????????"
evidence: []
superseded_by: []
---

# 切断方向を保つ斬撃の命中

## 推奨する主案

方向を持つ切り線を主役にし、接触の白芯でヒットを確定させる。丸い爆発や大量の火花で切る向きを隠さない。Wは対象の身体幅。

## 採用先が渡す入力

実際のhit-confirmedだけで発生し、swingの時刻から命中を推定しない。複数対象の接触点ごとに小さく再生する。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| contact-line | `technique/directional-streak` | 命中位置に攻撃接線へ沿う細い切り線。長さ0.45W、幅0.025W。 | hit-confirmedで0.02秒立上り、0.10秒侵食。 |
| contact-peak | `technique/body-shell` | 接触側の縁だけ淡い象牙色で一度点灯。対象全身を白くしない。 | 命中直後0.04秒をピーク、0.14秒で終了。 |
| cut-fragments | `technique/particle-emission` | 白金色の筋状片4個を法線と攻撃方向の間へ散らす。血や肉片は標準にしない。 | 寿命0.12〜0.22秒、0.4W以内に収める。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

剣・斧・大剣・鎌・爪で共用候補。線の長さ・厚さ・片の方向は武器ごとに調整する。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

白黒で切る方向が読める。命中がないときは発生せず、連打でも対象の輪郭とUIが見える。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
