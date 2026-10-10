---
name: design-system
description: 個人デザインシステム quiet-lab の値（色・書体・余白・形・禁止事項）を適用する。自分のアプリ・画面・ページ・ターミナルやエディタのテーマ・SVG アイコン・配色を作る/整えるとき、ユーザーが「quiet-lab」「デザインシステム」「いつものデザイン」と言ったときに使う。Claude アーティファクト（説明ページ・スライド・図）には既定では適用しない。ユーザーが quiet-lab と明示したときだけ使う。デザインの進め方（発散案出し等）ではなく「何色・何 px にするか」の正本への入口。
---

# design-system（quiet-lab）

正本は `~/design-system` リポジトリ。このスキルは場所を教えるだけで値を持たない
（値をここへコピーするとドリフト源になるため禁止）。

## 手順

1. まず `~/design-system/DESIGN.min.md` を読む（約 20 行。人格・色・書体・形・余白・禁止事項。ほとんどの作業はこれで足りる）
2. 媒体別の具体値・導入手順が要るときだけ `~/design-system/adapters/README.md` から該当アダプタへ：
   - Web（shadcn/ui + Tailwind v4）: `~/design-system/globals.css`
   - Claude アーティファクト（ユーザーが quiet-lab を明示したときのみ）: `adapters/artifact.md` + `adapters/artifact-template.html`。何を描くか迷ったら `adapters/explain.md`
   - SVG・アイコン: `adapters/svg.md` ／ 画像生成: `adapters/image-prompt.md`
   - iTerm2・Claude Code テーマ・Obsidian・Chrome: 各 `.md`
3. 根拠（OKLCH 正本・視角・コントラスト・媒体間優先順位）や迷う細部は `~/design-system/DESIGN.md`

## アーティファクトは対象外（2026-10-10 決定）

- Claude アーティファクト（HTML ページ・スライド・図）には**このシステムを既定で当てない**。artifact-design など Claude 標準の判断に任せ、色・構成・動き・ライブラリは自由に選ぶ
- ユーザーが「quiet-lab で」「いつものデザインで」と言ったときだけ、上の手順でアダプタを読んで適用する
- 理由：固定の型（表題→結論→図→本文→次の一手、動き 3 種、React 禁止）で出力が窮屈になった。ユーザーは「ある程度の自由さ」を望んだ

## 役割分担

- このスキル = 「何色・何 px にするか」（値の正本への参照）
- design-directions / artifact-design 等の進め方スキルと併用してよい。その場合もデザイントークンはこのシステムが優先
- ただし**他人のアプリの顔は塗り替えない**（既存の強いアクセントを持つツールではその色を残す。DESIGN.md §7）

## 禁止

- DESIGN.min.md の値をスキルや他プロジェクトのファイルへコピーして持ち回らない。常にリポを読む
- `~/design-system` が見つからない場合は値をでっち上げず、ユーザーに場所を確認する
