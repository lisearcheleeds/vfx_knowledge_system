---
schema_version: 0.1.0
id: recipe/weapon-dagger
kind: recipe
title: 短剣の実刺突：小さく鋭い針
summary: 実際に突き刺す攻撃の候補。短剣の素早い切りや判定後の三日月残像は別レシピで選ぶ。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases:
- 短剣：小さく鋭い刺突
- dagger
tags:
- recipe
- combat
scope: engine-neutral
relations:
- target: semantic/piercing
  type: expresses
  reason: この演出が伝える意味と視覚要件。
- target: composition/melee-strike
  type: composes
  requirement: required
  role: lifecycle
  reason: この推奨構成の時間・空間・発動と終了の契約。
- target: composition/combat-readability
  type: composes
  requirement: required
  role: visual-hierarchy
  reason: 主形状・接触・状態の明度と面積を整理する。
- target: technique/directional-streak
  type: composes
  requirement: required
  role: short-thrust
  reason: 刃の軸に沿う0.45Lの針。幅0.025L、暖白の芯。
- target: recipe/impact-pierce
  type: composes
  requirement: required
  role: hit
  reason: 直径0.18Wへ小さく締めた接触。
- target: evaluation/combat-shape-and-events
  type: evaluated_by
  reason: 採用先の実画面で形・イベント・終了条件を確認する。
- target: recipe/completed-slash-afterimage
  type: candidate
  reason: 判定後の完成残像は別構成として選ぶ。
  when: 発火時点で刃が通過済みの空間を表現する場合。
  role: afterimage
evidence: []
superseded_by: []
---

# 短剣の実刺突：小さく鋭い針

## 適用条件の改訂：動作中と判定後を分ける

上記は実際の振り・刺突に同期する初稿候補で、武器全般の唯一の表現ではない。発火時点で刃が通過済みなら、[完成した三日月の残像](../completed-slash-afterimage.md)を先に比較する。このレシピの展開・実履歴・Contactの必須依存を、残像だけのPreviewへ持ち込まない。採用先でSelectionを分ける。

武器名や既存アセット名だけで刺突・斬撃を確定しない。金属色と十分な色面opacityは採用先の美術基準に従い、上の象牙・青灰や秒数を無条件に固定しない。フェードインを保持して、消失との重なりも確認する。旧主案の実装・性能は未検証のまま残す。

## 推奨する主案

実際に突き刺す短剣攻撃を表す場合、短距離の急な前進と接触点を主役にする。粒子の余韻を少なくし、次の短い動作の邪魔をしない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| short-thrust | `technique/directional-streak` | 刃の軸に沿う0.45Lの針。幅0.025L、暖白の芯。 | 振りの終端で0.02秒立上り、0.08秒消失。 |
| hit | `recipe/impact-pierce` | 直径0.18Wへ小さく締めた接触。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

刺突命中を槍と共有し、針長と残留を短剣の差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

接近戦でも手・刃・対象の位置関係が読める。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
