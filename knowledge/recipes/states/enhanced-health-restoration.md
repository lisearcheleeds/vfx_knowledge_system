---
schema_version: "0.1.0"
id: "recipe/enhanced-health-restoration"
kind: "recipe"
title: "強調HP回復：二段の付与と葉の識別"
summary: "ポーションと同じHP言語を保ち、付与の二段の上昇と三枚の葉で上位品を読む。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["強調HP回復：二段の付与と葉の識別","enhanced-health-restoration"]
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
    role: "apply"
    reason: "ミントの身体縁に短い白芯。通常ポーションより縁の幅を1.25倍。"
  - target: "technique/particle-emission"
    type: "composes"
    requirement: "required"
    role: "double-rise"
    reason: "葉8個を二つの高さの束へ分けて上昇。白芯を一束だけに置く。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "active"
    reason: "HPの葉三枚。明度は通常と同程度に抑える。"
  - target: "technique/event-pulse"
    type: "composes"
    requirement: "required"
    role: "recovery-tick"
    reason: "葉の短い脈動と小光点三個。"
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

# 強調HP回復：二段の付与と葉の識別

## 推奨する主案

上位品は開始時の二段上昇と葉の数で読み分け、実状態期間の継続を常時強く発光させない。視覚上の差から回復量を2倍等に推定しない。

## 採用先が渡す入力

状態の付与・実回復刻み・更新・解除を入力にする。期間、回復量、強度、対象範囲は採用先が渡す。付与元と状態側の二重再生を避け、再付与では更新後の期限と表示の位相を維持する。複合状態はそれぞれの有効条件と期限を独立させる。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| apply | `technique/body-shell` | ミントの身体縁に短い白芯。通常ポーションより縁の幅を1.25倍。 | applyで0.05秒ピーク、0.22秒終了。 |
| double-rise | `technique/particle-emission` | 葉8個を二つの高さの束へ分けて上昇。白芯を一束だけに置く。 | 0.00/0.08秒の美術上の二段、寿命0.42秒。 |
| active | `technique/orbit-glyphs` | HPの葉三枚。明度は通常と同程度に抑える。 | 実active中、カテゴリ集約時の上位表現。 |
| recovery-tick | `technique/event-pulse` | 葉の短い脈動と小光点三個。 | 実回復イベントに同期。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

通常ポーションと運用を共有し、上位の付与・三枚の識別をパラメータ差分にする。

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
- [technique/particle-emission](../../techniques/particle-emission.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [technique/event-pulse](../../techniques/event-pulse.md)
- [evaluation/status-refresh-and-overlap](../../evaluation/status-refresh-and-overlap.md)
- [technique/billboard](../../techniques/billboard.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
