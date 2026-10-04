# 知識ツール

Python 3.13と `requirements.txt` の依存を使う。エンジン操作・画像評価・性能判定は行わない。

## セットアップ（Windows PowerShell）

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## コマンド

```powershell
.\.venv\Scripts\python.exe tools/knowledge.py index
.\.venv\Scripts\python.exe tools/knowledge.py validate --check-index
.\.venv\Scripts\python.exe tools/knowledge.py search "核" --kind technique
.\.venv\Scripts\python.exe tools/knowledge.py related technique/mesh-core
.\.venv\Scripts\python.exe tools/knowledge.py dependencies templates/SELECTION.yaml
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Linux/macOSではvenvの `bin/python` を使う。`--root` はサブコマンドの前に指定する。既定のrootはこのツールが置かれたリポジトリである。

| コマンド | 処理 |
| --- | --- |
| index | 正本を検証し、決定的なノード索引・逆参照・対称関係・閲覧一覧を生成 |
| validate | Front Matter、ID、管理語彙、参照先、必須依存・置換の循環、状態・Evidence、ローカルリンクを確認 |
| validate --check-index | 上記に加え、再生成した結果と配布索引の一致を確認 |
| search | ID・タイトル・要約・別名・タグを部分一致で検索。kind/engine/statusで絞り込み可能 |
| related | 正本の関係、逆参照、対称関係の派生表示を取得。採用は行わない |
| dependencies | 選択記録に指定したノードから、必須依存だけを列挙 |

終了コードは通常0、不正入力は1、依存解決の未判定条件は2。採用前の候補比較はAI・人間が行う。自然言語条件を評価せず、判断記録がない条件付き必須依存は未判定とする。

## 確認の限界

構造成功は、品質・性能・実装可能性・条件判断の正しさ・Evidenceの真正性を示さない。役割の充足、候補の棄却、競合、対象版での対応、証拠の内容を別途確認する。

ローカルリンクのパスは基本的なMarkdown構文に限って検証する。外部URLの到達性、見出しアンカー、複雑なHTML/Markdown構文は未対応。Schema変更を伴わない新規ノードはコード変更なしで登録・検索・逆参照へ反映できる。

ツールは許可した正本・文書ルートだけを走査する。テストの作業コピーはこのリポジトリ内の `.test-work/` に作る。既存プロジェクト・エンジン環境を参照しない。

依存の資料：[PyYAML](https://pypi.org/project/PyYAML/)、[jsonschema](https://pypi.org/project/jsonschema/)。CIの基本形は[GitHubのPython検証資料](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)を参照。
