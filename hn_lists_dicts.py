from random import choice
import engaging_accounts

#Tweets (without pictures)
human_nature_accounts = [
        #Steven Pinker
                '“Sex and excretion are reminders that anyone\'s claim to round-the-clock dignity is tenuous. The so-called rational animal has a desperate drive to pair up and moan and writhe.” - @sapinker',
                '"Human nature is complex. Even if we do have inclinations toward violence, we also have inclination to empathy, to cooperation, to self-control." - @sapinker',
                '"Language is a window into human nature, but it is also a fistula, an open wound through which we\'re exposed to an infectious world." - @sapinker',
                '"I suspect music is auditory cheesecake, an exquisite confection crafted to tickle the sensitive spots of... our mental faculties." - @sapinker',
                '"Cognitive psychology tells us that the unaided human mind is vulnerable to many fallacies and illusions because of its reliance on its memory for vivid anecdotes rather than systematic statistics." - @sapinker',
                '"Many artists and scholars have pointed out that ultimately art depends on human nature." - @sapinker',
        #Sebastian Junger
                '"Humans don’t mind hardship, in fact they thrive on it; what they mind is not feeling necessary. Modern society has perfected the art of making people not feel necessary. It\'s time for that to end." - @sebastianjunger',
                '"When people are actively engaged in a cause, their lives have more purpose... with a resulting improvement in mental health." - @sebastianjunger',
                '"If you want to make a society work, then you don’t keep underscoring the places where you’re different—you underscore your shared humanity" - @sebastianjunger',
                '"The beauty and the tragedy of the modern world is that it eliminates many situations that require people to demonstrate a commitment to the collective good." - @sebastianjunger',
                '"The economic and marketing forces of modern society have engineered an environment… that maximizes consumption at the long-term cost of well-being." - @sebastianjunger',
                '"Surely this was new in the human experience, I thought. How do you become an adult in a society that doesn’t ask for sacrifice? How do you become a man in a world that doesn’t require courage?" - @sebastianjunger',
                #multi-line start
                '''“Self-determination theory holds that human beings need three basic things in order to be content:

they need to feel competent at what they do; they need to feel authentic in their lives; and they need to feel connected to others.” - @sebastianjunger''',
                #multi-line end
                '“Whatever the technological advances of modern society – and they’re nearly miraculous – the individualized lifestyles that those technologies spawn seem to be deeply brutalizing to the human spirit.” - @sebastianjunger',
                '"Much of the evolutionary basis for moral development stems from group pressure." - @sebastianjunger'
                ]


###############################################################################################


human_nature_without = [
        #Arthur Schopenhauer
                '"If you come across any special trait of meanness or stupidity... you must be careful not to let it annoy or distress you, but to look upon it merely as an addition to your knowledge—a new fact to be considered in studying the character of humanity" - #ArthurSchopenhauer',
                '"All truth passes through three stages. First, it is ridiculed. Second, it is violently opposed. Third, it is accepted as being self-evident." - #ArthurSchopenhauer',
        #Anton Chekhov
                '“Man will only become better when you make him see what he is like. - #AntonChekhov”',
                '"Love, friendship, respect do not unite people as much as common hatred for something." - #AntonChekhov',
        #Abraham Lincoln
                '“I don’t like that man. I must get to know him better.” - #AbrahamLincoln',
                '"I am a firm believer in the people. If given the truth, they can be depended upon to meet any national crisis. The great point is to bring them the real facts." - #AbrahamLincoln',
        #Mark Twain
                '“Everyone is a moon, and has a dark side which he never shows to anybody.” - #MarkTwain',
                '"The most interesting information comes from children, for they tell all they know and then stop." - #MarkTwain',
                '"Whenever you find yourself on the side of the majority, it is time to pause and reflect." - #MarkTwain',
                '"Travel is fatal to prejudice, bigotry, and narrow-mindedness." - #MarkTwain',
                '"The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time." - #MarkTwain',
                '"A lie can travel half way around the world while the truth is putting on its shoes." - #MarkTwain',
                '"If you pick up a starving dog and make him prosperous he will not bite you. This is the principal difference between a dog and man." - #MarkTwain',
                '"Always do what is right. It will gratify half of mankind and astound the other." - #MarkTwain',
                '"Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured." - #MarkTwain'
                ]


######################################################################################################


birthday = {"@yuval_harari":"2-24",
            "@RobertGreene":"5-14",
            "@kellymcgonigal":"10-21",
            "@IAmMarkManson":"3-9"}


######################################################################################################


greene = open("greene_quotes.txt")
greene_quotes = greene.read().split("\n")
greene.close()

#Tweets with pictures
human_nature_dict = {#Robert Greene
                    choice(["greene.jpg", "greene2.jpg", "greene3.jpg", "greene4.jpg", "greene5.jpg"]) : choice(greene_quotes),

                    #Carl Jung
                    choice(["jung.jpg", "jung2.jpg", "jung3.jpg"]) : choice(['"Everything that irritates us about others can lead us to an understanding of ourselves." - #CarlJung', '"Knowing your own darkness is the best method for dealing with the darknesses of other people." - #CarlJung',
                    '"Unfortunately there is no doubt about the fact that man is, as a whole, less good than he imagines himself or wants to be. Everyone carries a shadow, and the less it is embodied in the individual\'s conscious life, the blacker and denser it is." - #CarlJung', '"We cannot change anything until we accept it. Condemnation does not liberate, it oppresses." - #CarlJung']),

                    #Frantz Fanon
                    choice(["fanon.jpg", "fanon2.jpg"]) : choice(['"Sometimes people hold a core belief that is very strong. When they are presented with evidence that works against that belief, the new evidence cannot be accepted.” - #FrantzFanon', '"A man who has a language consequently possesses the world expressed and implied by that language.” - #FrantzFanon']),

                    #Mark Twain
                    choice(["twain.jpg", "twain2.jpg", "twain3.jpg"]) : choice(['“Everyone is a moon, and has a dark side which he never shows to anybody.” - #MarkTwain', '"Whenever you find yourself on the side of the majority, it is time to pause and reflect." - #MarkTwain', '"Travel is fatal to prejudice, bigotry, and narrow-mindedness." - #MarkTwain', '"Always do what is right. It will gratify half of mankind and astound the other." - #MarkTwain',
                    '"Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured." - #MarkTwain'])
                    }


########################################################################################################


#Terms in psychology
psych = [
"""
The Paradox of Choice:

The more options we’re given, the less satisfied we become with whatever we choose, because we’re aware of all the other options we’re potentially forfeiting.
""",
"""
Bystander Effect:

The more people who are present at an emergency situation, the less likely it is that any one of them will help.
""",
"""
Mere Exposure Effect:

The more often people have been exposed to a stimulus, the more they like it—even when the stimulus is presented subliminally. Basically, people prefer things they're familiar with. (A common marketing technique)
""",
"""
Cognitive Dissonance:

The idea that we find it hard to hold two contradictory beliefs, so we unconsciously adjust one to make it fit with the other.
""",
"""
Reverse Psychology:

The urge to do the opposite of what someone wants you to do out of a need to resist a perceived attempt to constrain your freedom of choice.
"""
]
