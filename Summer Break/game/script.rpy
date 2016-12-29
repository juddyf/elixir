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

# The game starts here.
label start:
    
    #Game Variables
    $ romance_points = 0 #romance points
    $ friendship_points = 0 #friendship points? unlock scenes?

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

m "Nothing! Nothing, nothing."

"He squints at me suspiciously, but the limo door swings open at that point, and he ducks in, followed by Leila, Sunny, and then Blair."

"I glance at the school behind me and then duck in after them."

"The inside of the limo had black walls and silver-gray leather seats, which were occupied by five guys. It takes me a second and a nudge from Leila to realize that they are the rest of the members of Phantasy, two on the left, three on the right. They're chatting among themselves, but they look up when we walk in, and smiles brighten up their faces. The one with the ponytail pipes up."

"???" "Oh, finally. We were wondering if you'd managed to get lost somehow, Li."

"The words sound Korean, and my suspicions are confirmed when Leila - the only one of the four of us who is actually able to speak Korean fluently - leans over and translates. Li responds in kind."

h "Whatt? That would never happen."

"???" "Right. So which one is she, your beloved little sister?"

"He looks at all of us, and I grimace a little at the nickname. As a child, Chinese had been one of my primary languages, and I had referred to everyone by honorifics instead of their names - big brother had been Li's, even though we weren't related."

menu:

     "Wait for Li to introduce you.":
        "I look at Li, who smiles and grabs me by the hand."
        h "This is Mimi!"
        m "Hi. It's nice to meet you."

     "Introduce yourself.":
        $ friendship_points += 1
        m "Hi, I'm Mi Yang."
        "Leila and Li" "Mimi!"
        "Their words are perfectly in unison, and they meet each other's eyes with a grin, something that does not bode well for me. The rest of the members smile, indicating they understood my English."

"We all take our seats, Li pulling me down to sit next to him, while Leila plops down right afterwards, and Sunny and Blair take spots on the other side. Leila, Sunny, and Blair introduce themselves, and then the members go around."

"Next to Li is Yejun, the guy with the ponytail. He has a vaguely cutting edge to everything that he says, and he is, as told to me by Leila's helpful voice in my ear, as the 'pretty one', a title that he certainly deserves. Yejun is also the oldest at 26 and one of the lead vocalists."

l "Their parts are actually split pretty evenly for a k-pop group though. He's actually responsible for a lot of Phantasy's popularity, because he hosts a lot of shows, so lots of people know his face."

"On his other side is Quentin, who grins boyishly and who is half-American and speaks English as fluently as any of us, as well as Mandarin and French. He's the other lead vocalist, but unlike Yejun, he's actually the youngest member of the group at just 21."

l "You grew up in Canada, right?"

q "Yep!"

s "Really? So did I!"

"Across from Quentin is Minseo, who is coolly charming and speaks English fairly well, though not quite as good as Quentin. He's one of the rappers, though Leila notes in a very soft whisper that that is probably because he's not fantastic at singing or dancing. Minseo just smiles amicably through it all, giving no indication he's heard anything."

l "Oh! And he acts in dramas!"

m "...Is this like Phantasy fun fact time or something? Why do you know all this?"

l "They're a good band. I tell you about them at least once a week!"

m "...I have no memory of this."

"To Minseo's left, there is Jungsu, one of the lead dancers and main singers. He has a wide, easy smile in an open face and looks very comfortable ensconced between Minseo and the last member of Phantasy, Romel."

"Romel is the other lead dancer and makes a cheesy peace sign when Li introduces him, almost hitting Blair, who is sitting on his other side, in the face. She ducks and then glares as Romel hastily apologizes. Fans found his clumsiness 'charming', though by the looks of it, Blair didn't really agree."

m "So what are we doing here? We're just vacationing with you? How is your company letting you do this?"

"The members looked at each other as Quentin and Minseo translated and then, there was kind of a collective shrug that made Sunny laugh."

h "We made some agreements."

q "So we're actually in between albums right now, and we just finished our tour, so we all wanted to get some rest, and Li knew you."

h "And it's the perfect opportunity for us to get better at English!"

m "Okay, so the idea is that we're going to be teaching you English?"

h "Yep!"

m "...And for that you're getting a couple months off?"

h "Uh..."

q "There's actually something else. We're going to be recording it for a TV show."

menu:

     "What.":
          m "I'm sorry, what? Huh. What. Why. What's happening."

     "That's cool!":
          m "Oh wow, that's cool. How's it going to work?"

k "It's going to air as a English-learning program, with Quentin and you teaching us conversational English. We'll probably spend a couple weeks filming, but we should have a lot of free time."

l "What about you? Your English is pretty good."

"A sly smile snuck over Minseo's face, and he innocently shrugged his shoulders."

k "What can I say? They didn't think I was good enough to be an instructor. Or that I needed teaching."

r "He's going to skip out on everything!"

"Romel pouted at Minseo, who just looked smugly back, as Leila translated the words. It was quite dizzying, the whole array of languages being spat around."

"Quentin and Minseo were talking in English, belying anything Minseo might have told his producers, Li was switching between Chinese and Korean, sometimes mid-sentence, Leila was switching between Korean and English, Sunny and Blair stuck to English with occasional Korean from Blair, who had learned it from watching Korean drama shows, and Yejun, Romel, and Jungsu spoke in Korean with just enough English thrown in to make it really confusing."

"I shook my head, trying to clear some of the stray words out of it and focus on what Minseo had said."

m "So, wait. Quentin and I are going to be teaching the three of you by ourselves? Why are they here?"

"I point at Sunny, Blair, and Leila, who all feign various levels of shock."

b "Rude."

l "Mimi! Are you saying you don't want us here?"

s "That's so mean."

"I flap my hand dismissively at them, hiding a grin, and look at Li for an explanation."

h "For company! We didn't want you to get lonely while doing this."

k "Would you rather they did the show too? They signed waivers, so technically, they could."

menu:

     "Yes, definitely.":
          m "Yes. I do. I want them in front of that camera with me or possibly without me, 'cause I'm not a huge fan of getting mobbed by angry fangirls and fanboys when they see us teaching their beloved idols English."
          k "I don't think they could misconstrue teaching..."
          m "I've heard Lei talk about them. They can misconstrue anything. Also, if you know a word like 'misconstrue', you should be teaching!"
          "Minseo just grinned and leaned his head on Jongsu's shoulder casually."

     "Well...":
          m "Well, I think that's up to them. I don't want to force them into this when I have been."
          "I give Li a very pointed look, which he somehow misses completely. I resist the urge to just roll my eyes as I get flashbacks to back when I was 12 and trying to get Li to understand the troubles of a preteen."
          l "I think it would be fun!"
          b "Yeah, it sounds cool."
          s "I wouldn't mind!"

q "We can get that worked out then."
j "The more the merrier!"
"The words are English, albeit a little clumsy. Quentin nods encouragingly at him, Jongsu beams at his success."
