# coding=utf-8
# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants.backend.python.subsystems.isort import Isort
from pants.backend.python.tasks.python_tool_prep_base import PythonToolInstance, PythonToolPrepBase


class IsortInstance(PythonToolInstance):
  pass


class IsortPrep(PythonToolPrepBase):
  tool_subsystem_cls = Isort
  tool_instance_cls = IsortInstance
