import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

##参照元 https://qiita.com/bgg0u/items/630a87ce1a44778bbeb1


class Mail:
    def __init__(self, setting, counter):
        self.isSent = setting["mailSetting"]["isSent"]
        self.toAddress = setting["mailSetting"]["sentAddress"]
        self.fromAddress = setting["mailSetting"]["fromAddress"]
        self.subject = setting["mailSetting"]["subject"]
        self.password = setting["mailSetting"]["password"]
        self.counter = counter
    def sentMail(self):
        self.msg = self.createMassage(self.fromAddress, self.toAddress, self.subject, self.counter)
        self.send(self.fromAddress, self.toAddress, self.msg, self.password)
    def createMessage(self, fromAddress, toAddress, subject, counter):
        msg = MIMEText(counter+"件のツイートの遡りに成功しました")
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['To'] = toAddress
        msg['Date'] = formatdate()
        return msg
    def send(fromAddress, toAddress, msg, password):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(fromAddress, password)
        smtpobj.sendmail(fromAddress, toAddress, msg.as_string())
        smtpobj.close()
