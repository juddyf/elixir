# NOTES FOR JUDDY:
# I want different fonts for different languages. Please figure out fonts.

# Images
image black = "#000"
image white = "#fff"

# Declare Characters
define m = Character('Mimi')
define l = Character('Leila')
define b = Character('Blair')
define s = Character('Sunny')
define h = Character('Li')
define j = Character('Jongsu')
define k = Character('Minseo')
define r = Character('Romel')
define q = Character('Quentin')
define y = Character('Yejun')

#Game Variables
$ rp = 0 #romance points
$ fp = 0 #friendship points? unlock scenes?

# The game starts here.
label start:

    scene black
    with hpunch
    
    centered "A tackle. {w=1.0} A breath-crushing hug. {w=1.0}"
    centered "And that was how my summer break began. {w=1.0}"
    $ renpy.pause (3.0, hard=True)
    hide text
    with dissolve
    
    scene black
    with dissolve

#Title and theme song? Make the below fancy

    centered "Summer Break"
    
    scene black
    with dissolve
    
#Start - school background

"The morning before my last of junior year, my parents took extra care to hug and kiss me goodbye - definitely strange, because they had never been the most physically affectionate of guardians."

"I really should have known from that."

"School ended that day around noon, the bell completely drowned out yelling and cheering. {w} Everyone was running away."
 
"{i}I{/i} got run into. {w}On purpose."

scene white #need a pic of Li
with hpunch

"???" "MIMIIIIIIIIIIIIIIIIIIIIIII!!!!!!!!!!!!!!!!"

"I tumble to the ground as cloth and color and the scent of fresh laundry crash into me. It takes a second for my vision to clear, and when it does, my mouth drops open."

"Li Han is standing in front of me, practically beaming as he pulls back from his monstrous hug to look at me."

"To me, he is an old family friend, someone who used to babysit me way back when, but to the world at large, he's a star - an idol to be exact, 1/6 of the famous {i}Phantasy{/i}."

"Phantasy is a Korean pop idol group that came onto the k-pop scene about five years ago and grew popular globally really quickly, mostly due to their catchy debut album and diverse group members."

"Unlike most k-pop groups, Phantasy had members from all over Asia, instead of just from Korea, which meant that when they toured internationally, almost one of the members always had home court advantage, drawing out huge crowds."

"Of course, I'm not really thinking about any of that right now."

m "What are you doing here?"

"It comes out in English, because that was my first language, but I try to fumble for the Chinese translation for Li. Before I can get it out, he's replying, though he's speaking in Chinese."

h "We're vacationing in the U.S. for a couple months - and you're coming with us!" #chinese

m "...Wait, what?!"

h "The company thought it would be a good idea because our families are old friends, and it's a good chance to learn English! The U.S. is going to be part of our international tours from now on, and most of us need a lot of practice. And I talked to your parents, and they said yes (you wouldn't believe how long negotiations took though), and I even got them to let us bring some of your friends!" #chinese

"He continues on talking, most of which I struggle to understand because my Chinese has really deteriorated and because he's speaking far too fast."

m "Friends?" #chinese

"The word comes out in Chinese instinctively, and it causes Li to stop his tirade and squint at me."

h "Your accent has grown bad." #chinese

h "And friends! We got in contact with them a while ago, and the company talked to their families. They all agreed. I just wanted to surprise you!" #chinese

m "Who -"

"???" "Hey, Mimi!"

#pic of Leila, Blair and Sunny

"I turn my head, and standing just a few feet away are three of my best friends, each of them wearing a slightly different amused grin."


"Leila Kim." #pic of Leila comes forward a little?

"Blair Dunn." #pic of Blair comes forward, leila goes back

"Sona Darzi. (Also called affectionately, by me, 'Sunny'.)" #pic of sunny comes forward, blair goes back

m "Are you serious?"

s "Isn't it exciting?"

l "Phantasy is summering here! And we're summering with them!"

m "...You're very energetic."

l "Well, duh, Mimi, I'm going to learn all their songs!"

m "And, Blair, Sunny, you agreed to this because?"

b "You mean aside from the fact that it's a free vacation?"

s "And we get to bother you!"

b "That, too."

m "Oh. Great. Thanks."

"I roll my eyes at my friends and then look back at Li, who is still beaming at me."

h "Well?" #chinese

"It's a demanding voice, and it throws me right back to my childhood."

m "Alright, alright. Let's go!"

scene black


centered "Chapter One: {w=1.0} The Show"
$ renpy.pause (2.0, hard=True)

show white #car background
with fade

"Li brings the four of us out of the school and to the back field, which is normally used for soccer, but today holds a long, black limousine."

m "Wow, that is subtle."

h "Huh?" #chinese

m "Nothing."

