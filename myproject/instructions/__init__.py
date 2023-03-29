from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = [[-1, 'Very Inappropriate'], [-0.3, 'Somewhat Inappropriate'],
               [0.3, 'Somewhat Appropriate'], [1, 'Very Appropriate']]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response_E1 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    label='Take the wallet'
                                    )
    response_E2 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    label='Ask others nearby if the wallet belongs to them'
                                    )
    response_E3 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    label='Leave the wallet where it is'
                                    )
    response_E4 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    label='Give the wallet to the shop manager'
                                    )
    pass


class Instructions_N(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not player.session.config['incentive']

class Instructions_I(Page):
    @staticmethod
    def is_displayed(player: Player):
        return  player.session.config['incentive']


class Example1(Page):
    form_model = 'player'
    form_fields = ['response_E1', 'response_E2','response_E3','response_E4']


class Example2(Page):
    pass


class Final_Ins_I(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['incentive']


class Final_Ins_N(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not player.session.config['incentive']


class Wait(WaitPage):
    body_text = "Please wait for other participants. Situation 1 will appear momentarily."


page_sequence = [Instructions_N, Instructions_I, Example1, Example2, Final_Ins_I, Final_Ins_N, Wait]