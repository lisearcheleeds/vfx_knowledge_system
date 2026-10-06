---
schema_version: 0.1.0
id: evidence/completed-slash-inner-cut-preview
kind: evidence
title: 斬撃残像の内側SDFと並列立上りのPreview記録
summary: 参照との差を修正し、剣・細い短剣・大型刃の基準版が見た目承認された限定記録。ゲーム統合・性能の承認ではない。
status: reviewed
revision: 1
updated_at: '2026-10-06'
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
  - target: technique/completed-arc-afterimage
    statement: 完成外形を置き、立上り中から輪郭消失を並列に進めた残像の基準版がユーザーに承認された。
  - target: technique/inner-cut-sdf
    statement: 固定外形と内側の距離場を分離し、四段階の参照に合わせた薄い外縁への変化をPreviewで確認した。
  - target: adapter/unity-urp-inner-cut-afterimage
    statement: 外部時計、シーク、保存値、Shaderを専用Editor Previewで検査した。
  conditions: 専用Prefab Preview。ユーザー提供の曲線参照とレビュー。ゲーム用削減・統合前の基準版。
  result: 三種類の残像の見た目がユーザー承認。Riseと輪郭進行の並列を描画で確認。
  limitations: ゲーム統合・実機性能・他エンジン・全画角・独立内部構造レビューは未実施。現在の実装はローカル未コミット。今回は文書更新のみ。
  sources: []
  checked_at: '2026-10-06'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview。Graphics APIはこの記録で再取得していない。
    executed_at: '2026-10-06'
    procedure: 既存task_0366〜0368の実行記録を参照。内側輪郭、Bounds、Rise途中の輪郭進行、シークと終端を実描画し、ユーザーが見た目を確認。
    artifacts:
    - projects/dungeon-inn/runs/slash-afterimage-2026-10-06.md
    - projects/dungeon-inn/runs/slash-afterimage-2026-10-06.artifacts.json
---

# 斬撃残像の内側SDFと並列立上りのPreview記録

## 観察と判定

初稿は振りに沿う展開、薄い色面、短剣の針状形が要求と合わなかった。修正でも一様フェード、直線ワイプ、角度ワイプ、フェードイン省略、Rise後の消失開始が続き、形と時間の要求を同時に維持できなかった。

ユーザーが用意した四段階の曲線参照から、完成外形を保ちながら内側の穴を外縁へ近づけ、戻り側を短くする構成を選んだ。共通の円SDFを内側だけへ使い、外形と色UVを独立させた。最後にRiseと消失を同時開始へ修正し、ユーザーは「これでいい」と見た目を承認した。

## 実行確認

先行する輪郭検査で、最後の薄い外縁の連続性と初期外形内への残留を確認した。最新の並列検査はRiseを中立化した一時Preview Materialと通常Materialを分け、立上り中に輪郭が進むこと、0秒透明、終了後非表示、シーク再現を確認。compileのError/Warningは0。保存された値とShaderを照合した。

## 限界

本ノードのreviewedは、実行済みログとユーザー承認を整理した状態。新たなエンジン再実行や性能測定はしていない。画像・動画を生成せず、ユーザー提供の参照だけを制作記録に保存した。外部に公開済みの実装コミットはまだないため、ローカル保存ファイルのSHA256と作業ログを証拠の固定単位とする。祖先コミットを実装版として扱わない。

基準版の外観承認を最高品質の一般保証、旧ゲーム用版の再承認、製品ゲームへの接続・実機性能の合格へ拡張しない。固有の数値と比較は[共通カタログの採用例入口](../docs/KNOWLEDGE_CATALOG.md)から参照する。
