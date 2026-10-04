---
schema_version: 0.1.0
id: recipe/volumetric-fireball
kind: recipe
title: ファイアボール：立体の火球と鋭い着弾爆発
summary: 内部密度による炎の塊、後方へ流れる侵食面、暖色から煙へ変わる尾、冷却する着弾を組み合わせる。
status: draft
revision: 3
updated_at: '2026-10-04'
aliases:
- ファイアボール：立体の火球と鋭い着弾爆発
- fireball
tags:
- recipe
- combat
scope: engine-neutral
relations:
- target: semantic/fireball
  type: expresses
  reason: 炎の塊の飛翔と、一度の着弾を伝える。
- target: composition/projectile
  type: composes
  reason: 実投射体と発動・終了の契約。
  requirement: required
  role: lifecycle
- target: composition/combat-readability
  type: composes
  reason: 主形状、接触、境界の明度・面積を整理する。
  requirement: required
  role: visual-hierarchy
- target: technique/converge-motes
  type: composes
  reason: 詠唱進捗に従う収束。実行例では後続制作。
  requirement: required
  role: cast
- target: technique/volume-density
  type: composes
  reason: 短い射出の熱解放。飛翔・着弾と尺を統一しない。
  requirement: required
  role: release
- target: technique/volume-density
  type: composes
  reason: 球の面ではなく、侵食され伸びる内部密度を主形状にする。
  requirement: required
  role: core
- target: technique/directional-flow-surface
  type: composes
  reason: 前方から後方へ流れる炎舌。矩形面の境界は動画で要修正。
  requirement: required
  role: flame-shell
- target: technique/history-ribbon
  type: composes
  reason: 実移動の履歴に暖色から暗い煙色への変化を付ける。
  requirement: required
  role: tail
- target: technique/volume-density
  type: composes
  reason: 実位置の後方へ房を重ね、冷却する連続した煙を作る。
  requirement: required
  role: smoke-wake
- target: technique/volume-density
  type: composes
  reason: 種・位置・寿命の異なる房を一回解放し、膨張・冷却させる。
  requirement: required
  role: explosion-shell
- target: technique/radial-wave
  type: composes
  reason: 主炎より暗い薄環を走らせる。追加ダメージを持たない。
  requirement: required
  role: blast-wave
- target: technique/surface-sigil
  type: composes
  reason: 実範囲Rと地面に従う細い境界。
  requirement: required
  role: footprint
- target: recipe/impact-fire-contact
  type: composes
  reason: 実命中対象に小さな熱反応。実行例では後続制作。
  requirement: required
  role: hit
- target: evaluation/projectile-readability
  type: evaluated_by
  reason: 動画、背景、視点、停止、再利用、実範囲を確認する。
- target: technique/mesh-core
  type: alternative
  reason: 固体の核を伝えたい場合や軽量案として比較する。
  role: core
  when: この密度描画を採用できず、硬い輪郭が美術上許容される場合。
- target: technique/flipbook-particles
  type: alternative
  reason: 連番を使う軽量化候補。重複する輪郭と画角を再評価する。
  role: flame-shell
  when: 連番素材の再使用と限定画角で要求を満たせる場合。
- target: technique/surface-density-core
  type: alternative
  reason: 品質基準版を参照し、面近似で必要な見た目を保つゲーム用主役候補。
  role: core
  when: 画角と必要な奥行きが面近似で満たせる場合。
- target: technique/folded-axial-billboard
  type: candidate
  reason: 面上密度のゲーム用候補に適用できる向き。
  role: orientation
evidence:
- evidence/organic-fire-volume-preview
- evidence/quality-baseline-to-core-only
superseded_by: []
---


# ファイアボール：立体の火球と鋭い着弾爆発

## 改訂2の主案

火球は燃える球体ではなく、前方に熱を持ち後方へ流れて裂ける炎の塊にする。境界Meshではなく内部密度を主形状とし、外側の侵食面と煙を足す。Mesh・粒子・Shaderの役割を分け、粒子の数や画像の細部だけで品質を上げようとしない。

これは一つの制作案であり、全ての炎に体積描画を必須にする規約ではない。候補・代替・Adapterは自動採用しない。前案の硬い核と連番炎は代替として残し、現在の主案の必須依存には含めない。

## 入力と所有

詠唱は実進捗、射出は実launch、飛翔は実位置と方向、着弾は実impact、対象反応は実hitへ従う。Actor幅Wと実範囲Rを入力とし、演出から当たり判定や追加ダメージを作らない。ゲーム時計の停止・倍率、投射体消失、teleport、階層切替、再利用の所有は統合側で決める。

## レイヤー構成

| 役割 | 技法 | 形と運動 | 時間・終了 |
| --- | --- | --- | --- |
| cast | converge-motes | 使用者の手元へ熱が収束 | 実詠唱進捗。中断から成功演出を出さない |
| release | volume-density | 前方へ短く解放する熱の房 | launchの一回。投射体の飛翔尺と別 |
| core | volume-density | 内部に熱を持つ大きな房、後方の伸長、動く侵食 | 実投射体へ追従しimpact/stopで終える |
| flame-shell | directional-flow-surface | 長さ・角・Seedの異なる、後方へ流れる薄い炎舌 | 飛翔中のみ。矩形面の境界を動画で確認 |
| tail | history-ribbon | 黄橙→橙→赤→暗い煙色、先細り | 実移動の履歴。発生停止と残留を分離 |
| smoke-wake | volume-density | 後方のworld-spaceの房を重ね、冷却・成長・漂流 | 新規発生停止後は残留寿命で消える |
| explosion-shell | volume-density | 房の寸法・速度・寿命・Seedを変えて一回の膨張 | impactピーク→膨張→冷却→煙。個別の尺を持つ |
| blast-wave | radial-wave | 主炎より暗い圧力の薄環 | impact後の短い解放。範囲判定ではない |
| footprint | surface-sigil | 実地面・範囲Rに従う細い境界 | 移動する美術波と別に固定 |
| hit | impact-fire-contact | 命中した対象だけの小さな熱反応 | 実hitのみ。範囲内全員を推測しない |

## 制作順序

1. 炎の塊だけを作る。別の熱核・面・尾を外しても、硬い球ではなく炎として読めるか確認する。
2. 前方から後方への流れを確かめ、外炎を加える。面が矩形の板に見える、辺から急に生まれる、同じ輪郭が繰り返す場合は補助層を足す前に修正する。
3. 履歴帯と煙を加え、移動速度に対して房が途切れないかを動画で確認する。熱量と不透明度を分ける。
4. 射出と着弾を別に作る。着弾の一瞬の熱ピーク、膨張、冷却、消失を別々に調整する。
5. 見た目の品質基準を確認してから、表示サイズ・密集・実機予算に合わせて削減する。制約を一時保留する場合は採用先の明示判断を記録する。

## 調整と軽量化

房の大きさ、熱、密度、侵食、流れ速度、寿命、発生密度は別の調整口にする。大きな形が崩れている段階で細かなSprite・光点を増やさない。煙の重なりは速度と可視房の幅に合わせる。共通の固定秒数・個数を全レイヤーへ押し付けない。

体積描画の費用は大きい。積分数、煙の房数、画面面積、解像度を比較し、主輪郭と接触の読みを保つ。必要なら面・連番等の代替を選ぶ。削減後の再撮影・実機計測で採用を決める。

## 評価と現在の限界

明暗背景、複数視点、停止、再生、開始・ピーク・冷却・終了を動画で確認する。静止画だけの合格は避ける。実行例では大幅な見た目改善を確認した一方、外炎の矩形面がアニメーションで目立つ指摘が残った。原因切り分けと修正後の確認は未実施。

射出・飛翔・着弾のPreview制作は実施したが、詠唱・対象反応、実ゲーム接続、内部構造の独立レビュー、密集時の性能は未検証。このRecipeはdraft。

## 接続する知識

- [意味](../../semantics/fireball.md)、[投射体の契約](../../compositions/projectile.md)、[戦闘の視覚階層](../../compositions/combat-readability.md)
- [内部密度](../../techniques/volume-density.md)、[方向流れ面](../../techniques/directional-flow-surface.md)、[履歴帯](../../techniques/history-ribbon.md)
- [詠唱収束](../../techniques/converge-motes.md)、[薄環](../../techniques/radial-wave.md)、[地面境界](../../techniques/surface-sigil.md)、[対象の熱反応](../impacts/impact-fire-contact.md)
- 代替：[面の核](../../techniques/mesh-core.md)、[連番粒子](../../techniques/flipbook-particles.md)
- [評価条件](../../evaluation/projectile-readability.md)、[制作の実行記録](../../../evidence/organic-fire-volume-preview.md)


## 改訂3：品質基準版とゲーム用候補を分ける

上の必須構成は高品質の体積基準版を選ぶ場合の構成。ゲーム用へ引き算した後も全層を必須にし続ける意味ではない。まず基準版で目標の輪郭・熱・運動を得て、それを見ながら役割への貢献が小さい外炎・尾・煙・光点を比較し、削除・置換した派生のSelectionを別に記録する。full Recipeを選択しつつ必須依存を黙って省略しない。

軽量化後の主役候補に[面上密度と方向UV流れ](../../techniques/surface-density-core.md)を追加した。向きには[折り曲げ式ビルボード](../../techniques/folded-axial-billboard.md)を比較できる。一つの実例では飛翔Coreだけの見た目が完成品質として承認されたが、煙のある体積基準版全体の価値や、他スキルの必要層を否定しない。射出・着弾の尺・構成を飛翔の削減結果へ合わせない。

ダウンスケールは解像度を下げることだけではない。役割を保つ層の削除、表現方式の近似、Renderer/粒子の整理、画角に合わせた面とUVの再配分を含む。必要な識別・方向・イベント情報まで削らない。実行例と固有の採用値への入口は[変換Evidence](../../../evidence/quality-baseline-to-core-only.md)、共通の段階は[WORKFLOW](../../../WORKFLOW.md)に記録する。
