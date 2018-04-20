# import
import twitter
import json

# json形式の設定ファイル読み込み
settingFile = open('setting.json')
settingData = json.load(settingFile)

# 設定値を読み込み
CONSUMERKEY = settingData["twitterApp"]["consumerKey"]
CONSUMERSECRET = settingData["twitterApp"]["consumerSecret"]
ACCESSTOKEN = settingData["twitterApp"]["accessToken"]
ACCESSTOKENSECRET = settingData["twitterApp"]["accessTokenSecret"]

auth = twitter.OAuth(
                        consumer_key = CONSUMERKEY,
                        consumer_secret = CONSUMERSECRET,
                        token = ACCESSTOKEN,
                        token_secret = ACCESSTOKENSECRET
                    )

t = twitter.Twitter(auth = auth)

t.statuses.update(status="pythonからの送信テスト")
