from game.object import *


class Level:
    def __init__(self):
        self._objects = list()
        self._dialogue = ""


    @property
    def objects(self) -> list[GameObject]:
        return self._objects


    @property
    def dialogue(self) -> list[str]:
        return self._dialogue



class Level1(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (79, 63, 49)),
                         GameObject((.3,.5), (.15,.15), (159, 233, 252)),
                         GameObject((0,0), (1,0.4), (0,0,0))]
        self._dialogue = ["[Move using the arrow keys, Scroll text using Spacebar]",
                          'YOU: "..."',
                          '"I could just not go to work today..."',
                          '"..."',
                          '"Alright, let\'s go"',
                          "[Move to the next room to progress]",
                          '']
        

class Level2(Level):
    def __init__(self):
        self._objects = [Building(0, 0.2, (50,50,50)), 
                         Building(0.6, 0.35, (50,50,50)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0)),
                         Npc(0.6)] 
                                  
        self._dialogue = ['YOU: "So many young people with flying cars now."',
                          '"Some people just never have to work, huh?"',
                          '"*sigh* I just wish I could afford one myself"',
                          '"Just have to keep using public teleporters."',
                          '']


class Level3(Level):
    def __init__(self):
        self._objects = [Building(0.1, 0.4, (50,50,50)),
                         Building(0.8, 0.2, (50,50,50)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0))]

        self._dialogue = ['YOU: "Almost there..."',
                          '']


class Level4(Level):
    def __init__(self):
        self._objects = [Building(0, 0.15, (50,50,50)),
                         Building(0.55, 0.45, (50,50,50)),
                         GameObject((0.8,0.58), (0.2,0.17), (0,0,0)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0))]

        self._dialogue = ['YOU: "I\'m already running late."',
                          '"Just have to my boss won\'t fire me for this."',
                          '']


class Level5(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (175, 175, 175)),
                         GameObject((0,0), (1,0.2), (0,0,0)),
                         ImageObject((0.7,0.59), "officer"),
                         GameObject((0.95,0.50), (0.23, 0.3), (0,0,0)),
                         GameObject((0.945,0.51), (0.01, 0.29), (102,214,206)),
                         # ImageObject((0.6,0.59), "npc"),
                         ]

        self._dialogue = ['OPERATOR: "Right this way sir, just step right through."',
                          '']


class Level6(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (175, 175, 175)),
                         GameObject((0,0), (1,0.2), (0,0,0)),
                         GameObject((0.03,0.50), (0.05, 0.3), (0,0,0)),
                         GameObject((0.03,0.51), (0.01, 0.29), (102,214,206)),
                         ImageObject((0.03,0.59), "officer"),
                         GameObject((0.9,0.56), (0.2,0.20), (0,0,0)),
                         ]

        self._dialogue = ['"..."',
                          'YOU: "Nothing happened?"',
                          'OPERATOR: "Sorry sir, I\'ve never seen that happen myself."',
                          'OPERAOTR: "We\'re gonna have to close this down for today."',
                          'YOU: "I guess I\'ll walk then."',
                          'YOU: "Ugh, today couldn\'t get any worse, right?"',
                          '']

class Level7(Level):
    def __init__(self):
        self._objects = [Building(0.7, 0.5, (50,50,50)),
                         GameObject((0.85,0.56), (0.2,0.20), (0,0,0)),
                         Car((.2,.2), (0.02,0)),
                         Car((.9,.2), (0.02,0)),
                         ]

        self._dialogue = ['YOU: "God, I am in so much trouble"',
                          '']


class Level8(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (119, 109, 127)),
                         GameObject((0.5,0), (0.01, 0.3), (0,0,0)),
                         GameObject((0.45,0.3), (0.11, 0.01), (243, 247, 133)),
                         GameObject((0,0), (1,0.2), (0,0,0)),
                         ImageObject((0.7,0.59), "char_rev_image"),
                         Npc(0.2),
                         ]

        self._dialogue = ['YOU: "Is... that?"',
                          'OTHER YOU: "Who are you?"',
                          'YOU: "Who are YOU?"',
                          '...',
                          '.......',
                          'YOU: "Did you make it through the teleporter?"',
                          'OTHER YOU: "Of course I di-"',
                          'OTHER YOU: "Oh "',
                          'YOU: "My"',
                          'BOTH: "God"',
                          'YOU: "You\'re a version of me that made to the other end"',
                          'OTHER YOU: "What do we do?"',
                          'YOU: "We need to find a way to unsplit us or something."',
                          ''
                          ]


class Level9(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (119, 109, 127)),
                         ImageObject((0.3,0.59), "char_image"),
                         ImageObject((0.7,0.59), "officer"),
                         GameObject((0.95,0.50), (0.23, 0.3), (0,0,0)),
                         ]

        self._dialogue = ['YOU: "HEY!"',
                          'YOU: "Your broken machine ended up cloning me!"',
                          'YOU: "What am I gonna do? How do I fix this?"',
                          'OPERATOR: "Wow, I\'ve never seen that before."',
                          'OPERATOR: "I\'m sorry, but there\'s not much I can do"',
                          'OPERATOR: "The best I can is to forward this up the ladder"',
                          'OPERATOR: "Someone\'s bound to know what to do."',
                          'OTHER YOU: "Are you serious? We can only sit and wait?"',
                          'OPERATOR: "I wish there was something else I could do for you"',
                          'YOU: "Let\'s leave, there\'s nothing else we can do."',
                          ''
                          ]


class Level10(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (79, 63, 49)),
                         GameObject((.3,.5), (.15,.15), (159, 233, 252)),
                         GameObject((0,0), (1,0.4), (0,0,0)),
                         ImageObject((0.7,0.59), "char_rev_image"),
                         ]
        
        self._dialogue = ['YOU: "So that\'s it huh"',
                          'OTHER YOU: "All we can do is live with it for now."',
                          '[Continue to the right]',
                          '']


class Level11(Level):
    def __init__(self):
        self._objects = [Building(0,1,(0,0,0))]

        self._dialogue = ['A few weeks later...',
                          '[Move right]',
                          '']


class Level12(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (79, 63, 49)),
                         GameObject((.3,.5), (.15,.15), (159, 233, 252)),
                         GameObject((0,0), (1,0.4), (0,0,0)),
                         Clone(0.7, True),]

        self._dialogue = ['YOU: "Has the teleporter company gotten back yet?"',
                          'YOU2: "Nope, nothing"',
                          'YOU: "Well we can\'t just keep doing this,"',
                          'YOU: "We don\'t get double pay even though we both work."',
                          'YOU: "I just never thought it would take this long"',
                          'YOU2: "I\'m sure it won\'t be much longer."',
                          'YOU: "Just more waiting, huh"',
                          '[Choose left]                                                      [Choose right]',
                          '',]


class Level13(Level):
    def __init__(self):
        self._objects = [Building(0, 0.2, (50,50,50)), 
                         Building(0.6, 0.35, (50,50,50)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0)),
                         Npc(0.3)] 
        
        self._dialogue = ['YOU: "I guess there really isn\'t much else to do than wait."',
                          '']


class Level14(Level):
    def __init__(self):
        self._objects = [Building(0,1, (0,0,0)), ]

        self._dialogue = ['A few months later...',
                          '[Move right]',
                          '']


class Level15(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (119, 109, 127)),
                         GameObject((0.5,0), (0.01, 0.3), (0,0,0)),
                         GameObject((0.45,0.3), (0.11, 0.01), (243, 247, 133)),
                         GameObject((0,0), (1,0.2), (0,0,0)),
                         Npc(0), Npc(0.2), Npc(0.4),
                         GameObject((0.05,0.68), (0.12,0.15), (0,0,0)),
                         GameObject((0.11,0.63), (0.05,0.05), (40,40,40)),
                         GameObject((0.25,0.68), (0.12,0.15), (0,0,0)),
                         GameObject((0.31,0.63), (0.05,0.05), (40,40,40)),
                         GameObject((0.45,0.68), (0.12,0.15), (0,0,0)),
                         GameObject((0.51,0.63), (0.05,0.05), (40,40,40)),
                         GameObject((0.65,0.68), (0.12,0.15), (0,0,0)),
                         GameObject((0.71,0.63), (0.05,0.05), (40,40,40)),
                         ]

        self._dialogue = ['"Hey thats the guy that got cloned right?"',
                          '"Wonder when they\'re gonna get around to his problem"',
                          '"Poor guy already just slaves away here"',
                          '"You ever talked to him?"',
                          '"Nah, he just comes to work and leaves, nothing more."',
                          'YOU: (Yeah, nothing more huh)',
                          ''
                          ]


class Level16(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0)) ]

        self._dialogue = ['After work...',
                          '[Move right]',
                          '']


class Level17(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (26, 50, 104)),
                         Building(0,0.3, (30,30,30)),
                         GameObject((0.1,0.6), (0.15, 0.15), (0,0,0)),
                         ]

        self._dialogue = [ 'YOU: "..."',
                          'YOU: "How long have I been doing this?"',
                          'YOU: "Played this same game, over and over again."',
                          'YOU: "I\'ve done everything right, played by the rules.',
                          'YOU: "And I just feel like..."',
                          'YOU: (sigh)',
                          'YOU: "Time to go home."',
                          '',]


class Level18(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (79, 63, 49)),
                         GameObject((.3,.5), (.15,.15), (26, 50, 104)),
                         GameObject((0,0), (1,0.4), (0,0,0)),
                         Clone(0.7, True),]

        self._dialogue = ['YOU2: "How was work?"',
                          'YOU: "Same old."',
                          'YOU2: "Well at least there\'s some good news"',
                          'YOU2: "I got a call from the tele company"',
                          'YOU2: "They found a way to merge us back into one person."',
                          'YOU: "About time."',
                          '']


class Level19(Level):
    def __init__(self):
        self._objects =[Building(0, 1, (0,0,0))]

        self._dialogue = ['The next day...',
                          '[Move right]',
                          '']


class Level20(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (119, 109, 127)),
                         Clone(0.3,False),
                         ImageObject((0.7,0.59), "officer"),
                         ImageObject((0.63,0.59), "officer"),
                         ImageObject((0.55,0.59), "officer"),
                         GameObject((0.95,0.50), (0.23, 0.3), (0,0,0)),
                         GameObject((0.95,0.55), (0.01, 0.3), (102,214,206)),
                         ]

        self._dialogue = ['OPERATOR: "Right this way."',
                          'OPERATOR: "This machine will merge your memories"',
                          'OPERATOR: "The end result will take priority over one person"',
                          'OPERATOR: "So if you guys have had different experiences--"',
                          'OPERATOR: "Well, there\'s no guarentee everything will transfer"',
                          'YOU: "That\'s alright, let\'s just get this over with."',
                          '']


class Level21(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0))]

        self._dialogue = ['You stepped through the portal with a quick stride.',
                          'Not an ounce of regret was in your mind.',
                          'After all, this was all nothing more than',
                          'An inconvenience.',
                          'Nothing much else happened following this.',
                          'The company compensated you for your year long trouble',
                          'And all went back to what was before.',
                          'YOU: "..."',
                          'YOU: "I could just not go to work today..."',
                          'But you still decided to go anyway.',
                          'ENDING 1',
                          '']


class Level22(Level):
    def __init__(self):
        self._objects = [Building(0.1, 0.4, (50,50,50)), 
                         Building(0.8, 1, (50,50,50)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0)),
                         Clone(.8, True),
                         ]

        self._dialogue = ['YOU2: "Hey, where are you going?"',
                          'YOU: "Just not feeling it today."',
                          'YOU: "Can you fill in for me today?"',
                          'YOU: "I\'m just going for a walk."',
                          ''
                          ]


class Level23(Level):
    def __init__(self):
        self._objects = [ImageObject((0,0.11), "tree"),
                         ImageObject((0.5,0.11), "tree"),
                         ]

        self._dialogue = ['YOU: "Is this really all I\'m gonna amount to?"',
                          'YOU: "I\'ve literally been talking to myself for weeks"',
                          'YOU: "Why did this have to happen to me of all people?"',
                          'YOU: "..."',
                          'YOU: "What\'s even the point of any this?"',
                          'YOU: "It\'s like I\'m just living on autopilot."',
                          'YOU: "..."',
                          'YOU: "Maybe it\'s time to change."',
                          '[Move left to progress]'
                          ''
                          ]


class Level24(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0)),
                         ]

        self._dialogue = ['A few months later',
                          ''
                          ]



class Level25(Level):
    def __init__(self):
        self._objects = [Building(0.1, 0.4, (50,50,50)), 
                         Building(0.8, 1, (50,50,50)),
                         Car((.2,.2), (0.02,0)),
                         Car((.8,.4), (-0.02,0)),
                         ]

        self._dialogue = ['YOU2: "He just disappears one day and never returns"',
                          'YOU2: "Just a walk, yeah right"',
                          'YOU2: "Where the hell did he even go?"',
                          '',
                          ]


class Level26(Level):
    def __init__(self):
        self._objects = [ImageObject((0,0.11), "tree"),
                         ImageObject((0.5,0.11), "tree"),
                         ImageObject((0.25,0.61), "char_hippie"),
                         ImageObject((0.33,0.59), "guitar"),
                         ]

        self._dialogue = ['YOU 2: "There you ar-"',
                          'YOU 2: "..."',
                          'YOU 2: "what are you doing."',
                          'YOU 1: "busking"',
                          'YOU 2: "..."',
                          'YOU 1: "..."',
                          'YOU 2: "Well I\'ve just been working at the office..."',
                          'YOU 2: "Why\'d you up and leave like that?"',
                          'YOU 1: "I guess I just wanted a change of scenery."',
                          'YOU 1: "I know it doesn\'t look like much,"',
                          'YOU 1: "But this is everything I\'ve ever wanted"',
                          'YOU 1: "I looked up at those cars after leaving the apartment,"',
                          'YOU 1: "And everyday I felt just so..."',
                          'YOU 1: "Jealous."',
                          'YOU 1: "I didn\'t mean to leave you behind so abruptly."',
                          'YOU 2: "It\'s no problem actually, work hasn\'t been so bad."',
                          'YOU 2: "I got promoted last week actually."',
                          'YOU 1: "Well I\'m glad to see that that place going well for you."',
                          'YOU 1: "I probably won\'t go there again."',
                          'YOU 2: "You fine like this?"',
                          'YOU 1: "Yeah, I\'ve got some gigs going."',
                          'YOU 2: "Then I guess I\'ll see you around."',
                          'YOU 1: "Yeah, see you."',
                          ''
                          ]


class Level27(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0)),
                         ]

        self._dialogue = ['A year later',
                          ''
                          ]


class Level28(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (79, 63, 49)),
                         GameObject((.3,.5), (.15,.15), (159, 233, 252)),
                         GameObject((0,0), (1,0.4), (0,0,0)),
                         ImageObject((0.15,0.61), "char_hippie"),
                         ImageObject((0.23,0.59), "guitar"),
                         ]

        self._dialogue = ['YOU 2: "Oh hey, you\'re home."',
                          'YOU 1: "Yup, and with some news"',
                          'YOU 1: "Apparently they found a way to put us back together."',
                          'YOU 2: "Oh..."',
                          'YOU 2: "What\'s gonna happen?"',
                          'YOU 1: "I don\'t know,"',
                          'YOU 1: "But it\'ll be like only one of us existed this whole time."',
                          'YOU 1: "We can figure out what we wanna do after that."',
                          'YOU 2: "Alright then, let\'s go."',
                          ''
                          ]


class Level29(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (119, 109, 127)),
                         ImageObject((0.1,0.585), "char_hippie"),
                         ImageObject((0.22,0.59), "officer"),
                         ImageObject((0.30,0.59), "officer"),
                         GameObject((0,0.50), (0.05, 0.3), (0,0,0)),
                         GameObject((0.05,0.55), (0.01, 0.3), (102,214,206)),
                         ]

        self._dialogue = ['OPERATOR: "Right this way."',
                          'OPERATOR: "This machine will merge your memories"',
                          'OPERATOR: "The end result will take priority over one person"',
                          'OPERATOR: "So if you guys have had different experiences--"',
                          'YOU 1: "Wait, will we both remember our lives?"',
                          'OPERATOR: "Well, there\'s no guarentee everything will transfer"',
                          'YOU 1: "Are we really gonna go through with this?"',
                          'YOU 2: "..."',
                          '[Merge]                                                                         [Leave]',
                          '']


class Level30(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0))]

        self._dialogue = ['You walked through into the machine.',
                          'Your other self gives you a fearful look as you pass,',
                          'As if everything that had changed was being tossed away.',
                          'The merger was successful, and you left the building safely.',
                          'The company compensated you for your year long trouble,',
                          'And all went back to what was before.',
                          'Although it was difficult to find joy.',
                          'Memories of the previous clones clashed with one another,',
                          'Two people constantly yearning for opposite lives,',
                          'Forced to return to the same life that they had both escaped',
                          'ENDING 2'
                          '']


class Level31(Level):
    def __init__(self):
        self._objects = [Building(0, 1, (0,0,0))]

        self._dialogue = ['You declined the company\'s offer to merge,',
                          'There was no point, after all.',
                          'Both of you had become wildly different people,',
                          'Different passions, different paths,',
                          'Could you even still call yourselves the same person?',
                          'You returned to your lives, thriving in your own different ways.',
                          'Neither being the original',
                          'Yet both being the original',
                          'ENDING 3',
                          ''
                          ]
