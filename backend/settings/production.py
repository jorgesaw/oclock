"""Production settings."""

from .base import *  # NOQA
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-au=+r(#zy-tug66le4d8i6g1xe2facnkwt+8v_=86qn*d-0u(%'
SECRET_KEY = env.str("DJANGO_SECRET_KEY")
                                            
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')