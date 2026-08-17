# claude-config

Claude Code のユーザーレベル設定（`~/.claude`）。

## 追跡しているもの

| パス | 内容 |
|---|---|
| `settings.json` | 権限（denyリスト、Auto mode）、hooks登録、statusline登録、プラグインのオフスイッチ |
| `CLAUDE.md` | グローバル指示 |
| `keybindings.json` | キーバインド（Ctrl+Q でトランスクリプト切替） |
| `statusline.py` | ステータスライン |
| `hooks/` | field-guide 用フック（trigger-sentinel / merge-gate） |
| `skills/` | 汎用スキル（field-guide ファミリー） |

`.gitignore` はホワイトリスト方式。ランタイムファイル（sessions, projects, cache 等）は構造的にコミット対象外。

## 新しいマシンでの復元

```sh
git clone https://github.com/x24ken/claude-config.git ~/.claude
```

既存の `~/.claude` がある場合は、上記追跡ファイルだけ上書きコピーする。

## 運用ルール

- 秘密情報（トークン・APIキー・メールアドレス）は絶対にコミットしない。pre-commit フックがスキャンしてブロックする
- `settings.json` に Auto mode が自動追記する `autoMode` キーはコミット禁止（pre-commit がブロック）。混入したら `python3 -c "import json; p='settings.json'; d=json.load(open(p)); d.pop('autoMode', None); open(p,'w').write(json.dumps(d, indent=2, ensure_ascii=False)+'\n')"` で除去してからコミットする
- プロジェクト固有のスキルはここに置かない。各プロジェクトの `.claude/skills/` に置く

## クローン後の初期設定

```sh
git config core.hooksPath git-hooks
```
