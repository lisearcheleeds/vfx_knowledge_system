---
schema_version: 0.1.0
id: evidence/game-effect-conversion-preview
kind: evidence
title: 基準版71件をゲーム用版へ変換したPreview比較の記録
summary: 最高品質の基準版を、共有素材2 Shaderの粒子だけで描くゲーム用版へ生成スクリプトで変換し、同じ視点・時刻で並べて比べた。見つけたエンジンの挙動と、まとめ方の失敗と直し方の記録。
status: reviewed
revision: 2
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
  - target: adapter/unity-urp-game-particle-conversion
    statement: メッシュ粒子の法線に詰めた値を10倍しても描画が変わらず、法線は正規化されて値を運べなかった。UVの整数部に詰めると帯の模様と崩れ方が基準版に近づいた。
  - target: adapter/unity-urp-game-particle-conversion
    statement: Texture Sheet Animation の startFrame にコマ番号を入れると星・輪のタイルが丸い光になり、(コマ＋0.5)／16 で正しいタイルになった。メッシュ粒子はタイルが効かず薄く見え、UVをタイルの範囲へ焼き直し両面で描くと基準版と同じ濃さになった。
  - target: adapter/unity-urp-game-particle-conversion
    statement: トレイルの寿命に秒を入れると、寿命10秒の本体の尾が画面の端まで伸びた。尾の秒数を本体の寿命で割ると基準版の長さになった。
  - target: rendering/lightweight-vfx-catalog
    statement: 回る窓の位相・速さが違う帯（大鎌の3枚の刃、旋風斬の溜めのコイルと風）や発生の時刻が違う輪（拳圧）を1つのメッシュにまとめると、刃が同じ角度に重なる・2本目が崩れるなど見た目が破綻し、分けたまま残した。
  - target: rendering/lightweight-vfx-catalog
    statement: 狙い撃ちの矢のらせんの糸（距離あたり140粒×2本・上限各600）を、本体と一緒に動く剛体のらせんメッシュ1粒を毎秒26回転させる形に置き換え、基準版と同じらせんに見えた。
  - target: rendering/lightweight-vfx-catalog
    statement: 魔法弾・火の詠唱の核を、外の光と芯を焼き込んだ1チャンネルのタイル1粒にすると、青い光と白い芯（橙と淡黄）の差が消えて鈍い色になり、2粒に戻した。
  - target: rendering/lightweight-vfx-catalog
    statement: 打撃の命中 400 個（Editor の Play、主スレッド。空 約 5.5 ms）で、ParticleSystem 4 系は約 20 ms（粒子の更新 2.8 ms・頂点の生成 7.9 ms・Batches 22）、VAT を 1 粒のメッシュ粒子に載せると約 16.8 ms（頂点の生成 8.0 ms は残り、Batches は約 400 に増えた）、VAT を MeshRenderer＋GPU インスタンシングで描くと約 5.5 ms（空とほぼ同じ、Batches 17）。
  - target: rendering/lightweight-vfx-catalog
    statement: 65 種を混ぜた 100 個（1920×1080、240 フレーム平均）で、主スレッドは空 4.69 ms／ParticleSystem 30.38 ms／焼き込み 6.58 ms。Batches は 6／46／201。焼き込みの Batches は層・演出ごとに素材（焼いたテクスチャ）が分かれていたため。
  - target: rendering/lightweight-vfx-catalog
    statement: 焼いた記録 194 枚（RGBAFloat）は中身が約 277 万画素だが、大きさが幅 1〜60・高さ数百〜5291 とばらつき、配列テクスチャで最大にそろえると約 985 MB になる見積もりだった。最大は 2.2 秒で繰り返し粒が 7.5 秒生きる継続の演出で、4 周期 8.8 秒を 60 fps・1 フレーム 10 行・変種 3 で記録した 27×5291。
  conditions: 専用Prefab Preview。暗い背景、45度俯瞰、基準版と同じ視点・時刻の5コマを上下に並べた。
  result: 71件すべてが共有素材だけで描け、Editorの資産を参照しない。最大は5系・粒の上限68。
  limitations: 一つのプロジェクト・一つのカメラ条件。性能は対象機種で未計測。外観の承認はユーザー待ち。
  sources: []
  checked_at: '2026-10-10'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview
    executed_at: '2026-10-10'
    procedure: 生成スクリプトで変換し、基準版と同じ視点・時刻の連番の比較画像で確認・修正した。
    artifacts:
    - projects/dungeon-inn/runs/game-effect-conversion-2026-10-10.md
---

# 基準版71件をゲーム用版へ変換したPreview比較の記録

主張と条件は Front Matter の `evidence_details` を正とする。経緯は `projects/dungeon-inn/runs/game-effect-conversion-2026-10-10.md`。
