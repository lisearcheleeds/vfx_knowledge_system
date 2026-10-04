---
schema_version: "0.1.0"
id: "recipe/weakening-gaze"
kind: "recipe"
title: "呪いの眼光：眼の収束と対象の下降刻印"
summary: "使用者の眼の小さな紫の収束から、対象の眼形・下降形へ切り替える。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: ["呪いの眼光：眼の収束と対象の下降刻印","cursed-gaze"]
tags: ["recipe","combat"]
scope: "engine-neutral"
relations:
  - target: "semantic/attack-debuff"
    type: "expresses"
    reason: "この演出が伝える意味と視覚要件。"
  - target: "composition/targeted-activation"
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
    role: "eye-load"
    reason: "使用者の眼/頭部へ紫の点4個を収束。眼の外縁だけ細く点灯。"
  - target: "technique/surface-sigil"
    type: "composes"
    requirement: "required"
    role: "curse-seal"
    reason: "実対象の胸/肩の外縁へ紫の眼形を一回開き、下向きに割る。幅0.35W。"
  - target: "technique/body-shell"
    type: "composes"
    requirement: "required"
    role: "curse-pulse"
    reason: "紫の薄い縁が上から下へ一度沈む。"
  - target: "technique/orbit-glyphs"
    type: "composes"
    requirement: "required"
    role: "debuff-state"
    reason: "欠けた下降記号を低明度で維持。"
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
evidence: []
superseded_by: []
---

# 呪いの眼光：眼の収束と対象の下降刻印

## 推奨する主案

眼光の出所は使用者の眼、結果は対象の下降刻印に置く。両者の間へ恒久的なビームを張らず、呪いの成立と弱体中の読みを分ける。

## 採用先が渡す入力

準備・詠唱は入力された進捗とモーション、飛翔は実位置、命中は実際の適用イベントに同期する。範囲はRと角度θで入力し、レシピの光・波・尾から追加判定を生成しない。状態の期間・強度は実状態に従う。

食品名・スキルID・初期効果期間等のプロジェクト固有情報は、このノードに固定せず採用先の対応表で指定する。このレシピを選んだ後に、主案の必須依存を解決する。

## レイヤー構成

| 役割 | 採用する技法 | 形・素材・配置 | 時間・イベント |
| --- | --- | --- | --- |
| eye-load | `technique/converge-motes` | 使用者の眼/頭部へ紫の点4個を収束。眼の外縁だけ細く点灯。 | 詠唱の入力進捗。 |
| curse-seal | `technique/surface-sigil` | 実対象の胸/肩の外縁へ紫の眼形を一回開き、下向きに割る。幅0.35W。 | target-effect-appliedで0.06秒ピーク、0.28秒で終了。 |
| curse-pulse | `technique/body-shell` | 紫の薄い縁が上から下へ一度沈む。 | 付与後0.22秒。 |
| debuff-state | `technique/orbit-glyphs` | 欠けた下降記号を低明度で維持。 | 実状態の適用・更新・解除へ同期。 |

## 制作初期値と調整

Wは身体幅、Hは身長、Lは武器の可視長、Rは実範囲、θは実範囲の角度。秒数・比率・個数は具体的な初稿を作るための美術初期値で、測定値ではない。採用先の美術、カメラ、イベント、実範囲に合わせて調整する。[制作方針](../../../docs/VFX_ART_DIRECTION.md)を参照する。

## 共用と差分

詠唱収束と弱体カテゴリを共有候補にする。眼形と上から沈む付与を固有差分にする。

## 修正・削減の優先順位

主役の輪郭、接触と適用の一致、必要な範囲境界、状態の識別を保持する。密度や負荷を下げるときは補助光点・細い後流・煙から整理する。構成の改訂はrevisionと索引へ反映し、効果名のプログラム分岐を増やさない。

## 採用時の評価

使用者と対象が離れても出所と結果が読め、遮蔽や中断の成否はゲームの実適用に従う。

上記は観察条件であり、成功を確認した記録ではない。

## 接続する知識

- [semantic/attack-debuff](../../semantics/attack-debuff.md)
- [composition/targeted-activation](../../compositions/targeted-activation.md)
- [composition/combat-readability](../../compositions/combat-readability.md)
- [technique/converge-motes](../../techniques/converge-motes.md)
- [technique/surface-sigil](../../techniques/surface-sigil.md)
- [technique/body-shell](../../techniques/body-shell.md)
- [technique/orbit-glyphs](../../techniques/orbit-glyphs.md)
- [evaluation/combat-shape-and-events](../../evaluation/combat-shape-and-events.md)
- [recipe/attack-reduction](../states/attack-reduction.md)
- [recipe/strong-attack-reduction](../states/strong-attack-reduction.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
