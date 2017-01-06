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

"To Minseo's left, there is Jongsu, one of the lead dancers and main singers. He has a wide, easy smile in an open face and looks very comfortable ensconced between Minseo and the last member of Phantasy, Romel."

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

"Quentin and Minseo were talking in English, belying anything Minseo might have told his producers, Li was switching between Chinese and Korean, sometimes mid-sentence, Leila was switching between Korean and English, Sunny and Blair stuck to English with occasional Korean from Blair, who had learned it from watching Korean drama shows, and Yejun, Romel, and Jongsu spoke in Korean with just enough English thrown in to make it really confusing."

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

y "Well, if it's going to be like that, we clearly have to go shopping." #korean

m "Shopping? What's wrong with our clothes?"

"I look down at my outfit, _______, and then glance next to me at Leila, who's wearing a long tank and shorts. Blair is wearing _____, while Sunny has a cute off-the-shoulders shirt. All in all, variable in how dressy we are, but respectable none the less. I look back at Yejun."

"Yejun wrinkles his nose in distaste."

y "They're not exactly TV-ready." #korean

j "I think they look nice." #korean

r "Hyung, you can't insult their clothes!" #korean

"'Hyung', Lei whispers to me, is the honorific that males use for other males who are older than them."

b "I wouldn't mind going shopping." 

s "Yeah, it sounds like fun."

l "Mmm... but shopping is so boring."

m "Yeah, it's mostly just wandering around and then being disappointed by how expensive things are."

y "You're not going on TV dressed like that."

if friendship_points > 0:
     m "Wow, rude. Li, I don't like your friends. No, don't translate that!"
     "I grab a pillow and whack Leila with it as she turns my words into Korean for the benefit of the other members. She squawks and ducks out of the way. The pillow clips her shoulder and drops to the ground."
     "Quick as a flash, she grabs the pillow off the ground and swings up with it. I throw myself out of the way, and it hits both Li and Yejun, the latter of whom grabs a pillow and chucks it."
     "It bounces away as I bat at it and flies across to smack Romel in the face. He flails, manages to hit both Jongsu and Blair, who don't react favorably, and in another moment, everyone is chucking pillows around the place."
     "It only stops when one of them hits the partition, and the screen rolls down to reveal the driver looking at us in the rear view mirror. He doesn't quite glare, but we get the message."
     "Meekly, we all return to our seats, all of us in various states of disarray, except for Sunny, who has managed to get away unscathed. She always did have crazy luck."
else:
     m "..."

m "Alright, we'll go shopping. But I'm not paying for any overpriced blouses."

scene black


centered "Chapter Two: {w=1.0} Shopping"
$ renpy.pause (2.0, hard=True)

show white #limo
with fade

"In the end, we decide to separate into two groups, with me, Leila, Yejun, Li, and Minseo going shopping for clothes, while Sunny, Blair, Jongsu, Quentin, and Romel going shopping for food."

m "I'd way rather go shopping for food. Blair, you like clothes shopping. Switch with me."

b "No. I like food more. Besides, we're going to cook. Are you going to cook?"

y "You and Lei are the problem ones. You have to come with us." #korean

l "Whatt? I'm a problem? Why?" #korean

"Yejun gives her a look and stands up, taking a moment to get his balance in the moving limo before making his way to the partition and letting the driver know where we need to go."

"About ten minutes later, we pull into a mostly empty parking lot that sits outside a giant mall structure. It's not one that either Leila and I have ever seen before, which tells us how far we've really come."

l "Where are we going?"

k "We rented a house out in the countryside. It's about an hour away from here, I think. The car will come pick us up."

"He adjusts his baseball cap - he, Yejun, and Li are all wearing identical ones to avoid anyone possibly recognizing them - and then tugs at his hair a little."

"Yejun strides towards the closest entrance, the rest of us following close behind."

"He makes his way to one of the major clothing outlets, judging everything with a critical eye as the rest of us collectively wander slowly after him."

"Minseo eyes thinks speculatively, and Li calls me over to every other rack of clothes to judge his choices. They are varied and usually far too large for me, so I end up redirecting most of it to Lei."

"She still seems to be riding the energy high of actually getting to summer with a K-pop group, and she bounds from item to item, expressing approval and disapproval with equal vigor."

y "Try this one on." #korean

"Lei pops up to translate as he hands me a gray ruffled skirt and white blouse and pushes me towards the changing room."

menu:
     "Oh, pretty!":
        m "Oh, it's really pretty."
        y "I know. I have great taste. Go." #korean
        "Obediently, I do so as he goes to get Lei something to try."
     "Ew. Skirts.":
        m "Ew. I don't want to wear a skirt."
        y "I want to see how it looks. {i}Go.{/i}" #korean
        "Obediently, if a little grumpily, I do so as he goes to get Lei something to try."

"The skirt fits perfectly, but the blouse is about a size too large, the sleeves hanging over my hands. I step out of the dressing room and let Li coo over how cute the look is while Yejun gives a slightly more critical eye."

"Lei seems to have gone into a changing room so Li translates into Chinese as Yejun makes his judgment."

y "I like it. The shirt's a little big, but it makes you look more innocent, which you need help with." #korean

menu:
     "How mean. T_T":
          m "That's so mean."
          h "No! Mimi, it's okay! I'll protect you!"
     "Whatt? I'm innocent.":
          $ friendship_points += 1
          m "Whatt? I'm totally innocent. What are you talking about?"
          "Minseo and Li both giggle as Yejun just gives me a look. I try to bat my eyelashes, but it doesn't work very well."
     "Isn't that something you need more help?":
          $ friendship_points += 1
          m "Isn't that something you need more help with than me?"
          "Li chortles and then translates for Yejun, while Minseo chuckles in the background. Yejun gives me a look halfway between exasperated and amused."
          y "My fans have already accepted me for what I am. You have no fans yet."

"A few minutes later, he sends me in with a larger stack of clothes, and I head towards the dressing room resignedly. The clothes are pretty, though the price tags make me wince."

m "Although, I guess TV shows probably have a larger budget. It's not like I'm paying for it out of pocket or anything."

"I go through a series of costume changes, feeling vaguely like a dress up doll for Li and Yejun's entertainment. Minseo looks less amused and more bored as time goes by, though he does translate when Lei goes to change, which is useful."

"I wonder how easy it will be to pick up Korean, because we can't spend the whole summer just having Minseo and Quentin and Lei translate or having Li translate to Chinese."

m "Maybe they'll be really good at English?"

"I grin to myself. It seems unlikely given how utterly random English can be at times."

m "But then, I guess it'll depend on how good teachers we are."

"Stepping out of the dressing room, I spin in a circle, sending the sundress skirt flaring upwards. Yejun looks at it critically."

y "It's a little long on you, but that means it'll probably be good for that other one - what's her name? Sunny?"

m "Yeah, that's it."

y "Okay. We'll get that one for her then. Here, try on these next. You're about the same height as Blair, so we don't have to guess."

m "How come Lei doesn't have to go through this?"

"He gives me an amused look, and we both look at Lei, who has come leaping out of her most recent dressing room. She has been hopping around for God only knows what reason."

"Compared to me, Sunny, and Blair who are all around average height, Sunny a little taller than Blair and I, Lei towers above us at six feet, meaning that getting her to try on clothes that were meant for any of the rest of us would be a rather useless task."

"Right now, she is wearing a large button-up plaid shirt over a plain black tank with spaghetti straps, jean shorts, and the boots that she came in with, which are chunky and light tan, altogether quite fashionable."

l "What do you think?"

menu:
     "You look cute!":
          $ friendship_points +=1 #max is 3 now
          m "You look really cute. I like it."
          h "Yeah, it's nice!"
          y "It's a little casual." #korean
          l "What's wrong with that?"
          m "Yeah, it's not like we're actually going to be in school."
          y "I guess." #korean
          l "I wanna get it."
          k "I like it, too."
          l "Thanks, Minseo!"
          "She pats him on the head, and he frowns a bit as if he wasn't expecting that reaction. I can't help but laugh at his reaction, and I find that Li is doing the same when I turn back towards the dressing room"
     "Meh.":
          m "Meh. It's okay."
          h "Mimi! That's not nice."
          l "Awww, really? I like it a lot."
          y "It's a little casual." #korean
          k "I think it's nice. Yejun, it's not like they're actually going to be in school of anything. I think casual would be better." #korean
          l "Yeah!"
          "She points at Minseo as if to emphasize his point and then bounds over and pouts at me."
          l "See, he likes it."
          "I shrug noncommittally and turn back to the dressing room."

"We continue trying on clothes for another hour, though for the last 30 minutes or so, it's just me, since Lei has already picked out her clothes. I whirl through them with as much speed as possible, running through the clothes."

"Lei, at some point, takes her phone out and begins sending pictures to Blair and Sunny, who reply with a mild delay, so in the end, she just video chats them and lets them judge as I play guinea pig."

"At the end, I am fairly tired, but in addition to the three outfits that Lei has picked out, we have gotten four for Blair, three for Sunny, and three for me as well."

y "That should be okay for now. I'm sure you guys must have some nice things among your own clothes. We can come back later if we need to." #korean

l "Hey, I have nice clothes!"

m "Same. Please don't make us come back."

h "But you look so cute, Mimi."

m "I'm okay with not looking cute."

h "But Mimi!"

y "We'll see how many episodes they want us to shoot at once. You can't be wearing the same thing in every shot." #korean

m "Sure, I can. That's what a normal person would do. Please let me be a normal person."

"Yejun rolls his eyes, gathers up the clothes in the cart that we got and starts going towards the checkout counter, from where the cashier has been giving us the hairy eyeball for some time - most likely because we've gone through about half the store's inventory."

"We go to follow him, Lei still bouncing, Minseo eying her with some amusement, and Li clinging onto my arm. It's a little comical because he's almost as tall as Lei, and every time he takes a step, we get a little bit out of sync. Behind us, I can hear titters."

"We catch up with him as we get into line behind a few other people. There seems to be some problem with the machine that is causing a delay, which means that soon enough Lei is shuffling around, bored."

"She wanders over to another set of clothes, disappears behind it for a second and then ops back out with a top hat on her head, beaming."

l "Look, look! Isn't it cute?"

m "Very Mad Hatter-esque."

l "Come try them on with me!"

if friendship_points > 2:
     "I consider the silly way the top hat tilts on her head for a moment and then nod, grinning, heading towards the hat rack."
     "There are dozens of hats lining every single shelf, though, of course, many of them are duplicates. I grab a top hat like the one that Lei has, try it on, and then exchange it for a sun hat that has a very wide brim."
     "We both step out dramatically, Lei now wearing a beanie. She strikes a pose like an idol might do in a music video while I toss my hair daintily over one shoulder."
     "Li claps his hands in appreciation, and Minseo grins while Yejun rolls his eyes."
     k "Those look really good."
     h "Aww, Mimi, you look like a lady." #chinese
     m "Oh gross."
     "I take the hat off and toss it, frisbee-style, at Li, who ducks his head at the exact moment to catch it. It lands perfectly on top of his baseball cap, and he flutters his eyes."
     h "Am I pretty?" #chinese
     m "You're always pretty. All of you really. Disturbingly so."
     "He grins and tosses the hat back."
     "The line moves forward, and Lei and I go to look for new hats."
else:
     "I consider Lei for a second and then shake my head, grinning."
     m "I think I'll pass this time. Thanks."
     "She pouts and heads back towards the hats by herself."
     h "I think you'd look good in a hat, Mimi."
     m "Uh, I think it probably depends on what kind of hat."
     h "No, you'd look good in any hat. You're adorable."
     "He ruffles my hair, and I have a distinct feeling of being transported into the past. Suddenly, I'm eight, and Li is smiling down at me from what feels like a long way up."
     "Lei pops back out with a beanie on her head, striking a pose like an idol might do in a music video."
     k "I like that one. It makes you look very cool."
     l "That's cause I am cool."

"Eventually, we get to the front of the line. Minseo talks to the cashier, Yejun pays, and Li ends up bringing all the stuff back to the car. Yejun surveys the load after we all get in."

y "Well, I think that was a successful trip."

scene black

centered "Chapter Three: {w=1.0} The House"
$ renpy.pause (1.0, hard=True)

show white #house

"We arrive at the house a little bit later. It is quite large, but then I suppose it has to be to hold ten people comfortably. It looks to be two stories high, rather wide, with a round window at the top that I'm certain leads to an attic."

"The others are already inside, unpacking in the kitchen, when we walk in. Jongsu looks up and beams at us, then nudges Romel."

"Romel & Jongsu" "Welcome home!"

l "Awww. We're home!"

b "Hey, you guys finally made it. We're going to start dinner soon."

m "Ooo, what's for dinner?"

s "We're making kimchi hot pot! I've never had it before, but it sounds yummy."

b "Come upstairs first though. I wanna see the clothes, and we have to pick rooms."

"Blair leads the way upstairs, Sunny and Lei close behind her while I bring up the rear. Upstairs is carpeted as compared to the wood floors of the downstairs, and it looks soft and lush as we head towards the end of the hall."

b "We're on this side. They're on the other side."

"She points down the hall, where I can see more doors leading to either side of the hall. Blair points at two doors at the end of the hall, whose doors are slightly open."
 
b "We have these two."

"She nudges the doors open more. Both the rooms have two twin sized beds with a giant window on one side, and besides the vaguely different views, they look identical."

m "What are we choosing between here? They're the same."

s "No, they're not! Look!"

"Sunny throws open the curtain to the window of the room to the left and points down at the ledge."

m "...What am I looking at?"

s "The ledge here is like a foot shorter than it is in the other room."

"I look at Lei, who is smiling, Blair, who seems to be resisting rolling her eyes, and then back at Sunny."

m "Oh. No. I see it now. You're right. I think I'd prefer this room."

"She somehow misses the sarcasm by a mile and just nods understandingly."

s "Okay! We can take this room then. And Blair and Lei can take the other one."

l "Okay!"

b "Whatever."

"We unpack out stuff somewhat. Luggage has been sent over from our houses, and Blair and Sunny are eager to try on the clothes that we bought them."

"About half an hour later, we head downstairs, where there are loud noises coming from the kitchen and living room. The guys are all clustered in the area in between, Quentin, Romel, Li and Jongsu crowded around Yejun and Minseo."

"Yejun and Minseo" "Kai bai bo!"

"I peer between Jongsu and Li. Yejun is glaring at Minseo, both hands held out in front of him, one palm turned up, the other one in a fist on top of the first hand. Minseo had a similar pose, but was grinning."

k "Come on, hyung." #korean

m "Are they playing rock-paper-scissors?"

l "Yep. Kai bai bo!"

"She brandished a fist, almost whacking Romel in the head."

m "What are you playing for?"

h "Loser has to help me and Romel cook. You wanna help, Mimi?" # chinese

m "Uh... what's my other option?"

j "You could come play video games in other room with me and Quentin."

l "Ooo! I wanna play video games."

b "I can help you guys cook."

menu:
     "Yeah, I can help cook.":
          jump cooking_li

     "Mmm... I think I'm gonna go with the games.":
          jump vg_jongsu

label cooking_li:
     $ friendship_points +=1
     m "Yeah, I'll help, too."
     s "I'll go with you then, Quentin."
     q "Okay!"
     h "Yay! Mimi!" #chinese
     "He hugs me with one arm and then tugs me along to the kitchen. Over my shoulder, I can hear Yejun and Minseo still shouting and then a cry of despair that sounds like it's coming from Yejun."
     "Looking over my shoulder, I see Minseo with both arms raised in the air in triumph as Yejun, who has fallen dramatically back against Romel, lays a delicate hand to his forehead."
     "Grinning, I turn back towards the kitchen."
     h "Are you having fun, Mimi?" #chinese
     m "Uh, like so far? Yeah, I think so. I really can't believe my parents agreed to this though." #chinese
     h "It took a lot of convincing, but I think they trust me. A little less so since I became an idol, but they still know I'll protect you. I did used to change your diapers after all." # chinese
     m "Ew, can we not talk about that when we're going to cook something?" # chinese
     "He ignores me, babbling on as he rummages around in the fridge to get the ingredients. I look around for any cookware I can start preparing, even though I'm not quite sure what we're doing."
     h "Get the big pot with the wide base. You were such a cute little kid. You used to follow me around. It was like having my own little sister." #chinese
     m "That's pretty much what I was, so that makes sense. What do I do with this?"
     "From behind me, I hear a dramatic sigh. Romel has gently towed Yejun into the kitchen, though he is still support Yejun's wait. Blair has followed them and is giving Yejun a faintly exasperated look."
     h "Yejun, stop being so lazy. Cooking isn't going to kill you. Romel and I cook all the time." #korean
     r "Hyung, it's really not that bad. You can cut up the kimchi." #korean
     "Without any of our translators in the room, Li ends up translating what he's saying to Chinese, so that I can then translate for Blair, who is still watching everything with faint exasperation."
     "Romel sets up Yejun with the knife, the latter muttering something rude and that Li doesn't translate. Li starts up with the meat on the other cutting board, and I set the water boiling. Since there really isn't that much to do, Romel and Blair start up on the dessert."
     "It's quite entertaining to watch them attempt to work on it together, as Romel is attempting to use his English, which for some reason is mostly tourist English, and Blair ends up both confused and very amused."
     "She's giggling at the end of it, when they slide the lava cakes into the oven, and Romel has resorted to wild arm gestures to get his point across."
     h "How's the soup?" #chinese
     m "Spicy. I'm tearing up." #chinese
     "He ducks over my shoulder to taste it and makes a noise of satisfaction."
     h "Delicious. We should get it ready -" #chinese
     l "Is it done yet?"
     "Lei's strident voice came cutting through the kitchen air, and she, Jongsu, Quentin, and Sunny come tumbling through to the entrance of the kitchen, sniffing eagerly."
     s "Ooo, it smells so good."
     "She comes up right behind me to take a sniff as Jongsu hops to the other side and sneaks a bite."
     m "Hey!"
     "I whack at his hand with the spoon I'm using, and though I don't make contact, he backs off, licking his finger."
     j "It's tasty!" #korean
     l "What? I want some!"
     m "Oh my God, we're almost done. Go wait in the dining room."
     "There's some more whining and complaining and some muttering about how I might be a tyrant (mostly from Lei), but Quentin and Minseo eventually grab some bowls and cutlery and bring it to the dining room to set up the places."
     jump firstday_dinner

label vg_jongsu:
     $ romance_points +=1
     m "Mmm... let's see, I could cook or I could play video games... I think I'm going to go with the video games."
     "Li clutches his heart as if I've mortally wounded him."
     h "Mimi, you don't want to spend time with me?" #chinese
     m "...I don't want to do work."
     s "I'll come help with the cooking."
     "Li looks only the mildest bit mollified, but perks up when Yejun loses the rock-paper-scissors war and is dragged to the kitchen by him and Romel, with Sunny and Blair following."
     "The triumphant Minseo, who receives a high five from Lei, leads us to the living room, where he places himself on one of the couches with deep satisfaction, spreading out his arms."
     "He doesn't get to stay relaxed for very long though, because Jongsu dive-bombs him a second later, and Lei, deciding it looks fun, follows suit. Minseo makes a strangled noise as he gets buried."
     "I laugh watching them and then start to rummage in the drawers under the TV."
     m "What do you want to play?"
     "There's no response, and when I look behind me, Quentin has joined the pile. I roll my eyes and chuck a convenient cushion at them."
     m "Hey!"
     "Jongsu's head pops out, and he looks at me remorsefully, though his eyes brighten when he sees the games I'm holding. He wiggles his way out of the pile and rolls his way over to me, landing neatly, though his hair is in disarray."
     m "What do you want?"
     j "Hmm... what do you want?" #chinese
     "I blink at him in surprise for a second because his response wasn't in Korean, but in Chinese."
     m "You speak Chinese?" #chinese
     "He shrugged shyly, taking some of the games from my hand and flipping them over to read the backs."
     j "Just a little. We do tours there almost every year, and I try to learn when I have time." #chinese
     m "...Do you have any time? Li used to visit me like every summer and the holidays, and he hasn't in years cause of Phantasy." #chinese
     "Another shrug, and he looks up at me. Even this close, his skin looks flawless, and he has the loveliest eyes, smoked mahogany and warm with the traces of fire."
     j "It's worth it to hear the fans happy." #chinese
     "There is a crash behind me, and when I look, the other three have fallen off the couch, followed by two of the sitting cushions."
     l "Mimi, help!"
     "They are jammed between the couch and the coffee table, which has scattered cards and mugs across it. Rolling my eyes, I get up and carefully edge the table back so that the three can untangle themselves and get to their feet, faces flushed."
     "By the time I turn back, Jongsu has picked a game and is handing out controllers, of which there are only four."
     q "I can sit out this round. I'll take loser's spot?"
     "We readily agree. Minseo, Quentin, and Lei take their spot on the couch after they repair it, while Jongsu and I get settled on the one facing the TV."
     "The game Jongsu has picked is a fairly straightforward racing game, with the usual power-ups and debuffs. I manage to eke out a not losing position in the first few rounds, but once the field changes to one where there aren't walls on either side, I spend most of my time being picked up and placed back on the track."
     "At the end of the round, I am terribly exasperated, but I surrender my controller with an eyeroll."
     m "At least I can drive in real life."
     k "I don't think there are giant mushrooms in the road in real life."
     m "...Crush him, Jongsu."
     "Jongsu laughs and then turns his controller so he rams into Minseo just as they're rounding an unguarded corner. Minseo looks on in mild horror as his cart flies off the screen."
     k "Hyung! Why! Betrayal!"
     "We switch out for a puzzle game next and then one involving deactivating a bomb, which turns around very interesting because during moments of panic, everyone just reverts to their first language, meaning there's a lot of multilingual yelling going around."
     l "The red wire, the red wire!"
     k "There isn't a red wire!" #korean
     m "No, it's black, then yellow! He said there's no -"
     "{i}BOOM{/i}"
     "We all turn to gape at the screen, and then I flop over, throwing my arms up and nearly hitting Jongsu in the face."
     m "God dammit, Lei."
     l "Whatt. It wasn't my fault."
     q "That was stressful." #korean
     j "It was. I thought you would be better at giving instructions."
     m "I was fine at giving instructions. Lei, on the other hand."
     "Sympathetically, Jongsu gives me a pat on the head, and before the bickering could escalate, there is a call from the other room, and then Blair pokes her head out."
     b "Hey. Dinner's ready. Come eat."
     jump firstday_dinner

label firstday_dinner:
     "The smell of the kimchi hot pot burns my nose, but at the same time, it's incredibly fragrant."
     j "It smells sooo good." #korean
     k "It really does." #korean
     s "Let's eat!"
     "Li serves us all, starting with me and then Yejun, who grumbles about how he should be first since he's the oldest. Li points out that Yejun has maybe two months on him, and Yejun sits huffily back as Li continues on."
     "When everyone has been served, we all begin to dig in."
     s "Omigod, this is so spicy."
     m "Isn't it great?"
     r "I'm dying." #korean
     "Snorting with laughter, Blair hands him a tissue to wipe his face, which has turned bright red."
     q "Water, where's the water?"
     "There's scrambling for a few minutes until everyone gets settled. Like everyone else, I'm sweating, but it's a nice heat and tasty besides."
     "After dinner, there are lava cakes, prepared carefully, if a bit messily, by Romel and Blair."
     m "This is really good. You have a gift, Blair."
     b "Thanks. Romel did most of it, actually. Please don't talk with your mouth full. It's gross."
     "I make a face at her and offer the remaining quarter I have left to Li, who shakes his head. Jongsu takes it at the offer and woofs it down, leaving a spot of chocolate at the corner of his mouth."
     "Grinning, I grab a napkin and swipe at it."
     "After dinner comes some relaxing in the living room, where Romel, Jongsu, and Lei have an impromtu dance battle and then the two begin to teach Lei one of their more recent dances, before I catch Sunny yawning."
     "A second later, I yawn as well, and I see Quentin yawn less than 30 seconds later."
     m "Okay. I think it's time for bed. For me, at least. Hey."
     "I tug on Li's sleeve, give him a hug."
     m "Good night. I'm looking forward to the summer." #chinese
     "He beams at me, and I head towards the stairs."
     
     if romance_points >0:
        "Before I can make it, Jongsu catches my arm, and I stop to look back at him. His hair is mussed from the dancing, but he still looks fresh-faced and energetic."
        j "Good night, sleep tight."
        m "Thank you."
     else:
        "It's gonna be a fun summer."

scene black

centered "Chapter Four: {w=1.0} Meetings"
$ renpy.pause (1.0, hard=True)

show white

"I am drifting in a sea of white when I become aware of a yelling in the distance. It gradually grows closer, and then -"

h "Mimiiiiiiiii!!!!!"

"My eyes fly open as at the same time the door to my and Sunny's room flies open, and Li bursts in, far too awake for the time of morning. I grab my pillow and chuck it at Li. It hits him in the face, and as soon as it drops, Sunny's pillow hits him as well."

"I can't help, but snicker. Sunny, unlike Blair and I, is much harder to annoy, but then, early mornings are hard for everyone."

"From beneath the pillows, I hear a moan."

h "Wh-why, Mimi?" #chinese

"I check my phone."

m "It's 8AM on the first day of summer break. Let me {i}sleep{/i}." #chinese

"There's a groan from the other bed that tells me that Sunny agrees with me a hundred percent."

"Jongsu and Quentin poke their heads in, see Li on the floor, and then duck out again."

m "Seriously, get out." #chinese

"From the door, there is a muffled sound and a clearing of a throat."

q "There's actually something... well, you know the TV show? Our managers wanna talk to you."

m "Oh. My. God - NOW?!"

q "They're waiting in the dining room."

m "...Go wake up Blair. If she gets up, I'll get up."

"I throw myself under the covers, fairly certain that the task is impossible. However, less than five minutes later, the covers are yanked back viciously by a very grumpy looking Blair."

m "Wha - How -"

b "Romel promised me cupcakes. Get up. Let's get this over with."

"I blink, disoriented, as she goes and does the same to Sunny, and then when she starts to make her way back to me, I scurry out of bed."

"There are actually a couple managers waiting downstairs, who both look far too awake for this time of morning. The four of us are in various stages of liveliness. Lei and Sunny are both quietly sleepy, while I am rumpled, and Blair looks like she is being run exclusively by anger."

"Manager #1" "Hi, it's nice to meet you guys. We're going to be taking care of the show."

"They introduce themselves, though the names completely escape me."

"Manager #2" "We're sorry to get you up so early, but we just wanted to talk about some things before we officially got started with filming."

"One of them hands over four copies of large stacks of paper, which seems to be guidelines to filming. I flip through it without really seeing it as they keep on talking. Most of the conversation is just them clarifying what the show is and how they're going to go about filming it."

"They want to publish it online via a Youtube channel, with lessons being filmed for the first three weeks or so and then published every Monday and Friday."

"Manager #1" "It should go on for about three months, and we'll start uploading next week, assuming we're ready."

m "And the rest of the time is just free time?"

"Manager #2" "Well, we hoped that we might be able to convince you to vlog about your vacation, both during the filming and afterwards, and we'll upload it to another channel. It'll be good exposure for both you and Phantasy. What do you think?"

"Out of the corner of my eye, I see movement, and when I glance to the side, I can see figures ducking out of sight. The guys are eavesdropping."

l "...It might be fun..."

s "But it'll be kind of creepy."

b "I don't really like that. I kinda don't want to feel like everyone is watching me all the time."

s "Yeah!"

m "Yeah, I'm not too big a fan either."

"Manager #1" "May I ask why?"

menu:
     "It's an invasion of privacy.":
          m "Well, it's an invasion of privacy. This is supposed to be a vacation for us, and I'm with Blair. I don't want people tracking me. I'm okay with the English lessons, cause that's controlled and scripted, but... not this."
     "Phantasy deserves a break.":
          $ friendship_points += 1 #max = 5
          $ romance_points += 1 #max = 2
          m "I haven't seen Li in years cause he's always working so hard with Phantasy. Phantasy deserves a break. They all work really hard. And they can't really relax if they're going to have to keep their faces on all the time for the vlog. I don't want to do it."

"They looked disappointed, but nod their nods."

"Manager #2" "Alright then. We'll start filming this afternoon. It's a pleasure to finally meet you four."

"Both of them shake all four of our hands, and then they depart after a brief conversation with Yejun."

"As soon as the door closed, Sunny let out the biggest yawn."

s "I'm going back to bed."

b "Yes. Good idea."

m "Lei?"

"Lei yawned as well, but shook her head."

l "I'm awake now. I'm hungry. Did you guys buy apples yesterday?"

b "I think so. Check the fridge."

"The two trudge upstairs, while Lei bounds over to the kitchen at about 3/4 full energy. I follow her, stifling my own yawn. Why do they have to be so contagious?"

"Li is cooking up something on the stove when we walk in. He pats Lei on the head and hugs me with one arm."

h "Thanks." #chinese

"His voice is quiet, low, and for a second, I think I misheard."

m "What?" #chinese

h "For saying no to the vlogging. It'll be nice to actually take a break without cameras. I'm excited." #chinese

m "I am, too. Do we have plans?" #chinese

h "Not really. We'll find something though. Or we can just relax here. It's nice to get a break." #chinese

"He grins at me and nudges me."

h "Go find plates. Yejun is going to be up soon, and he'll complain if he doesn't have breakfast." #chinese

m "Oh, so this is all for Yejun? What about the rest of us?" #chinese

h "You'll come up with something." #chinese

"Rolling my eyes fondly, I rummage in the cabinets until I find enough plates for the six of us who are awake, since Blair and Sunny went back to bed, and I've yet to see Romel or Minseo."

"I set up the plates in the dining room, Li comes in five minutes later with the food - egg fried rice - and half a minute after that, Quentin, Jongsu, and Lei come rolling in."

m "You guys are like dogs to slaughter."

q "I don't think that's what the expression is."

"I wave him off, digging into the food."

h "So Mimi brings up a good point. What do you guys want to do after filming is done?" #korean

l "Amusement park?"

m "That's like a one day thing, though."

l "We could spend like a week there."

m "...Yes, but who wants to?"

l "I do. What do you want to do?"

menu:
     "Hiking.":
          m "Mmm... what about hiking? We could do like a camping trip or something like that."
          l "Eww, peeing out doors."
          h "I think it would be fun. There are some really good trails around here, I think." #chinese
          m "And, it wouldn't involve roller-coasters either."
     "Go to the beach.":
          m "I think I'd want to go to the beach."
          l "Ooo, that would be fun."
          h "Mimi, you're being so cliched. That's what everyone says." #chinese
          m "The beach is awesome. You can sit in the sun and relax or swim or walk along the boardwalk or just stare at how unbelievably large and wonderful and vaguely terrifying the ocean is."
          $ romance_points +=1
          j "I love the ocean. It can make all your problems seem so small." #korean
          "The first part is in English, but the second part is in Korean, his voice dropping a little. I glance at him, and his eyes are a little wistful, but he smiles when he sees me looking, expression still soft."

"We continue to discuss ideas - there are also suggestions to do touristy things, since it is some of their first time in the US - and we're still talking when Yejun comes down and even, way later, when everyone else gets up."

"At that point, most of us clear out the kitchen, though Quentin opts to stay behind with Sunny complaining that we didn't leave her any food as Romel sleepily rummages in the fridge."

"We try to go to the living room, but there's a camera crew setting up in there, so we wander around, pausing briefly in the study, which has a bookshelf with no books and a beautiful desk with no chair."

"Jongsu and Li fight briefly over who gets to sit on top, while Lei and I discuss what books the bookshelf should have and then discover that there is actually one book: the Bible."

"There's a nice sun-room near the back of the house, with a patio, but there are crew members back there, too, so the four of us scurry upstairs. Lei chooses to go harass Minseo, and I consider for a moment doing the same for Blair, but then I decide that I value my life too much."

"With a very sleepy Minseo in tow, we find the door to the attic and make our way up there. I find the window that I saw yesterday and peer out it at the driveway and the presence of the crew cars."

m "Do they really need that many people to film us teaching English?"

k "Oh, I forgot that was happening today."

l "In the afternoon."

m "But I guess it doesn't matter for you, cause you aren't going to be involved right."

"He grins a little smugly."

k "Yep."

l "How did you convince them your English wasn't good enough? It's sooo good."

k "But they don't know that."

l " You're speaking in English right now! I'm gonna tell them."

"They go back and forth as I turn to Li and Jongsu and switch to Chinese."

m "Are you guys looking forward to learning English?" #chinese

h "It's going to be so much work." #chinese

j "I think it'll be fun. We're going to start touring here next year." #chinese

m "Yeah? That's really awesome. Lei will be super excited." #chinese

j "Not you?" #chinese

"He smiles shyly, absently running a hand through his hair."

m "Mmm... concerts aren't really my thing." #chinese

h "Mimi! Are you saying you wouldn't come see me perform?!" #chinese

"I give Jongsu a look, which I hope gets across my message that I am blaming him for what's happening. He grins full out now and shrugs his shoulders."

m "I'd come, I'd come." #chinese

"Around two, Sunny comes up to get us so we can start filming. We go off in pairs, starting with me and Lei introducing ourselves to the camera and then Sunny and Blair."

"Yejun is staring at me in mild disgust when the director calls cut."

m "What?"

y "What happened to your voice?" #korean

m "Huh?"

"Before I come to an understanding of what he means, Lei butts in."

l "It's her teacher voice. So that they'll think she's {i}sweet{/i}."

"She wrinkles her nose in disgust, and I elbow her."

m "I am sweet to them."

"Yejun makes a face and walks away to film his intro with the rest of Phantasy."

"The plan is to film eight 20-minute episodes every week, which doesn't sound so bad at first, but by the end of the first week, I'm fairly exhausted and have reverted to my normal voice. It startles the managers at first, but they don't say anything about it, so I just continue on with it."

"The first episode is put up on the second day of the second week, and Sunny and Lei make me watch it with them, even while Blair insists that she doesn't want to watch herself."

"It's less cringe inducing than I thought it would be, but I still can't listen to the sound of my voice for more than a couple minutes before I fight my way out of the room."

m "Ugh. Gross."

scene black

centered "Chapter Five: {w=1.0} Extracurriculars"
$ renpy.pause (1.0, hard=True)

show white

"Phantasy works hard at their English both during filming and afterwards, with Quentin and Lei giving addition lessons. Minseo, Sunny, Blair, and I help out pretty often, but none of us are as good as the other two at both English and Korean, though Blair is learning fairly quickly."

"The morning after the first episode goes up, I wake up when the sun has barely cracked through the window, quite a feat since it's almost full summer."

"Quietly, I sneak out of bed and make my way downstairs. Everything is terribly quiet and peaceful at the same time. I look in the fridge, make a face at the apples, and then wander out of the kitchen."

"I wind up in the sun-room, settling in at the window ledge. It holds an almost perfect view of the sunset, hampered by one little tree that was probably planted after the house was made."

"There are padding steps behind me, and Jongsu steps into the room, yawning. He pauses when he sees me and then smiles, early morning light streaking across his face."

m "Good morning."

j "Good morning. It's early."

m "...I woke up. I can't fall back asleep when I wake up."

"He sits on the window ledge, leaning against the other wall so that he is facing me and pulls a leg up to his chest."

j "Are you having fun?"

m "Yeah. Of course. I mean - it's tiring, but it's fun."

"I look at him, wondering what to ask him in return."

menu:
     "What do you want to do today?":
          j "Hm... well, Romel bought some watermelon yesterday."
          m "Ooo, watermelon smashing?"
          "His eyebrows wrinkle up, and he mouths the words back at me. He's been picking up English fast, having put in more work than almost anyone."
          m "It's a game. You put the watermelon on the ground and then you blindfold someone and spin them around, give them a bat, and have them try to break the watermelon." #chinese
          "It takes a couple more tries to get him to understand what I'm saying, as even his Chinese finds it difficult to keep up, and my Chinese is just barely good enough as it is, but when he gets it, his eyes light up, and he laughs."
          j "Isn't that a waste of watermelon?" #chinese
          m "It's a creative way to eat watermelon." #chinese
     "Are {i}you{/i} having fun?":
          $ romance_points +=1
          "His eyes flicker a moment, as if in surprise, but his expression fades back to his normal, cheerful smile after a moment, and he nods."
          j "I like it. We all spend a lot of time together, but not that much when we aren't working. We're all busy."
          m "Yeah, Lei mentioned that. Minseo acts, and Yejun hosts."
          j "Yeah, we all have a lot of activities."
          "He pauses for a moment, hesitating."
          j "It can get lonely." #chinese
          "I blink at him and then reach out and nudge his foot with mine. He looks away from the sunrise and smiles, and there is sunlight caught in his gaze."
          j "I'm glad we got to meet you. Li's told us a lot about you. He really loves you." #chinese
          m "I love him. He's my older brother. Even if it's not by blood." #chinese
          j "Thanks for asking about me." #chinese
          m "Yeah, of course. I hope we keep having fun."
          "He lays his leg flat so that it's pressed against mine, and we watch the sunrise."

"When the sun is a few inches above the horizon, we hear the first sounds of activity. Li is first down, active as he always is. He greets me with his morning hug and then asks if I want to go on a morning run with him."

m "Oh God. No. Never. I only run for volleyball, and even that, I do with the utmost reluctance." #chinese

"Jongsu perks up at 'volleyball', and for a moment, I imagine him as a dog with a wagging tail."

j "Volleyball? You play volleyball?" #chinese

m "We all do. It's how we met. Well, it's how I met Sunny and Lei. Blair went to my middle school." #chinese

j "Let's go play!"

m "...Uh... is there a place around here?"

j "Yeah! There's a gym nearby that has a court. Let's go." #chinese

"He starts to drag me upstairs, presumably to get the others. I look over my shoulder at Li, who shrugs and grins."

m "Do you play?" #chinese

j "No, but you can teach me. I play soccer."

m "...Yes, those two are very interchangeable."

"He finds little success rousing Blair or Lei, who has the protection of Blair being in the same room, but manages to get a very sleepy Sunny up and then proceeds to wake the rest of Phantasy. Yejun refuses outright, Minseo equivocates, but Romel and Quentin both agree."

j "And with Li, that's four of us, and four of you." #chinese

m "So we can play quads. I wouldn't recommend it though. We were second in the state last year." #chinese

j "Ooo ~ So you're good."

m "Eh."

"It takes another half hour to get Lei up and only with alternating persuasion from Lei, me, Romel, and Jongsu does Blair finally roll out of bed and get herself ready."

"It's a short walk in warming sunlight outside to the gym, and luckily, it seems pretty empty. Most of the early morning people have already gone to work, so we have the court, at the very least, to ourselves."

"Li forces us to jog to warm up, completing several annoying laps, and then Sunny and I start teaching the guys how to pass - the most fundamental skill - and set (less fundamental, but still important) while Blair and Lei warm up their arms."

"When they're finished, I go to pepper (a combination of pass, set, and spiking between two people without a net between them) with Lei while Blair takes my spot with Sunny, starting them on spiking or hitting the ball."

"About two minutes in, I glance over, and the guys are all staring."

m "What?"

"Minseo, who tagged along, but isn't participating is the one who finally responds from the corner, where he's sitting on his phone."

k "How are you not dead if she hits at you like that?"

"I look at Lei in mild confusion. We have been peppering partners for a long time, though I did have a vague understanding that most people found Lei's hits, wild at the best of times, scary."

m "It's good for both of us. She warms up her arms, and I get to practice digging."

"There's more staring."

r "...I don't wanna play against her." #korean

q "Me either."

s "You shouldn't. She's scary."

l "I'm not scary! Blair hits well."

k "Sure, but Blair doesn't look like she's going to kill someone every time she hits."

m "Yeah, only half the time."

b "Shut up, Mimi."

"We practice a little more until all of us are feeling warm, and then we split so that Lei, Sunny, Jongsu, and Romel are on one side with Blair, me, Li, and Quentin on the other, as Minseo takes the reluctant position of referee, even though he clearly has no idea what's happening."

"Though there are actually a few good rallies, most of the runs end in Jongsu and Romel running into each other or Quentin or Li running away from Lei's hits."

q "It's a bomb!"

b "It's not a bomb, just get behind it!"

m "Quentin, just duck, and I'll get it."

q "But if I duck, it'll hit me."

b "You're not ducking right!"

h "Mimi, this is scary. You have scary friends."

m "You invited them on this. I take no responsibility."

"From the other side, Jongsu, Romel, and Sunny are cheering. Out of vengeance, I serve the ball straight between Romel and Jongsu, who watch it drop between them and then begin arguing over who should have gotten it."

"The game ends rather climatically when Lei hits a ball way out of bounds, and it flies towards the door to the gym as it slides open, smacking the newcomer in the face. The ball drops down, and the newcomer's head drops down -"

h "Oh no. Yejun."

s "Lei!"

l "It wasn't on purpose!"

r "Run!"

"We break in a giggling mass and charge out as Yejun roars after us. In the end, he only catches Romel, who takes the wrath of the hit, eventually being rescued by Blair and Li."

scene black


centered "Chapter Six: {w=1.0} Lessons & Escapes"
$ renpy.pause (1.0, hard=True)

show white

"A couple days later, Li decides that those aren't the only lessons we need to work on."

m "Chinese?! Why?!" #chinese

h "Because your Chinese has gotten very bad over the years, and I promised your parents that I would. That was one of the conditions to letting you come." #chinese

m "...You're kidding."

"He grins at me and starts pulling out textbooks and notebooks with Chinese characters on them. I look at them and groan, because I thought I had buried them in my basement where they couldn't be ever found."

"That's how my days proceed for the next week. About halfway through, I discover that Sunny and Blair are getting Korean lessons from Quentin and Romel, though they ask for the lessons, so my resentment towards Li doesn't really die."

"Deep down, I understand that it'll be a good skill, and my Chinese really could use work, but not so deep down, I just want to laze around."

h "Mimi! Wake up!" #chinese

m "Wah!"

"I jerk up, my head having fallen to the table before me. I glare at Li, who just smiles amicably at me and taps on the book in front of me. We're doing traditional poems that day, which feels more useless than anything else, but it's good for enunciation, which I need 'a lot of work on'."

"Feeling vaguely defeated, I recite the next one down. Li gives me corrections, and I try it again. As I'm going through the third time, Lei wanders in."

l "Li, do you know where the cord is for connecting the TV to the laptop? I wanna practice {i}Rain{/i} on a big screen."

"She names a song from Phantasy's most recent album, which I have by this point listened to enough times to be able to actually recognize most if not all of them."

h "It should be downstairs in the cabinet."

"He stands up to go downstairs with Lei. I let my head drop back to the table, but before a minute even passes, the door bursts open again, and Jongsu springs in. I jump up, surprised."

j "Mimi! Let's go!"

m "What? Go - go where?"

"He holds out his hand and gestures urgently."

j "Trust me!"

menu:
     "Hesitate.":
          m "I... don't know. Li wouldn't be really happy."
          j "Hyung will understand. Come on. It'll be fun, I promise."
          "I hesitate for a moment more, but finally get up and hurry out of the room with Jongsu."
     "Take his hand.":
          $ romance_points +=1 #max = 5
          "I reach out and grab his hand. Jongsu hauls me to my feet, and for a moment, I almost stumble, but his grip steadies me."
          "A grin splits his face, and he runs with me out of the room."

m "Where are we going?"

j "You'll see. We gotta go fast, though."

"We sneak down the stairs and then go charging out of the house as soon as we're clear of Li, who is helping Lei find her thing. She gives us a face as we run out, so I have a feeling whatever he's looking for is stashed upstairs where Li would never look."

"He catches sight of us just as we make it outside."

h "What - MIMI!"

j "Runrunrunrunrun!"

"I do so, charging out and then hopping into the car that is waiting outside. Minseo, in the driver's seat, makes a peace sign at me. About five seconds later, the door to the front swings open, and both Lei and Li come charging out, Lei in front. She also dives into the car, and Minseo steps on it, leaving Li behind."

h "MIMI! YOU GET BACK HERE!" #chinese

"A few seconds later, my phone rings, then Jongsu's, and Minseo's."

m "At least, he doesn't have yours, Lei."

"She grins, still breathing a little hard from her all out sprint. Meanwhile, Jongsu has picked up his call."

j "You've been working her so hard. She deserves a break." #korean

j "Yeah, I get that it's important, but so is relaxing! Come on, hyung!" #korean

"There is some more furious discussion that Lei doesn't translate, as she is now chatting animatedly at Minseo."

l "There's a fair in town."

m "Is that where we're going? Are Sunny and Blair not coming?"

l "They said they wanted to go another day."

j "Come on, hyung!" #korean

"There is a pause and then Jongsu gives me a huge grin."

j "Thanks, hyung. I knew you'd understand." #korean

"He hangs up the phone and gives me a victory sign. I can't help, but grin back at him."

j "Crime accomplished."

m "...You know, I'm concerned you learned to say that in English." 

"We arrive at the fair about 20 minutes later, white tents spread all around and a ferris wheel in the distance. It's spinning idly, most of the seats empty at this point."

k "Where should we start?"

l "Games?"

menu:
     "Games!":
          $ friendship_points +=1
          m "Games!"
          l "Games!"
     "Uh...":
          m "I don't know. I'm not really feeling it."
          l "Oh come on, Mimi. Please?"
          m "...Mmm, alright."

"Lei cheers, and we go off to buy tokens at a rate that makes me wince, and then it's off to the metaphorical races."

"I turn out to be a pretty good shot and manage to win a small, stuffed cat that I bestow onto Jongsu when I get tired of holding it."

"Lei completely crushes Minseo at the obstacle course when he gets tangled in the ropes and then just gives up, which results in a lot of complaining from Lei that it wasn't a 'real win'."

"There's a girl juggling knives at one station. She grins at us between throws, tosses all the knives high up, spins in a tight circle, and continues juggling, prompting a lot of cheering. She stops to talk to people every now and then, the knives coming down to a casual distance that still scare her companions."

"Knife Juggler" "Thank you for watching guys! We're going to be doing a knife throwing show here later. Come see what an amazing markswoman I am!"

"She waves between throws, catches two knives, throws them, catches a few others as those two are in the air, and bows with a flourish of the knives like a fan, before coming up and catching the rest. She bows again and then waves one more time."

m "Wanna get some ice cream?"

l "Yeah!"

j "Sounds yummy."

k "I could go for ice cream."

"The guy running the ice cream stand also seems to be a performer, as he throws the ice cream up into the air and juggles it before handing it over the counter. Jongsu gasps when he pretends to drop it, looking as terrified as some of the children that I just burst into helpless giggles."

j "What?"

menu:
     "You're cute.":
          $ romance_points +=1
          m "Nothing. Nothing. You're just - you're cute."
          "Slowly, a grin spreads over his face, and he thanks the ice cream guy when he finally hands over the cone. He presents it to me with a flourish as dramatic as any of the performers have been."
          "Unable to stop my smile, I give him a small bow and accept it."
     "You look like a kid.":
          "He pouts, which just ups the resemblance."
          m "Not in a {i}bad{/i} way. Just a - well -"
          "He sulks for a moment more until he gets his ice cream, and then he brightens again. I roll my eyes as the ice cream guy starts the same thing with my cone."

"We stop by a face painting booth so that Lei and Jongsu can get butterflies on their face. After some persuasion, Minseo gets a dragonfly, and I choose a small cat under my right eye."

"Almost immediately, I get the urge to itch the spot."

m "...Don't do it, Mimi. Don't do it."

l "Want something deep fried?"

m "Yes. Anything to take my mind off this."

"She looks at me, frowning, head tilted to one side."

l "What's wrong with it? It suits you. You're just like a cat."

m "Thanks. Cats are magnificent. But apparently, they're very itchy."

"She nods her head wisely."

l "That's cause of all the fur."

m "I hate you."

"Lei sticks her tongue out at me and then runs after Minseo, who is now looking at the lunch options, most of which are fried in enough oil to probably cook one of us."

"After lunch, I lie back on the bench, feeling completely stuffed."

j "Mimi, are you okay?"

"His head appears above mine, eyes wide in mild concern."

m "No. Just leave me to die here. I'm going to turn into a sphere and melt into fatty acid chains."

j "That doesn't sound fun."

m "It's probably not. It's just punishment for eating your own weight in deep fried things."

j "You won't be punished for enjoying yourself."

"He offers me part of a churro, sugar powder drifting off his fingers."

m "You're trying to kill me, aren't you?"

j "It's good! You should have some. It's so sweet."

m "That's 'cause it's nothing, but sugar."

"Not so reluctantly though, I lean up and bite the piece out of Jongsu's hand. He waits for me to chew and then offers me another one. I glare at him."

m "You're just trying to fatten me up."

j "You'd look cute as a sphere."

"He beams, ducks when I throw the next piece at him."

l "Mimi! Don't waste food."

m "Do you - do you see what he's - okay, fine. Sorry."

"I grumble and slowly rise to my feet, stretching. The sun, by this point, is blistering, and I'm sweating just standing."

"We hide from it under one of those shower mists that are a huge waste of water, but are always blissfully cool. There's a water balloon fight later in the day, which we participate in and are terribly successful, even if we leave it completely soaked (like most of the population)."

"When the sun has started to think about setting (though we all know it won't for another two hours at least), we're winding down, feeling lazy and warm. Lei and I are leaning against each other on a bench, Minseo to one side, Jongsu tossing some trash."

k "Do you want to go on the ferris wheel?"

"His tone is casual, but he glances at Lei, who obliviously fails to notice. I roll my eyes and nudge her."

m "Ferris wheel?"

l "Yeah, that sounds fun!"

"She bounds towards the giant wheel, and I smirk at Minseo."

m "You're welcome."

k "Shouldn't I be saying that to you?"

m "What?"

"He raises an eyebrow at me and then follows Lei towards the ferris wheel."

j "Oh hey, are we going on the ferris wheel?"

"I glance behind me to see Jongsu has returned from the trashcan. He tugs at the collar of his shirt absently."

m "...Yeah, let's go."

if romance_points > 4:
     "We follow them up to the ferris wheel and wait until the next cart comes. Jongsu takes the open door from the ride conductor and bows to me. Rolling my eyes, but unable to stop a grin, I step inside and scoot to the side so that Jongsu will have room."
     "He hops in after me, and we begin our slow descent to the top. As we go, we catch sight of the sights that we'd spent the day enjoying."
     m "We should tell Blair about the churros. She would love them."
     j "Romel would, too. They can come together."
     "There is suddenly warmth to the side, warmer even than the summer day, and Jongsu's head rests on my shoulder. His eyes have fluttered closed, and his eyelashes are casting shadows on his cheekbones."
     "I watch him for a moment, redness gathering in my cheeks. Finally, as we reach the top, I lean my head on top of his and close my eyes as well."
     m "Hey. This has been... really fun. Thanks."
     "He hums appreciatively in his throat, and I let out a breath, allowing the summer air to wash over us."
elif friendship_points > 4:
     "We follow them up to the ferris wheel and all crowd into the same cart, shifting around until our cart sways unstably, Lei is giggling, and the conductor is glaring at us."
     "He closes the door behind us with an audible snap, and then we begin to lurch upwards."
     "The sudden movement sends Lei tumbling into me."
     m "Ah! Help! I'm being crushed."
     l "It's not my fault! It started really quickly!"
     m "Still being crushed, Lei."
     j "Hey, look! You can see that girl with the knife from here."
     k "Is she still going?"
     j "Yeah. She was so good. It was scary."
     m "I think that's the point."
     "We chatter incessantly as we rise upwards, a warmth rising in my chest as we go. I am full and comfortable and with friends who I care about more every single day."
     "Maybe I should thank Li."
else:
     "We follow them up to the ferris wheel and all get into the same cart. We go up slowly and gently, taking in the sights."
     "Everything looks like it is touched with fire and maybe just a bit of magic. I spot a balloon artist, who is currently making a giant pile that looks vaguely like a Golden Retriever."
     "Though I know that I will soon have to go back to learning with Li, I find comfort in having gotten this break. And besides, it isn't as if Chinese isn't useful."
     "We take several trips around the wheel, and when we step off, my entire mind feels lighter, and I feel ready to face whatever the world might throw at me."

scene black