# import
import twitter
import json
import datetime
from modules import function as fn

#ツイート格納タプル
tweetsList = []

# json形式の設定ファイル読み込み
settingFile = open('setting.json')
settingData = json.load(settingFile)

# 設定値を読み込み
CONSUMER_KEY = settingData["twitterApp"]["consumerKey"]
CONSUMER_SECRET = settingData["twitterApp"]["consumerSecret"]
ACCESS_TOKEN = settingData["twitterApp"]["accessToken"]
ACCESS_TOKEN_SECRET = settingData["twitterApp"]["accessTokenSecret"]

# インスタンスを生成
auth = twitter.OAuth(consumer_key = CONSUMER_KEY ,
                     consumer_secret = CONSUMER_SECRET ,
                     token = ACCESS_TOKEN ,
                     token_secret = ACCESS_TOKEN_SECRET)

t = twitter.Twitter(auth = auth)

#現在時刻記録
nowTime = datetime.datetime.now()

#取得開始時刻
DAY = settingData["setting"]["Day"]
sinceTime = nowTime - datetime.timedelta(days = DAY)

#最大ツイート取得
NUMBER_OF_TWEETS = settingData["setting"]["numberOfTweets"]

#リスト取得
listIds = settingData["setting"]["listID"]

#ツイート取得
for listId in listIds:
    tweets = fn.getTimeLine(listId, NUMBER_OF_TWEETS, t)
    for tweet in tweets:
        tmpDic = {
            "data" : tweet['created_at'] ,
            "id" : tweet['id'] ,
            "tweet" : tweet['text'] ,
            "user" : tweet['user']['screen_name'] ,
            "source" : tweet['source']
        }
        tweetsList.append(tmpDic)
print(tweetsList)
