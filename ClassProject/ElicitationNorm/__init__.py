from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'ElicitationNorm'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = 5
    INSTRUCTIONS_TEMPLATE = 'ElicitationNorm/introduction.html'
    ENDOWMENT = cu(6)
    CHOICES = [[-1, 'Very Inappropriate'], [-0.3, 'Somewhat Inappropriate'],
              [0.3, 'Somewhat Appropriate'], [1, 'Very Appropriate']]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

   # response_1a = models.StringField(widget=widgets.RadioSelect,
   #    choices=[[-1, 'Very Inappropriate'],
   #             [-0.3, 'Somewhat Inappropriate'],
   #               [0.3, 'Somewhat Appropriate'],
   #             [1, 'Very Appropriate']],
   #    label='Take $5 from Individual B <p style="font-size:10px"> (Individual A gets $10, Individual B gets $0) </p>'
   # )

    response_1a = models.StringField(widget=widgets.RadioSelect,
                                     choices=C.CHOICES,
                                     label='Take $5 from Individual B. <p style="font-size:10px"> Text goes here.</p>'
                                     )
    response_1b = models.FloatField(widget=widgets.RadioSelect,
                                   choices=C.CHOICES,
                                    label='Take $4 from Individual B (Individual A gets $9, Individual B gets $1)'
                                   )
  #  response_1c = models.FloatField(widget=widgets.RadioSelect,
    #    choices=[[-1, 'Very Inappropriate'],
           #      [-0.3, 'Somewhat Inappropriate'],
            #     [0.3, 'Somewhat Appropriate'],
            #     [1, 'Very Appropriate']],
     #   label="Take $3 from Individual B (Individual A gets $8, Individual B gets $2)"
  #  )
  #  response_1d = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
       #          [-0.3, 'Somewhat Inappropriate'],
        #         [0.3, 'Somewhat Appropriate'],
        #         [1, 'Very Appropriate']],
     #   label="Take $2 from Individual B (Individual A gets $7, Individual B gets $3)"
  #  )
   # response_1e = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
          #       [-0.3, 'Somewhat Inappropriate'],
           #      [0.3, 'Somewhat Appropriate'],
           #      [1, 'Very Appropriate']],
      #  label="Take $1 from Individual B (Individual A gets $6, Individual B gets $4)"
   # )
  #  response_1f = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
            #     [-0.3, 'Somewhat Inappropriate'],
            #     [0.3, 'Somewhat Appropriate'],
             #    [1, 'Very Appropriate']],
      #  label="Give $0/Take $0 to/from Individual B(Individual A gets $5, Individual B gets $5)"
   # )
   # response_1g = models.FloatField(widget=widgets.RadioSelect,
      #  choices=[[-1, 'Very Inappropriate'],
         #        [-0.3, 'Somewhat Inappropriate'],
          #       [0.3, 'Somewhat Appropriate'],
           #      [1, 'Very Appropriate']],
       # label="Give $1 to Individual B(Individual A gets $4, Individual B gets $6)"
   # )
  #  response_1h = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
            #     [-0.3, 'Somewhat Inappropriate'],
             #    [0.3, 'Somewhat Appropriate'],
              #   [1, 'Very Appropriate']],
    #    label="Give $2 to Individual B(Individual A gets $3, Individual B gets $7)"
  #  )
  #  response_1i = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
            #     [-0.3, 'Somewhat Inappropriate'],
              #   [0.3, 'Somewhat Appropriate'],
              #   [1, 'Very Appropriate']],
       # label="Give $3 to Individual B(Individual A gets $2, Individual B gets $8)"
   # )
   # response_1j = models.FloatField(widget=widgets.RadioSelect,
      #  choices=[[-1, 'Very Inappropriate'],
            #     [-0.3, 'Somewhat Inappropriate'],
             #    [0.3, 'Somewhat Appropriate'],
              #   [1, 'Very Appropriate']],
      #  label="Give $4 to Individual B(Individual A gets $1, Individual B gets $9)"
   # )
   # response_1k = models.FloatField(widget=widgets.RadioSelect,
     #   choices=[[-1, 'Very Inappropriate'],
          #       [-0.3, 'Somewhat Inappropriate'],
           #      [0.3, 'Somewhat Appropriate'],
            #     [1, 'Very Appropriate']],
       # label="Give $5 to Individual B(Individual A gets $0, Individual B gets $10)"
   # )
   # response_2a = models.FloatField(widget=widgets.RadioSelect,
                                  #  choices=[[-1, 'Very Inappropriate'],
                                       #      [-0.3, 'Somewhat Inappropriate'],
                                         #    [0.3, 'Somewhat Appropriate'],
                                         #    [1, 'Very Appropriate']],
                                  #  label="Pass (Do not Play Game) (No pairing occurs, Individual A gets $10, Individual B is told nothing about game and gets $0)"
                                  #  )
    #response_2b = models.FloatField(widget=widgets.RadioSelect,
                              #      choices=[[-1, 'Very Inappropriate'],
                                           #  [-0.3, 'Somewhat Inappropriate'],
                                           #  [0.3, 'Somewhat Appropriate'],
                                          #   [1, 'Very Appropriate']],
                                 #   label="Play Game and Give $0 to Individual B(Individuals A and B are paired, Individual A gets $10, Individual B is told about game and gets $0)"
                                 #   )
    #response_2c = models.FloatField(widget=widgets.RadioSelect,
                                   # choices=[[-1, 'Very Inappropriate'],
                                          #   [-0.3, 'Somewhat Inappropriate'],
                                          #   [0.3, 'Somewhat Appropriate'],
                                          #   [1, 'Very Appropriate']],
    #  label="  Play Game and Give $1 to Individual B  (Individuals A and B are paired, Individual A gets $9, Individual B is told about game and gets $1)"
    #                               )
    # response_2d = models.FloatField(widget=widgets.RadioSelect,
    #    choices=[[-1, 'Very Inappropriate'],
    #           [-0.3, 'Somewhat Inappropriate'],
    #            [0.3, 'Somewhat Appropriate'],
    #             [1, 'Very Appropriate']],
    #         label="Play Game and Give $2 to Individual B(Individuals A and B are paired, Individual A gets $8, Individual B is told about game and gets $2)"
    #           )
    # response_2e = models.FloatField(widget=widgets.RadioSelect,
    #                            choices=[[-1, 'Very Inappropriate'],
    #                                    [-0.3, 'Somewhat Inappropriate'],
    #                                   [0.3, 'Somewhat Appropriate'],
    #                                   [1, 'Very Appropriate']],
    #                            label="Play Game and Give $3 to Individual B(Individuals A and B are paired, Individual A gets $7, Individual B is told about game and gets $3)"
    #                             )
    # response_2f = models.FloatField(widget=widgets.RadioSelect,
    #         choices=[[-1, 'Very Inappropriate'],
    #           [-0.3, 'Somewhat Inappropriate'],
    #             [0.3, 'Somewhat Appropriate'],
    #              [1, 'Very Appropriate']],
    #       label="Play Game and Give $4 to Individual B(Individuals A and B are paired, Individual A gets $6, Individual B is told about game and gets $4)"
    #         )
    # response_2g = models.FloatField(widget=widgets.RadioSelect,
    #    choices=[[-1, 'Very Inappropriate'],
    #             [-0.3, 'Somewhat Inappropriate'],
    #             [0.3, 'Somewhat Appropriate'],
    #             [1, 'Very Appropriate']],
    #      label="Play Game and Give $5 to Individual B(Individuals A and B are paired, Individual A gets $5, Individual B is told about game and gets $5)"
    #      )
    # response_2h = models.FloatField(widget=widgets.RadioSelect,
    #     choices=[[-1, 'Very Inappropriate'],
    #             [-0.3, 'Somewhat Inappropriate'],
    #             [0.3, 'Somewhat Appropriate'],
    #              [1, 'Very Appropriate']],
    #      label="Play Game and Give $6 to Individual B(Individuals A and B are paired, Individual A gets $4, Individual B is told about game and gets $6)"
    #      )
    #  response_2i = models.FloatField(widget=widgets.RadioSelect,
    #                choices=[[-1, 'Very Inappropriate'],
    #                        [-0.3, 'Somewhat Inappropriate'],
    #                       [0.3, 'Somewhat Appropriate'],
    #                      [1, 'Very Appropriate']],
    #                label="Play Game and Give $7 to Individual B(Individuals A and B are paired, Individual A gets $3, Individual B is told about game and gets $7)"
    #                            )
    #  response_2j = models.FloatField(widget=widgets.RadioSelect,
    #  choices=[[-1, 'Very Inappropriate'],
    #          [-0.3, 'Somewhat Inappropriate'],
    #           [0.3, 'Somewhat Appropriate'],
    #           [1, 'Very Appropriate']],
    #   label="Play Game and Give $8 to Individual B(Individuals A and B are paired, Individual A gets $2, Individual B is told about game and gets $8)"
    #    )
    # response_2k = models.FloatField(widget=widgets.RadioSelect,
    #            choices=[[-1, 'Very Inappropriate'],
    #                     [-0.3, 'Somewhat Inappropriate'],
    #                     [0.3, 'Somewhat Appropriate'],
    #                     [1, 'Very Appropriate']],
    #            label="Play Game and Give $9 to Individual B(Individuals A and B are paired, Individual A gets $1, Individual B is told about game and gets $9)"
    #            )
    #  response_2l = models.FloatField(widget=widgets.RadioSelect,
    #       choices=[[-1, 'Very Inappropriate'],
    #               [-0.3, 'Somewhat Inappropriate'],
    #              [0.3, 'Somewhat Appropriate'],
    #              [1, 'Very Appropriate']],
    #        label="Play Game and Give $10 to Individual B(Individuals A and B are paired, Individual A gets $0, Individual B is told about game and gets $10)"
    #        )

pass

#functions
# def creating_session(subsession: Subsession):
    #   for p in subsession.get_players():
    #      if p.id_in_subsession % 4 == 1:
    #        p.incentivized = False
    #    else:
#        p.incentivized = True


# def get_mode(group):
# import random
#s_values = None
    #  random_field = random.randint(1, 2)
    #  players = group.get_players()
    #      if random_field == 1:
    #         s_values= [p.field_maybe_none('response_1a') for p in players ]


    #    elif random_field == 2:
#     s_values = [p.field_maybe_none('response_1b') for p in players ]

#group.s_mode = mode(s_values)
#   group.chosen = random_field


#def set_payoffs(group):
    #  if group.chosen == 1:
    #   for p in group.get_players():
    #  if p.incentivized == True:

    #   if p.response_S1 == group.s_mode:
    #       p.payoff = 17
    #   else:
    #    p.payoff = 7
    #  else:
    #     p.payoff = 7
    #  elif group.chosen == 2:
    #   for p in group.get_players():
    #  if p.incentivized == True:
    #   if p.response_S2 == group.s_mode:
    #     p.payoff = 17
    #  else:
    ##  p.payoff = 7


    #    else:




# PAGES

class Introduction(Page):
    pass

#class Example(Page):
   # pass
class Situation1(Page):
        pass


class Response1(Page):
    form_model = 'player'
    form_fields = ['response_1a', 'response_1b']


#class Response1_U(Page):

  #  form_model = 'player'
  #  form_fields = ['response_1a','response_1b','response_1c','response_1d','response_1e','response_1f','response_1g','response_1h','response_1i','response_1j','response_1k']

#class Response1_U(Page):
 #   @staticmethod
  #  def is_displayed(player: Player):
  #      return player.incentivized != True
  #  form_model = 'player'
  #  form_fields = ['response_1a','response_1b','response_1c','response_1d','response_1e','response_1f','response_1g','response_1h','response_1i','response_1j','response_1k']

#class Response1_I(Page):
  #  @staticmethod
  #  def is_displayed(player: Player):
  #      return player.incentivized == True
  #  form_model = 'player'
  #  form_fields = ['response_1a','response_1b','response_1c','response_1d','response_1e','response_1f','response_1g','response_1h','response_1i','response_1j','response_1k']


#class Situation2(Page):
 #       pass

#class Response2(Page):

   # form_model = 'player'
  #  form_fields = ['response_2a', 'response_2b']


# class Response2_U(Page):
  #  @staticmethod
 #   def is_displayed(player: Player):
  #      return player.incentivized != True
 #   form_model = 'player'
 #   form_fields = ['response_2a', 'response_2b', 'response_2c', 'response_2d', 'response_2e', 'response_2f',
             #      'response_2g', 'response_2h', 'response_2i', 'response_2j', 'response_2k', 'response_2l']

#class Response2_I(Page):
  #  @staticmethod
  #  def is_displayed(player: Player):
  #      return player.incentivized == True
  #  form_model = 'player'
  #  form_fields = ['response_2a', 'response_2b', 'response_2c', 'response_2d', 'response_2e', 'response_2f',
   #                'response_2g', 'response_2h', 'response_2i', 'response_2j', 'response_2k', 'response_2l']

#class Waitforpayment(WaitPage):
  #  after_all_players_arrive = set_payoffs

#class Final_U(Page):
  #  @staticmethod
  #  def is_displayed(player: Player):
   #     return player.incentivized != True


#class Final_I(Page):
 #   @staticmethod
  #  def is_displayed(player: Player):
    #    return player.incentivized == True


page_sequence = [Introduction, Situation1,  Response1]

#page_sequence = [Introduction, Example, Situation1,  Response1_U, Response1_I, Situation2, Response2_U, Response2_I, Waitforpayment, Final_U, Final_I]
