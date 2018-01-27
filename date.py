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

from datetime import timedelta


def daterange(start_date, end_date):
    if not start_date or not end_date:
        return
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)
