# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request


class BaseParser:
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'

    def fetch(self, url, quote=True, data=None, user_agent=False, extra_headers={}):
        headers = {}
        if user_agent:
            headers = {'User-Agent': self.user_agent}
        if extra_headers:
            headers = dict(headers.items(), **dict(extra_headers.items()))
        if data:
            data = urllib.parse.urlencode(data).encode('utf-8')
            request = urllib.request.Request(urllib.parse.quote(url, ':/?=&') if qoute else url, data, headers)
        else:
            request = urllib.request.Request(urllib.parse.quote(url, ':/?=&') if quote else url, headers=headers)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            if 'charset' in response.getheader('Content-Type'):
                encoding = response.getheader('Content-Type').split('charset=', 1)[-1].split('"', 1)[0]
                if encoding:
                    content = content.decode(encoding)
            if 'application/json' in response.getheader('Content-Type'):
                content = json.loads(content.decode('utf-8'))
        return content

    def get_redirect_url(self, url):
        response = urllib.request.urlopen(url)
        return response.url
