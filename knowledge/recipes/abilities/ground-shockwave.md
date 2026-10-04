---
schema_version: "0.1.0"
id: "recipe/ground-shockwave"
kind: "recipe"
title: "地面衝撃：接地の圧縮と広がる低い波"
summary: "接地の圧縮、正確な境界、薄い地面波、低い粉塵で重い地響きを作る。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["地響き：足元の圧縮と半径Rの地面衝撃","ground-quake"]
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
  - target: "semantic/attack-debuff"
    type: "expresses"
    reason: "複合構成で伝えるもう一つの意味。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "ground-load"
    reason: "足元の小さな土色の圧縮環を収束させる。未発動の半径R全面を地割れで埋めない。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "actual-radius"
    reason: "半径Rの細い境界。薄い土色の面と暖白の外縁。"
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "ground-wave"
    reason: "中心からR内へ低い薄環を一枚解放。"
  - target: "technique/flipbook-particles"
    type: "composes"
    requirement: "required"
    role: "dust"
    reason: "地表近くの土埃4房と短い破片6個。胴体へ昇る煙柱にしない。"
  - target: "recipe/impact-blunt"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "実命中位置の小さな圧縮反応。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "debuff-mark"
    reason: "実状態適用で下降記号を表示。状態ID・強度は実入力を使う。"
  - target: "evaluation/combat-shape-and-events"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "recipe/attack-reduction"
    type: "candidate"
    role: "debuff-state"
    when: "採用先がこの強度の攻撃低下を実際に付与する場合。"
    reason: "通常/強の継続表現を比較して一つ選ぶ。自動採用しない。"
  - target: "recipe/strong-attack-reduction"
    type: "candidate"
    role: "debuff-state"
    when: "採用先がこの強度の攻撃低下を実際に付与する場合。"
    reason: "通常/強の継続表現を比較して一つ選ぶ。自動採用しない。"
  - target: "resource/smoke-flipbook"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 地面衝撃：接地の圧縮と広がる低い波

## 推奨する主案

床に貼り付く圧縮と低い土埃で地面からの力を作る。高い魔法球や巨大な煙で地面・対象を隠さず、固定の実範囲境界と膨張する美術波を分ける。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| ground-load | `technique/surface-sigil` | 足元の小さな土色の圧縮環を収束させる。未発動の半径R全面を地割れで埋めない。 | 詠唱と準備の進捗に同期。 |
| actual-radius | `technique/surface-sigil` | 半径Rの細い境界。薄い土色の面と暖白の外縁。 | 発動イベントで全体を表示、0.25秒で終了。 |
| ground-wave | `technique/radial-wave` | 中心からR内へ低い薄環を一枚解放。 | 発動後0.04〜0.20秒。ゲームの判定進行を代用しない。 |
| dust | `technique/flipbook-particles` | 地表近くの土埃4房と短い破片6個。胴体へ昇る煙柱にしない。 | 粉塵0.55秒、破片0.25秒。 |
| hit | `recipe/impact-blunt` | 実命中位置の小さな圧縮反応。 | hit-confirmed。 |
| debuff-mark | `technique/orbit-glyphs` | 実状態適用で下降記号を表示。状態ID・強度は実入力を使う。 | effect-applied→refresh/remove。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

地面波・粉塵素材・打撃接触・弱体の記号を共用候補にする。足元の圧縮と低い塵の配分は地響き専用。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

発動時に範囲全体が読め、段差で円が壁を通らず、粉塵が対象の足とUIを覆わない。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/blunt-impact](../../semantics/blunt-impact.md)
- [composition/melee-strike](../../compositions/melee-strike.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [semantic/attack-debuff](../../semantics/attack-debuff.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [technique/flipbook-particles](../../techniques/flipbook-particles.md)
- [recipe/impact-blunt](../impacts/impact-blunt.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [recipe/attack-reduction](../states/attack-reduction.md)
- [recipe/strong-attack-reduction](../states/strong-attack-reduction.md)
- [resource/smoke-flipbook](../../resources/smoke-flipbook.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
