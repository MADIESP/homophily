from statistics import mode
from otree.api import *
import pandas as pd


class C(BaseConstants):
    NAME_IN_URL = 'norms'
    NUM_ROUNDS = 4
    PLAYERS_PER_GROUP = None
    #INSTRUCTIONS_TEMPLATE = 'norms/Instructions_N.html'
    CHOICES = [[-1, 'Very Inappropriate'], [-0.3, 'Somewhat Inappropriate'],
               [0.3, 'Somewhat Appropriate'], [1, 'Very Appropriate']]
    S_LABELS = ["Give $0 to Individual B (Individual A gets $10, Individual B gets $0)",
                "Give $1 to Individual B (Individual A gets $9, Individual B gets $1)",
                "Give $2 to Individual B (Individual A gets $8, Individual B gets $2)",
                "Give $3 to Individual B (Individual A gets $7, Individual B gets $3)",
                "Give $4 to Individual B (Individual A gets $6, Individual B gets $4)",
                "Give $5 to Individual B (Individual A gets $5, Individual B gets $5)",
                "Give $6 to Individual B (Individual A gets $4, Individual B gets $6)",
                "Give $7 to Individual B (Individual A gets $3, Individual B gets $7)",
                "Give $8 to Individual B (Individual A gets $2, Individual B gets $8)",
                "Give $9 to Individual B (Individual A gets $1, Individual B gets $9)",
                "Give $10 to Individual B (Individual A gets $0, Individual B gets $10)"]
    B_LABELS = ["Take $5 from Individual B (Individual A gets $10, Individual B gets $0)",
                "Take $4 from Individual B (Individual A gets $9, Individual B gets $1)",
                "Take $3 from Individual B (Individual A gets $8, Individual B gets $2)",
                "Take $2 from Individual B (Individual A gets $7, Individual B gets $3)",
                "Take $1 from Individual B (Individual A gets $6, Individual B gets $4)",
                "Give $0/Take $0 to/from Individual B(Individual A gets $5, Individual B gets $5)",
                "Give $1 to Individual B(Individual A gets $4, Individual B gets $6)",
                "Give $2 to Individual B(Individual A gets $3, Individual B gets $7)",
                "Give $3 to Individual B(Individual A gets $2, Individual B gets $8)",
                "Give $4 to Individual B(Individual A gets $1, Individual B gets $9)",
                "Give $5 to Individual B(Individual A gets $0, Individual B gets $10)"]
    TWO_LABELS = ["Pass (Do not Play Game) (No pairing occurs, Individual A gets $10,"
                  "Individual B is told nothing about game and gets $0)",
                  "Play Game and Give $0 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $10, Individual B is told about game and gets $0)",
                  "Play Game and Give $1 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $9, Individual B is told about game and gets $1)",
                  "Play Game and Give $2 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $8, Individual B is told about game and gets $2)",
                  "Play Game and Give $3 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $7, Individual B is told about game and gets $3)",
                  "Play Game and Give $4 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $6, Individual B is told about game and gets $4)",
                  "Play Game and Give $5 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $5, Individual B is told about game and gets $5)",
                  "Play Game and Give $6 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $4, Individual B is told about game and gets $6)",
                  "Play Game and Give $7 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $3, Individual B is told about game and gets $7)",
                  "Play Game and Give $8 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $2, Individual B is told about game and gets $8)",
                  "Play Game and Give $9 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $1, Individual B is told about game and gets $9)",
                  "Play Game and Give $10 to Individual B (Individuals A and B are paired, "
                  "Individual A gets $0, Individual B is told about game and gets $10)"]
    THREE_LABELS = ["Give $0 to Participant B (Participant A gets $5, Participant B gets $0)",
                    "Give $0.50 to Participant B (Participant A gets $4.50, Participant B gets $0.50)",
                    "Give $1 to Participant B (Participant A gets $4, Participant B gets $1)",
                    "Give $1.50 to Participant B (Participant A gets $3.50, Participant B gets $1.50)",
                    "Give $2 to Participant B (Participant A gets $3, Participant B gets $2)",
                    "Give $2.50 to Participant B (Participant A gets $2.50, Participant B gets $2.50)",
                    "Give $3 to Participant B (Participant A gets $2, Participant B gets $3)",
                    "Give $3.50 to Participant B (Participant A gets $1.50, Participant B gets $3.50)",
                    "Give $4 to Participant B (Participant A gets $1, Participant B gets $4)",
                    "Give $4.50 to Participant B (Participant A gets $0.50, Participant B gets $4.50)",
                    "Give $5 to Participant B (Participant A gets $0, Participant B gets $5)"]
    FOUR_LABELS = ["Take $1 from Participant B (Participant A gets $6, Participant B loses $1)",
                   "Give/Take $0 to/from Participant B (Participant A gets $5, Participant B gets $0)",
                   "Give $0.50 to Participant B (Participant A gets $4.50, Participant B gets $0.50)",
                   "Give $1 to Participant B (Participant A gets $4, Participant B gets $1)",
                   "Give $1.50 to Participant B (Participant A gets $3.50, Participant B gets $1.50)",
                   "Give $2 to Participant B (Participant A gets $3, Participant B gets $2)",
                   "Give $2.50 to Participant B (Participant A gets $2.50, Participant B gets $2.50)",
                   "Give $3 to Participant B (Participant A gets $2, Participant B gets $3)",
                   "Give $3.50 to Participant B (Participant A gets $1.50, Participant B gets $3.50)",
                   "Give $4 to Participant B (Participant A gets $1, Participant B gets $4)",
                   "Give $4.50 to Participant B (Participant A gets $0.50, Participant B gets $4.50)",
                   "Give $5 to Participant B (Participant A gets $0, Participant B gets $5)"]


class Subsession(BaseSubsession):
    variant = models.BooleanField()
    incentive = models.BooleanField()


class Group(BaseGroup):
    s_mode = models.FloatField()
    b_mode = models.FloatField()
    chosen = models.IntegerField()
    chosen_situation = models.IntegerField()
    chosen_text = models.StringField()


class Player(BasePlayer):
    incentivized = models.BooleanField()
    variant = models.BooleanField()
    response_S1 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S2 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S3 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S4 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S5 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S6 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S7 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S8 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S9 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_S10 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    response_S11 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    response_S12 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    response_B1 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B2 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B3 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B4 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B5 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B6 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B7 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B8 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B9 = models.FloatField(widget=widgets.RadioSelect,
                                    choices=C.CHOICES,
                                    )
    response_B10 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    response_B11 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    response_B12 = models.FloatField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     )
    pass


# functions
def creating_session(subsession: Subsession):
    subsession.variant = subsession.session.config['variant']
    subsession.incentive = subsession.session.config['incentive']


def get_mode(group):
    import random
    random_situation = random.randint(1, 4)
    group.chosen_situation = random_situation
    group.session.chosen_situation = random_situation

    # get modal response from non-incentivized participants for randomly chosen situation and decision
    if group.subsession.incentive:
        df = pd.read_csv('_static/csv/n_responses.csv')
        #If Standard
        if not group.subsession.variant:
            if random_situation == 1:
                random_field = random.randint(1, 11)
                for i in range(11):
                    if random_field == i + 1:
                        prev = df['norms1playerresponse_s' + str(i+1)]
                        group.chosen_text = C.S_LABELS[i]
            elif random_situation == 2:
                random_field = random.randint(1, 12)
                for i in range(12):
                    if random_field == i + 1:
                        prev = df['norms2playerresponse_s' + str(i+1)]
                        group.chosen_text = C.TWO_LABELS[i]
            elif random_situation == 3:
                random_field = random.randint(1, 11)
                for i in range(11):
                    if random_field == i + 1:
                        prev = df['norms3playerresponse_s' + str(i+1)]
                        group.chosen_text = C.THREE_LABELS[i]
            elif random_situation == 4:
                random_field = random.randint(1, 12)
                for i in range(12):
                    if random_field == i + 1:
                        prev = df['norms4playerresponse_s' + str(i+1)]
                        group.chosen_text = C.FOUR_LABELS[i]

            group.chosen = random_field
            group.s_mode = mode(prev)

        if group.s_mode == -1:
            group.session.modalresponse = "Very socially inappropriate"
        elif group.s_mode == -0.3:
            group.session.modalresponse = "Somewhat socially inappropriate"
        elif group.s_mode == 0.3:
            group.session.modalresponse = "Somewhat socially appropriate"
        elif group.s_mode == 1:
            group.session.modalresponse = "Very socially appropriate"



        #If Bully
        else:
            if random_situation == 1:
                random_field = random.randint(1, 11)
                for i in range(11):
                    if random_field == i + 1:
                        prev = df['norms1playerresponse_b' + str(i+1)]
                        group.chosen_text = C.B_LABELS[i]

            elif random_situation == 2:
                random_field = random.randint(1, 12)
                for i in range(12):
                    if random_field == i + 1:
                        prev = df['norms2playerresponse_b' + str(i+1)]
                        group.chosen_text = C.TWO_LABELS[i]

            elif random_situation == 3:
                random_field = random.randint(1, 11)
                for i in range(11):
                    if random_field == i + 1:
                        prev = df['norms3playerresponse_b' + str(i+1)]
                        group.chosen_text = C.THREE_LABELS[i]

            elif random_situation == 4:
                random_field = random.randint(1, 12)
                for i in range(12):
                    if random_field == i + 1:
                        prev = df['norms4playerresponse_b' + str(i+1)]
                        group.chosen_text = C.FOUR_LABELS[i]

            group.chosen = random_field
            group.b_mode = mode(prev)
            if group.b_mode == -1:
                group.session.modalresponse = "Very socially inappropriate"
            elif group.b_mode == -0.3:
                group.session.modalresponse = "Somewhat socially inappropriate"
            elif group.b_mode == 0.3:
                group.session.modalresponse = "Somewhat socially appropriate"
            elif group.b_mode == 1:
                group.session.modalresponse = "Very socially appropriate"
        group.session.chosen_text = group.chosen_text


def set_payoffs(group):
    if not group.subsession.incentive:
        for p in group.get_players():
            p.payoff = 7
    else:
        for i in range(4):
            if group.chosen_situation == i+1:
                for j in range(12):
                    if group.chosen == j+1:
                        if not group.subsession.variant:
                            for p in group.get_players():
                                prev = p.in_round(i+1)
                                p.participant.response = prev.field_display('response_S' + str(j + 1))
                                if prev.field_maybe_none('response_S' + str(j + 1)) == group.s_mode:
                                    p.payoff = 17
                                else:
                                    p.payoff = 7
                        else:
                            for p in group.get_players():
                                prev = p.in_round(i+1)
                                p.participant.response = prev.field_display('response_B' + str(j + 1))
                                if prev.field_maybe_none('response_B' + str(j + 1)) == group.b_mode:
                                    p.payoff = 17
                                else:
                                    p.payoff = 7
    for p in group.get_players():
        p.participant.normpayoff = p.payoff



# PAGES
class Situation_S(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.variant != True


class Situation_B(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.variant == True


class Response_NS(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.incentive != True and player.subsession.variant != True

    form_model = 'player'

    def get_form_fields(player: Player):
        if player.round_number == 1:
            return ['response_S' + str(k) for k in range(1, 12)]
        elif player.round_number == 2:
            return ['response_S' + str(k) for k in range(1, 13)]
        elif player.round_number == 3:
            return ['response_S' + str(k) for k in range(1, 12)]
        elif player.round_number == 4:
            return ['response_S' + str(k) for k in range(1, 13)]

    def vars_for_template(player: Player):
        if player.round_number == 1:
            s_list = C.S_LABELS
        elif player.round_number == 2:
            s_list = C.TWO_LABELS
        elif player.round_number == 3:
            s_list = C.THREE_LABELS
        elif player.round_number == 4:
            s_list = C.FOUR_LABELS
        f = ['response_S' + str(k) for k in range(1, 13)]
        temp = zip(s_list, f)
        value = ["-1", "-0.3", "0.3", "1"]

        return dict(page_temp=temp, page_value=value, debug=player.session.config['debug'], )


class Response_NB(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.incentive != True and player.subsession.variant == True

    form_model = 'player'

    def get_form_fields(player: Player):
        if player.round_number == 1:
            return ['response_B' + str(k) for k in range(1, 12)]
        elif player.round_number == 2:
            return ['response_B' + str(k) for k in range(1, 13)]
        elif player.round_number == 3:
            return ['response_B' + str(k) for k in range(1, 12)]
        elif player.round_number == 4:
            return ['response_B' + str(k) for k in range(1, 13)]

    def vars_for_template(player: Player):
        if player.round_number == 1:
            b_list = C.B_LABELS
        elif player.round_number == 2:
            b_list = C.TWO_LABELS
        elif player.round_number == 3:
            b_list = C.THREE_LABELS
        elif player.round_number == 4:
            b_list = C.FOUR_LABELS
        f = ['response_B' + str(k) for k in range(1, 13)]
        temp = zip(b_list, f)
        value = ["-1", "-0.3", "0.3", "1"]

        return dict(page_temp=temp, page_value=value, debug=player.session.config['debug'], )


class Response_IS(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.incentive == True and player.subsession.variant != True

    form_model = 'player'

    def get_form_fields(player: Player):
        if player.round_number == 1:
            return ['response_S' + str(k) for k in range(1, 12)]
        elif player.round_number == 2:
            return ['response_S' + str(k) for k in range(1, 13)]
        elif player.round_number == 3:
            return ['response_S' + str(k) for k in range(1, 12)]
        elif player.round_number == 4:
            return ['response_S' + str(k) for k in range(1, 13)]

    def vars_for_template(player: Player):
        if player.round_number == 1:
            s_list = C.S_LABELS
        elif player.round_number == 2:
            s_list = C.TWO_LABELS
        elif player.round_number == 3:
            s_list = C.THREE_LABELS
        elif player.round_number == 4:
            s_list = C.FOUR_LABELS

        f = ['response_S' + str(k) for k in range(1, 13)]
        temp = zip(s_list, f)
        value = ["-1", "-0.3", "0.3", "1"]

        return dict(page_temp=temp, page_value=value, debug=player.session.config['debug'], )


class Response_IB(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.incentive == True and player.subsession.variant == True

    form_model = 'player'

    def get_form_fields(player: Player):
        if player.round_number == 1:
            return ['response_B' + str(k) for k in range(1, 12)]
        elif player.round_number == 2:
            return ['response_B' + str(k) for k in range(1, 13)]
        elif player.round_number == 3:
            return ['response_B' + str(k) for k in range(1, 12)]
        elif player.round_number == 4:
            return ['response_B' + str(k) for k in range(1, 13)]

    def vars_for_template(player: Player):
        if player.round_number == 1:
            b_list = C.B_LABELS
        elif player.round_number == 2:
            b_list = C.TWO_LABELS
        elif player.round_number == 3:
            b_list = C.THREE_LABELS
        elif player.round_number == 4:
            b_list = C.FOUR_LABELS

        f = ['response_B' + str(k) for k in range(1, 13)]
        temp = zip(b_list, f)
        value = ["-1", "-0.3", "0.3", "1"]

        return dict(page_temp=temp, page_value=value, debug=player.session.config['debug'], )


class WaitRounds(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number != 4


class Waitformode(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 4

    after_all_players_arrive = get_mode


class Waitforpayment(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 4

    after_all_players_arrive = set_payoffs


page_sequence = [Situation_S, Situation_B, Response_NS, Response_NB, Response_IS,
                 Response_IB, WaitRounds, Waitformode, Waitforpayment]