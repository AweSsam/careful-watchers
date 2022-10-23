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
define ag = Character("Agatha")
define q = Character("???")
define kmom = Character("Kurt's Mom")

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
    xalign 0.35
    yalign 1.0

transform slightright:
    xalign 0.65
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
    subtitle "After our protagonists solved their very first mystery at their own school, they decide to start an agency. {w}Now the hardest part is deciding the name."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "classroom.png" or "classroom.jpg") to the
    # images directory to show it.

    scene classroom
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "AJ happy.png" to the images
    # directory.

    show aj at slightleft

    # These display lines of dialogue.

    a "How about... {w}{i}The Careful Watchers.{/i}"
    subtitle "This is AJ, otherwise known as Ajay Sharma. {w}Someone always pronounces his name wrong, hence the nickname."
    show kurt at slightright
    k "How about... {w}an award for the world's stupidest detective agency name?"
    subtitle "Kurt. {w}Her last name? {w}No one knows."
    a "It's not dumb, it's clever. {w}Mysterious. {w}{i}Careful.{/i} {w}Unlike anything you've ever seen before."
    show moe at right
    m "Yeah it fits that last category pretty well."
    subtitle "Moe \"Makoa\" Carter. {w}Overwhelming fondness for cats and nothing else."
    a "Think about it! {w}Has there ever been anything weird or suspicious going on in Esteredge? {w}No."
    k "Which is why I don't understand why we're starting this agency in the first place? {w}Solving one thing doesn't mean we need to solve a thousand others."
    a "All good quests take a little bit of digging. {w}Maybe our town just needs some real careful watching if we ever really wanna bring justice to the table and uncover truth. {w}Right?"
    show christie at left
    c "Hmm... {w}You're not wrong."
    subtitle "Christie Castillo. {w}Her and Moe are the smartest ones in the group, if you couldn't tell."
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

    show aj at slightleft
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

    show aj at slightleft
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
    scene dinerafternoon

    show aj at slightleft
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

        scene dinerafternoon

        show demployee

        de "How can I help you? {w}Table for four?"
        k "We're looking for Agatha, owner of Agatha's diner?"
        de "Umm... {w} I'll call for her. {w} What's your relation to her?"
        k "Ene-"
        c "Haha, she means, we're just looking to ask some questions."
        de "Hmm...{w} ok.{w} I'll be just one second."

        scene dinerafternoon

        show agatha

        a "Hello? {w} You said you were looking to ask some questions?"
        c "Yes, thank you for coming to meet us!"





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
                
                scene dinerafternoon
                
                show demployee

                de "How can I help you?"
                c "Hi! Can we ask you a few questions about any missing deliveries?"
                de "Missing deliveries? {w}We haven't had any missing deliveries here. {w} At least as of {i}now.{/i}"
                c "Hmm."
                menu:
                    "What do you mean by that?":
                        jump agathasbegmean
                    "Well have you heard anything about any missing pies?":
                        de "Hmm... yeah, I know {b}Bake n' Take{/b} is having their run with those. {w}Sorry, but I don't really know much else about that, so I can't help you."
                        de "And I'm not really on break right now, so I have to go."
                        show demployee
                        de "What is this for again?"
                        a "We're detectives, part of the Careful Watchers!"
                        m "He means, we're investigating the missing pie deliveries in the downtown mart."
                        de "Right. {w}The Careful Watchers huh?"
                        jump agathasbegmean2


    if cat: 
        m "My cat loves pancakes. {w}The cat {i}must{/i} be here."
        a "Are cat's even allowed to eat pancakes?"
        m "Probably? My cat's been fine."
        a "Makes sense."

        scene dinerafternoon

        show demployee

        de "How can I help you?"
        c "Hi! {w}We were wondering if you had seen a cat somewhere nearby?"
        a "Gray fur, green-yellow eyes? {w}Also, kinda chub?" 
        de "Oh, sorry, no idea. {w}I barely go outside as is, I'm either waiting on tables all day! {w}The only cats I see are in those cat videos online {w}Sorry to disappoint you."
        
        scene dinerafternoon
        show aj at slightleft
        show kurt at slightright
        show moe at right
        show christie at left

        c "Well that's unfortunate."
        m "I can't believe he wasn't here! {w}"


label agathasbegmean:
    scene dinerafternoon

    show demployee

    de "Well, a few months ago there was someone stealing some of our to-go boxes. {w} Specifically the pancakes..."
    c "Wait, Agatha's does pancake deliveries?"
    de "You bet. {w} We deliver pancakes, hashbrowns, bacon, fries, sausages, ham, our homemade maple syrup, crepes, and a whole lot more."
    k "Of {i}course{/i} you do."
    menu:
        "Which pancakes were stolen?":
            de "Uhh... I think the signature homemade ones. {w}Probably."
            menu:
                "Uh... are you sure?":
                    $ deannoyance = 1
                    show deticked
                    de "I think I am pretty sure. {w}I have to go now, since my coworkers will probably be looking for me."
                    jump agathasbegmean2
                "Anything else?":
                    $ deannoyance = 2
                    de "No, that was it."
                    
        "Did they ever catch who did it?":
            de "No I don't think so. {w}Agatha put out the warning the next week of, and I guess the thief was scared pretty easily cause they never came back."
            c "Oh wow..."
            k "Do you think it had anything to do with the secret ingredient?"
            show deticked
            de "Uhh... I'm not sure I can answer any questions about that. {w}Actually, I have to go, I think a coworker is calling me. {w} Bye!"
            $ deannoyance = 1
            jump agathasbegmean2

label agathasbegmean2:
    scene dinerafternoon
    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if deannoyance == 1:
        m "Well. {w}Wow. {w}That was abrupt."
        k "And not in a good way. {w} I {i}told{/i} you something weird was happening here. {w}It has to be something to do with their secret ingredient!"
        a "Which is {i}not{/i} what we're here for. {w}The deliveries Kurt, the deliveries."
        k "Right..."
        c "The only other place that sells anything to do with making pies is probably {b}Bake n' Take.{/b} {w}Wanna try our luck there?"
        m "Yeah, that sounds like a good idea."
    if deannoyance == 2:
        k "Well we didn't learn anything about any pie deliveries! {w}Only that Agatha's has had their signature homemeade pancakes stolen before too. {w}Of course they would only ever talk about themselves and their own problems!"
        m "Uhh... {w}I'm not sure if that has anything to do with self-obsession but okay."
        c "Hmm... {w}but maybe the two events could be related right?"

    else:
        a "Bake n' Take huh? {w}Should we go there?"
        m "Probably."



label kurtsbeg:
    scene kenempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if ing:
        show kurtopen at slightright
        k "Alright, I don't know why we're here! {w}I told you guys that my family knows nothing about the scheming Agatha and what she puts in her pancakes!"
        c "Then should we leave?"
        menu:
            "Yes.":
                a "Fine."
                jump mapback1
            "No.":
                a "No, maybe we can still gather information."
                scene kensmile
                q "Hi, how can I help-"
                scene kenhappy
                kmom "Oh hey kids! {w}How's your detective agency going?"
                k "Pretty boring mom. {w}We're trying to find out what Agatha puts in her pancakes..."
                c "So we were wondering if you knew, Mrs. Nguyen! {w}Or you knew something about it?"
                scene kenmad
                kmom "Oh I could go on and on about this. {w}Just the other day I saw Agatha at the gorcery store, and we struck up conversation, because of social obligation of course, and she had the audacity to say that she would never tell me what she puts in her pancakes!"
                c "Oh! {w}So no one really knows."
                scene kencon
                kmom "Well no... even if I did I don't think I would go around telling everyone because of respect. {w}Although she's a little stingy about her profits, she does make good pancakes... {w}And it's not like I would steal her recipe and make it!"
                kmom "We're a pho restaurant, not a pancake restaurant."
                k "What!? Mom, what if her secret ingredient was like tasty-{w}tasty poison or something?! {w} It's social obligation to know at that point!!!"
                kmom "If it was tasty poison, half the town would be dead by now Kurt."
                m "Exactly."
                menu:
                    "Wait, then if you wouldn't tell anyone her secret ingredient even if you knew, why would you want to know anyway?":
                        $ friend = True
                        kmom "Actually...{w} me and Agatha {b}used to be friends{/b} back in the day."
                        k "No way! {w}You never told me this!"
                        kmom "It was in college, and we both had our dreams of starting our own restaurants."
                        scene kenmad
                        kmom "Obviously our dreams both came true, but she somehow got the idea that I wanted to start a pancake place as well! {w}As if I would ever start a diner when I could share my own other food with the world!"
                        scene kenmad2
                        kmom "She didn't like the way I said that though, as if apparently the idea of a diner was horrible! {w}But I never even said that!"
                        a "Oh wow. {i}There seems to be a lot of history here.{/i}"
                        scene kencon 
                        kmom "Yeah. {w}And that's why we never talk. {w}Ever."
                        k "I can't believe you kept this from me!"
                        kmom "I didn't keep it from you Kurt, you just never asked."
                        scene kenhappy
                        kmom "But anyway kids, before you go, you should eat dinner!"
                        m "Oh no, we wouldn't want to intrude Mrs. Nguyen."
                        scene kenmad
                        kmom "Nonsense! {w}Kurt was the one who dashed off before telling me that you kids were coming over later today! {w}Now you guys are hungry!"
                        scene kenmad2
                        "{i}They never said they were hungry.{/i}"
                        k "How is that my fault mom?!"
                        kmom "Just sit down and eat!"
                        scene black
                        subtitle "Out protagonists sit and eat after being forcefully made to eat until their stomachs are full by Kurt's mother."
                    "Well, do you know anyone who knows what her secret ingredient might be?":
                        kmom "Hmm... I'm not sure. Maybe {b}Emily{/b} at Bake n' Take knows. {w}She makes plenty of sweet stuff too, and pancakes technically fall under that category?"
                        scene kenhappy
                        kmom "But before you kids go, you should eat dinner!"
                        m "Oh no, we wouldn't want to intrude Mrs. Nguyen."
                        scene kenmad
                        kmom "Nonsense! {w}Kurt was the one who dashed off before telling me that you kids were coming over later today! {w}Now you guys are hungry!"
                        scene kenmad2
                        "{i}They never said they were hungry.{/i}"
                        k "How is that my fault mom?!"
                        kmom "Just sit down and eat!"
                        scene black
                        subtitle "Out protagonists sit and eat after being forcefully made to eat until their stomachs are full by Kurt's mother."

        

    #if deliv:

    #if cat:

    
label bakery:
    scene bakeempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    #if ing:

    #if deliv:

    #if cat:


label taco1:
    scene tacomorning

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    #if ing:

    #if deliv:

    #if cat:
        