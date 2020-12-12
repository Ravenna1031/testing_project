# coding: utf-8
import time

def test_rerun():
    time.sleep(0.5)
    assert 1 == 2

def test_rerun1():
    time.sleep(0.5)
    assert 1 == 1

def test_rerun2():
    time.sleep(0.5)
    assert 3 == 2