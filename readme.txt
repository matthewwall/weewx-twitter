twitter - weewx extension that sends data to Twitter
Copyright 2014 Matthew Wall

Installation instructions:

1) download

wget -O weewx-twitter.zip https://github.com/matthewwall/weewx-twitter/archive/master.zip

2) install twython

sudo pip install twython

3) run the installer:

wee_extension --install weewx-twitter.zip

4) modify weewx.conf:

[StdRESTful]
    [[Twitter]]
        app_key = APP_KEY
        app_key_secret = APP_KEY_SECRET
        oauth_token = OAUTH_TOKEN
        oauth_token_secret = OAUTH_TOKEN_SECRET

5) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
