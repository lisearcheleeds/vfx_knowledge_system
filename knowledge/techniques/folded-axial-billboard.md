---
schema_version: 0.1.0
id: technique/folded-axial-billboard
kind: technique
title: 折り曲げ式の軸固定ビルボード
summary: 進行軸を保つ中央面とカメラを向く前後面をつなぎ、主形状を折り目で分断しない。
status: draft
revision: 1
updated_at: '2026-10-04'
aliases:
- 折り曲げビルボード
- 軸固定ビルボード
tags:
- technique
- mesh
- billboard
scope: engine-neutral
relations:
- target: resource/unit-effect-mesh-kit
  type: requires
  reason: 頂点・UV・支点を持つ連続面を用意する。
- target: rendering/world-depth-and-transparency
  type: requires
  reason: 透明面の前後関係とカメラ依存を確認する。
- target: adapter/unity-urp-noise-density
  type: implemented_by
  reason: 支点をMeshの追加UVへ格納するUnity例。
evidence:
- evidence/quality-baseline-to-core-only
superseded_by: []
---


# 折り曲げ式の軸固定ビルボード

## 構造と目的

幅方向に2頂点、長さ方向に4列を持つ8頂点・3面・6三角形を使用する。Meshの長さ軸を進行方向に向け、中央面はその軸まわりにカメラを向く。前後の外端は、中央との共有辺を支点として面をカメラへ向ける。共有辺は移動させず、前後面の長さを保つ。

「折り曲げ式」はこの構成の説明名で、特定の標準技法名の主張ではない。軸固定ビルボードと、前後面の折り曲げを組み合わせる。

## 頂点Shaderの対応

カメラ方向から進行軸成分を除いて中央面の向きを求め、進行軸と面の向きの外積で幅方向を得る。前後面では支点からの視線と幅方向の外積を長さ方向に使う。透視カメラでは支点からカメラへの方向、平行投影では共通の視線方向を使う。

軸と視線が一致すると中央面の方向が定まらないため、固定の基準方向を用意する。それでも中央面の投影長がゼロへ近づく性質は残る。MeshのBoundsは頂点Shaderで折り曲げた範囲を含める。CPU上の元の平面だけのBoundsでは消失し得る。

## 折り目は視覚上の区切りに置く

等間隔の3面を先に決め、描画内容を無検討に貼らない。主役の明るい楕円や識別形状が折り目をまたぐと、軸方向に近い視点で縮む中央面とカメラへ向く前後面に分かれ、途中で切れたように見え得る。

1. 色・密度から主役の中心と可視範囲を調べる。ノイズによる位置の揺れも含める。
2. 主役を一つのカメラ向き面へ収め、折り目を低温の尾や役割の境界へ置く。
3. 頂点位置とUVの対応を同時に変更し、横から見た全長・模様の比率を保つ。
4. 支点の情報をMeshが所有し、Shaderへ同じ位置を別定数として写さない。

UVだけを変更すると伸縮比が変わり、頂点だけを変更すると模様の範囲と折り目がずれる。側面の外観を保ちながら区切りを移すには、基準の位置とUVの対応式を維持する。

## 評価と限界

前・後・左右、俯角の変化、透視・平行投影、時間変化で確認する。前側の面を長くするほど頂点の回転範囲と主形状の見かけの位置も変わる。軸方向での中央面の短縮、複数面の重なり、全方向の立体感は解決したと扱わない。[実行Evidence](../../evidence/quality-baseline-to-core-only.md)では主役の分断を避ける比率に変更し、人間の見た目承認を得た。製品実機・全カメラ条件の保証ではない。
