# -*- coding: utf-8 -*-
# Copyright (C) 2017-2018 Nathanael Philipp (jnphilipp) <mail@jnphilipp.org>
#
# This file is part of utils.
#
# utils is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with utils.  If not, see <http://www.gnu.org/licenses/>.

import json
import urllib.parse
import urllib.request


class BaseParser:
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) ' + \
        'Gecko/20100101 Firefox/41.0'

    def __init__(self, user_agent=None, *args, **kwargs):
        self.user_agent = user_agent

    def fetch(self, url, headers={}, data=None, user_agent=None):
        if user_agent:
            headers = {'User-Agent': user_agent}
        elif self.user_agent:
            headers = {'User-Agent': self.user_agent}
        if data:
            data = urllib.parse.urlencode(data).encode('utf-8')

        request = urllib.request.Request(urllib.parse.quote(url, ':/?=&'),
                                         data if data else None, headers)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            if 'charset' in response.getheader('Content-Type'):
                encoding = response.getheader('Content-Type') \
                    .split('charset=', 1)[-1].split('"', 1)[0]
                if encoding:
                    content = content.decode(encoding)
            if 'application/json' in response.getheader('Content-Type') or \
                    'text/json' in response.getheader('Content-Type'):
                content = json.loads(
                    content.decode('utf-8') if not encoding else content
                )
        return content

    def get_redirect_url(self, url):
        response = urllib.request.urlopen(url)
        return response.url
