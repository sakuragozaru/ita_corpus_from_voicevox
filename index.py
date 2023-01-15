import PySimpleGUI as sg
import requests
import csv
import os
import threading

speakers = {}
corpus = []
with open('corpus.csv', encoding="utf_8") as f:
  reader = csv.reader(f)
  for row in reader:
    corpus.append(dict(zip(["filername", "text"], row)))

# 初期化
def get_speakers():
  try:
      response = requests.get('http://localhost:50021/speakers', timeout=5)
      response.raise_for_status()
      if response.status_code == 200:
        return response.json()
      else:
        window.write_event_value("-ERROR-", response.status_code)
        return {}
  except requests.exceptions.RequestException as e:
    window.write_event_value("-ERROR-", e)
    return {}

# UI用関数
def get_speaker_names():
  return [speaker["name"] for speaker in speakers]

def get_style_names(speaker_name):
  speaker = [speaker for speaker in speakers if speaker["name"] == speaker_name][0]
  styles = [style["name"] for style in speaker["styles"]]
  return styles

def get_speaker_id(speaker_name, style_name):
  speaker = [speaker for speaker in speakers if speaker["name"] == speaker_name][0]
  speaker_id = [style["id"] for style in speaker["styles"] if style["name"] == style_name][0]
  return speaker_id

# 音声出力用
def audio_query(speaker, text):
  params = {
      'speaker': speaker,
      'text': text,
  }
  response = requests.post('http://localhost:50021/audio_query', params=params)
  return response

def synthesis(speaker, json):
  headers = {
      'Accept': 'application/json',
  }
  params = {
      'speaker': speaker,
  }
  response = requests.post('http://localhost:50021/synthesis', headers=headers, params=params, data=json.encode('utf-8'))
  return response

def output_wav_txt(folder, speaker, filername, text):
  audio_query_response = audio_query(speaker, text)
  os.makedirs(f"{folder}/text", exist_ok=True)
  with open(f'{folder}/text/{filername}.txt',"w", encoding='utf-8') as file:
    file.write(audio_query_response.json()["kana"].replace("'","").replace("_","").replace("/",""))

  wav_response = synthesis(speaker, audio_query_response.text)
  os.makedirs(f"{folder}/wav", exist_ok=True)
  with open(f'{folder}/wav/{filername}.wav',"wb") as file:
    for chunk in wav_response.iter_content(100000):
      file.write(chunk)

def outputs(speaker_id, speaker_name, style_name):
  window.find_element('-MESSAGE-').Update("VOICEVOXから音声を出力します")
  for count, line in enumerate(corpus):
    window.find_element('-PROG-').update(count+1)
    window.find_element('-MESSAGE-').Update(f"VOICEVOXから音声を出力中({count+1}/{len(corpus)})")
    speaker_folder_name = f"{speaker_id}_{speaker_name}_{style_name}"
    u_dict = { "/":"／", "\\":"＼", ":":"：", "*":"＊", "?":"？",  "\"":"”", "<":"＜", ">":"＞", "|":"｜"}
    for word, read in u_dict.items():
      speaker_folder_name = speaker_folder_name.replace(word, read)
    output_wav_txt(f"data/{speaker_folder_name}", speaker_id, line["filername"], line["text"])
  window.find_element('-MESSAGE-').Update("出力完了")


def main():
  global window
  layout = [[sg.Text('Voicevoxと接続中')]]
  window = sg.Window('ITAコーパス出力くん', size=(300, 300)).Layout(layout)
  def setup():
    global speakers
    speakers = get_speakers()
  thread = threading.Thread(target=setup)
  thread.start()

  while True:
    event, values = window.Read(timeout=100)
    if event is None or event == 'Exit' or event == '-ERROR-':
      window.close()
      return
    elif len(speakers) > 0:
      break
  window.close()

  # UI
  layout = [[sg.Text('話者')],
            [sg.Combo(values=get_speaker_names(), size=(20, 1), key='-SPEAKER_NAME-', enable_events=True)],
            [sg.Text('スタイル')],
            [sg.Combo(values=[''], size=(20, 1), key='-STYLE_NAME-')],
            [sg.Button('Start')],
            [sg.Text('進捗')],
            [sg.ProgressBar(len(corpus), orientation='h', size=(20,20), key='-PROG-')],
            [sg.Text(size=(55,1), key='-MESSAGE-')],
            [sg.Button('Exit')]]
  window = sg.Window('ITAコーパス出力くん', size=(300, 300)).Layout(layout)


  # UIイベント処理
  while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
      break

    if event == '-SPEAKER_NAME-':
      speaker_name = values['-SPEAKER_NAME-']
      style_names = get_style_names(speaker_name)
      window.find_element('-STYLE_NAME-').Update(values=style_names)

    if event == 'Start':
      speaker_name = values['-SPEAKER_NAME-']
      style_name = values['-STYLE_NAME-']
      if(speaker_name == "" or style_name == ""):
        window.find_element('-MESSAGE-').Update("話者とスタイルを選択してください")
      else:
        speaker_id = get_speaker_id(speaker_name, style_name)
        thread = threading.Thread(target=outputs, args=(speaker_id, speaker_name, style_name))
        thread.start()

  window.Close()

if __name__ == "__main__":
  main()