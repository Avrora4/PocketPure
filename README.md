# PocketPure
## 1. Git運用ルール

本プロジェクトでは、Googleの開発哲学に基づいた「小規模で頻繁なコミット」と「明確な履歴管理」を重視し、**シンプルなTrunk-Based Development（トランクベース開発）**を採用します。

### 1.1. ブランチ戦略
- `main` ブランチは**常に動く（デプロイ可能な）状態**を維持する。
- 作業は必ず `main` から feature ブランチを切って行う。
- **ブランチの命名規則:** `プレフィックス/短い説明`
  - `feat/add-transaction-api` (新機能)
  - `fix/date-format-bug` (バグ修正)
  - `refactor/ui-components` (リファクタリング)

### 1.2. コミットメッセージのルール (Conventional Commits)
「何をしたか」ではなく**「なぜ変更したか・何がどう変わったか」**が後から見て1秒でわかるように書くこと。

### 命名フォーマット
- **ブランチ名:** `タイプ/短い英単語の説明` （例: `feat/add-csv-upload`）
- **コミットメッセージ:** `タイプ: 変更内容の要約` （例: `feat: CSVファイルのアップロード機能を追加`）

### プレフィックス（タイプ）一覧

| タイプ | 概要 | 具体的な使用例（コミットメッセージ） |
| :--- | :--- | :--- |
| **`feat`** | 新機能の追加 (Feature) | `feat: 画面から明細を手動入力するフォームを追加` |
| **`fix`** | バグの修正 (Bug Fix) | `fix: 金額にマイナス値が登録できてしまう不具合を修正` |
| **`docs`** | ドキュメントのみの変更 | `docs: READMEにAPIのエンドポイント一覧を追記` |
| **`style`** | コードの動作に影響しないフォーマット変更 | `style: Prettier/Ruffによるコードの自動整形` |
| **`refactor`**| リファクタリング (機能追加やバグ修正を含まない) | `refactor: fetchを使ったAPI通信処理を共通関数に分離` |
| **`perf`** | パフォーマンス向上のための変更 | `perf: DBからの明細一覧取得クエリを最適化` |
| **`test`** | テストコードの追加・既存テストの修正 | `test: 合計金額の計算ロジックに対する単体テストを追加` |
| **`build`** | ビルドシステムや外部依存関係の変更 | `build: Viteの設定変更、不要なnpmパッケージの削除` |
| **`ci`** | CI/CDの設定ファイルやスクリプトの変更 | `ci: GitHub Actionsによる自動デプロイ設定を追加` |
| **`chore`** | その他、ソースやテストに影響しない雑務 | `chore: .gitignoreを更新、エディタ設定の追加` |

### 1.3. マージルール
- 1.5時間の作業の終わりには、必ずコミットしてPushする（WIP: Work In Progress でも可）。
- ひとつの機能（垂直スライス）が完成したら `main` へ Pull Request (PR) を作成する。
- マージする際は **「Squash and Merge」** を推奨。細かいWIPコミットを1つにまとめ、`main` の履歴を綺麗に保つ。

---

## 2. ディレクトリ構成

バックエンド（FastAPI）とフロントエンド（React+Vite）を明確に分離したモノレポ構成とします。学習コストと開発スピード（1.5h/day）を最優先し、過度な階層化（Atomic Design等）は避けたフラットで実用的な設計です。

```text
credit-card-tracker/  (プロジェクトルート)
│
├── backend/                  # FastAPI (Python)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py           # アプリケーションのエントリーポイント
│       ├── database.py       # DB接続設定 (SQLAlchemyなど)
│       ├── models/           # DBのテーブル定義 (SQLモデル)
│       │   └── transaction.py
│       ├── schemas/          # APIの入出力の型定義 (Pydanticモデル)
│       │   └── transaction.py
│       └── api/              # APIエンドポイント (ルーター)
│           └── transactions.py
│
├── frontend/                 # React + Vite (JavaScript/TypeScript)
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx          # Reactのマウントポイント
│       ├── App.jsx           # ルーティングや大枠のレイアウト
│       ├── api/              # fetch通信の共通処理 (axiosの代替)
│       │   └── client.js
│       ├── components/       # UIコンポーネント (Atomic Design不使用・フラット配置)
│       │   ├── Button.jsx
│       │   ├── Button.module.scss
│       │   ├── TransactionForm.jsx
│       │   └── TransactionTable.jsx
│       └── styles/           # グローバルなCSS/SCSS
│           └── global.scss
│
├── docker-compose.yml        # DB(PostgreSQL)やバックエンドをまとめて起動する用
├── .gitignore
└── README.md                 # このファイル
