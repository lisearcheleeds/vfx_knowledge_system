---
schema_version: 0.1.0
id: adapter/unity-urp-baseline-sheet-particles
kind: adapter
title: Unity URP：時間で動く帯の面と粒子の層で残像を組む
summary: 弧・円環・円盤の帯Meshに外部経過秒で動く汎用のシートShaderを載せ、ParticleSystemの層と組み合わせて近接武器の残像を作ったPreview実装。
status: draft
revision: 1
updated_at: '2026-10-07'
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

## 粒子の配置と向き

- Shape の Circle は既定でXY面にある。`rotation = (90, 0, 0)` で水平面に寝かせると、角度0が+X、90度が+Zになる。弧の範囲の開始角は、GameObjectのY回転（負の値で開始角が+Z側へ回る）で合わせた。
- 公転（orbital）の符号と見た目の回転の向きの関係は、粒子の位置を2時刻 `GetParticles` で読み、`atan2(x, z)` の変化で確かめた。符号を推測で決めて逆回転になった例がある。

## 制限

性能未計測。共通Shaderへの統合は未判断（基準版の間はユーザー判断で新設を許可）。
