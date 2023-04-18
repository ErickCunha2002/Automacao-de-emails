import smtplib
import datetime as dt
import random

my_email='cunhaerick88@gmail.com'
password='lmzgsgucklhlgpjp'
lista_de_emails=['erick-pirata2@hotmail.com','erick-pirata4@hotmail.com','erick-pirata0@hotmail.com']


with open('frases.txt', encoding='utf-8') as arquivo:
    frases= arquivo.readlines()
    frase_do_dia= random.choice(frases)
    

hoje=dt.datetime.now()
dia_semana=hoje.weekday()

if dia_semana == 6:
    with smtplib.SMTP_SSL('smtp.gmail.com',port=465) as smtp:
     smtp.login(user=my_email,password=password)
     for email in lista_de_emails:
         smtp.sendmail(from_addr=my_email, 
                     to_addrs=email,
                     msg=f'Subject: Monday Motivation\n\n{frase_do_dia}')