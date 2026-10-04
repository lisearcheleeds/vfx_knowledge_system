---
schema_version: 0.1.0
id: technique/surface-density-core
kind: technique
title: 面上の密度近似と方向UV流れによる主形状
summary: 体積積分の外観を参照し、面上の密度・侵食・熱色で主役を近似する。
status: draft
revision: 1
updated_at: '2026-10-04'
aliases:
- 密度近似
- 方向UVアニメーション
tags:
- technique
- mesh
- readable-silhouette
scope: engine-neutral
relations:
- target: resource/periodic-density-noise
  type: requires
  reason: 房と侵食の運動を同一ノイズで作る。
- target: rendering/emission-and-opacity
  type: requires
  reason: 温度色と不透明度を分けて計算する。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明面の重なりと裏面を確認する。
- target: technique/folded-axial-billboard
  type: candidate
  reason: 進行方向を保ちながら面上の主形状を見せる候補。
  role: orientation
- target: technique/volume-density
  type: alternative
  reason: 内部密度・奥行き・画角の要件が面近似では満たせない場合に比較する。
  role: core
- target: adapter/unity-urp-noise-density
  type: implemented_by
  reason: 固定MeshRendererと外部時間入力で描画するUnity例。
evidence:
- evidence/quality-baseline-to-core-only
superseded_by: []
---


# 面上の密度近似と方向UV流れによる主形状

## 原理と適用

最高品質の基準版で必要な輪郭・明部・流れを確認した後、必要な外観を面上で近似する。画角を限定でき、実際の内部奥行きや厚みによる吸収より、輪郭と熱の塊が主な手掛かりになる場合の候補。体積描画と同じ現象を再現する技法ではない。

UV上に明るい主房、後方の低温房、尾の房を配置する。例えば `exp(-dot((p-center)*inverseRadius,(p-center)*inverseRadius))` を重ね、座標ノイズと侵食で輪郭を崩す。密度からalpha、主房とノイズから熱を求め、熱に応じて淡黄・橙・赤・低温色へ変える。単純な球の外形を固定する必要はない。

## UVの運動と時間

前端をUVの小さい値、後端を大きい値へ対応させ、模様の参照座標を `uv - velocity * elapsed` とする。正のvelocityでは可視模様がUVの正方向へ動く。位置・進行軸・UVの向きの対応を再生して確認する。ノイズの色成分や周波数を、侵食・中心線・座標変位へ分担する。

時間は外部の再生時計から渡す。UVアニメーションはShaderが模様の参照位置を変える方式で、CPUでMesh UVを書き換える必要はない。MeshRendererに置いただけでは時計は進まない。生成時Seedを固定し、シーク・停止・再利用で入力をリセットする。ゲーム時計とPreview時計は接続範囲を区別する。

## 輪郭マスク

流れる色・侵食の座標と、Mesh端を隠す元UVのマスクを分ける。四辺で最終alphaをゼロにし、ノイズが端の描画を復活させない。

不自然な底辺・三角形の角を薄くするだけでは、輪郭の形は残る。必要なら前端の断面幅を半楕円のようにゼロから広げ、後端へ細める輪郭マスクを別に掛ける。侵食はその内側で行う。主役と補助層を切り離して評価し、角を丸めても補助層の貢献が小さければ削除候補にする。

## 限界と根拠

平面の画角・折り目・遮蔽・透明合成で見え方が変わる。全方向の体積代替、GPU時間の一定倍率改善、バッチ成立を保証しない。[折り曲げ式](folded-axial-billboard.md)は選択候補で必須ではない。[削減の実行Evidence](../../evidence/quality-baseline-to-core-only.md)にUnityでの実例を記録。共通技法はdraft。
