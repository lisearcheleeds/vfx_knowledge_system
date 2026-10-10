---
schema_version: 0.1.0
id: evidence/skill-baselines-preview
kind: evidence
title: スキル41種を名称から一から作ったPreview記録
summary: 溜め・解放・命中・適用・継続のスキル41種の版1が60〜120点と評価され、指摘が「回転の量と端」「層の棲み分け」「力の出どころ」「継続表示の記号」「命中の星」に集中した記録。
status: reviewed
revision: 1
updated_at: '2026-10-10'
aliases: []
tags:
- combat
- evidence
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: first-party-experiment
  claims:
  - target: technique/rotation-overshoot
    statement: 一周の回転斬りは85点。斬り跡と低い風が360度きっかりで途切れて見え、約390度（1.1回転）回して端をグラデーションにすると自然な回転になると指摘された。手元の小さな渦も390度回してごく短いフェードで消すよう指摘された（85点）。
  - target: technique/radial-layered-vortex
    statement: 回転斬りの溜めは75点で風感が少ない。外周に風、中央にコイル、最外周にほこりと棲み分けると竜巻・渦巻き感が出ると指摘された。
  - target: technique/ignition-burst
    statement: 炎の命中は80点。炎が最初から上へ向かうのでなく、全方位へ一瞬向かってから上へ（コンロの着火のボッ）と指摘された。
  - target: technique/internal-source-leak
    statement: ブレスの溜めで外から内へ集める粒は70点。炎は体内で生まれるので外からの粒は不要で、口内から漏れる光の筋がよいと指摘された。自己再生の溜めは主張しなくてよい（霞は不要、70点）。
  - target: technique/status-flow-particles
    statement: 上向き・下向きの山形の継続表示は60点。表示範囲が広く記号の意味が強い。同じ色の上昇・下降の粒子（弱体は下降する針状の線）にとどめ、色と粒子の向きでバフ・デバフを表すよう指摘された。強い弱体（三枚）は通常の弱体（二枚）と区別が付かず、色で棲み分けるよう指摘された。食事の継続の穂は「食べ物？」と読めなかった。
  - target: composition/combat-readability
    statement: 重い打撃の命中の五方向の星は「ださい」（65・75点）。内側にもう一つ輪を足す方がよく、解放の圧（120点）のような指向性を命中にも持たせてよいと指摘された。回復に輪は入らないが、輪のある版は状態異常の回復なら色を少し青に寄せるだけで100点。実回復の刻みは葉と光を外し、粒を増やして一瞬だけ発生させ、ゆっくり動かすよう指摘された。
  - target: technique/status-flow-particles
    statement: 版2の継続表示（同色の上昇・下降の粒子）は、粒子の速度が速すぎる（0.2倍ぐらいに）と指摘された。
  - target: composition/combat-readability
    statement: 地面の亀裂は地面に付くものなので、大きさがアニメーションするのはおかしいと指摘された。
  conditions: 専用Prefab Preview。暗い背景、主に45度俯瞰。ユーザーがライブPreviewで評価。名称とManifestのラベル・時間から意味を推測し、前任のアセットは参照していない。
  result: 版1は60〜120点。120点は剛腕・強打の解放（前へ押し出す椀形の圧）、110点は呪いの印（眼が開いて割れて落ちる）、100点は火の詠唱・急所突きの収束と命中・狙い撃ちの収束。指摘を直した版2は評価待ち。
  limitations: 一つのカメラ条件・一つのプロジェクトの例。評価点はユーザーの主観。ゲーム接続・実状態への同期・性能は未確認。
  sources: []
  checked_at: '2026-10-10'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview
    executed_at: '2026-10-10'
    procedure: 生成スクリプトで面と粒子の層を作り、連番の一覧画像と粒子の位置の読み取りで確認・修正してからユーザーが評価した。
    artifacts:
    - projects/dungeon-inn/runs/skill-baselines-2026-10-08.md
---

# スキル41種を名称から一から作ったPreview記録

## 判定

近接・投射の因子（収束は内向き、押す圧は前へ、突きは伸びる円錐、点の命中は粒子）を使った溜め・解放・命中は90〜120点だった。指摘は、回る表現の量と端、渦の層の分け方、力の出どころ、継続表示の記号、命中の星に集中した。

## 限界

一つのカメラ条件・一つのプロジェクトの例。版2の評価は未取得。
