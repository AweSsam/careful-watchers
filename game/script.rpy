# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("AJ")
define a_shout = Character("AJ", what_size = 34)
define a_whisper = Character("AJ", what_size = 18)
define c = Character("Christie")
define c_shout = Character("Christie", what_size = 34)
define c_whisper = Character("Christie", what_size = 18)
define m = Character("Moe")
define m_shout = Character("Moe", what_size = 34)
define m_shout = Character("Moe", what_size = 34)
define k = Character("Kurt")
define k_shout = Character("Kurt", what_size = 34)
define k_shout = Character("Kurt", what_size = 34)
define e = Character("Eli")
define s = Character("Sandy")
define de = Character("Diner Employee")

define subtitle = Character(
    None,
    window_background = None,

    what_size=40,
    what_outlines=[( 1, "#000000", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')
 
default asad = 0
default deannoyance = 0

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

# The game starts here.

label start:

    scene black

    subtitle "Welcome to Esteredge, a small town where our protagonists reside."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "classroom.png" or "classroom.jpg") to the
    # images directory to show it.

    scene classroom
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "AJ happy.png" to the images
    # directory.

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    # These display lines of dialogue.

    a "How about... {w}{i}The Careful Watchers.{/i}"
    k "How about... {w}an award for the world's stupidest detective agency name?"
    a "It's not dumb, it's clever. {w}Mysterious. {w}{i}Careful.{/i} {w}Unlike anything you've ever seen before."
    m "Yeah it fits that last category pretty well."
    a "Think about it! {w}Has there ever been anything weird or suspicious going on in Esteredge? {w}No."
    k "Which is why I don't understand why we're starting this agency in the first place? {w}Solving one thing doesn't mean we need to solve a thousand others."
    a "All good quests take a little bit of digging. {w}Maybe our town just needs some real careful watching if we ever really wanna bring justice to the table and uncover truth. {w}Right?"
    c "Hmm... {w}You're not wrong."
    k "Uncover what?! {w}The truth about what Agatha really puts in her pancakes to get everyone to only go to her diner and no one elses in the whole downtown mart?"
    "{i}Her parents own a restaurant in the same downtown mart.{/i}"
    a "Uh... no. {w}That seems like a personal problem. {w}Or a street problem."
    c "Can we just get this started already? {w}Moe, your place after school?"
    m "Sure, but what are we even gonna start with?"
    a "As all good mysteries start... {w}with a newspaper."
    c "Ohh, my dad's obsessed with those. We have stacks of them in his office. {w}I can bring them over!"
    k "Sounds good. See ya'll then!"

label moes:

    scene moesplace 

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    scene desk
    with dissolve

    m "Alright Christie, where are our newspapers at?"
    c "Right here!"

    scene newspaperdesk
    with dissolve

    k "Well we only need the most recent one right? {w}Anything else is mostly going to be outdated."
    c "Oh, well in that case, this is the most recent one."

    scene newspage1scene
    a "Nice! Let's look through and see if there's anything that we can investigate."
    jump newspaper1
 
label newspaper1:
    scene desk
    call screen firstpage

label newspaper2:
    scene desk
    call screen secondpage

label newspaper3:
    scene desk
    call screen thirdpage

label ingredient:
    $ ing = True
    $ deliv = False
    $ cat = False
    scene newspage3scene
    k "I told you there was something fishy about her pancakes! {w}Even the newspapers are writing about her!"
    a "But that doesn't have anything to do with a mystery!"
    k "Umm... yes it does! {w}No one knows what she puts in them!"
    a "So what? {w}Who cares what she put in her pancakes?"
    k "Everyone! {w}The fate of the whole downtown mart is depending on it!"
    a "Ughhh... {w}fine."
    k "Yes!"
    
    jump map

label deliveries:
    $ ing = False
    $ deliv = True
    $ cat = False
    scene newspage3scene 
    a "This could be the work of a real thief out there!"
    k "Really?"
    a "Definitely."
    c "I can see it. {w}{i}The case of the missing pies.{/i}"

    jump map

label thecat:
    $ ing = False
    $ deliv = False
    $ cat = True
    scene newspage3scene
    m "Man... {w}I can't imagine ever losing {i}my cat.{/i} {w}We've got to help them."
    subtitle "A unanimous decision is made amongst our protagonists to go rescue the missing cat. {w}Erm. {w}I meant find."

    jump map

label map:

    scene moesplace 

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    a "This calls for map making! {w}The key to any detectives path paving, it's knowing where to go!"
    m "We could also use our phones... {w} or {i}my{/i} phone, because we all know AJ doesn't have one.{w}...but I guess the physical map is more for effect than actual effective{i}ness.{/}"
    a "I'm gonna pretend you didn't say that. {w}...But yeah."

    scene black
    with dissolve
    
    subtitle "Our protagonists go on to make the map. {w}It brings upon conflict within the team.{w} Kind of."
    c "Ajay, you {i}need{/i} to stop writing in all caps. {w}Please. {w}It's stressing me out."
    k "Christie's right. {w}You literally write like my dad."
    a "Your dad must have good handwriting then. {w}{i}*sigh*{/i} {w}Alright fine, I know, I know."
    c "I'm taking over this. {w}I clearly have the best handwriting."
    k "Moe, can't you at {i}least{/i} help with drawing the trees?"
    m "Fine."
    subtitle "Christie takes over, fixing what she can of AJ's mess and adding her flair. {w}Moe's clouds on sticks add great personality to the piece as well."
    subtitle "They finally finish the map."

    scene map1

    a "Alright, now where should we go?"
    
    if ing: 
        k "We need to go to the mart and investigate Agatha's secret ingredient. {w} Let's go!"
        call screen mapbeg
    
    if deliv:
        a "We need to investigate the deliveries! Something about pies?"
        call screen mapbeg

    if cat: 
        m "The poor cat... Where could it be?"
        call screen mapbeg

label mapforward1:
    call screen mapbeg2

label mapback1:
    call screen mapbeg

label agathasbeg:
    scene agathasdiner

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if ing: 
        k "Alright, let's get down to business. {w}We're at the scene of the crime already."
        m "I don't think this qualifies as a crime?"
        k "You're missing the point. {w}{i}*Visible Shuddering*{/i} {w}I can't believe I'm even here. {w}My worst enemy's place."
        m "I'm pretty sure Ms. Agatha has no clue who you are."
        c "Anyway, do you guys think we can get a hold of her? {w}What if she isn't here?"
        a "She's always here!"

        scene agathasdiner

        show demployee

        de "How can I help you? {w}Table for four?"
        k "We're looking for Agatha, owner of Agatha's diner?"
        de "Umm... {w} I'll call for her. {w} What's your relation to her?"
        k "Ene-"
        c "Haha, she means, we're just looking to ask some questions."
        de "Alright, great, I'll be just one second."

    if deliv:
        a "Hmm... pies. {i}Missing pies.{/i}"
        c "Does Agatha's diner even make pies?"
        a "I don't think so."
        c "Then why are we here?"
        m "Should we leave?"
        
        menu:
            "Yes.":
                jump mapback1
            "No.":
                a "No, maybe we can still find something about the deliveries here. {w}Word {i}does{/i} travel fast in Esteredge."
                
                scene agathasdiner
                
                show demployee

                de "How can I help you?"
                c "Hi! Can we ask you a few questions about any missing deliveries?"
                de "Missing deliveries? {w}We haven't had any missing deliveries here. {w} At least as of {i}now.{/i}"
                c "Hmm."
                menu:
                    "What do you mean by that?":
                        jump agathasbegmean
                    "Well have you heard anything about any missing pies?":
                        de "Hmm... yeah, I know Bake n' Take is having their run with those. {w} "           

    if cat: 
        m "My cat loves pancakes. {w}The cat {i}must{/i} be here."
        a "Are cat's even allowed to eat pancakes?"
        m "Probably? My cat's been fine."
        a "Makes sense."

label agathasbegmean:
    scene agathasdiner

    show demployee

    de "Well, a few months ago there was someone stealing some of our to-go boxes."

label kurtsbeg:
    scene kurtsplace

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left
    
label bakery:
    scene bakery

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

label taco1:
    scene tacotruck

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left


    
