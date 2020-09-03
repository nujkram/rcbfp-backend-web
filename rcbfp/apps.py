# Application definition

INSTALLED_APPS = [

]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
]

# Logging and debugging
INSTALLED_APPS += [
    'debug_toolbar',
]

INSTALLED_APPS += [
    'django_extensions',
    'django_filters'
]

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

# Utilities
INSTALLED_APPS += [
]

# Template Tags
INSTALLED_APPS += [

]

# Common Scaffold
INSTALLED_APPS += [
    'crispy_forms',
    'phonenumber_field',
]

# Core
INSTALLED_APPS += [
    'locations',
    'datesdim',
    'accounts',
    'profiles',
    'buildings',
    'business',
    'checklists',
    'incidents',
    'admin_dashboards',
    'inspections',
    'inspector_dashboards',
]