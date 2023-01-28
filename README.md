ITAコーパス出力くん
====
# これはなに？
[ITAコーパス]( https://github.com/mmorise/ita-corpus )の424文を[VOICEVOX]( https://github.com/VOICEVOX/voicevox_engine )を用いて出力します。  
![スクリーンショット](https://github.com/sakuragozaru/ita_corpus_from_voicevox/blob/images/images/2023-01-14_093223.png "スクリーンショット")  
（一部の文は分割されているため進捗バーの分母は443となっています）   

# 使い方
1. [VOICEVOX ENGINE]( https://github.com/VOICEVOX/voicevox_engine )をダウンロードして起動してください (VOICEVOXの起動でもOK)
2. index.exe (またはpython index.py) を実行してください。ウィンドウが表示され「Voicevoxと接続中」と表示されます。
3. 接続に成功すると話者とスタイル選択画面になります。話者とスタイルを選択してください。
4. 選択したら「Start」を押して進捗が完了するまでお待ちください。
5. 「出力完了」と表示されたら完了です。dataフォルダに以下の形で音声ファイルと読み仮名テキストが出力されています。
```
data
├── 3_ずんだもん_ノーマル
│   ├── text
│   │   ├── emotion001.txt
│   │   ├── emotion002.txt
│   │   ├── ...
│   └── wav
│       ├── emotion001.wav
│       ├── emotion002.wav
│       ├── ...
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
  
***

# (2023/01/28追加_動作確認中)AssistantSeika利用版

## これはなに？
[ITAコーパス]( https://github.com/mmorise/ita-corpus )の424文を[AssistantSeika]( https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-000 )を用いて出力します。  
例えば東北きりたんの音声ファイルを出力する目的などで利用することを想定しています  
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">きりたんになる場合はボイロで100から400文章程度をボイロに読ませるとできるかもですヽ(′▽︎`*)乂(*′▽︎`)ﾉ<br>読ませる文章はITAコーパス使えばいいのでどなたか良ければやってみてください⸜( ´ ꒳ ` )⸝♡︎<br> <a href="https://t.co/HDwbDZielq">https://t.co/HDwbDZielq</a></p>&mdash; 東北ずん子💚きりたんボイスピ クラウドファンディング (@t_zunko) <a href="https://twitter.com/t_zunko/status/1519841867009257472?ref_src=twsrc%5Etfw">April 29, 2022</a></blockquote> 

## 使い方
1. [AssistantSeika]( https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-000 )をダウンロードして起動してください
2. 使用製品のスキャンを行ってください（スキャン時の音声効果で収録されます）
3. 画像の通りにHTTP機能を設定してください  (ワークフォルダとドキュメントルートフォルダは自由に設定してください)  
![スクリーンショット 2023-01-28 211403](https://user-images.githubusercontent.com/77018668/215267415-c063d0af-65a5-4dad-bc92-854625582ad8.png)
4. seika.exe (またはpython seika.py) を実行してください。ウィンドウが表示され「AssistantSeikaと接続中」と表示されます。
5. 接続に成功すると話者選択画面になります。話者を選択してください。
6. 選択したら「Start」を押して進捗が完了するまでお待ちください。  
（再生されている全音声がwavに記録されるようなので他音声が鳴っていない状態にしてください）
7. 「出力完了」と表示されたら完了です。dataフォルダに音声ファイルが出力されています。
```
data
├── 1707_東北きりたん EX_VOICEROID+EX_1707
│   └── wav
│       ├── emotion001.wav
│       ├── emotion002.wav
│       ├── ...
```

# 制作ログ
* 2023/01/14 00:48 制作開始
* 2023/01/14 02:26 ITAコーパスからCSV作成完了
* 2023/01/14 11:15 実装完了
* 2023/01/14 11:50 GithubのReadme整備
* 2023/01/28 22:00 AssisantSeikaに対応
* 2023/01/29 01:40 AssisantSeikaから収集する音声を22000HZに変更
