---
schema_version: 0.1.0
id: evidence/organic-fire-volume-preview
kind: evidence
title: 体積炎・方向流れ・煙のPreview制作と人間評価
summary: 一つのUnity制作例での反復・撮影・主観評価と、動画に残る矩形面の欠点を記録する。
status: reviewed
revision: 1
updated_at: '2026-10-04'
aliases: []
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
  - target: recipe/volumetric-fireball
    statement: 射出・飛翔・着弾の3部分を改訂構成で制作・撮影した。詠唱と各対象の熱反応は今回の範囲外。
  - target: technique/volume-density
    statement: 表面の球形核を内部密度・吸収・発光へ置き換え、侵食された炎と冷却する着弾をPreviewで観察した。
  - target: technique/directional-flow-surface
    statement: 方向性のあるUV流れ・ノイズ侵食・Mesh変位を実描画した。ただし動画で矩形面が見える欠点が残る。
  - target: resource/periodic-density-noise
    statement: 周期3DノイズのデータをUnityで生成し、体積と流れ面から利用して撮影した。
  - target: technique/history-ribbon
    statement: 実移動を与えたnative Trailに暖色から煙色への変化を設定し、煙の房との併用を観察した。
  - target: adapter/unity-urp-noise-density
    statement: Unity 6000.3.14f1 / URP 17.3.0 / Windows Editor / DX12で3つのPrefabを手動Simulateして撮影した。
  conditions: 射出・飛翔・着弾を個別Preview。明暗背景、透視カメラ2視点、手動Simulate。ゲーム制約への削減を保留した品質基準版。
  result: 内部密度の炎、前方から後方への流れ、重なる煙、膨張と冷却を撮影した。人間から大幅改善の評価を受けたが、流れ面の矩形境界が動画で目立つという追加指摘がある。
  limitations: 各変更の因果を分離した比較ではない。見た目評価は主観。内部構造の独立レビュー、ゲーム時計・Pool・階層復元・実ゲーム接続、正射影、遮蔽、密集時性能は未確認。流れ面の矩形境界の原因と対策は未検証。
  sources:
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Common/Shader/VfxVolumeDensity.shader
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Common/Shader/VfxMeshSurface.shader
  - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Common/Editor/制作条件.txt
  checked_at: '2026-10-04'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0 / DX12
    environment: Windows Editorの隔離PreviewScene。GPU型番・OS詳細・製品実機の性能は未収集。選択Build TargetはWebだがWebビルドは未実施。
    executed_at: '2026-10-04'
    procedure: ParticleSystemを小刻みにSimulateして移動履歴を作り、部品ごとの開始・ピーク・膨張・冷却・終了を撮影。明暗背景と2視点を比較し、Clear後の再生を確認。
    artifacts:
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101001_FireLaunchFlash/Editor/KnowledgePreview.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101001_FireLaunchFlash/Editor/PreviewLight.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101001_FireLaunchFlash/Editor/KnowledgePreview.mp4
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101001_FireLaunchFlash/Editor/確認記録.txt
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101001_FireLaunchFlash/Editor/要素分解.txt
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/Editor/KnowledgePreview.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/Editor/PreviewLight.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/Editor/KnowledgePreview.mp4
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/Editor/確認記録.txt
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101002_ProjectileFireball/Editor/要素分解.txt
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101003_FireImpactBurst/Editor/KnowledgePreview.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101003_FireImpactBurst/Editor/PreviewLight.png
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101003_FireImpactBurst/Editor/KnowledgePreview.mp4
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101003_FireImpactBurst/Editor/確認記録.txt
    - https://github.com/lisearcheleeds/DesktopDungeon/blob/7c8f5e3e6967f0ec46b20017eff364f35cc6d1b3/Client/Assets/DungeonInn/Runtime/Content/Effect/Effects/1020101003_FireImpactBurst/Editor/要素分解.txt
---


# 体積炎・方向流れ・煙のPreview制作と人間評価

## 証拠の扱い

メタデータのexecutionに固定した実装版と撮影成果物を示す。既に実行した制作の記録であり、今回の知識更新でエンジンを再実行したものではない。reviewedは記録と適用範囲を確認したことを指し、Shader設計の独立レビューや製品品質の合格を意味しない。

## 観察と改訂

| 観察 | 原因仮説 | 変更 | 結果・限界 |
| --- | --- | --- | --- |
| 球の外形が強く、燃えている固体に見える | 主輪郭を球Meshが決めている | 内部密度・吸収・発光へ変更し、独立した球の熱核を除去 | 侵食された炎の塊として見た目が改善。比較は複数変更を含む |
| 同形の炎が繰り返される | 同じ連番素材と一様な運動が形を固定する | UVの方向流れ、幅の侵食、Mesh変位、固定Seedの差を導入 | 見た目は改善したが、動画で矩形の板を差し込んだような境界が残る |
| 後方の煙が点々と見える | 発生間隔に対し可視密度の房が小さく、初期熱も高い | 発生密度・初期寸法・成長・初期熱を調整 | 重なる暗い煙の尾を観察。負荷は未計測 |
| 着弾が同じSpriteの集合に見える | 連番の共通輪郭が目立つ | 固定Seedの体積房に寸法・速度・寿命・冷却の差を付ける | 膨張→低温火炎→煙を動画で観察 |

## 人間評価と未解決事項

制作者の変更後、ユーザーは見た目が大幅に改善し理想に近いと評価した。続いて、外側の流れ面では静止画に現れにくい矩形の範囲、何もない所から突然炎が現れる辺がアニメーション中に目立つと指摘した。したがって全面的な完成扱いにはしない。

矩形Meshの切断面、UV侵食、頂点変位、面同士の重なりのいずれが支配的かは未切り分け。修正後の撮影も未実施。複数変更を同時に行ったため、一つの提案だけで品質が上がったとは結論しない。

## 実行確認と未確認

Shaderエラーは3本ともなし。短時間再生→消失または継続→Clear→再生で粒子数の初期復帰を確認した。これは隔離Previewの確認で、製品Poolやゲームの終了契約は未実装。既存EditMode全件成功はコード回帰の確認で、画面の美術品質やGPU時間を測るものではない。

未確認は、内部構造の独立レビュー、ゲームのイベント・時間・階層切替、遮蔽・密集・製品実機負荷、正射影、拡縮、粒子回転。共通Recipe・Technique・Adapterはdraftを維持する。
