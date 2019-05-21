# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from jsymbol import Symbol

def test_mdn_demo():
    symbol1 = Symbol();
    symbol3 = Symbol('foo');

    assert isinstance(symbol1, Symbol)
    assert str(symbol3) == 'Symbol(foo)'
    assert Symbol('foo') is not Symbol('foo')
    assert Symbol('foo') != Symbol('foo')

def test_symbol_can_use_as_key():
    data = {}
    symbol = Symbol()
    data[symbol] = 1
    assert data[symbol] == 1

def test_symbol_for_key():
    assert Symbol.for_key(15) is Symbol.for_key(15)

def test_symbol_key_for():
    key = 15
    sym = Symbol.for_key(key)
    assert Symbol.key_for(sym) is key

def test_symbol_dir():
    class C:
        pass

    c = C()
    vars(c)[Symbol.for_key('x')] = 15
    dir(c) # dir require order
