---
schema_version: "0.1.0"
id: "recipe/weapon-claw"
kind: "recipe"
title: "爪：並行する三本の引っかき"
summary: "近接した三本の短い曲線を一回の動作として解放する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["爪：並行する三本の引っかき","claw"]
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
  - target: "technique/arc-sweep"
    type: "composes"
    requirement: "required"
    role: "claw-cuts"
    reason: "三本の短い湾曲帯。間隔0.10W、中央を最も太く、色は象牙灰。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "短い切断反応を一組にまとめる。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 爪：並行する三本の引っかき

## 推奨する主案

三本の平行形状で爪を即座に識別し、線の重なりと中央の重みでまとまりを作る。三本の線を三回ダメージの演出にしない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| claw-cuts | `technique/arc-sweep` | 三本の短い湾曲帯。間隔0.10W、中央を最も太く、色は象牙灰。 | 動作に合わせ、一回の解放で0.015秒ずつ美術上のずれ、0.12秒侵食。 |
| hit | `recipe/impact-cut` | 短い切断反応を一組にまとめる。 | ゲームの実命中のみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

弧メッシュと切断接触は共通、平行本数と短い曲率を爪の差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

小型/大型モンスターで線間隔が読め、空振りと接触が区別できる。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/arc-sweep](../../techniques/arc-sweep.md)
- [recipe/impact-cut](../impacts/impact-cut.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
