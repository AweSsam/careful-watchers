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

define subtitle = Character(
    None,
    window_background = None,

    what_size=40,
    what_outlines=[( 1, "#000000", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')
 
default asad = 0

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
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
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

    scene moes room 

    show AJ at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    scene desk
    with dissolve

    m "Alright Christie, where are our newspapers at?"
    c "Right here!"

    scene desk
    with dissolve

    k "Well we only need the most recent one right? {w}Anything else is mostly going to be outdated."
    c "Oh, well in that case, this is the most recent one."

    scene newspaperdesk
    jump newspaper1
    a "Nice! Let's look through and see if there's anything that we can investigate."

 
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
    scene desk 
    k "I told you there was something fishy about her pancakes! {w}Even the newspapers are writing about her!"
    a "But that doesn't have anything to do with a mystery!"
    k "Umm... yes it does! {w}No one knows what she puts in them!"
    a "So what? {w}Who cares what she put in her pancakes?"
    k "Everyone! {w}The fate of the whole downtown mart is depending on it!"
    a "Ughhh... {w}fine."
    k "Yes!"

label deliveries:
    scene desk 
    a "This could be the work of a real thief out there!"
    k "Really?"
    a "Definitely."
    c "I can see it. {w}{i}The case of the missing pies.{/i}"

label thecat:
    scene desk
    m "Man... {w}I can't imagine ever losing {i}my cat.{/i} {w}We've got to help them."
    subtitle "A unanimous decision is made amongst our protagonists to go rescue the missing cat. {w}Erm. {w}I meant find."
    
