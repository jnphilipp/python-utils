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

from math import ceil, floor


def app_version(app_name, description, version, license, author, email,
                url=None):
    """Generate command line version text."""
    def line(text):
        """Make single line with padding left and right."""
        return '#%s%s%s#\n' % (' ' * floor((47 - len(text)) / 2),
                               text,
                               ' ' * ceil((47 - len(text)) / 2))

    return (('#################################################\n' +
             line(app_name) +
             line(description) +
             line('') +
             line(version) +
             line(license) +
             line(author) +
             line(email) +
             (line('') + line(url) if url else '') +
             '#################################################'))
