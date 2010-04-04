# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from lettuce.registry import world
from lettuce.registry import CALLBACK_REGISTRY
world._set = True

class before:
    @classmethod
    def each_step(cls, function):
        CALLBACK_REGISTRY['step']['%s_each' % cls.__name__].append(function)
        return function

    @classmethod
    def each_scenario(cls, function):
        CALLBACK_REGISTRY['scenario']['%s_each' % cls.__name__].append(function)
        return function

class after:
    @classmethod
    def each_step(cls, function):
        CALLBACK_REGISTRY['step']['%s_each' % cls.__name__].append(function)
        return function

    @classmethod
    def each_scenario(cls, function):
        CALLBACK_REGISTRY['scenario']['%s_each' % cls.__name__].append(function)
        return function
