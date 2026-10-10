---
schema_version: "0.1.0"
id: "recipe/weapon-greatshield"
kind: "recipe"
title: "大盾：面で押し込む衝撃"
summary: "盾の面に沿う楕円の圧力と幅広い接触で、面の打撃を伝える。"
status: "draft"
revision: 2
updated_at: "2026-10-08"
aliases: ["大盾：面で押し込む衝撃","greatshield"]
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
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "shield-pressure"
    reason: "盾面の法線に沿う楕円環。横幅0.75W、縦幅0.55H。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "接触星は横幅1.3倍、輪は薄く広い。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/wave-direction-semantics"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# 大盾：面で押し込む衝撃

## 推奨する主案

盾の面を使った押し込みを主役にし、刺突の針や魔法バリアの球殻と読み分ける。圧力環は接触面に固定して長時間残さない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| shield-pressure | `technique/radial-wave` | 盾面の法線に沿う楕円環。横幅0.75W、縦幅0.55H。 | 前進終盤で圧縮し、0.14秒で小さく解放。 |
| hit | `recipe/impact-blunt` | 接触星は横幅1.3倍、輪は薄く広い。 | 実命中。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

打撃の接触は共通、楕円比率と面の圧縮が大盾の差分。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

攻撃の面が読め、防御バリアや周囲への範囲攻撃と誤認しない。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- 押し出しの圧は前へ進める。盾の面に沿って横へだけ広げると受け流しに見える。（[technique/wave-direction-semantics](../../techniques/wave-direction-semantics.md)）

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
