---
schema_version: 0.1.0
id: recipe/weapon-greatsword
kind: recipe
title: 大剣の動作同期：長く厚い弧
summary: 動作中の大型刃と慣性を見せる初稿候補。判定後の幅広い三日月残像は専用レシピを比較する。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases:
- 大剣：長く厚い入力角度θの斬撃
- greatsword
tags:
- recipe
- combat
scope: engine-neutral
relations:
- target: semantic/slash
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
- target: technique/arc-sweep
  type: composes
  requirement: required
  role: long-arc
  reason: 入力角度θの長い弧。幅0.10L、外縁を連続させ内側を二つの大きな裂け目へ分ける。
- target: technique/history-ribbon
  type: composes
  requirement: required
  role: drag-wake
  reason: 刃全体の運動を追う幅広い灰青の帯。
- target: recipe/impact-cut
  type: composes
  requirement: required
  role: hit
  reason: 切断線の長さ1.5倍、幅1.25倍。
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

# 大剣の動作同期：長く厚い弧

## 適用条件の改訂：動作中と判定後を分ける

上記は実際の振り・刺突に同期する初稿候補で、武器全般の唯一の表現ではない。発火時点で刃が通過済みなら、[完成した三日月の残像](../completed-slash-afterimage.md)を先に比較する。このレシピの展開・実履歴・Contactの必須依存を、残像だけのPreviewへ持ち込まない。採用先でSelectionを分ける。

武器名や既存アセット名だけで刺突・斬撃を確定しない。金属色と十分な色面opacityは採用先の美術基準に従い、上の象牙・青灰や秒数を無条件に固定しない。フェードインを保持して、消失との重なりも確認する。旧主案の実装・性能は未検証のまま残す。

## 推奨する主案

長い一本の外縁で大剣の長さを保ち、幅広い後流を暗くして重さを添える。斧の先端重心とは違い、刃全体が運ぶ大きな平面を主役にする。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| long-arc | `technique/arc-sweep` | 入力角度θの長い弧。幅0.10L、外縁を連続させ内側を二つの大きな裂け目へ分ける。 | 立上り0.04秒、形の保持0.08秒、残留0.24秒。 |
| drag-wake | `technique/history-ribbon` | 刃全体の運動を追う幅広い灰青の帯。 | 履歴0.10秒、attack-end後0.18秒減衰。 |
| hit | `recipe/impact-cut` | 切断線の長さ1.5倍、幅1.25倍。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

メッシュ形と命中部品は共有し、長さ・幅・後流・滞留は大剣の差分。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

刃の全長と振り方向が読め、残留が次の攻撃の有効判定に見えない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/slash](../../semantics/slash.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/arc-sweep](../../techniques/arc-sweep.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-cut](../impacts/impact-cut.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
