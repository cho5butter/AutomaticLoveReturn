import twitter
import json

# json形式の設定ファイル読み込み
settingFile = open('setting.json')
settingData = json.load(settingFile)

print(settingData)
