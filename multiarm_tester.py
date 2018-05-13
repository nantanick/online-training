#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:44:06 2018

@author: nantanick
"""
import numpy as np
from multiarmbandit import ucb1,egreedy

"""
This file is used to thest the multiarm bandit
"""
#test = ucb1(['a','b','c'])
test = egreedy(['a','b','c'], .3)
centers = [1,2,3]


def get_feedback(index):
    return np.random.normal(loc=centers[index], scale=.5, size=None)

for i in range(50):
    arm = test.pick_arm()
    print(arm)
    test.update(arm[1], get_feedback(arm[1]))