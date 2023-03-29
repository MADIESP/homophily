from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Final_I(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['incentive'] == True

class Final_N(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['incentive'] != True


page_sequence = [Final_I, Final_N]