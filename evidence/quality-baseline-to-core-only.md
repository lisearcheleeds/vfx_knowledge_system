---
schema_version: 0.1.0
id: evidence/quality-baseline-to-core-only
kind: evidence
title: 品質基準版からCore単独への削減と見た目承認
summary: 高品質の体積火球を起点に、補助層の削除・面近似・折り目修正を経て飛翔の見た目承認を得た例。
status: reviewed
revision: 1
updated_at: '2026-10-04'
aliases:
- ダウンスケール
- 最高品質からゲーム用アセットへの変換
tags:
- evidence
- fire
- projectile
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: first-party-experiment
  claims:
  - target: technique/surface-density-core
    statement: 体積火球の主役を方向UV流れと面上密度近似へ置換し、補助層を削除した飛翔Coreの見た目が完成品質として承認された。
  - target: technique/folded-axial-billboard
    statement: 明部をまたぐ等間隔の折り目を尾側へ移し、8頂点を維持して前後方向の分断を避ける構成へ修正した。
  - target: technique/directional-flow-surface
    statement: 開始フェードだけでは底辺の角の改善が小さく、輪郭マスクの改訂後も補助層は不要と判断された。
  - target: adapter/unity-urp-noise-density
    statement: 固定描画をMeshRendererへ整理し、粒子なしのPreview時計とシーク、前後左右・平行投影を実行確認した。
  conditions: Unityの隔離Editor Preview。ゲーム制約を保留した高品質版を起点にユーザーの実物レビューで削減。飛翔だけの承認。
  result: 飛翔はCoreのMeshRenderer1つ、ParticleSystem0個、8頂点・6三角形。ユーザーが完成品質と承認。
  limitations: 製品ゲームへの登録・時計・イベント・Pool・階層復元・密集時GPU/CPU計測は未実施。軸方向での中央面短縮は残る。独立内部構造レビュー・全画角・他エンジンは未検証。画像・動画を再生成せずライブPreviewで確認した。
  sources: &id001
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/1020101002_ProjectileFireball.prefab
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/Client/Assets/DungeonInn/Runtime/Content/Effect/Common/Mesh/VfxUnitFoldedBillboard.asset
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/Client/Assets/DungeonInn/Runtime/Content/Effect/Common/Shader/VfxMeshSurface.shader
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/Client/Assets/DungeonInn/Runtime/Scripts/View/Scene/MainScene/World/Effect/WorldEffectMeshView.cs
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/Client/Assets/DungeonInn/Editor/WorldEffectPrefabPreviewWindow.cs
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/6963c273/tasks/task_0357.md
  checked_at: '2026-10-04'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0 / DX12
    environment: Windows Editor、PreviewRenderUtilityの隔離Scene。製品実機の性能未測定。
    executed_at: '2026-10-04'
    procedure: 主役と補助層を比較して削除。体積Coreを面近似へ変更し、折り目を明部外へ移動。前後左右の45度俯角・平行投影を描画し、粒子なし時計0.9→0.2秒のシークを確認。ユーザーが見た目を評価。
    artifacts: *id001
---


# 品質基準版からCore単独への削減と見た目承認

## 実行と判定

既に実行したUnity制作を記録し、この知識更新でエンジンを再実行したものではない。reviewedは観察・承認・限定条件の記録を確認した状態。共通TechniqueやAdapterをvalidatedへ昇格させない。

最高品質の基準版で必要な輪郭・熱・方向流れを作った後、補助層を個別に比較した。Coreで主役が成立しているため外炎・履歴の尾・煙・見えない火の粉を削除した。主役は体積積分から面上密度へ置き換えた。面上の赤い尾はCore自身に含まれ、履歴のTrail削除は尾の見た目を全て消すことではない。

三分割の折り目が明るい楕円のほぼ中心を横切っていた。前面を長くし、UVと頂点の比率を保って折り目を赤い尾側へ移した。ユーザーはその後「完成品質に達したと言っていいでしょう」と承認した。

## 失敗から残す判断

開始辺のフェード幅を広げるだけでは三角形の底辺の角が残った。根元を半楕円の輪郭で切ると改善したが、補助外炎の価値は主役に対して小さく、最終的には削除された。足した層の修正へ固執せず、合成への貢献で採否を決める。

固定の1粒子をMeshへ移しただけで大きなGPU改善とは断定しない。今回は体積積分の置換とRenderer・粒子の削減も行った。設定値のmaxParticlesは実発生数ではない。構成の削減と実時間の改善は別の証拠を要する。

## 条件付きの確認結果

compileはError0/既存Warning2、ShaderHasError=false、規約チェック違反0。保存Prefabは子Core1・Renderer1・ParticleSystem0。8頂点のMeshと支点UVをnative確認。前後左右・平行投影の描画、0.9→0.2秒のシーク、既存射出/着弾の粒子PreviewのLoad/Seekを確認。Launcher Scene dirty=false。

ライブPreviewでユーザーが確認し、新しい画像・動画や自動レビュー待機は追加していない。承認記録とPreview PNGの削除は実装側ローカルcommit d6781bb3に記録された。ここでは公開済みの実装固定版と本制作記録へリンクし、削除済みの画像を現在の証拠として参照しない。

固有値・段階別の採否・未達項目は利用プロジェクトの変換記録に分離し、[共通カタログの採用例入口](../docs/KNOWLEDGE_CATALOG.md)から参照する。射出・着弾をCore単独へ一般化せず、実ゲーム性能の合格とも混同しない。
