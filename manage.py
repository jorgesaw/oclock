#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from environs import Env

def main():
    env = Env()
    env.read_env()

    production = env.bool("ENV_VPS_PRODUCTION")

    settings = 'backend.settings.local'
    
    if production:
        settings = 'backend.settings.production'

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
