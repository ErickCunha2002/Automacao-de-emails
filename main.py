import smtplib
import datetime as dt
import pandas as pd
import random


EMAIL='Seu email aqui'
#Você precisa gerar uma senha automática dentro das configurações do seu email.
SENHA='Sua senha aqui'

data=dt.datetime.now()
hoje=(data.month, data.day)
arquivo=pd.read_csv('Dia-33/birthdays.csv')
aniversarios={(pessoa.month, pessoa.day): pessoa for (indice, pessoa) in arquivo.iterrows()}


if hoje in aniversarios:
    aniversario_pessoa=aniversarios[hoje]
    carta_aleatoria=f'Dia-33/todas_cartas/letter_{random.randint(1,3)}.txt'
    
    with open(carta_aleatoria) as carta:
        dados=carta.read()
        carta_aniversario=dados.replace('[NAME]', aniversario_pessoa['name'])
    
    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(user=EMAIL,password=SENHA)
        smtp.sendmail(from_addr=EMAIL, 
                      to_addrs=aniversario_pessoa['email'], 
                      msg=f'Subject: Feliz Aniversario!\n\n{carta_aniversario}'
                     )



