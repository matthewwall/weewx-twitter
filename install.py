# $Id: install.py 1491 2016-05-15 23:00:28Z mwall $
# installer for Twitter
# Copyright 2014-2020 Matthew Wall

from weecfg.extension import ExtensionInstaller


def loader():
    return TwitterInstaller()


class TwitterInstaller(ExtensionInstaller):
    def __init__(self):
        super(TwitterInstaller, self).__init__(
            version="0.15",
            name='twitter',
            description='tweet weather data',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            restful_services='user.twitter.Twitter',
            config={
                'StdRESTful': {
                    'Twitter': {
                        'app_key': 'APP_KEY',
                        'app_key_secret': 'APP_KEY_SECRET',
                        'oauth_token': 'OAUTH_TOKEN',
                        'oauth_token_secret': 'OAUTH_TOKEN_SECRET'}}},
            files=[('bin/user', ['bin/user/twitter.py'])]
        )
