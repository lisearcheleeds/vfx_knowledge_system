---
schema_version: "0.1.0"
id: "recipe/weapon-sword"
kind: "recipe"
title: "剣：鋭く薄い扇状の斬撃"
summary: "薄い象牙色の入力角度θ弧と一点の切断反応で、標準的な剣の切れを作る。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["剣：鋭い入力角度θの斬撃","sword"]
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
    role: "blade-arc"
    reason: "入力角度θの弧。外縁は白金、内側は青灰。幅0.07L、根元を細く終端を鋭くする。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "blade-wake"
    reason: "刃の根元と先端の二点から薄い追従帯。主弧より暗く短い。"
  - target: "recipe/impact-cut"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "命中方向に小さな切り線。通常の接触寸法を使う。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 剣：鋭く薄い扇状の斬撃

## 推奨する主案

主役を固定弧にして判定方向と剣の切れを明瞭にし、履歴帯は刃と弧をつなぐ補助にする。大量のスパークより、薄い前縁と鋭い終端の質で仕上げる。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| blade-arc | `technique/arc-sweep` | 入力角度θの弧。外縁は白金、内側は青灰。幅0.07L、根元を細く終端を鋭くする。 | 振りの位相で展開、ピーク0.04秒、残留0.12秒。 |
| blade-wake | `technique/history-ribbon` | 刃の根元と先端の二点から薄い追従帯。主弧より暗く短い。 | 履歴0.06秒、attack-endで発生停止。 |
| hit | `recipe/impact-cut` | 命中方向に小さな切り線。通常の接触寸法を使う。 | hit-confirmedのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

弧・侵食・切断命中を斧や大剣と共有し、幅・曲率・明度曲線を剣専用に持つ。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

白黒で細い弧が読め、軸の後方へ主形状が回り込まない。

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
