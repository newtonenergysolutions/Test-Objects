# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:40:48 2023

@author: MartinMohana-NewtonE
"""

import random

def sample_list(element_type, n:int=3):
    # TODO: add error if n is higher than sample list length
    # TODO: add random element_type
    # TODO: find standard test strings/numbers
    # TODO: add float
    # TODO: add nested list option
    if element_type == str:
        return ['a', 'b', 'c'][:n]
    if element_type == int:
        return [1, 2, 3][:n]
    
def sample_dict(keys_type=str, values_type=int):
    # TODO: add nested dict option
    return dict(zip(sample_list(keys_type), sample_list(values_type)))

def sample_set(element_type):
    return set(sample_list(element_type))
    
def sample_tuple(element_type):
    return tuple(sample_list(element_type))

def random_list(element_type, n:int=10):
    # TODO: add random int
    # TODO: add random string
    # TODO: add random float
    # TODO: add nested list option
    pass