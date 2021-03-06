# AutomaticLoveReturn

[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg?longCache=true&style=flat)]()
[![Maintainability](https://api.codeclimate.com/v1/badges/f0c0914087d81e0922d7/maintainability)](https://codeclimate.com/github/cho5butter/AutomaticLoveReturn/maintainability)
[![Python](https://img.shields.io/badge/python-3.6.4-ff69b4.svg?longCache=true&style=flat)]()
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Progress](https://img.shields.io/badge/progress-completion-green.svg?longCache=true&style=flat)]()


## 説明

AutomaticLoveReturnは特定のリストを自動遡りするツールです
自分用に開発しているので、設定ファイル等に不親切なところがある点、ご了承ください

## 使い方

1. srcの中の[ setting-default.json ]をコピーして、コピーしたものの名前を[ setting.json ]に改名
2. そして、そのファイルの中身を自分の設定に変更（詳しくは以下項目、設定の仕方を参照してください）
3. 環境変数を登録して下さい（以下に記載）
4. run.pyを実行(定期的に実行させたい場合はcronなどを使って実行してください)

## 設定の仕方

### version

変更する必要はありません、そのまま使っていただいて構いません

### setting

* Day
リストのツイートを最大何日遡るかを設定します
記入例) 3
必ず半角英数字の整数で記入してください
また、既にお気に入りに登録したかどうかの判定は現バージョンでは行っていませんので、cronなどで定期的に実行する場合は、Dayで設定した日数より長いスパンで実行するようにしてください

* numberOfTweets
一回の実行でお気に入りに登録するツイートの最大数です
記入例) 200
1回でのお気に入りに登録できるツイートの上限が決まっているので、それより大きい値を入力した場合でも、上限数のツイートまでしかお気に入りに登録することができませんのでご了承ください

* incrts
RTも遡り対象にするかどうかを決めます
する場合は true しない場合は false を入力します

* listID
遡り対象のリストのIDを記入します
リストのIDの取得方法はGoogle先生に聞いてください

### blackList

* blackArray
遡り対象にしたくないユーザー名をここに入れてください
記入例) @null

### mailSetting
* isSent
プログラムが実行されたときに実行結果のメールを送るかどうかの設定です
true （送信する）か false（送信しない）のどちらかを入力してください
記入例）false

* subject
メールの題名（件名）を記入してください


## 環境変数

環境変数の設定の仕方は環境により異なりますのでご自身の環境に合わせた方法で行って下さい

* TWITTER_CK
ConsumerKey

<https://apps.twitter.com/>にアクセスし、アプリを作成して、それぞれの値を取得してください
詳しい説明は省きますので、わからない方はGoogle先生に質問すると沢山出てきます
* TWITTER_CS
ConsumerSecret
* TWITTER_AT
AccessToken
* TWITTER_ATS
AccessTokenSecret
* TWITTER_ADDRESS
結果を送信するメールアドレスを入力してください
（送信元もここで設定したものと同じになります）
記入例) test@null.com
* TWITTER_PASSWORD
Gmailのアプリパスワードを記入してください
詳細はこちら：<https://support.google.com/accounts/answer/185833?hl=ja&ctx=ch_b%2F0%2FDisplayUnlockCaptcha>

## サポート

twitter
<https://twitter.com/__cho__>
メールフォーム
<https://c5bt.net/contact>
