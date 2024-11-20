# SPDX-License-Identifier: MIT
import unittest
import os
from python_pkg_tmpl.tmpl_module import get_pkg_cache_dir


class NamingTest(unittest.TestCase):
    def test_get_cache_dir(self) -> None:
        cache_dir = get_pkg_cache_dir()
        os.mkdir(cache_dir)
        self.assertTrue(os.path.exists(cache_dir))
