"""
Created on 2018/04/22

@author: ちょこばた
"""


# import
import twitter
import json
import datetime
from modules import function as fn
from modules import object as cs

#ツイート格納タプル
tweetsList = []

#カウンター
counter = 0

# json形式の設定ファイル読み込み
settingFile = open('setting.json')
settingData = json.load(settingFile)

#ブラックリスト取得
blackLists = settingData["blackList"]["blackArray"]

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

#ブラックリスト@削除処理
for i in range(len(blackLists)):
    blackLists[i] = blackLists[i].replace("@","")

#ツイート取得
for listId in listIds:
    tweets = fn.getTimeLine(listId, NUMBER_OF_TWEETS, t)
    for tweet in tweets:
        tmpDic = {
            "date" : tweet['created_at'] ,
            "id" : tweet['id'] ,
            "tweet" : tweet['text'] ,
            "user" : tweet['user']['screen_name'] ,
            "source" : tweet['source']
        }
        tweetsList.append(tmpDic)

#取得ツイート処理
for tweetList in tweetsList:
    tmpUser = tweetList["user"]
    tmpTweetID = tweetList["id"]
    tmpDate = datetime.datetime.strptime(tweetList["date"], '%a %b %d %H:%M:%S +0000 %Y')
    print(tmpUser)
    print(tmpTweetID)
    print(tmpDate)
    isIncludeBlackList = fn.isIncludeBlackList(blackLists, tmpUser)
    if not isIncludeBlackList:
        isExtendedTweetID = fn.isExtendedTweetID(tmpTweetID)
        if not isExtendedTweetID:
            if tmpDate > sinceTime:
                if counter < NUMBER_OF_TWEETS:
                    try:
                        t.favorites.create(_id = tmpTweetID)
                    except:
                        print("既にお気に入りに登録されている可能性があります")
                    counter+=1
                    print(counter)

#メール送信
mail = cs.Mail(settingData, counter)
mail.sentMail()
