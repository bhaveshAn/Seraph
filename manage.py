#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Use development platform if not set
    platform = os.getenv('SERAPH_PLATFORM', 'dev')

    if platform == 'dev':
        settings = 'seraph.settings.dev'
    elif platform == 'heroku':
        settings = 'seraph.settings.heroku'
    else:
        settings = 'seraph.settings.prod'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
