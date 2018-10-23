#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from bdp_package_template.skeleton import fib

__author__ = "lindelanig"
__copyright__ = "lindelanig"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
