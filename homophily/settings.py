from os import environ

SESSION_CONFIGS = [
     dict(
        name='CountingTask',
        app_sequence=['CountingTask'],
        num_demo_participants=1,
     ),
    dict(
        name='counting2',
        app_sequence=['counting2'],
        num_demo_participants=2,
    ),
    dict(
        name='communication',
        app_sequence=['communication'],
        num_demo_participants=2,
    ),
dict(
        name='Communication2',
        app_sequence=['Communication2'],
        num_demo_participants=2,
    ),
]

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
        use_secure_urls=True
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['expiry', 'sum1', 'answerA', 'answerB', 'sum2', 'sumE']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4308297569828'
