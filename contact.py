from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import AddContactRequest
import configparser
import sys, os, re, csv
import random

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    print(re+"[!] run python setup.py first !!\n")
    sys.exit(1)

gr="\033[1;32m"

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))


users = []
with open(r"members.csv", encoding='UTF-8') as f: 
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    count = 0
    for row in rows:
        if count == 40:
            break
        if row[0] != '':
            user = row[0]
            users.append(user)
        count += 1
        
j = 0
for user in users:
    j += 1
    print(j)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = random.randint(3, 10)
    firstname = alphabet[:i]
    lastname = alphabet[:i-1]
    phone = alphabet[:i+1]
    client(AddContactRequest(client.get_entity(user), firstname, lastname, phone))
