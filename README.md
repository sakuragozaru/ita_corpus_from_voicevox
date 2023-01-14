ITAコーパス出力くん
====
## Description
ITAコーパス(https://github.com/mmorise/ita-corpus)の424文を
VOICEVOX(https://github.com/VOICEVOX/voicevox_engine)を用いて出力します。
（一部の文は分割されているため進捗バーの分母は443となっています）

## Requirement
VOICEVOX ENGINE(https://github.com/VOICEVOX/voicevox_engine)の起動

## Usage
1. VOICEVOX ENGINE(https://github.com/VOICEVOX/voicevox_engine)をダウンロードして起動してください
2. index.exe (またはpython index.py) を実行してください。ウィンドウが表示され「Voicevoxと接続中」と表示されます。
3. 接続に成功すると話者とスタイル選択画面になります。話者とスタイルを選択してください。
4. 選択したら「Start」を押して進捗が完了するまでお待ちください。
5. 「出力完了」と表示されたら完了です。dataフォルダにファイルが出力されています。

## Q&A
### Voicevoxと接続中と表示されたあとに何も表示されません
VOICEVOX ENGINEの起動に失敗してるかも
### 出力に時間がかかります
それなりに時間がかかります。参考に私の環境では全部完了するのに45分程度かかります。
### 用いるコーパスを変更したいです
corpus.csvを別のファイルに置き換えてください。各行は「ファイル名,日本語文」です。
### 選びたい話者がいません
話者とスタイルは今起動しているVOICEVOX ENGINEから取得しています。最新のVOICEVOX ENGINEを入手してください。

## 制作ログ
* 2023/01/14 00:48 制作開始
* 2023/01/14 02:26 ITAコーパスからCSV作成
* 2023/01/14 11:15 実装完了