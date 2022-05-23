from math import *
from function_for_filter import f
from function_for_map import f_map

def test_filter():
    assert list(filter(f,[1, 2, 4, 5, 7, 8, 10, 11]))==[2, 4, 8, 10]
def test_map():
    assert list(map(f_map,[1,2,3,4,5]))==[1,4,9,16,25]
def test_sorted():
    assert sorted([3,2,62,46,12,1])==[1,2,3,12,46,62]

def test_math_pi():
    assert round(pi,2)==3.14
def test_math_sqrt():
    assert sqrt(25)==5
def test_math_pow():
    assert pow(2,3)==8
def test_math_hypot():
    assert hypot(3, 4)==5

