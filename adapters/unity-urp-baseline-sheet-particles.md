---
schema_version: 0.1.0
id: adapter/unity-urp-baseline-sheet-particles
kind: adapter
title: Unity URP：時間で動く帯の面と粒子の層で残像を組む
summary: 弧・円環・円盤の帯Meshに外部経過秒で動く汎用のシートShaderを載せ、ParticleSystemの層と組み合わせて近接武器の残像を作ったPreview実装。
status: draft
revision: 3
updated_at: '2026-10-10'
aliases: []
tags:
- combat
- mesh
scope: engine-specific
relations:
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明合成と奥行きの規約。
evidence:
- evidence/melee-weapon-free-design-preview
- evidence/weapon-contact-free-design-preview
- evidence/skill-baselines-preview
superseded_by: []
engine: unity
compatibility:
  engine_version: 6000.3.14f1
  renderer: URP 17.3.0
  platforms:
  - Windows Editor
  verification: engine-tested
---

# Unity URP：時間で動く帯の面と粒子の層で残像を組む

## 実行範囲

Unity 6000.3.14f1 / URP 17.3.0 / Windows Editor の専用Prefab Previewで実描画した。ゲーム接続・性能は未確認。

## 構成

- **シートShader**（前乗算 `Blend One OneMinusSrcAlpha`、ZWrite Off、Cull Off）。帯Mesh（UV.x＝弧に沿って0→1、UV.y＝内縁0→外縁1）の上で次を値で切り替える: くさびの厚み、内外と両端の柔らかさ、外縁の荒れ、雲状／筋状のノイズの模様と流れ、溶解（振り始め側・内側から先に消す偏り、焼けた縁の色）、円環の上を回る窓、扇の骨と骨の間の薄い面、外縁が広がる輪、弧の始めから開く出現。時間は外部経過秒だけ（_Timeを使わない）。
- **粒子Shader**（前乗算、テクスチャのRを形、頂点色で色と透明度。加算の割合を値で）。
- **テクスチャ**: 雲状ノイズ・筋のノイズ・柔らかい丸・煙の塊・細長いレンズ・柔らかい線。スクリプトで生成し、周期のあるものは継ぎ目なし。
- **組み立て**: 一つの生成スクリプトに、面の層（半径・弧の範囲・Materialの値）と粒子の層（テクスチャ・色・ParticleSystemの設定）の配列を差し込む。ルートのParticleSystemを子の再生の操作口にする。

- ParticleSystemの Velocity over Lifetime は、x・y・z の値のモード（定数・曲線）をそろえる。一つの軸だけ曲線にすると速度全体が無視され、粒子が動かない（牙が閉じなかった例）。
- 粒子を離れた点（顎の蝶番など）を中心に回すときは、軌跡の位置の微分を Velocity over Lifetime（Local）、同じ角度の微分を Rotation over Lifetime（3D・分離軸、ラジアン毎秒）の曲線にする。開始の位置と向きは開始時の角度から計算して、GameObjectの位置と startRotation3D に入れる。曲線は標本を多めに取り、`SmoothTangents` で接線を付ける（既定の平らな接線のままだと積分した位置がずれる）。
- 全周の帯（弧0〜360度）の継ぎ目では、補間と微分の補助ピクセルで UV.x がわずかに1を越える。UV.x で分岐・計算する値（厚みの区間など）は `saturate` してから使う。越えた値で厚みが0へ飛び、`fwidth` が巨大になって中心から継ぎ目に沿う細い線が出た例がある（正面では見えず、斜めで見える）。
- ParticleSystemRendererの Max Particle Size は既定 0.5（画面の半分）で、大きな粒（地面の亀裂・炎・身体のまわりの光）が切り詰められる。大きさを指定どおりに見せる粒は上限を外す。上限で切り詰められた見た目で評価を受けた後に外すと、見た目が変わるので大きさを合わせ直す。
- Limit Velocity over Lifetimeの抵抗（drag）は既定で粒子の大きさと速さに比例して強まり、大きな炎や煙がすぐ止まる。届く距離を設計したい粒は、大きさ・速さに比例しない抵抗にする。
- 速度の軸のモードの混在（上記）は見た目では気付きにくいので、生成スクリプトで全てのParticleSystemのx・y・zのモードが一致するかを検査して報告する。
- 帯Mesh を長さ方向の中心線で v＝1 にする細長い帯では、中心線が外縁（d＝0）になる。外縁の柔らかさを大きくすると中心線が暗く抜ける。中心を明るくしたい帯は外縁の柔らかさを0近くにし、柔らかさは内側（両脇）で取る。
- Mesh の粒子に周回する模様のテクスチャを貼るときは、長さ方向を Clamp、周方向を Repeat にする。両方 Repeat だと後端に先端の明るさがにじみ、輪の線が出る。

## 粒子の配置と向き

- Shape の Circle は既定でXY面にある。`rotation = (90, 0, 0)` で水平面に寝かせると、角度0が+X、90度が+Zになる。弧の範囲の開始角は、GameObjectのY回転（負の値で開始角が+Z側へ回る）で合わせた。
- 公転（orbital）の符号と見た目の回転の向きの関係は、粒子の位置を2時刻 `GetParticles` で読み、`atan2(x, z)` の変化で確かめた。符号を推測で決めて逆回転になった例がある。

## 制限

性能未計測。共通Shaderへの統合は未判断（基準版の間はユーザー判断で新設を許可）。
