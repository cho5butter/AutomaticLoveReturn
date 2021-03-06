import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import os

##参照元 https://qiita.com/bgg0u/items/630a87ce1a44778bbeb1


class Mail:
    def __init__(self, setting, counter):
        self.isSent = setting["mailSetting"]["isSent"]
        self.toAddress = os.environ['TWITTER_ADDRESS']
        self.fromAddress = os.environ['TWITTER_ADDRESS']
        self.subject = setting["mailSetting"]["subject"]
        self.password = os.environ['TWITTER_PASSWORD']
        self.counter = counter
    def sentMail(self):
        if self.isSent == "true":
            self.msg = self.createMessage(self.fromAddress, self.toAddress, self.subject, self.counter)
            self.send(self.fromAddress, self.toAddress, self.msg, self.password)
    def createMessage(self, fromAddress, toAddress, subject, counter):
        msg = MIMEText(str(counter)+"件のツイートの遡りに成功しました")
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['To'] = toAddress
        msg['Date'] = formatdate()
        return msg
    def send(self, fromAddress, toAddress, msg, password):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(fromAddress, password)
        smtpobj.sendmail(fromAddress, toAddress, msg.as_string())
        smtpobj.close()
