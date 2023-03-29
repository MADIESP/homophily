from otree.api import *
import random

author = 'David Danz'

doc = """
Cognitive Reflection Test (Frederick, 2005)
"""

class C(BaseConstants):
    NAME_IN_URL = 'CRT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    TIME_PER_PROBLEM = 45  # 20 was announced but 45 was actually allotted per question
    PAYMENT_CURRENT_PER_ITEM = cu(1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    paidPerson = models.IntegerField(default=99, )

    def paymentSelector(group:BaseGroup):

        if group.paidPerson == 99:
            selected = random.randint(1, group.session.num_participants)
            p = group.get_player_by_id(selected)
            p.picked = True
            group.paidPerson = selected
        else:
            pass


class Player(BasePlayer):
    picked = models.BooleanField(default=False,)
    answer = models.FloatField()
    timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")
    points = models.IntegerField(doc="Number of correct answers {0,...3}.")

    def get_points(player:BasePlayer):
        points = 0
        correct_answers = [5, 5, 47]
        for p, correct in zip(player.in_all_rounds(), correct_answers):
            # print(p.answer, correct, p.answer == correct)
            points = points + 1 if p.answer == correct else points
        player.points = points

        if player.picked:
            player.payoff = player.points * C.PAYMENT_CURRENT_PER_ITEM
            player.participant.crtpayoff = player.payoff
            player.participant.picked = True

        else:
            player.participant.crtpayoff = 0
            player.participant.picked = False


class Instructions(Page):
    def is_displayed(player:BasePlayer):
        return player.round_number == 1

    def vars_for_template(player:BasePlayer):
        return dict(
            time_per_problem=C.TIME_PER_PROBLEM,
            payment_correct_per_item=C.PAYMENT_CURRENT_PER_ITEM,
        )


class CRT(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    # 20 seconds per question in the z-Tree announced, but 45 given; no constraints in original study and typical applications it seems.

    form_model = 'player'
    form_fields = ['answer']

    def before_next_page(player, timeout_happened):
        #player.timed_out = True if player.timed_out else False
        if player.round_number == C.NUM_ROUNDS:
            player.group.paymentSelector()
            player.get_points()


class waitforend(WaitPage):
    @staticmethod
    def is_displayed(player:BasePlayer):
        return player.round_number == 3
    body_text = "Please wait for all participants to finish."

page_sequence = [Instructions,CRT,waitforend]