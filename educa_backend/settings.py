INSTALLED_APPS = [
    'rest_framework',
    'users',
    'contents',
    'statistics',
    ...
]
AUTH_USER_MODEL = 'users.CustomUser'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
