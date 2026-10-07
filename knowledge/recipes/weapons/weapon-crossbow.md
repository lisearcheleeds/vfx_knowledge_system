---
schema_version: "0.1.0"
id: "recipe/weapon-crossbow"
kind: "recipe"
title: "クロスボウ：硬い射出と短いボルト"
summary: "鋭い一閃と短い太めのボルトで2半径R/sの機械的な射出を表す。"
status: "draft"
revision: 2
updated_at: "2026-10-08"
aliases: ["クロスボウ：硬い射出と短いボルト","crossbow"]
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
    role: "snap-release"
    reason: "射出口に幅の締まった白芯と二本の短い側筋。"
  - target: "technique/oriented-projectile-core"
    type: "composes"
    requirement: "required"
    role: "bolt"
    reason: "短いボルトの実体。矢より軸が短く鏃を強調。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "bolt-trail"
    reason: "灰白の硬い短尾。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "接触針を短く、白芯を締める。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/volumetric-object-proxy"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# クロスボウ：硬い射出と短いボルト

## 推奨する主案

弓の流れる尾よりも射出の短さとボルトの硬い形を強調する。火薬武器の巨大なマズル炎や煙は追加しない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| snap-release | `technique/directional-streak` | 射出口に幅の締まった白芯と二本の短い側筋。 | launchで0.04秒。 |
| bolt | `technique/oriented-projectile-core` | 短いボルトの実体。矢より軸が短く鏃を強調。 | ゲーム位置・姿勢、2半径R/s。 |
| bolt-trail | `technique/history-ribbon` | 灰白の硬い短尾。 | 履歴0.04秒、通常速度で尾長約0.88m。 |
| hit | `recipe/impact-pierce` | 接触針を短く、白芯を締める。 | impactのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

矢の機構を共用し、核の形、射出時間、尾の長さを差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

弓との違いが発射と核のシルエットで読める。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- ボルトの本体は絵ではなく、矢より短く太い立体。（[technique/volumetric-object-proxy](../../techniques/volumetric-object-proxy.md)）
- 射出に弦の線を重ねない。（[composition/combat-readability](../../compositions/combat-readability.md)）

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
