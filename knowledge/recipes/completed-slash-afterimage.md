---
schema_version: 0.1.0
id: recipe/completed-slash-afterimage
kind: recipe
title: 完成した三日月の斬撃残像
summary: 判定後に発火する剣・短剣・大型刃の残像。主役は弧帯UV上の解析式の非対称三日月を優先し、色面の流れ、並列の立上りと消失、先端へ縮む最後を採用する。
status: draft
revision: 2
updated_at: '2026-10-06'
aliases:
- SwordSlash
- DaggerThrust
- GreatswordSlash
- 剣の残像
- 短剣の三日月
tags:
- combat
- recipe
scope: engine-neutral
relations:
- target: technique/completed-arc-afterimage
  type: composes
  reason: 判定後の固定空間に残像を置く。
  requirement: required
  role: afterimage
- target: technique/analytic-crescent-uv
  type: composes
  reason: 非対称の三日月の形・内側の抜き・短縮・外縁と外光を式で連続に作る（改訂2の優先案）。
  requirement: required
  role: contour
- target: technique/inner-cut-sdf
  type: candidate
  reason: 改訂1の主案。参照の内側曲線が円の組み合わせで近似でき、解析式で作りにくい場合に比較する。
- target: semantic/slash
  type: expresses
  reason: 刃の通過方向と形を伝える。
- target: evaluation/combat-shape-and-events
  type: evaluated_by
  reason: 発火時点と時間を含めて確認する。
- target: adapter/unity-urp-inner-cut-afterimage
  type: implemented_by
  reason: Unityで実行した候補（改訂1の内側SDF）。
- target: adapter/unity-urp-analytic-crescent
  type: implemented_by
  reason: Unityで実行した改訂2の解析式三日月。
evidence:
- evidence/completed-slash-inner-cut-preview
- evidence/sword-slash-analytic-crescent-preview
superseded_by: []
---

# 完成した三日月の斬撃残像

## 改訂2：優先する作り方（2026-10-06）

前の版（内側SDF、ユーザー評価65点）を参照せずに作り直した版が85点と評価された。**新しく斬撃の残像を作るときは、まずこの節の作り方から始める。** 詳細は[解析式の三日月](../techniques/analytic-crescent-uv.md)。

1. 主役は一枚の非対称の三日月。厚みの最大を振り終わり寄り（弧の6〜7割）に置き、両端を尖らせる。最大の厚みは外半径の約4割と十分に取る。
2. 色は外縁の細い明部（白に近い淡黄）→ 熱い淡黄 → 内側の橙。主面は不透明寄りで、透明にするのは内縁側だけ。外縁の外側に柔らかい外光を加算で置く。
3. 模様は接線方向に長い筋を振り方向へ流す。内縁は細かく裂くが、外縁と最後の細い外縁は崩さない。
4. 時間は、立上り（尺は保ち前半で大きく上げる）と同時に、内側の抜き（線形寄り）と振り始め側の短縮を始める。細い外縁だけになったら、明るいまま振り終わりの先端へ縮めて消す。
5. **入れないもの**: 暗い補助帯（泥色の爪痕に見える）、先端の火花（振り終わりに目標がいるように読める。火花は命中演出の recipe/metal-contact-sparks へ）。
6. 評価は通常の画角に加えて、振り面の真上からも撮る。真上で形の欠点が分かる。
7. 残る課題は消失の時間カーブ（0.1秒単位）。明るい背景で淡くなる点も未解決。

以下は改訂1の記述。考え方（完成した外形を置く・並列の時間・維持一覧）は引き続き有効。

## 採用契約

刃が通過済みの空間を見せる場合の主案。現在の刃の動きを追うレシピへ無条件に適用しない。攻撃方向、運動面、発火イベント、参照形状、秒単位の尺を採用先から受け取る。見た目からダメージや射程を作らない。

## 主役

[完成弧の残像](../techniques/completed-arc-afterimage.md)に[内側SDF](../techniques/inner-cut-sdf.md)を組み合わせる。外形を覆う静止Mesh、色面のUV流れ、内側穴の変化、細い明部で構成する。立上りと輪郭消失は同じ経過秒から並列に進む。色のある面のopacityは十分に保ち、端だけグラデーションで透明へ落とす。

## 個体差と補助

基準形を共有しても、内側の深さ、帯幅、縦横比、残留を独立にする。細い刃は深い内側抜きと鋭い奥行き、大型刃は幅広い面と少し長い残留で差を出す。前後の残像、履歴Trail、Contact、スパークはこの主案の必須依存に含めない。各役割が必要な場合に選択記録へ追加する。

## 修正・承認

形、色、opacity、立上り、UV流れ、消失方向、終端、既存補助層の維持一覧を作る。部分指摘を直すために他の成立済み要素を削除しない。主役だけ・補助だけ・合成後、通常速度と代表時刻で比較する。内側の抜きを動かしただけで方向性が合うと決めない。

Previewでの実行例はあるが、ゲーム用削減、ゲーム接続、製品端末負荷の合格は別段階。一般化したこのレシピはdraftを維持する。
