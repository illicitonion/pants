# coding=utf-8
# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants.rules.core import fastlist, filedeps
from pants.rules.core.test import coordinator_of_tests, fast_test


def rules():
  return fastlist.rules() + filedeps.rules() + [
    fast_test,
    coordinator_of_tests,
  ]
