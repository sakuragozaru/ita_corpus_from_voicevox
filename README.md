ITAコーパス出力くん
====
# これはなに？
ITAコーパス( https://github.com/mmorise/ita-corpus )の424文を  
VOICEVOX( https://github.com/VOICEVOX/voicevox_engine )を用いて出力します。  
（一部の文は分割されているため進捗バーの分母は443となっています）   
![スクリーンショット](https://github.com/sakuragozaru/ita_corpus_from_voicevox/blob/images/images/2023-01-14_093223.png "スクリーンショット")

# 使い方
1. VOICEVOX ENGINE( https://github.com/VOICEVOX/voicevox_engine )をダウンロードして起動してください
2. index.exe (またはpython index.py) を実行してください。ウィンドウが表示され「Voicevoxと接続中」と表示されます。
3. 接続に成功すると話者とスタイル選択画面になります。話者とスタイルを選択してください。
4. 選択したら「Start」を押して進捗が完了するまでお待ちください。
5. 「出力完了」と表示されたら完了です。dataフォルダに以下の形でファイルが出力されています。
```
data
├── 3_ずんだもん_ノーマル
│   ├── 000_myvoice
│   │   ├── text
│   │   │   ├── emotion001.txt
│   │   │   ├── emotion002.txt
│   │   │   ├── ...
│   │   └── wav
│   │        ├── emotion001.wav
│   │        ├── emotion002.wav
```

# Q&A
### Voicevoxと接続中と表示されたあとに何も表示されません
VOICEVOX ENGINEの起動に失敗してるかも。  
VOICEVOX ENGINEの画面に `Application startup complete.` と表示されているか確認してください。
### 出力に時間がかかります
それなりに時間がかかります。参考に私の環境では全部完了するのに45分程度かかります。
### 用いるコーパスを変更したいです
corpus.csvを別のファイルに置き換えてください。各行は「ファイル名,日本語文」です。
### 選びたい話者がいません
話者とスタイルは今起動しているVOICEVOX ENGINEから取得しています。  
最新のVOICEVOX ENGINEを入手してください。

# 制作ログ
* 2023/01/14 00:48 制作開始
* 2023/01/14 02:26 ITAコーパスからCSV作成完了
* 2023/01/14 11:15 実装完了
* 2023/01/14 11:25 Github用のREADME.md作成
* 2023/01/14 11:50 exe再出力とREADMEに画像添付