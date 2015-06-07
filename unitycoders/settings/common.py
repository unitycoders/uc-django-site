"""
Django settings for unitycoders project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))+"/../"
DATA_DIR = os.path.join(BASE_DIR, 'data')
VAR_DIR = os.path.join(BASE_DIR, 'var') # volitile data

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = '' # Override this in your production settings

# default to disabling everything
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'rest_framework',
    'bs_themetools',
    'markdown_deux',
    'bootstrap3',
    'crispy_forms',
    'lectern',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'unitycoders.urls'
WSGI_APPLICATION = 'unitycoders.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.contrib.messages.context_processors.messages",
	"django.template.context_processors.debug",
	"django.template.context_processors.i18n",
	"django.template.context_processors.media",
	"django.template.context_processors.static",
	"django.template.context_processors.tz",
	'django.core.context_processors.request',
	'allauth.account.context_processors.account',
	'allauth.socialaccount.context_processors.socialaccount',
)

TEMPLATE_DIRS = [os.path.join(DATA_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(DATA_DIR, 'theme')]
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
STATIC_URL = '/static/'

# Gatekeeper Profile
#AUTH_USER_MODEL = 'gatekeeper.Member'

# Markdown deux
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
            "fenced-code-blocks": None,
            "tables": None,
            "metadata": None
        },
        "safe_mode": "escape",
    },
}

# Django rest framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# django crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

ACCOUNT_FORMS = {
	'login': 'unitycoders.forms.LoginForm',
	'signup': 'unitycoders.forms.RegisterForm'
}

# Authentication Backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
