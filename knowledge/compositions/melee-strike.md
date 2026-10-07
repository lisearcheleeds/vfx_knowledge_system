---
schema_version: 0.1.0
id: composition/melee-strike
kind: composition
title: 近接攻撃の振り・接触・残留
summary: 動作中の振り、判定後の残像、実命中の反応を分け、発火時点から主役と時計を選ぶ。
status: draft
revision: 4
updated_at: '2026-10-08'
aliases: []
tags:
- combat
- melee
- lifecycle
scope: engine-neutral
relations:
- target: technique/completed-arc-afterimage
  type: candidate
  reason: 判定後に表示する残像の分岐。
  role: afterimage
- target: recipe/melee-weapon-afterimages
  type: candidate
  reason: 判定後の残像を武器から推測して作る入口。
  role: afterimage
- target: technique/wave-direction-semantics
  type: enhances
  reason: 振り・命中の圧や波の進む向きで、押す・逸らす等の力の意味を決める。
evidence:
- evidence/melee-weapon-free-design-preview
- evidence/weapon-contact-free-design-preview
superseded_by: []
---

# 近接攻撃の振り・接触・残留

## 役割
主役の振りは武器の運動面と入力された攻撃方向に置く。接触反応はhit-confirmedの位置・法線・攻撃ベクトルを受け取る。空振りにも振りを表示し、命中反応は実際の命中時だけ出す。

## 時間・空間
windup/attack-active/attack-endは要求する意味上のイベントであり、ゲームに存在するAPI名ではない。接続時に実際のイベントへ対応付ける。モーション速度変更では振りの位相を攻撃動作に合わせる。ゲーム側のヒット回数を粒子やメッシュの枚数から生成しない。

## 選択
動作中に振りを見せる場合は弧状メッシュのマスク展開を比較する。武器先端の実軌道を見せる部分だけ履歴帯を加える。前方の判定扇形を全方向の円に置き換えない。

## 停止・再利用
中断で主役の展開を止めて0.08秒の視覚減衰に入り、履歴を切る。Pool再利用では座標・帯・命中済みの表示をリセットする。これらの秒数は制作初期値。

## 評価
運動方向、空振り/命中の区別、背後への誤表示、連続攻撃時の帯の接続を確認する。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。

## 発火時点で表現を選ぶ

動作中の刃と、判定後に残った空間は別の時間契約。[完成弧の残像](../techniques/completed-arc-afterimage.md)では外側を初めから完成させ、内部流れと方向の読める消失を動かす。立上りopacityと消失時計は独立にし、直列再生を既定にしない。意味が異なる既存の展開・履歴方式は削除せず、用途を分けて保持する。

## 残像と命中の役割の分担（2026-10-07）

- 判定後の残像は「武器が通った空間・振りの性格」だけを表す。**衝突・命中（衝撃の輪・土煙・火花）は命中の演出（Contact）の仕事**で、残像に入れない。入れると、何を表しているのか分からなくなる（棒の振りに付けた衝撃の輪と土煙、剣の残像の先端の火花が「何か不明」と評価された）。
- 攻撃部位から**前へ飛ぶ粒子は飛び道具・術に見える**。粒子を使うなら振る・斬る向きに沿わせる。
- 残像の再生開始の時点で判定は済んでいる。開く・回るアニメーションにするなら、判定済みの形（完成した弧の線・範囲の円盤）を最初から置く。
- 武器ごとの作り方の入口は recipe/melee-weapon-afterimages。

## 振る側と受ける側の向き（2026-10-08）

- 振り・残像は**攻撃する側の動作の向き**（閉じる・突き出す・振り抜く）を表す。命中（Contact）は**受けた側の反応**で、接触点から外へ飛び散る向きにする。噛みつきの命中で光を内へ閉じると、振りの側の動作を繰り返したように読め、受けた反応に見えない。
- 押す技の圧は前へ、受け流す技の圧は横へ、のように、衝撃の進む向きで力の意味を決める（technique/wave-direction-semantics）。
