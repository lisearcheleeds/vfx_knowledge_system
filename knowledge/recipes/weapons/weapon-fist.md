---
schema_version: "0.1.0"
id: "recipe/weapon-fist"
kind: "recipe"
title: "拳：短い拳圧と鋭い接触"
summary: "拳の前に短い圧縮形状を置き、局所の放射でパンチを締める。"
status: "draft"
revision: 2
updated_at: "2026-10-08"
aliases: ["拳：短い拳圧と鋭い接触","fist"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/blunt-impact"
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
  - target: "technique/cone-burst"
    type: "composes"
    requirement: "required"
    role: "fist-pressure"
    reason: "拳の前へ長さ0.25Wの短い圧力殻。無彩色の薄い面に白い先端。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "接触星を0.35Wへ締め、輪の距離を短くする。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# 拳：短い拳圧と鋭い接触

## 推奨する主案

拳の素早い加速と一点の重さを、小さな前方形状と短い星で表す。巨大な衝撃波を通常パンチの標準にしない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| fist-pressure | `technique/cone-burst` | 拳の前へ長さ0.25Wの短い圧力殻。無彩色の薄い面に白い先端。 | 突き出し終盤0.05秒、接触後0.08秒で終了。 |
| hit | `recipe/impact-blunt` | 接触星を0.35Wへ締め、輪の距離を短くする。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

強打・剛腕の一撃は圧力殻と打撃反応を拡張し、通常拳との差を作る。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

連打時に拳の形が隠れず、空振りは前方の後流だけで終わる。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- 前へ抜ける輪などの繰り返しは二つまで。（[composition/combat-readability](../../compositions/combat-readability.md)）

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/cone-burst](../../techniques/cone-burst.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
