---
schema_version: "0.1.0"
id: "recipe/charged-arrow"
kind: "recipe"
title: "狙い撃ち：張り詰めた収束と強い矢"
summary: "細い照準の収束から、鋭い矢の実体と長い一本の尾へ解放する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["狙い撃ち：張り詰めた収束と強い矢","aimed-shot"]
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
  - target: "technique/converge-motes"
    type: "composes"
    requirement: "required"
    role: "aim-gather"
    reason: "矢の根元へ小さな銀白の点6個を集め、最後に一本の細い軸へ締める。"
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "release"
    reason: "通常弓より鋭く、二本の側筋を添えた一閃。"
  - target: "technique/oriented-projectile-core"
    type: "composes"
    requirement: "required"
    role: "arrow"
    reason: "ゲーム側の矢の先端だけ白金に光らせる。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "tail"
    reason: "一本の細い白金の尾。通常矢より長く、先頭を最も明るくする。"
  - target: "recipe/impact-pierce"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "針長1.4倍、接触白芯を一度だけ強くする。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
evidence: []
superseded_by: []
---

# 狙い撃ち：張り詰めた収束と強い矢

## 推奨する主案

精度は照準の一点収束と一直線の尾で表す。大きな球や爆発で威力を誇張せず、通常矢との差は張り詰めた準備・細い長尾・締まった命中で出す。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| aim-gather | `technique/converge-motes` | 矢の根元へ小さな銀白の点6個を集め、最後に一本の細い軸へ締める。 | 準備の入力進捗へ同期。最後の20%で明度上昇。 |
| release | `technique/directional-streak` | 通常弓より鋭く、二本の側筋を添えた一閃。 | launchで0.04秒のピーク、0.10秒終了。 |
| arrow | `technique/oriented-projectile-core` | ゲーム側の矢の先端だけ白金に光らせる。 | 実投射体の位置と向きに追従。 |
| tail | `technique/history-ribbon` | 一本の細い白金の尾。通常矢より長く、先頭を最も明るくする。 | 履歴0.10秒、実速度×0.10秒を尾長の目安にする。 |
| hit | `recipe/impact-pierce` | 針長1.4倍、接触白芯を一度だけ強くする。 | 実impact。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

弓の実体・飛翔・刺突命中を共有候補にする。準備の収束と尾長は固有調整。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

通常弓より強いが輪郭は細い。準備中断で射出・命中が出ない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/projectile](../../compositions/projectile.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/oriented-projectile-core](../../techniques/oriented-projectile-core.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [recipe/impact-pierce](../impacts/impact-pierce.md)
- [evaluation/projectile-readability](../../evaluation/projectile-readability.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
