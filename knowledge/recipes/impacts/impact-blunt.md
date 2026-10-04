---
schema_version: "0.1.0"
id: "recipe/impact-blunt"
kind: "recipe"
title: "押し込んで弾ける打撃の命中"
summary: "幅広い接触星と薄い圧縮波で、打撃の面と重量を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["押し込んで弾ける打撃の命中","impact-blunt"]
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
  - target: "technique/directional-streak"
    type: "composes"
    requirement: "required"
    role: "broad-contact"
    reason: "幅広い5方向の短い星。直径0.45W、最も太い一筋を攻撃軸へ向ける。"
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "compression-wave"
    reason: "接触面に沿う0.25W→0.65Wの薄い輪。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "chips"
    reason: "象牙〜灰色の短い片5個。煙は通常打撃に追加しない。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "????????????????????????"
evidence: []
superseded_by: []
---

# 押し込んで弾ける打撃の命中

## 推奨する主案

一度押し込む幅広い形で衝撃を作り、細い斬撃線との差を出す。重量は明度ピークの短い滞留と圧縮環の遅れで増やす。

## 採用先が渡す入力

接触起点の演出。環の広がりに追加判定を結び付けない。Actorや武器の速度をVFXだけで停止させない。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| broad-contact | `technique/directional-streak` | 幅広い5方向の短い星。直径0.45W、最も太い一筋を攻撃軸へ向ける。 | 0.02秒でピーク、0.12秒で侵食。 |
| compression-wave | `technique/radial-wave` | 接触面に沿う0.25W→0.65Wの薄い輪。 | 0.04秒遅れて解放し、0.18秒で消す。 |
| chips | `technique/particle-emission` | 象牙〜灰色の短い片5個。煙は通常打撃に追加しない。 | 0.15〜0.28秒。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

棒・拳・大盾・強打・剛腕の一撃・地響きの対象接触で共用候補。大技は接触の幅と滞留を拡張し、粒子数だけで差を付けない。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

接触の面が読める。複数対象に同時命中しても圧縮環の合成で画面全体を白くしない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
