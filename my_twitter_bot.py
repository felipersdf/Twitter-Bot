import tweepy
import time

CONSUMER_KEY = 'ZUeC3IaKYOuU7EPHgpf6nUHR5'
CONSUMER_SECRET = 'TB6FuDOZzLEVlA98tg5EAK3PmT4qjAG7yAif5zWSGQocOypjfQ'
ACCESS_KEY = '1092557643288375296-RAig6zvWAtSNxe0DXDFUO3Ht5lbry6'
ACCESS_SECRET = 'Io2MSSdJlKKDxBxGnNN1sVVBPB7qqRynoMn0FqNmWaLKT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

canalhices_fabricio = 0
FILE_NAME = 'qtdcanalhices.txt'

def buscar_canalhices(file_name):
    f_read = open(file_name, 'r')
    qtd = int(f_read.read().strip())
    f_read.close()
    return qtd

def guardar_canalhices(qtd, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(qtd))
    f_write.close()
    return

def reply_to_tweets():
    print('searching for canalhices...')
    canalhices_fabricio = buscar_canalhices(FILE_NAME)

    mentions = api.mentions_timeline()

    for mention in reversed(mentions):
        if '#fabriciocanalha' in mention.text.lower():
            canalhices_fabricio += 1
            guardar_canalhices(canalhices_fabricio, FILE_NAME)
            print('Canalhice computada!')
            
    api.update_status('Fabrício já produziu ' + str(canalhices_fabricio) + ' canalhices. É um verdadeiro canalha!')

while True:
    reply_to_tweets()
    time.sleep(20)