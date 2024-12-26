import schedule, time, os, smtplib, random
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 


quotes = ["You must be the change you wish to see in the world. ","Spread love everywhere you go."]


password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
  quote = random.choice(quotes)
  print(quote)
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = username 
  msg['From'] = username 
  msg['Subject'] = "Take a BREAK" 
  msg.attach(MIMEText(quote, 'html'))
  s.send_message(msg) 
  del msg 

schedule.every(2).seconds.do(sendMail) 

while True:
  schedule.run_pending()
  time.sleep(1)