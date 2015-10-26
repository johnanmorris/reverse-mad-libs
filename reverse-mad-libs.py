# ------------- BLANKS -------------

blank_list = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]

# ------------- EASY -------------
easy_level = ('EASY: Linguistics is the scientific study of Q1 and '
            'their structures. There are 4 main branches of theoretical linguistics. '
            'Q2 is the study of sound systems. Q3 is the study '
            'of words and affixes, and how these are put together '
            'to create units of meaning. Q4 is the study of '
            'sentences and their structure. And finally, Q5 is '
            'the study of meaning.'
            )

easy_answers = ['languages', # 1
                'phonology', # 2
                'morphology', # 3
                'syntax', # 4
                'semantics'] # 5

# ------------- MEDIUM -------------
medium_level = ('MEDIUM: Phonologists distinguish between two '
            'different sound categories, phonemes and '
            'allophones. Q1 are phones that are '
            'perceived as the same sound by speakers '
            'of a language, while Q2 are considered '
            'different sounds. The location of '
            'allophones are usually in Q3 distribution: '
            'where one occurs, the other does not. '
            'In some cases, however, there are allophones '
            'which do occur in the same phonetic enviromentment; '
            'these are said to be in Q4 variation. These are '
            'are usually due to differences in dialect or '
            'personal preference. Similarly, morphologists '
            'use the word Q5 to describe variation in form '
            'within a morpheme. For example, the plural in '
            'English has 3 productive forms: [s], after Q6 stops, '
            'such as [t] or [k] ("cats"); [iz], after voiced Q7, '
            'such as [s] or [z] ("horses"); and [z], in most other places. '
            )

medium_answers = ['allophones', # 1
                  'phonemes', # 2
                  'complementary', # 3
                  'free', # 4
                  'allomorph', # 5
                  'voiceless', # 6
                  'fricatives'] # 7

# ------------- HARD -------------
hard_level = ('HARD: Historical linguists study language change. '
            'One common method for doing this is called Q1 '
            'linguistics. This method involves comparing languages '
            'known or suspected to be related in order to determine '
            'their degree of relatedness. Through these methods, '
            'English has been determined to be a West Q2 '
            'language, related to Dutch, Yiddish, and German, '
            'among others. This grouping, in turn, is part of '
            'the Q3 language family, one of the largest '
            'language families in the world. Other subfamilies '
            'in this family are: Q4, which includes French, '
            'Italian, and Spanish; Q5, which includes '
            'Irish and Welsh; and Q6, which includes '
            'Farsi, Hindi/Urdu, and Bengali. The oldest known '
            'branch in this family is Q7, which includes '
            'Hittite, a language spoken in modern-day Turkey '
            'around 3,500 to 3,200 years ago.'
            )

hard_answers = ['comparative', # 1
                'germanic', # 2
                'indo-european', # 3
                'romance', # 4
                'celtic', # 5
                'indo-iranian', # 6
                'anatolian'] # 7

# ------------- MAIN FUNCTIONS -------------

'''Prompts the user to choose level. Calls the play function for the given choice,
or prompts user to try again if they have made an invalid choice.'''
def choose_level():
    choice = raw_input("Pick a level: easy (E), medium (M), or hard (H): ")
    choice = choice.lower()
    while True:
        if choice == 'e' or choice == 'easy':
            play(easy_level, easy_answers)
            break
        if choice == 'm' or choice == 'medium':
            play(medium_level, medium_answers)
            break
        if choice == 'h' or choice == 'hard':
            play(hard_level, hard_answers)
            break
        choice = raw_input("Invalid choice. Pick E, M, or H: ")

'''Takes two inputs, the level choice and answer, determined in choose_level
function. Uses these inputs to loop through get_answer function and fill_in_answer
function, increasing the index of answers and blank_list by 1 after
completion of each loop.'''
def play(level, answers):
    print level
#    print "FOR TESTING PURPOSES, HERE ARE THE ANSWERS: " + ", ".join(answers)
    index = 0
    while index < len(answers):
        get_answer(answers[index], blank_list[index])
        level = fill_in_answer(level, answers[index], blank_list[index])
        print level
        index += 1
    print "Hooray! You finished the level!"

'''Takes user input, converted to lower case, and compares it to the answer.
If correct, prints correct. If incorrect, prompts user to try again.'''
def get_answer(answer, blank):
    user_input = raw_input("What is the answer to " + blank + "?: ")
    user_input = user_input.lower()
    while True:
        if user_input == answer:
            print "You're correct!"
            break
        user_input = raw_input("Try again. What is the answer to " + blank + "?: ")

'''Splits the level text (e.g., easy_level) into a list, then loops through the
list. If the word is a blank (eg, Q1, q2, etc.), the blank is replaced with the
answer and appended to replaced list. Otherwise, the word is appended to replaced
without change.'''
def fill_in_answer(level, answer_list_item, blank_item):
    replaced = []
    level = level.split()
    for word in level:
        if blank_item in word:
            word = word.replace(blank_item, answer_list_item)
            word = word.upper()
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

# ------------- PLAY THE GAME -------------
print ("Welcome to Noelle's reverse madlibs game. This\n"
    "game will help you review linguistics vocabulary.\n")

choose_level()