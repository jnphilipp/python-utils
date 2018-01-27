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


def p(fields, line_length=100, after='_', positions=[.33, .55, .67, 1.]):
    if positions[-1] <= 1:
        positions = [int(line_length * p) for p in positions]

    def print_row(fields, positions):
        line = ''
        rfields = []
        for i in range(len(fields)):
            line += str(fields[i])

            if len(line) > positions[i]:
                rf = line.rfind(' ', positions[i - 1] if i > 0 else 0,
                                positions[i])
                if rf > 0:
                    rfields.append(line[rf + 1:])
                    line = line[:rf]
                else:
                    line = line[:positions[i]]
                    rfields.append(line[positions[i]:])
            else:
                rfields.append('')
            line += ' ' * (positions[i] - len(line))
        print(line)
        if max([f != '' for f in rfields]):
            print_row(rfields, positions)

    print_row(fields, positions)
    if after:
        print(after * line_length)
