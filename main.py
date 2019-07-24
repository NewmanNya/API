import tweepy

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
def Tweet(api, PicAddress, PicName, Content):




    api.update_with_media(r"bg.jpg", "Hello World!\nSend from Pycharm by official APIs\n@Neko__Nya__\no(=•ェ•=)m")


if __name__ == '__main__':
    api = ApiInit()
    Tweet(api)
    pass
