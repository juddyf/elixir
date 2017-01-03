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

"In the end, we decide to separate into two groups, with me, Leila, Yejun, Li, and Minseo going shopping for clothes, while Sunny, Blair, Jungsu, Quentin, and Romel going shopping for food."

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
