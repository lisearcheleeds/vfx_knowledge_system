---
schema_version: "0.1.0"
id: "recipe/weapon-bow"
kind: "recipe"
title: "弓：実体の矢と短い飛翔線"
summary: "可視の矢を主役にし、射出の細い筋と短い尾で実速度の飛翔を読む。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["弓：実体の矢と短い飛翔線","bow"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/piercing"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/projectile"
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
    role: "release"
    reason: "弓の矢の出口に短い銀白の射出筋。"
  - target: "technique/oriented-projectile-core"
    type: "composes"
    requirement: "required"
    role: "arrow"
    reason: "ゲーム側の矢を核に使う。可視矢がなければ矢の素体を用意する。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "flight-trail"
    reason: "白灰の細い一本。矢より暗い。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "小さな刺突接触。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 弓：実体の矢と短い飛翔線

## 推奨する主案

矢を大きな発光球で代用せず、実体と短い尾で方向を見せる。細い射出ピークから落ち着いた飛翔へ切り替える。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| release | `technique/directional-streak` | 弓の矢の出口に短い銀白の射出筋。 | launchで0.07秒。 |
| arrow | `technique/oriented-projectile-core` | ゲーム側の矢を核に使う。可視矢がなければ矢の素体を用意する。 | 位置・速度方向はゲーム入力、実速度。 |
| flight-trail | `technique/history-ribbon` | 白灰の細い一本。矢より暗い。 | 履歴0.05秒、通常速度で尾長実速度×履歴時間の距離。 |
| hit | `recipe/impact-pierce` | 小さな刺突接触。 | impact時、核と尾の新規発生を停止。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

クロスボウ・狙い撃ちと飛翔・接触の部品を共用候補にし、矢の実体と尾の形を区別する。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

高速でも先頭位置を読み取れ、impact後に矢や尾が対象を貫いて残らない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/projectile](../../compositions/projectile.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/oriented-projectile-core](../../techniques/oriented-projectile-core.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [evaluation/projectile-readability](../../evaluation/projectile-readability.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
