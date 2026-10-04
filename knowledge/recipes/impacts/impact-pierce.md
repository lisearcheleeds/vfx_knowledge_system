---
schema_version: "0.1.0"
id: "recipe/impact-pierce"
kind: "recipe"
title: "一点へ刺さる刺突の命中"
summary: "攻撃軸の細い白芯、短い圧縮環、背後へ抜ける小片で一点接触を強調する。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["一点へ刺さる刺突の命中","impact-pierce"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/piercing"
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
    role: "axial-contact"
    reason: "接触を貫く細い針。攻撃軸に0.35W、横幅0.02W。"
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "pinch-ring"
    reason: "接触法線へ置く直径0.25Wの薄い輪。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "pin-fragments"
    reason: "攻撃軸に沿う細い片3個。扇状の広い飛散にしない。"
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

# 一点へ刺さる刺突の命中

## 推奨する主案

刺突の説得力は一点の鋭さと前進軸に置く。太い丸い火花より、短い針と締まった圧縮環が武器の精度を伝える。

## 採用先が渡す入力

hit-confirmedの位置と法線を使う。可視の矢やボルトはimpact入力で核を消し、この接触へ引き継ぐ。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| axial-contact | `technique/directional-streak` | 接触を貫く細い針。攻撃軸に0.35W、横幅0.02W。 | 命中0.02秒で点灯、0.08秒で先端から消す。 |
| pinch-ring | `technique/radial-wave` | 接触法線へ置く直径0.25Wの薄い輪。 | 0.03秒で圧縮して開き、0.12秒で畳む。 |
| pin-fragments | `technique/particle-emission` | 攻撃軸に沿う細い片3個。扇状の広い飛散にしない。 | 0.10〜0.18秒、移動0.3W。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

短剣・槍・矢・ボルト・牙・急所突きの小さな接触を共用候補とする。急所の強調は色と軸の長さを変える。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

接触位置が一点で読め、空振りでは反応しない。頭上UIに長い針を伸ばさない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/piercing](../../semantics/piercing.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/directional-streak](../../techniques/directional-streak.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
