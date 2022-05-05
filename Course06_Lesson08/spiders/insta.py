# [Crawler] Учебник по Python Scrapy
# https://russianblogs.com/article/1404366259/
# Spiders
# https://docs.scrapy.org/en/latest/topics/spiders.html
import json
import re
import scrapy
from scrapy.http import HtmlResponse
from instaparser.items import InstaparserItem
from urllib.parse import urlencode
from copy import deepcopy
from pprint import pprint

def fetch_user_id(text, username):
    try:
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')
    except:
        return re.findall('\"id\":\"\\d+\"', text)[-1].split('"')[-2]


def fetch_csrf_token(text):
    """ Get csrf-token for auth"""
    matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
    return matched.split(':').pop().replace(r'"', '')


class InstaSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']
    insta_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    insta_username = 'XXX'
    insta_password = '#PWD_INSTAGRAM_BROWSER:10:YYY'
    parse_user = ['techskills_2022', 'a.i.india']
    insta_api_friendships_url = 'https://i.instagram.com/api/v1/friendships/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
    user_agent02 = 'Instagram 155.0.0.37.107'

    def parse(self, response: HtmlResponse, **kwargs):
        csrf = fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            self.insta_login_link,
            method='POST',
            callback=self.login,
            formdata={'username': self.insta_username,
                      'enc_password': self.insta_password},
            cb_kwargs={'csrf': csrf},
            headers={'X-CSRFToken': csrf,
                     'User-Agent': self.user_agent})

    def login(self, response: HtmlResponse, csrf):
        j_body = response.json()
        if j_body.get('authenticated'):
            for username in self.parse_user:
                yield response.follow(url=f'/{username}/',
                                      callback=self.user_data_parse,
                                      cb_kwargs={'username': username,
                                                 'csrf': csrf},
                                      headers={'X-CSRFToken': csrf,
                                               'User-Agent': self.user_agent02})

    def user_data_parse(self, response: HtmlResponse, username, csrf):
        user_id = fetch_user_id(response.text, username)
        variables_followers = {'search_surface': 'follow_list_page',
                               'count': 12}
        variables_following = {'count': 12}
        url_followers = f'{self.insta_api_friendships_url}{user_id}/followers/?{urlencode(variables_followers)}'
        url_following = f'{self.insta_api_friendships_url}{user_id}/following/?{urlencode(variables_following)}'
        yield response.follow(url_followers,
                              callback=self.user_followers,
                              cb_kwargs={'username': username,
                                         'user_id': user_id,
                                         'csrf': csrf,
                                         'variables_followers': deepcopy(variables_followers)},
                              headers={'X-CSRFToken': csrf,
                                       'User-Agent': self.user_agent02})
        yield response.follow(url_following,
                              callback=self.user_following,
                              cb_kwargs={'username': username,
                                         'user_id': user_id,
                                         'csrf': csrf,
                                         'variables_following': deepcopy(variables_following)},
                              headers={'X-CSRFToken': csrf,
                                       'User-Agent': self.user_agent02})

    def user_followers(self, response: HtmlResponse, username, user_id, csrf, variables_followers):
        j_body = response.json()
        if j_body.get('big_list'):
            variables_followers['max_id'] = j_body.get('next_max_id')
            url_followers = f'{self.insta_api_friendships_url}{user_id}/followers/?{urlencode(variables_followers)}'
            yield response.follow(url_followers,
                                  callback=self.user_followers,
                                  cb_kwargs={'username': username,
                                             'user_id': user_id,
                                             'csrf': csrf,
                                             'variables_followers': deepcopy(variables_followers)
                                             },
                                  headers={'X-CSRFToken': csrf,
                                           'User-Agent': self.user_agent02})
        for user in j_body.get('users'):
            item = InstaparserItem(
                profile_username=username,
                status='follower',
                user_id=user.get('pk'),
                username=user.get('username'),
                pic=user.get('profile_pic_url'),
                data=user)
            yield item

    def user_following(self, response: HtmlResponse, username, user_id, csrf, variables_following):
        j_body = response.json()
        if j_body.get('big_list'):
            variables_following['max_id'] = j_body.get('next_max_id')
            url_following = f'{self.insta_api_friendships_url}{user_id}/following/?{urlencode(variables_following)}'
            yield response.follow(url_following,
                                  callback=self.user_following,
                                  cb_kwargs={'username': username,
                                             'user_id': user_id,
                                             'csrf': csrf,
                                             'variables_following': deepcopy(variables_following)
                                             },
                                  headers={'X-CSRFToken': csrf,
                                           'User-Agent': self.user_agent02})
        for user in j_body.get('users'):
            item = InstaparserItem(
                profile_username=username,
                status='followee',
                user_id=user.get('pk'),
                username=user.get('username'),
                pic=user.get('profile_pic_url'),
                data=user)
            yield item
