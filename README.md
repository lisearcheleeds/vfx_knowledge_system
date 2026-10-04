# VFX Knowledge System

AIにゲームエンジン上で高品質なリアルタイム3D VFXを作らせるための知識・制作・評価・更新の仕組みを構築する。

Unity、Unreal Engine、Godotで共有する設計判断と、各エンジン固有の実装知識を分離し、制作結果と失敗分析から知識を改善する。

## 現在の状態

**知識基盤の土台は構築済み。Unityで最初の制作・撮影・修正・知識還元を実施。** 共通レシピ62件を含む116ノード。火球から体積描画・方向流れ・周期ノイズ・Unity Adapter・実行Evidenceを追加した。見た目の改善を確認した一方、外炎の矩形境界、内部構造・ゲーム接続・性能は未確認。制作ワークフロー全体の完了ではない。

| 入口 | 内容 |
| --- | --- |
| [設計書](vfx_knowledge_system_design.md)・[実装上の補足](docs/IMPLEMENTATION_NOTES.md) | 設計と申し送り7項目 |
| [WORKFLOW](WORKFLOW.md) | 制作・評価・更新の手順 |
| [SCHEMA](SCHEMA.md)・[GLOSSARY](GLOSSARY.md) | ノード・関係・用語の規約 |
| [索引](index/README.md) | 登録済み知識の入口 |
| [共通レシピ](docs/KNOWLEDGE_CATALOG.md)・[知識の境界](docs/KNOWLEDGE_BOUNDARIES.md) | 具体的な推奨構成と再利用の単位 |
| [DungeonInn採用例](projects/dungeon-inn/CATALOG.md)・[火球の制作記録](projects/dungeon-inn/runs/fireball-2026-10-04.md) | 固有の品目・ID・ゲーム値、反復・評価・未解決事項 |
| [Unity Adapter](adapters/unity-urp-noise-density.md)・[実行Evidence](evidence/organic-fire-volume-preview.md) | 粒子の密度体積・方向流れ・煙の実装条件と観察 |
| [更新規則](CONTRIBUTING.md)・[テンプレート](templates/NODE.md) | 追加・変更の手順 |
| [状態・次の実証](docs/STATUS.md)・[未確定事項](docs/OPEN_ITEMS.md) | 到達点、不足、次の確認 |

設計書・テンプレートの例は知識として登録しない。実測・成功記録を推測で補わない。

## AIが作業するときの参照順序

1. このREADME、実装上の補足、WORKFLOWを読み、現在の構築範囲を確認する。
2. 制作時は利用プロジェクトのProfileと参照する知識のコミットを確認する。
3. 要求に関係する知識、必須依存、根拠、検証条件を取得する。
4. 構成候補の採用・棄却理由を残し、抽象仕様からエンジン別の実装計画へ進む。
5. 動画・背景・視点・性能・停止と再利用を評価し、結果を制作記録と知識更新案に残す。

候補探索と採用を分け、採用後に必須依存を解決する。`when` は自然言語の判断材料であり、自動評価しない。詳細は設計書の該当章を参照する。

| 作業 | 設計書の参照箇所 |
| --- | --- |
| 目標・基本原則・責務の確認 | 第1〜3章 |
| 知識ノード・スキーマ・関係の整備 | 第4〜7章、付録A |
| 抽象仕様・Adapter・Profileの作成 | 第8〜10章、付録B |
| 制作・検索・評価 | 第11〜13章 |
| 記録・根拠・知識更新 | 第14〜15章 |
| 配置・版管理・検証・構築計画 | 第16〜20章、付録C |

## ツール

セットアップと探索・依存解決の使い方は[ツールの説明](tools/README.md)を参照する。

```powershell
.\.venv\Scripts\python.exe tools/knowledge.py index
.\.venv\Scripts\python.exe tools/knowledge.py validate --check-index
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

次は火球の動画上の矩形境界を切り分け、内部構造・ゲーム接続・実機負荷を確認する。他エンジンへの適合はそれぞれ実行して判断する。別フォルダの確認・参照にはユーザーへの確認が必要。

設計書は現在、直下の `vfx_knowledge_system_design.md` に置いている。設計書に記載された `docs/SYSTEM_DESIGN.md` は将来の想定配置。
