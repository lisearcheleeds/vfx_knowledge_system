---
schema_version: 0.1.0
id: adapter/unity-urp-analytic-crescent
kind: adapter
title: Unity URP：弧帯Meshと解析式の三日月Shader
summary: 生成した弧帯MeshにMaterialPropertyBlockで外部経過秒を渡し、Shaderで三日月の形・消え方・外光を計算したPreview実装。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases: []
tags:
- combat
- mesh
scope: engine-specific
relations:
- target: technique/analytic-crescent-uv
  type: requires
  reason: 形と時間の式の正本。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明合成と奥行きの規約。
evidence:
- evidence/sword-slash-analytic-crescent-preview
superseded_by: []
engine: unity
compatibility:
  engine_version: 6000.3.14f1
  renderer: URP 17.3.0
  platforms:
  - Windows Editor
  verification: engine-tested
---

# Unity URP：弧帯Meshと解析式の三日月Shader

## 実行範囲

Unity 6000.3.14f1 / URP 17.3.0 / Windows Editor の専用Prefab Previewで実描画した。engine-testedはこの条件だけ。ゲーム時計・Pool・実機・他APIは未確認。

## 構成

- Mesh: Editorスクリプトで生成した弧の帯（角度160×半径20分割、UV.x=振り始め→振り終わり、UV.y=内縁→外縁）。外縁の外側に外光の余白を含める。
- Shader: URP Unlit相当のHLSL。`Blend One OneMinusSrcAlpha`（前乗算）、ZWrite Off、Cull Off、Queue Transparent。時間は `_EffectTime.x`（外部経過秒）、`_EffectTime.y` をSeed。`_Time` は使わない。縁は `fwidth` でアンチエイリアス。
- 模様: 512×128の周期Value noise（R8、x方向は低周波・y方向は高周波）をScriptで生成し、Texture2Dアセットとして保存。
- 入力: MeshRendererと同じGameObjectの時間入力コンポーネントがMaterialPropertyBlockで時間・Seed・Tintを渡す。Scene配置だけでは時間が進まず、Previewの時計で再生する。
- 火花・閃き: ParticleSystem（Stretched Billboard／Billboard）と加算の小さなShader。ルートのParticleSystemを子の再生の操作口にし、Previewがルートを進める。

## 制作・撮影の手順で効いたこと

- アセットはEditorスクリプト（動的実行）で一括生成し、値を変えて再実行する。既存アセットは削除せず、新しく作った物で中身を上書きする（`EditorUtility.CopySerialized`）。動的実行の制限で `AssetDatabase.DeleteAsset` が使えない環境があった。
- 撮影はPreviewの描画を任意の俯角・方位・距離・時刻で書き出し、一覧画像にして評価する。**ゲームの45度俯瞰だけでなく、振り面の真上からも撮る**。真上で形の欠点（幅の揃った帯）が初めて分かった。
- 生成・撮影に使ったスクリプトは制作物フォルダのEditor/に `.txt` で残す（`.cs` のままだとUnityがコンパイルする）。

## 制限

性能未計測。明るい背景で加算が勝つ。共通Shaderへの統合は未判断（基準版の間はユーザー判断で専用Shaderを許可）。
