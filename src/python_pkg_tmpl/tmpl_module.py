# SPDX-License-Identifier: MIT
from os.path import join
from platformdirs import user_cache_dir


PKG_NAME = "python_pkg_tmpl"


def get_pkg_cache_dir() -> str:
    return join(user_cache_dir(), PKG_NAME)
