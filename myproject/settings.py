from os import environ


SESSION_CONFIGS = [
        dict(
            name = 'Krupka_Weber_SI',
            num_demo_participants = 4,
            app_sequence = ['instructions','norms','survey','CRT','end'],
            lab = True,
            variant = False,
            incentive = True,
        ),
        dict(
            name='Krupka_Weber_BI',
            num_demo_participants = 4,
            app_sequence = ['instructions','norms','survey','CRT','end'],
            lab=True,
            variant = True,
            incentive = True,
        ),
        dict(
            name='Krupka_Weber_SN',
            num_demo_participants=4,
            app_sequence=['instructions', 'norms', 'survey','CRT','end'],
            lab=True,
            variant=False,
            incentive=False,
        ),
        dict(
            name='Krupka_Weber_BN',
            num_demo_participants=4,
            app_sequence=['instructions', 'norms', 'survey','CRT','end'],
            lab=True,
            variant=True,
            incentive=False,
        ),
        dict(
            name = 'norm_SI',
            num_demo_participants = 1,
            app_sequence = ['norms','end'],
            variant = False,
            debug = True,
            incentive = True,
        ),
        dict(
            name='norm_SN',
            num_demo_participants=1,
            app_sequence=['norms', 'end'],
            variant=False,
            debug=True,
            incentive=False,
        ),
        dict(
            name = 'norm_BI',
            num_demo_participants = 1,
            app_sequence = ['norms','end'],
            variant = True,
            debug = True,
            incentive = True,
        ),
        dict(
            name = 'norm_BN',
            num_demo_participants = 1,
            app_sequence = ['norms','end'],
            variant = True,
            debug = True,
            incentive = False,
        ),
        dict(
            name = 'survey',
            num_demo_participants = 2,
            app_sequence = ['survey'],
        ),
        dict(
            name = 'instructions',
            num_demo_participants = 2,
            app_sequence = ['instructions'],
            incentive = False
        ),
        dict(
            name = 'crt',
            num_demo_participants = 4,
            app_sequence = ['CRT','end'],
            incentive=False,
        )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=7,
    doc="",
    debug=False,
)

PARTICIPANT_FIELDS = [ 'normpayoff', 'crtpayoff', 'response', 'picked']
SESSION_FIELDS = ['variant','incentive','chosen_situation','chosen_text', 'modalresponse']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='peel',
        display_name='PEEL Lab',
        participant_label_file='_rooms/peel.txt',
    ),
]


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6573692948079'

INSTALLED_APPS = ['otree']

#SECRET_KEY = '6573692948079'

#INSTALLED_APPS = ['otree']



#SECRET_KEY = '7847846432613'
