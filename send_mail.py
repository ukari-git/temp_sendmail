from asyncore import read
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



import openpyxl

wb = openpyxl.load_workbook('customer.xlsx')
ws = wb['Sheet1']

customer_list =[]

for i in ws.iter_rows():
    if i[0] is None:
        break
    templist = []
    for j in i:
        templist.append(j.value)
    customer_list.append(templist)


my_adress = "ukari1986@gmail.com"
smtp_server ="smtp.gmail.com"
port_number = 587
account = "ukari1986"
password = "4266711$a"



with open("test.txt",encoding='utf_8') as f:
    body = f.read()


    for i in customer_list:

        msg = MIMEMultipart()
        msg["subject"]="test_subject"
        msg["to"]=my_adress
        msg["from"]=my_adress
        
        body_one =  body.format(customer=i[0],book=i[2])
        print(type(body_one))

        body_msg = MIMEText(body_one)
        msg.attach(body_msg)
        server = smtplib.SMTP(smtp_server,port_number)
        server.starttls()
        server.login(account,password)
        server.send_message(msg)
        del msg





server.quit()