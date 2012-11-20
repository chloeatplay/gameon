# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py
from funfactory.settings_base import *

# Name of the top-level module where you put all your apps.
# If you did not install Playdoh with the funfactory installer script
# you may need to edit this value. See the docs about installing from a
# clone.
PROJECT_MODULE = 'gameon'

GAMEON_CHALLENGE_SLUG = 'gameon-2013'

# Defines the views served for root URLs.
ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Django admin
    'django.contrib.admin',
    # Application base, containing global templates.
    '%s.base' % PROJECT_MODULE,
    # Static website base, containing global templates.
    '%s.static_site' % PROJECT_MODULE,
    '%s.users' % PROJECT_MODULE,
    '%s.submissions' % PROJECT_MODULE,
    'south',
]

LOCALE_PATHS = (
    os.path.join(ROOT, PROJECT_MODULE, 'locale'),
)

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
]

# BrowserID configuration
AUTHENTICATION_BACKENDS = [
    'django_browserid.auth.BrowserIDBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PROFILE_MODULE = 'users.Profile'

SITE_URL = 'http://127.0.0.1:8000'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = 'static_site.home'

BROWSERID_CREATE_USER = True

TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS) + [
    'django_browserid.context_processors.browserid_form',
]

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES) + [
    'gameon.users.middleware.ProfileMiddleware',
    'gameon.submissions.middleware.ChallengeStatusMiddleware',
]

MIDDLEWARE_URL_EXCEPTIONS = [
    '/__debug__/',
    '/admin/',
    '/static/',
    MEDIA_URL,
    ]

# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False

# Always generate a CSRF token for anonymous users.
ANON_ALWAYS = True

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS['messages'] = [
    ('%s/**.py' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_python'),
    ('%s/**/templates/**.html' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_template'),
    ('templates/**.html',
        'tower.management.commands.extract.extract_tower_template'),
]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable JS files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

LOGGING = dict(loggers=dict(playdoh = {'level': logging.DEBUG}))
