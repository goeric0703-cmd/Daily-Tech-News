import feedparser
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

# 1. 抓取资讯
rss_url = "https://news.ycombinator.com/rss"
feed = feedparser.parse(rss_url)

content = "🌍 每日全球科技资讯推送\n\n"
for entry in feed.entries[:15]:
    content += f"- {entry.title}\n  链接: {entry.link}\n\n"

# 2. 邮件配置
sender = 'goeric0703@gmail.com'
receiver = 'goeric0703@gmail.com'
password = os.environ.get("EMAIL_PASSWORD") # 从 GitHub Secrets 读取
subject = '今日科技资讯日报'

# 3. 构造邮件格式
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(subject, 'utf-8')

try:
    # Gmail 的 SMTP 服务器和端口
    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_obj.login(sender, password)
    smtp_obj.sendmail(sender, [receiver], message.as_string())
    print("🎉 邮件发送成功！")
except Exception as e:
    print(f"❌ 发送失败，原因: {e}")
