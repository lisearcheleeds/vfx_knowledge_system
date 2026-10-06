---
schema_version: 0.1.0
id: adapter/unity-urp-inner-cut-afterimage
kind: adapter
title: Unity URP：静止Meshと内側SDFの斬撃残像
summary: MeshRendererへ外部秒・Seed・Tintを渡し、線形円SDFによる内側抜きと色UVを独立に駆動したPreview実装。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases: []
tags:
- combat
scope: engine-specific
relations:
- target: technique/inner-cut-sdf
  type: requires
  reason: 固定外形と内側穴を分ける。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明合成と奥行き規約を確認する。
evidence:
- evidence/completed-slash-inner-cut-preview
superseded_by: []
engine: unity
compatibility:
  engine_version: 6000.3.14f1
  renderer: URP 17.3.0
  platforms:
  - Windows Editor
  verification: engine-tested
---

# Unity URP：静止Meshと内側SDFの斬撃残像

## 実行範囲

Unity 6000.3.14f1 / URP 17.3.0 / Windows Editorの専用Prefab Previewで実描画した。engine-testedはこの限定条件。今回の知識更新ではUnityを再実行していない。ゲーム登録、ゲーム時計・Pool、実機、他APIの描画・性能は未確認。

## 構成と入力

静止MeshをMeshFilter/MeshRendererで描画する。WorldEffectMeshViewはMaterialPropertyBlockで外部経過秒・Seed・Tintを渡す入力コンポーネント。独自Update時計や_Time依存を追加しない。Scene配置だけでは時間が進まず、WorldEffectPrefabPreviewWindowが時計を渡す。シーク後の描画も同じ入力から再現する。

主役の色UV流れ、opacityのRise、内側SDFの輪郭時計を分け、同じ外部秒を原点とする。今回の素材は `_HoldSeconds=0`、`_SdfContourTimes.x=0` を明示する。既存Shaderの既定値には旧開始遅延が残るため、素材の保存値で上書きし照合する。Holdと輪郭開始にRise秒を自動加算しない。SDF座標はローカル面から変換し、色UVアニメーションから独立させる。

## 素材とcoverage

共有Texture2Dは単位円の符号付き距離。線形RFloat、Bilinear/Clamp、Mipなしで作成した。最終形式対応は対象端末で確認する。外側coverageから穴coverageを引き、縁のAAと全体opacityを掛ける。色面のalphaが高い領域を確保する。Transparent QueueとZWrite Offを使うが、これを全面半透明にする指示と解釈しない。

初期Mesh内側より広い描画支持面が必要な箇所ではSDFモードだけ静的なラスタライズ余白を用い、外側coverageで隠す。時間による頂点変形はしていない。拡張後の支持面をBoundsに含め、細い終端のクリップを確認する。

## 編集と保存

Prefab変更はUnity API経由で行う。既存アセット本体→SavePrefabAsset→SaveAssets→ImportAsset(ForceUpdate)を用い、保存状態とディスクの参照を確認し、検証前にgit addで保護する。Sceneの未保存編集を巻き戻さない。

今回のMaterial編集ではSetFloat/SetVector/SetTextureで設定した一部値が保存・再取込後に既定値へ戻る例があり、SerializedObjectのm_SavedPropertiesを通して保存し、再取込値を照合した。Unityのsetter全般が壊れているという結論ではない。メモリ上の値だけで永続化を証明しない。

## 検証と制限

0秒の透明、Rise途中の輪郭進行、終端の非表示、シーク再現、Shaderエラー、保存値を確認した。輪郭進行の検査ではPreview一時MaterialのみRiseを中立化し、輪郭時計が先に進むかを分けて観察した。共有SDFとPropertyBlockの使用はDrawCall統合、SRP Batcher、Instancing、GPU削減を保証しない。性能測定は保留。
