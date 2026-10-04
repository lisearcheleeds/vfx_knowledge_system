---
schema_version: "0.1.0"
id: "technique/converge-motes"
kind: "technique"
title: "詠唱点へ収束する光点"
summary: "発生点へ吸い込む少数の粒子と縮む環で準備の圧力を作る。"
status: "draft"
revision: 1
updated_at: "2026-10-04"
aliases: []
tags: ["technique","combat"]
scope: "engine-neutral"
relations:
  - target: "technique/particle-emission"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "technique/billboard"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
  - target: "rendering/emission-and-opacity"
    type: "requires"
    reason: "この技法の採用時に必要な素材・処理・描画規約。"
evidence: []
superseded_by: []
---

# 詠唱点へ収束する光点

## 主案
手・武器先端・口元の周囲から、6〜10点を弧状に中心へ集める。詠唱の進捗につれて軌道半径を縮め、最後の点が集まった核から発動する。外へ飛散する発動と運動を明確に分ける。

## 時間
ゲーム側のcast/windup進捗に追従し、VFX側で完了時刻を固定しない。終盤20%で明度を上げ、発動前に大きな爆発ピークを置かない。

## 原点・中断
使用者の手/武器/口のソケットへ追従する。元Actorや対象変更で古い原点へ光点を残さない。cancelは80msで暗く畳み、releaseのBurstを出さない。

## 評価
進捗速度変更、途中停止、原点移動、複数Actorの同時詠唱を確認する。

## 接続する知識

- [technique/particle-emission](particle-emission.md)
- [technique/billboard](billboard.md)
- [rendering/emission-and-opacity](../rendering/emission-and-opacity.md)

## 検証状態

実装・エンジン再生・撮影・性能測定は未実施。数値は制作初期値であり、実測値ではない。
