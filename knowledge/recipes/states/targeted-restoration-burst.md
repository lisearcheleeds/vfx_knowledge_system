---
schema_version: "0.1.0"
id: "recipe/targeted-restoration-burst"
kind: "recipe"
title: "対象への短い回復：一度の明瞭な上昇"
summary: "対象のミントの輪郭と一本にまとまる葉の上昇で実状態期間の回復を示す。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["対象への短い回復：一度の明瞭な上昇","targeted-restoration-burst"]
tags: ["recipe","status"]
scope: "engine-neutral"
relations:
  - target: "semantic/restoration"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/refreshable-status"
    type: "composes"
    requirement: "required"
    role: "lifecycle"
    reason: "この推奨構成の時間・空間・発動と終了の契約。"
  - target: "composition/combat-readability"
    type: "composes"
    requirement: "required"
    role: "visual-hierarchy"
    reason: "主形状・接触・状態の明度と面積を整理する。"
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "heal-apply"
    reason: "身体のミントの縁に小さな白芯を一度置く。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "heal-seal"
    reason: "足元の細い環。半径0.40W、内側は透明。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "heal-rise"
    reason: "葉6個を胸から0.55Hまで一本の上昇へまとめる。"
  - target: "evaluation/status-refresh-and-overlap"
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

# 対象への短い回復：一度の明瞭な上昇

## 推奨する主案

回復の成立は身体の輪郭と上向きのまとまった動きに置く。短い効果へ回復刻みのループを追加せず、付与の一回を明瞭にする。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| heal-apply | `technique/body-shell` | 身体のミントの縁に小さな白芯を一度置く。 | applyで0.05秒ピーク、0.22秒終了。 |
| heal-seal | `technique/surface-sigil` | 足元の細い環。半径0.40W、内側は透明。 | applyで0.08秒ピーク、0.26秒侵食。 |
| heal-rise | `technique/particle-emission` | 葉6個を胸から0.55Hまで一本の上昇へまとめる。 | 寿命0.40秒、実状態終了で新規発生を止める。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

ポーションの葉と身体縁を共用候補にし、ヒールは一度の強い上昇を専用曲線にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

付与は一回、継続は小さく、refreshは位相を維持する。実tickと更新後の期限、同カテゴリ集約、解除・消失後の残留を確認する。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/restoration](../../semantics/restoration.md)
- [composition/refreshable-status](../../compositions/refreshable-status.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [technique/particle-emission](../../techniques/particle-emission.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
