import tweepy
import time


##Chaves necessárias para acessar a conta 
##Keys necessaries to access the account

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

canalhices_fabricio = 0
last_seen_id = 0

#File to archive the total of the counter
#Arquivo para guardar o total do contador
FILE_NAME = 'qtdcanalhices.txt'
FILE_NAME2 = 'last_seen_id.txt'

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
    last_seen_id = buscar_canalhices(FILE_NAME2)

    mentions = api.mentions_timeline(last_seen_id)

    for mention in reversed(mentions):
        if '#fabriciocanalha' in mention.text.lower():
            last_seen_id = mention.id
            guardar_canalhices(last_seen_id, FILE_NAME2)
            canalhices_fabricio += 1
            guardar_canalhices(canalhices_fabricio, FILE_NAME)
            print('Canalhice computada!')
            
    api.update_status('Fabrício já produziu ' + str(canalhices_fabricio) + ' canalhices. É um verdadeiro canalha!')

while True:
    reply_to_tweets()
    time.sleep(20)

