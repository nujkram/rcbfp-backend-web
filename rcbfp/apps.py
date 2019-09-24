# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.postgres',
  'django.contrib.humanize',

  'debug_toolbar',

  'rest_framework',
  'rest_framework.authtoken',
  'crispy_forms',
  'phonenumber_field',

  'django_extensions',

  'locations',
  'datesdim',
  'accounts',
  'profiles',
  'buildings',
  'business',
  'checklists'
]
