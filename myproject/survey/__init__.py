from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"], [2, "Other"]])
    year = models.IntegerField(label="What year of study are you?", widget=widgets.RadioSelectHorizontal,
                               choices=[[1, "Freshman"], [2, "Sophomore"], [3, "Junior"], [4, "Senior"],
                                        [5, 'Graduate Student'], [6, 'Other']])
    age = models.IntegerField(label="What is your age?", min=18)
    major = models.IntegerField(label="What is your major?", widget=widgets.RadioSelectHorizontal,
                                choices=[[0, "Arts"], [1, 'Business'], [2, 'Humanities'], [3, 'Natural Sciences'],
                                         [4, 'Social Sciences'], [5, 'Phsyical Sciences'], [6, 'Other']])
    race = models.IntegerField(label="What is your race/ethnicity?", widget=widgets.RadioSelectHorizontal,
                               choices=[[0, 'Asian'], [1, 'Black'], [2, 'Caucasian'], [3, 'Hispanic'], [4, 'Other']])
    language = models.IntegerField(label='What is your native language?', widget=widgets.RadioSelectHorizontal,
                                   choices=[[0, 'English'], [1, 'Other']])
    move = models.IntegerField(label='When did you move to the US?', widget=widgets.RadioSelectHorizontal,
                               choices=[[0, 'Born in the US'], [1, 'Moved prior to age 5'], [2, 'Age 5 - 10'],
                                        [3, 'Age 11 - 15'], [4, 'Age 16-20'], [5, 'After age 20']])


class survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'year', 'age', 'major', 'race', 'language', 'move']



page_sequence = [survey]