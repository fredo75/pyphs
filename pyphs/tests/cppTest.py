#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 05:40:20 2017

@author: Falaize
"""

# Support for Python 2.x and Python 3.x
from __future__ import division

# retrieve the pyphs.PHSCore of a nonlinear RLC from the tutorial on PHSCore
from pyphs.tutorials.phscore import core as nlcore

from pyphs import PHSNumeric, numcore2cpp
import os
import shutil

here = os.path.realpath(__file__)[:os.path.realpath(__file__).rfind(os.sep)]


def cpp_nlcore_full():
    nums = PHSNumeric(nlcore)

    label = 'test'
    path = os.path.join(here, label)

    numcore2cpp(nums, objlabel=label, path=path)
    if not os.name.lower().startswith('nt'):
        shutil.rmtree(path)
    return True
