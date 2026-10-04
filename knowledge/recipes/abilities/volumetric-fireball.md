---
schema_version: "0.1.0"
id: "recipe/volumetric-fireball"
kind: "recipe"
title: "ファイアボール：立体の火球と鋭い着弾爆発"
summary: "小さな熱核・方向性のある炎殻・先細り尾・半径Rの一回の爆発を組み合わせる。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["ファイアボール：立体の火球と鋭い着弾爆発","fireball"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/fireball"
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
    role: "cast"
    reason: "手元の橙の点8個を収束し、淡黄の小さな核を作る。"
  - target: "technique/mesh-core"
    type: "composes"
    requirement: "required"
    role: "core"
    reason: "直径0.45Wの球/紡錘。淡黄の芯は直径0.14W、外面は橙。"
  - target: "technique/flipbook-particles"
    type: "composes"
    requirement: "required"
    role: "flame-shell"
    reason: "核の周囲へ向きの異なる炎舌4枚。根元は核、先端は後方へ伸ばす。"
  - target: "technique/history-ribbon"
    type: "composes"
    requirement: "required"
    role: "tail"
    reason: "核の後方へ幅0.22W→先端0の橙の帯。芯は狭く外縁は赤。"
  - target: "technique/flipbook-particles"
    type: "composes"
    requirement: "required"
    role: "explosion-shell"
    reason: "impact中心で低い球状の炎塊6枚を一回解放。煙は小さな房3枚。"
  - target: "technique/radial-wave"
    type: "composes"
    requirement: "required"
    role: "blast-wave"
    reason: "低い薄環が中心から半径R内へ走る。主炎より暗い。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "footprint"
    reason: "実impact位置の地面へ半径Rの細い境界。面はごく薄い橙。"
  - target: "recipe/impact-fire-contact"
    type: "composes"
    requirement: "required"
    role: "hit"
    reason: "範囲内の実命中対象に小さな熱反応。"
  - target: "evaluation/projectile-readability"
    type: "evaluated_by"
    reason: "採用先の実画面で形・イベント・終了条件を確認する。"
  - target: "resource/flame-flipbook"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "resource/smoke-flipbook"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "resource/unit-effect-mesh-kit"
    type: "requires"
    reason: "?????????????????UV??????"
evidence: []
superseded_by: []
---

# ファイアボール：立体の火球と鋭い着弾爆発

## 推奨する主案

主役は粒子の塊ではなく、毎フレーム輪郭が読める立体の熱核にする。少数の連番炎で有機的な揺らぎを加え、飛翔方向は先細り尾、着弾の威力は短い白芯と膨張の差で作る。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| cast | `technique/converge-motes` | 手元の橙の点8個を収束し、淡黄の小さな核を作る。 | 詠唱進捗と発射準備の進捗に同期。 |
| core | `technique/mesh-core` | 直径0.45Wの球/紡錘。淡黄の芯は直径0.14W、外面は橙。 | launch→impact/stop、位置は実投射体。 |
| flame-shell | `technique/flipbook-particles` | 核の周囲へ向きの異なる炎舌4枚。根元は核、先端は後方へ伸ばす。 | 飛翔中は位相をずらし、impactで新規発生停止。 |
| tail | `technique/history-ribbon` | 核の後方へ幅0.22W→先端0の橙の帯。芯は狭く外縁は赤。 | 履歴0.12秒、実速度で尾長実速度×履歴時間の距離、停止後0.20秒減衰。 |
| explosion-shell | `technique/flipbook-particles` | impact中心で低い球状の炎塊6枚を一回解放。煙は小さな房3枚。 | 淡黄ピーク0.03〜0.07秒、橙の膨張0.07〜0.22秒、煙0.60秒まで。 |
| blast-wave | `technique/radial-wave` | 低い薄環が中心から半径R内へ走る。主炎より暗い。 | 0.08〜0.24秒。追加ダメージを持たない美術波。 |
| footprint | `technique/surface-sigil` | 実impact位置の地面へ半径Rの細い境界。面はごく薄い橙。 | impactで全体表示、0.30秒で侵食して終了。 |
| hit | `recipe/impact-fire-contact` | 範囲内の実命中対象に小さな熱反応。 | 実hit-confirmedのみ。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

詠唱収束、投射体、炎素材、熱接触を共有候補にする。炎殻・着弾膨張・尾の比率はこの火球の主案。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

核・尾・着弾を同じ白い雲にしない。明背景で橙の面、暗背景で淡黄の芯が読め、地面の実範囲と着弾瞬間が一致する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/fireball](../../semantics/fireball.md)
- [composition/projectile](../../compositions/projectile.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/mesh-core](../../techniques/mesh-core.md)
- [technique/flipbook-particles](../../techniques/flipbook-particles.md)
- [technique/history-ribbon](../../techniques/history-ribbon.md)
- [technique/radial-wave](../../techniques/radial-wave.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [recipe/impact-fire-contact](../impacts/impact-fire-contact.md)
- [evaluation/projectile-readability](../../evaluation/projectile-readability.md)
- [resource/flame-flipbook](../../resources/flame-flipbook.md)
- [resource/smoke-flipbook](../../resources/smoke-flipbook.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
