import tweepy
import time
import os

# For safety, Read key from txt
def ReadKey():
    Key_list = []
    with open('password.txt','r') as f:
        for line in f:
            # Copy from internet [works]
            Key_list.append(line.strip('\n').split(',')[0])

    return Key_list

# Init API
def ApiInit():
    Key_list = ReadKey()
    auth = tweepy.OAuthHandler(Key_list[0], Key_list[1])
    auth.set_access_token(Key_list[2], Key_list[3])
    return tweepy.API(auth)

# Tweet function
def TweetFunction(api, PicAddress, PicName, Content):
    filelist = os.listdir(PicAddress)
    for item in filelist:
        if(item.startswith(PicName)):
            PicCmd = PicAddress+ '/' + item
            break
    try:
        api.update_with_media(PicCmd, Content)
        print("Send "+item)
    except:
        print()

def TweetCmd(num):
    for i in range(0,num):
        Content = 'Set Time Test\nTask: '+ str(i)
        Picname = str(i)
        Tweet(api, PicAddress="./UPLOAD",PicName= Picname, Content=Content)
        time.sleep(600)

if __name__ == '__main__':
    api = ApiInit()
    TweetCmd(5)

