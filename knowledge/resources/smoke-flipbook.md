---
schema_version: "0.1.0"
id: "resource/smoke-flipbook"
kind: "resource"
title: "衝撃後の薄い煙と粉塵Flipbook"
summary: "大きな塊と裂け目を持つ薄い粉塵・煙の素材仕様。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["resource","combat"]
scope: "engine-neutral"
relations: []
evidence: []
superseded_by: []
---

# 衝撃後の薄い煙と粉塵Flipbook

## 主案
1024×1024、8×8セル、64フレーム、RGBA straight alpha。暗灰煙と土色粉塵を同じ色焼込みで兼用せず、明度構造を保ったニュートラル素材を別の色パラメータで調整する。

## 形
3〜5個の大きな房が膨張し、間の穴が開きながら消える。輪郭の残る低周波形状を使い、写真の細かい粒状模様を主役にしない。単発爆発用の非ループ素材とする。

## 描画
煙は通常アルファ合成、加算は使わない。足元の土埃は低い高さに制限し、人物の胴体とUIを覆わない。フレーム補間の二重輪郭を確認する。

## 検証・状態
明暗背景・遠距離・多重表示・地面交差を確認する。実素材は未作成。性能は透明面積と重なりを実機で測定する。

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
