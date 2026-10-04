---
schema_version: "0.1.0"
id: "recipe/weapon-staff"
kind: "recipe"
title: "杖：丸い魔法核と柔らかな尾"
summary: "青白い立体の核と細い周回筋で、杖の実速度魔法弾を表す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["杖：丸い魔法核と柔らかな尾","staff"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/magic-orb"
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
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "staff-release"
    reason: "杖先に直径0.30Wの小さな環と青白の点。"
  - target: "technique/oriented-projectile-core"
    type: "composes"
    requirement: "required"
    role: "orb"
    reason: "直径0.20Wの球/紡錘。青白の小さな芯と青の面。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "soft-tail"
    reason: "淡青の先細り尾。核より暗くする。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "impact"
    reason: "魔法接触の小さな放射へ調整。色は青白、土片を光点へ置換。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 杖：丸い魔法核と柔らかな尾

## 推奨する主案

丸い核と少し長い柔らかな尾で、杖の魔力のまとまりを表す。火炎属性や凍結を根拠なく与えず、無属性の青白をこの版の美術主案とする。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| staff-release | `technique/surface-sigil` | 杖先に直径0.30Wの小さな環と青白の点。 | launchで0.12秒、詠唱を追加しない。 |
| orb | `technique/oriented-projectile-core` | 直径0.20Wの球/紡錘。青白の小さな芯と青の面。 | 位置・姿勢はゲーム入力、実速度。 |
| soft-tail | `technique/history-ribbon` | 淡青の先細り尾。核より暗くする。 | 履歴0.12秒、通常速度で約1.半径R。 |
| impact | `recipe/impact-blunt` | 魔法接触の小さな放射へ調整。色は青白、土片を光点へ置換。 | impactで0.16秒。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

ワンドと魔法核の描画・接触を共用候補にし、Staffは丸さと柔らかい尾で区別する。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

核が尾と混ざらず、無属性魔法として炎・回復の配色と識別できる。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/magic-orb](../../semantics/magic-orb.md)
- [composition/projectile](../../compositions/projectile.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [technique/oriented-projectile-core](../../techniques/oriented-projectile-core.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/projectile-readability](../../evaluation/projectile-readability.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
