---
schema_version: "0.1.0"
id: "recipe/charged-heavy-impact"
kind: "recipe"
title: "剛腕の一撃：長い圧縮からの強い一点解放"
summary: "入力進捗区間の溜めを腕の圧縮で見せ、幅広い命中と遅れる圧力で重さを作る。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["剛腕の一撃：長い圧縮からの強い一点解放","mighty-blow"]
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
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "arm-load"
    reason: "腕/武器の打点へ暖白の点8個を集める。終盤は核を小さく締める。"
  - target: "technique/cone-burst"
    type: "composes"
    requirement: "required"
    role: "arm-pressure"
    reason: "前方0.40Wの太い圧力殻。灰金の面に小さな白芯。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "heavy-hit"
    reason: "接触星の幅1.8倍、ピーク保持0.08秒、圧縮環は二枚目を暗く遅らせる。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 剛腕の一撃：長い圧縮からの強い一点解放

## 推奨する主案

威力の差は長い収束、短い圧縮、接触の広さ、余韻の遅れで作る。画面を白くする巨大な球や、定義されていない地面範囲波を加えない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| arm-load | `technique/converge-motes` | 腕/武器の打点へ暖白の点8個を集める。終盤は核を小さく締める。 | 準備の入力進捗、最後の0.15秒で圧縮を強める。 |
| arm-pressure | `technique/cone-burst` | 前方0.40Wの太い圧力殻。灰金の面に小さな白芯。 | attack-activeで一度解放、0.12秒で畳む。 |
| heavy-hit | `recipe/impact-blunt` | 接触星の幅1.8倍、ピーク保持0.08秒、圧縮環は二枚目を暗く遅らせる。 | 実hit-confirmed。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

通常拳・強打と圧力殻/打撃反応を共有し、入力進捗区間の準備と幅広い接触を剛腕専用にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

溜めが解放の強さに結び付き、空振りで大きな命中反応が発生しない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/cone-burst](../../techniques/cone-burst.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
