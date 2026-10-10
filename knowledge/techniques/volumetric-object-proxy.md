---
schema_version: 0.1.0
id: technique/volumetric-object-proxy
kind: technique
title: 実体の物は絵ではなく単純な立体で表す
summary: 矢・弾・牙など実体のある物は、その絵（アイコン）の板ではなく、縦横比・最も太い位置・反りを合わせた単純な回転体で表す。視点が変わっても物として読め、尾や光と組み合わせやすい。
status: draft
revision: 1
updated_at: '2026-10-08'
aliases:
- アイコン
- 楕円体
- 紡錘
- 回転体
- 立体の代理
tags:
- technique
- projectile
- readable-silhouette
scope: engine-neutral
relations:
- target: technique/oriented-projectile-core
  type: enhances
  reason: 進行方向に向けた本体の形を、絵ではなく立体のシルエットで作る。
- target: technique/mesh-core
  type: enhances
  reason: 本体のメッシュの形の決め方。
evidence:
- evidence/weapon-contact-free-design-preview
superseded_by: []
---

# 実体の物は絵ではなく単純な立体で表す

## 何を伝えるか

飛ぶ矢・ボルト・魔法の矢、噛む牙のように「物」として見せる要素を、物の絵を描いた板（アイコン）にすると、俯瞰や斜めの視点で記号に見え、エフェクトとして浮く。細部を描かず、**シルエットを決める三つの量**だけを合わせた単純な立体にすると、どの視点でも物として読める。

| 量 | 読まれ方の例 |
| --- | --- |
| 縦横比（長さ÷太さ） | 長く細い＝矢、短く太い＝ボルト、太く短い＝弾・牙 |
| 最も太い位置 | 中央＝矢軸の流線形、前寄りで急に尖る＝ダーツ・鏃、根元＝牙 |
| 軸の反り | まっすぐ＝飛ぶ物、根元から先へ反る＝牙・爪・角 |

## 作り方

- 長さ方向の太さの関数を持つ回転体（中央が太い楕円体、前で尖る紡錘、根元が太く反る円錐）にする。断面を少し平たくすると、硬い物の面が出る。
- 面の向きで明るさを変える陰影（上を明るく）を付け、平たい白にしない。明るすぎて白飛びすると陰影が消え、絵に戻る。
- 端は丸く閉じる。開いた断面が見えると筒に見える。
- 尾・光・粒子は立体の外に重ねる。本体の形を光でぼかさない。

## 確認

進行方向の真横・斜め・ほぼ正面から撮り、どの視点でもその物に見えるかを見る。
