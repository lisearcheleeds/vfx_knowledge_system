---
schema_version: 0.1.0
id: evidence/lightweight-vfx-web-sources
kind: evidence
title: 軽量なゲーム用VFXの技法に関する公開資料
summary: オーバードロー・トリミング・粒子のカリング・バッチ・素材の共有・テクスチャの詰め込み・同時数の管理について、エンジンの公式資料と制作者の記事で確認した内容。
status: draft
revision: 1
updated_at: '2026-10-10'
aliases: []
tags:
- evidence
- rendering
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: official-documentation
  claims:
  - target: rendering/lightweight-vfx-catalog
    statement: 半透明の費用は描く画素×重なる層×処理の重さで、大きな重なりが主な原因になる（Unreal/UDKの最適化資料、PowerVRの粒子描画の推奨、各記事）。
  - target: rendering/lightweight-vfx-catalog
    statement: 粒子の透明の余白を、見える範囲を囲む多角形で削ると、煙の例で4角形60%・8角形52%の画素になり、8角形を超えると効果が薄い（Humus、Persson）。
  - target: rendering/lightweight-vfx-catalog
    statement: Unityの粒子はローカル空間などの条件で決定的（procedural）になり、画面外で模擬を止めて早送りできる。ワールド空間・重力・ノイズ・衝突・トレイル・サブエミッタ・距離あたりの発生・9区間以上の曲線・スクリプトでの変更で外れる（Unity公式ブログ）。
  - target: rendering/lightweight-vfx-catalog
    statement: URPではMaterialPropertyBlockを付けたレンダラーはSRP Batcherの対象外になり、粒子のレンダラーもMPBを使うため対象外（Unity公式マニュアル・フォーラム）。
  - target: rendering/lightweight-vfx-catalog
    statement: 粒子の個体差はCustom Vertex Streams・Custom Dataで素材を増やさず渡せる（Unity公式マニュアル）。
  - target: rendering/lightweight-vfx-catalog
    statement: 大人数の戦闘のモバイルゲームで、1演出の粒子を3〜10個、命中を30粒から焼き込みの2粒へ、200粒から大きな50粒へ減らした例。共通のシェーダとアトラスで素材を共有し、全体を一様にする計算は頂点へ移す（PocketGamer.biz、Stabrov）。
  - target: rendering/lightweight-vfx-catalog
    statement: 一つの演出の部品（描画の単位）を減らし、物理は少数の部品だけに、薄い粒を重ねるより少ない不透明寄りの粒を使う（id Software Quake 4の資料）。
  - target: rendering/lightweight-vfx-catalog
    statement: 同時数の上限・重要度・距離で演出を間引き、品質設定で落とす（Unreal Niagaraのスケーラビリティ資料）。
  - target: rendering/lightweight-vfx-catalog
    statement: 多数の別種の小さな演出には従来の粒子が軽く、同じ演出の大量表示はVFX Graphのインスタンシングが有利（Unityフォーラム・VFX Graph資料）。
  conditions: Web検索と公開ページの読み込みで確認した（2026-10-10）。数値は各出典の条件の例。
  result: 軽量化の技法を7分類のカタログにまとめた。
  limitations: 本プロジェクトの機種・画面で測った値ではない。各技法の効果は条件で変わる。
  sources:
  - https://www.pocketgamer.biz/vfx-optimisation-in-midcore-games-commonly-overlooked-techniques-and-advanced-methods/
  - https://www.humus.name/index.php?ID=266
  - https://www.humus.name/Articles/Persson_GraphicsGemsForGames.pdf
  - https://unity.com/blog/engine-platform/particlesystem-performance-culling-tips
  - https://docs.imgtec.com/performance-guides/graphics-recommendations/html/topics/optimal-particle-rendering-on-powervr.html
  - https://docs.unity.cn/Manual/SRPBatcher-Incompatible.html
  - https://discussions.unity.com/t/could-srp-batcher-work-with-particles/790166
  - https://docs.unity3d.com/6000.2/Documentation/Manual/PartSysVertexStreams.html
  - https://docs.unity3d.com/6000.4/Documentation/Manual/PartSysInstancing.html
  - https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@17.2/manual/Instancing
  - https://discussions.unity.com/t/is-vfx-graph-always-better-than-the-particle-system/816576
  - https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine
  - https://docs.unrealengine.com/udk/Three/VFXOptimizationResults.html
  - https://iddevnet.dhewm3.org/quake4/Effects_Performance.html
  - https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles
  - https://realtimevfx.com/t/flipbook-texture-packing-atlas-super-pack-and-stagger-pack/5609
  - https://realtimevfx.com/t/why-are-additive-shaders-so-heavy-for-phones/23998
  - https://nexus.leagueoflegends.com/en-us/2017/10/dev-leagues-vfx-style-guide/
  - https://docs.unity3d.com/cn/2022.1/Manual/DrawCallBatching.html
  checked_at: '2026-10-10'
---

# 軽量なゲーム用VFXの技法に関する公開資料

## 確認内容

エンジンの公式資料（Unity・Unreal・PowerVR）と、制作者の記事（大人数の戦闘のモバイルゲーム、Quake 4、粒子のトリミング、GPU Gems）で、軽量化の技法と、その効果・代償を確認した。

## 適用範囲

技法の選択肢と判断の根拠として使う。数値は出典の条件の例で、本プロジェクトの予算・推奨値ではない。予算は対象機種と最悪時の同時数で計測して決める。
