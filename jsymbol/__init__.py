# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from functools import total_ordering
from typing import Union
from threading import Lock
from weakref import WeakKeyDictionary, WeakValueDictionary

@total_ordering
class Symbol:
    _for_key_registrys = WeakValueDictionary()
    _key_for_registrys = WeakKeyDictionary()
    _lock = Lock()
    __slots__ = ('_desc', '__weakref__')

    def __init__(self, description: Union[str, int] = None):
        if description is None:
            self._desc = ''
        else:
            self._desc = str(description)

    def __init_subclass__(cls):
        raise TypeError # does not allow subclass

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'Symbol({self._desc})'

    def __gt__(self, other):
        if other.__class__ is not Symbol:
            return False
        return id(self) > id(other)

    @classmethod
    def for_key(cls, key: Union[str, int]):
        '''
        Returns a Symbol object from the global symbol registry matching the given key if found.
        Otherwise, returns a new symbol with this key.
        '''
        if not isinstance(key, (str, int)):
            raise TypeError

        with cls._lock:
            try:
                return cls._for_key_registrys[key]
            except KeyError:
                pass

            symbol = Symbol(key)
            cls._for_key_registrys[key] = symbol
            cls._key_for_registrys[symbol] = key
            return symbol

    @classmethod
    def key_for(cls, symbol):
        '''
        Returns a key from the global symbol registry matching the given Symbol if found.
        Otherwise, returns `None`.
        '''
        if not isinstance(symbol, Symbol):
            raise TypeError

        with cls._lock:
            return cls._key_for_registrys.get(symbol)
