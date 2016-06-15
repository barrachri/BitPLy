#!/usr/bin/env python
import os
import sys

import utils

if __name__ == "__main__":
    # Check if the PRODUCTION_ENV exists, if not set it to False
    # and loads the normal settings
    PRODUCTION_ENV = utils.get_env("PRODUCTION_ENV", False)
    if PRODUCTION_ENV:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitply.prod_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitply.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
