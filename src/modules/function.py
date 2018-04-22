tweetIds = []

#ツイート取得
def getTimeLine(listId, numberOfTweets, t):
    return t.lists.statuses(list_id = listId, count = numberOfTweets)

def isIncludeBlackList(blackLists, tmpUser):
    isIncludeBlackList = tmpUser in blackLists
    if isIncludeBlackList:
        return True
    else:
        return False

def isExtendedTweetID(tmpTweetID):
    isExtendedTweetID = tmpTweetID in tweetIds
    if isExtendedTweetID:
        return True
    else:
        tweetIds.append(tmpTweetID)
        return False
