# OfficeToPDFConverter

OfficeToPDFConverterは、Pythonを使用してOfficeドキュメント（Word、Excel、PowerPoint）をPDFに自動変換するためのツールです。このリポジトリは、`unoconv`を利用しており、Google Colabやその他のLinuxベースの環境で動作します。

## 特徴

- Word、Excel、PowerPointファイルをPDFに変換
- Google Colabで簡単に使用可能
- Linux環境でのサポート
- 出力パスを指定してPDFを保存

## 必要条件

このプロジェクトを使用するには、以下が必要です：

- Python 3.x
- `unoconv`
- LibreOffice

## インストール方法

### LibreOfficeとunoconvのインストール

Google ColabやLinux環境でのインストール例：

```bash
sudo apt-get install -y libreoffice
sudo apt-get install -y unoconv
```

### プロジェクトのクローン

```bash
git clone https://github.com/your-username/OfficeToPDFConverter.git
```

## 使用方法

関数をインポートして使用します：

```python
from OfficeToPDFConverter import convert_to_pdf

# WordファイルをPDFに変換
convert_to_pdf('path/to/your/document.docx', 'path/to/output.pdf')

# ExcelファイルをPDFに変換
convert_to_pdf('path/to/your/spreadsheet.xlsx', 'path/to/output.pdf')

# PowerPointファイルをPDFに変換
convert_to_pdf('path/to/your/presentation.pptx', 'path/to/output.pdf')

```

## ライセンス

このプロジェクトはGPLv2ライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。

## 貢献

貢献を歓迎します。プルリクエストを送る前に、まずはissueを開いてください。

## サポート

プロジェクトに関する質問やサポートが必要な場合は、GitHubのIssuesを通じてお問い合わせください。