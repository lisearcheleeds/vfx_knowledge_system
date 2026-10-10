---
schema_version: "0.1.0"
id: "recipe/weapon-wand"
kind: "recipe"
title: "ワンド：小さな滴状の魔法弾"
summary: "小さな鋭い滴と短い細尾で、ワンドの1半径R/s射出を軽快に見せる。"
status: "draft"
revision: 2
updated_at: "2026-10-08"
aliases: ["ワンド：小さな滴状の魔法弾","wand"]
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
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "wand-release"
    reason: "ワンド先の細い青白の針と小さな点。"
  - target: "technique/oriented-projectile-core"
    type: "composes"
    requirement: "required"
    role: "dart-core"
    reason: "幅0.10W、長さ0.22Wの滴/紡錘。先端だけ高明度。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "fine-tail"
    reason: "淡青の細い尾。Staffの半分程度の横幅。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "impact"
    reason: "青白の小さな3方向の星へ調整。圧縮環は直径0.22W。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/volumetric-object-proxy"
    type: "enhances"
    reason: "この武器・命中に関わる因子。"
evidence: ["evidence/weapon-contact-free-design-preview"]
superseded_by: []
---

# ワンド：小さな滴状の魔法弾

## 推奨する主案

球を小さくするだけでなく、先端の鋭い滴と短い射出でStaffより軽く速い印象を作る。核・尾・接触を同時に太くしない。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| wand-release | `technique/directional-streak` | ワンド先の細い青白の針と小さな点。 | launchで0.06秒。 |
| dart-core | `technique/oriented-projectile-core` | 幅0.10W、長さ0.22Wの滴/紡錘。先端だけ高明度。 | ゲーム位置・姿勢、1半径R/s。 |
| fine-tail | `technique/history-ribbon` | 淡青の細い尾。Staffの半分程度の横幅。 | 履歴0.09秒、通常速度で約1.08m。 |
| impact | `recipe/impact-blunt` | 青白の小さな3方向の星へ調整。圧縮環は直径0.22W。 | impactで0.12秒。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

Staffと基本部品を共用し、核の縦横比、射出、尾幅、接触形を専用差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

遠距離で小型核を見失わず、Staffとの違いが形で読める。

上記は観察条件であり、成功を確認した記録ではない。

## 関わる因子

- 魔法の矢の芯は丸い光ではなく、前寄りで尖る立体（ダーツの読み）。（[technique/volumetric-object-proxy](../../techniques/volumetric-object-proxy.md)）

## 接続する知識

- [semantic/magic-orb](../../semantics/magic-orb.md)
- [composition/projectile](../../compositions/projectile.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/oriented-projectile-core](../../techniques/oriented-projectile-core.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [evaluation/projectile-readability](../../evaluation/projectile-readability.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
