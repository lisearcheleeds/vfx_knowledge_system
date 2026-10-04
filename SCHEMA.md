# 知識ノードと索引の規約

現在のメタデータ構造は `0.1.0`。[JSON Schema](schemas/node.schema.json)と[関係・タグ設定](schemas/graph-config.json)で機械検証する。[設計書](vfx_knowledge_system_design.md)第4〜8章を土台とした初期実装である。

## 正本・登録対象

`knowledge/`、`adapters/`、`evidence/` 配下のMarkdownを再帰的に登録する。各ファイルは冒頭のYAML Front Matterと本文を持つ。UTF-8、英語kebab-caseのファイル名、引用符付きの日付を用いる。YAMLの重複キーを許可しない。

設計書、文書、テンプレート、テスト用データ、`projects/` の採用対応表は登録対象外。固有の品目名・ID・マスタ値は採用先へ置き、共通ノードには固定しない。[境界の例](docs/KNOWLEDGE_BOUNDARIES.md)を参照する。空の本文や見出しだけのノードを拒否するが、意味上の十分性は内容レビューで判断する。

## 共通メタデータ

| フィールド | 規約 |
| --- | --- |
| `schema_version` | `"0.1.0"` |
| `id` | `kind/英語kebab-case`。全体で一意、移動・改名時も維持 |
| `kind` | semantic / composition / recipe / technique / resource / rendering / evaluation / adapter / evidence |
| `title`, `summary` | 空ではない名前と検索用の短い要約 |
| `status` | draft / reviewed / validated / deprecated |
| `revision` | 1以上の整数。内容更新時に増やす |
| `updated_at` | `"YYYY-MM-DD"`。実在する日付 |
| `aliases`, `tags` | 重複しない文字列配列。タグは設定の管理語彙から選ぶ |
| `scope` | engine-neutral / engine-specific |
| `relations` | 関係オブジェクトの配列 |
| `evidence` | Evidence IDの配列 |
| `superseded_by` | 廃止時の置換先ID配列。置換先がなくても deprecated は可能 |
| `engine`, `compatibility` | Adapterまたはengine-specificで必須 |
| `evidence_details` | Evidenceで必須。それ以外のノードには付けない |

定義外のフィールドを拒否する。IDの名前空間と `kind` を一致させる。`superseded_by` が空でない場合は `deprecated` にする。廃止・統合でも過去のIDを追跡できるよう残す。

## 関係

`target`, `type`, `reason` を必須とし、`when`, `role`, `evidence` を必要に応じて付ける。`requirement` は `composes` にのみ必須で、required / optional のどちらかを指定する。

| type | 探索上の意味 | 自動の必須依存 |
| --- | --- | --- |
| expresses | 表現するSemantic | なし |
| composes | 構成要素 | requirementがrequiredの場合のみ |
| candidate | 条件に応じて比較・選択する候補 | なし |
| requires | 採用時に必要な知識・素材 | あり |
| enhances | 任意の補強 | なし |
| alternative | 同じ役割の代替。対称 | なし |
| conflicts_with | 条件付きの競合。対称 | なし |
| implemented_by | Adapterへの実装対応 | なし |
| evaluated_by | Evaluationへの対応 | なし |

`when` は自然言語であり、式・ルールエンジンとして評価しない。条件付き必須依存も循環検査には含める。一般的な関連リンクの循環は許可する。条件付きの循環が相互排他的だと主張する場合も、初期ツールは自動で解決せず構成を見直す。

逆参照と対称関係の逆方向は生成索引に保持する。正本へ二重登録しない。本文から別の登録ノードへリンクするときは、relations、evidence、superseded_by、Evidenceのclaimsのいずれかにも対象IDを記載する。文書への補助リンクにはノード関係を要求しない。

## Adapterの互換条件

`engine` は対象名の文字列（例：`unity`）。具体的な版はこのリポジトリ全体では未確定。

`compatibility` は `engine_version`, `renderer`, `platforms`, `verification` を持つ。未確定の版・Rendererはnull、platformsは空配列にできる。verificationは unverified / documentation-only / engine-tested。未確認を対応済みと解釈しない。

`engine-tested` またはAdapterの `validated` には具体的な版・Renderer・対象環境と実行Evidenceを要求する。選択記録のengineと異なるengine-specificノードは依存解決で拒否するが、実機互換性は自動判定しない。

## 状態・Evidence

draftは提案・仮説、reviewedは内容レビュー済み、validatedは根拠の対象条件で再現確認済み、deprecatedは新規利用非推奨。ツールは自動昇格しない。

Evidenceの `evidence_details` には次を記録する。

- `source_kind`：official-documentation / first-party-experiment / reproduced-test / production-observation / hypothesis。
- `claims`：対象ノードID `target` と主張 `statement` の配列。
- `conditions`, `result`, `limitations`：条件、観察・結果、未検証範囲。
- `sources`：参照URL配列。公式資料の記録では必須。`checked_at` は確認日、未確認ならnull。
- `execution`：実際のエンジン再現があるときだけ、engine、engine_version、renderer、environment、executed_at、procedure、artifactsを記録する。

validatedには対象IDをclaimsで明記した、reviewed/validatedの非仮説Evidenceと確認日が必要。Recipe・Adapterには、reproduced-test、first-party-experiment、production-observationのいずれかによる実行記録が必要。Adapterの版・Rendererと実行記録を照合する。

構造検証は証拠の存在・形式を確認する。証拠が本物か、性能が合格か、すべての主張を裏付けるかは人・AIの内容レビューと実行確認で判断する。測定値・動画・成功記録を形式合わせで創作しない。

## 選択記録

[選択スキーマ](schemas/selection.schema.json)を使い、selected_nodes、engine、conditional_decisionsを指定する。selected_nodesは採用済みノードのID配列、engineは対象エンジンまたはnull。

条件判断はsource、source_revision、relation_index（relations配列の0始まり）、applies（真偽）、reasonを記録する。対象は `when` を持つ必須関係だけ。改訂が変わった判断、重複判断、採用グラフ外の判断を拒否する。

`dependencies` は未判定条件を返して終了コード2、構造不正は1、必須依存が列挙できれば0を返す。0も実装可能・条件成立・性能合格を意味しない。役割の充足、任意要素の選択、競合の解決は制作判断として別途行う。

## 派生索引

`index/nodes.json` はノードのメタデータ、パス、内容ハッシュ、逆参照、対称関係の派生表示を保持する。`index/README.md` は閲覧用一覧。生成時刻を含めず、同じ正本から同じUTF-8/LFの出力を生成する。

本文の変更もハッシュへ反映する。`validate --check-index` は再生成結果と配布索引をバイト単位で比較する。古い索引を正本として読み込まず、`index` で置き換える。

ローカルMarkdownリンク検証は、コード例以外の基本的なインライン・参照・画像リンクのパスを対象とする。外部URLの到達性、見出しアンカー、複雑なMarkdown/HTML構文は初期ツールの対象外。
