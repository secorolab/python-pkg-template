# SPDX-License-Identifier: MIT
from os.path import join
from platformdirs import user_cache_dir


PKG_NAME = "python_pkg_tmpl"


def get_pkg_cache_dir(subdir: str = PKG_NAME) -> str:
    """Returns a subdirectory under the user's cache directory

    Parameters:
        subdir: subdirectory name

    Returns:
        path to subdir in the user's cache directory
    """
    return join(user_cache_dir(), subdir)
