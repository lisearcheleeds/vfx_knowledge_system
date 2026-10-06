---
schema_version: 0.1.0
id: resource/signed-distance-mask
kind: resource
title: 輪郭を抜く符号付き距離マスク
summary: 色画像と分離した線形距離データ。単純な場は一枚を変換して共有し、符号・単位・有効域を記録する。
status: draft
revision: 1
updated_at: '2026-10-06'
aliases:
- signed distance field
- SDF Texture
tags:
- combat
scope: engine-neutral
relations: []
evidence:
- evidence/completed-slash-inner-cut-preview
superseded_by: []
---

# 輪郭を抜く符号付き距離マスク

内外の符号、ゼロ境界、距離単位、テクスチャ座標への変換、有効な描画域を記録する。線形データとして扱いsRGB色変換をしない。単なるalpha画像を符号付き距離データと呼ばない。

単位円なら距離は `length(p)-1` で、負が穴の内部。同じ場を楕円座標へ写して共有できるが、非一様Scale後の値はワールド空間の正確な距離ではない。縁幅を画面上で確認する。補間、精度、Clamp/Repeat、Mipの選択で境界が変わるため素材仕様と一緒に記録する。

任意形状や形状間補間には別の距離場が必要な場合がある。一枚の共有素材が全輪郭を表現できるとは限らない。一般マスクAtlasの全セルやFlipbookを必須にせず、実際に採用した場だけを用意する。

本ノードは素材仕様。実際の形式・寸法・サンプリング精度は各実行記録の条件を参照し、他端末での形式対応や費用は未検証として残す。
