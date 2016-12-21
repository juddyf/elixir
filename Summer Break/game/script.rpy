# NOTES FOR JUDDY:
# Pick a font. Also incorporate fonts? Idk.

# Images
image black = "#000"

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

    scene black
    with hpunch
    
    #Okay, so what I want for this next part is for the text to appear in the center
    #and fade in. That's number one. I don't want it to just suddenly appear. But I 
    #also want the first line to appear sentence by sentence, so "A tackle" first and
    #then "A breath-crushing hug." So I can do one of these and not the other one, but
    #not both simultaneously. the {w=1.0} makes it wait and then appear, but it just
    #appears, not fades in. And the dissolve overrides the other wait??
    
    show text "A tackle. {w=1.0} A breath-crushing hug. {w=1.0}" at truecenter
    with dissolve
    pause 2
    show text "And that was how my summer break began. {w=1.0}" at truecenter
    with dissolve
    pause 2
    hide text
    with dissolve
    
    scene black
    with dissolve

#Title and theme song?

