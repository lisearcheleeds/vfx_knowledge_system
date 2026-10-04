---
schema_version: "0.1.0"
id: "recipe/circular-slash"
kind: "recipe"
title: "旋回斬撃：一周する主弧と低い風の残留"
summary: "半径Rの一周する厚薄のある弧で周囲攻撃を見せる。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["旋風斬：一周する主弧と低い風の残留","whirlwind-slash"]
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
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "coil"
    reason: "武器と腰の周囲へ淡い白青の短線を収束。"
  - target: "technique/arc-sweep"
    type: "composes"
    requirement: "required"
    role: "round-slash"
    reason: "半径Rの360度弧。幅0.10mを初期値にし、先頭を厚く後端を薄くする。"
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "low-wind"
    reason: "低い薄環を主弧の内側へ一枚。白灰、主弧より暗い。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "対象ごとの小さな切断接触。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 旋回斬撃：一周する主弧と低い風の残留

## 推奨する主案

360度の一本の主弧で攻撃の一周を明瞭にする。風の粒子を何周もループさせず、旋回の先頭・厚薄・後端で速度を表す。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| coil | `technique/converge-motes` | 武器と腰の周囲へ淡い白青の短線を収束。 | 準備の入力進捗に同期。 |
| round-slash | `technique/arc-sweep` | 半径Rの360度弧。幅0.10mを初期値にし、先頭を厚く後端を薄くする。 | 発動で一周を実モーションに同期し、残留0.20秒。 |
| low-wind | `technique/radial-wave` | 低い薄環を主弧の内側へ一枚。白灰、主弧より暗い。 | 発動後0.12〜0.28秒で侵食。 |
| hit | `recipe/impact-cut` | 対象ごとの小さな切断接触。 | 実hit-confirmedのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

鎌の円形弧を共有候補にするが、旋風斬の半径・厚み・発動の解放を固有調整にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

一周と範囲が読め、残留の風環を二回目の攻撃と誤認しない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/arc-sweep](../../techniques/arc-sweep.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [recipe/impact-cut](../impacts/impact-cut.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
