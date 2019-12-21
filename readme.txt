twitter - weewx extension that sends data to Twitter
Copyright 2014 Matthew Wall

Installation instructions:

0) install twython

sudo pip install twython

1) run the installer:

wee_extension --install weewx-twitter.tgz

2) modify weewx.conf:

[StdRESTful]
    [[Twitter]]
        app_key = APP_KEY
        app_key_secret = APP_KEY_SECRET
        oauth_token = OAUTH_TOKEN
        oauth_token_secret = OAUTH_TOKEN_SECRET

4) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
