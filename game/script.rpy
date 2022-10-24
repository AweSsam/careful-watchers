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
define j = Character("Jose")
define e = Character("Emily")

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
default visits = 1

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

    $ agathasbegvisit = False
    $ kenvisit = False
    $ tacovisit = False
    $ bakevisit = False

    $ friend = False
    $ friendagain = False
    $ obvious = False
    $ strange = False
    $ close = False
    $ answer = False

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
    with dissolve

    # These display lines of dialogue.

    a "How about... {w}{i}The Careful Watchers.{/i}"
    subtitle "This is AJ, otherwise known as Ajay Sharma. {w}Someone always pronounces his name wrong, hence the nickname."
    show kurt at slightright
    with dissolve
    k "How about... {w}an award for the world's stupidest detective agency name?"
    subtitle "Kurt. {w}Her last name? {w}No one knows."
    a "It's not dumb, it's clever. {w}Mysterious. {w}{i}Careful.{/i} {w}Unlike anything you've ever seen before."
    show moe at right
    with dissolve
    m "Yeah it fits that last category pretty well."
    subtitle "Moe \"Makoa\" Carter. {w}Overwhelming fondness for cats and nothing else."
    a "Think about it! {w}Has there ever been anything weird or suspicious going on in Esteredge? {w}No."
    k "Which is why I don't understand why we're starting this agency in the first place? {w}Solving one thing doesn't mean we need to solve a thousand others."
    a "All good quests take a little bit of digging. {w}Maybe our town just needs some real careful watching if we ever really wanna bring justice to the table and uncover truth. {w}Right?"
    show christie at left
    with dissolve
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

    if agathasbegvisit:
        show ajdropopen at slightleft
        a "Here again? {w}Alright then."
        if ing:
            scene dinerafternoon

            show demployee
            with dissolve

            de "How can I help you? {w}Table for four?"
            k "We're looking for Agatha, owner of Agatha's diner?"
            de "Umm... {w} I'll call for her. {w} What's your relation to her?"
            k "Ene-"
            c "Haha, she means, we're just looking to ask some questions."
            de "Hmm...{w} ok.{w} I'll be just one second."

            scene dinerafternoon

            show agatha
            with dissolve

            ag "Hello? {w}You said you were looking to ask some questions?"
            c "Yes, thank you for coming to meet us!"
            k "{i}Agatha herself... we've gotta keep up our guard!{/i} {w}We were wondering why your pancakes, were, err, so good!"
            c "Yeah, everyone's been raving about them recently!"
            show agathahappy

            ag "Haha, I'm always happy to see people appreciate my art! {w}Honestly I just put all of my love into the pancakes, and hope for the best!"
            ag "But I think people forget we specialize in a lot of other things too as well... {w}we make{b} pancakes, hashbrowns, bacon, fries, sausages, ham, our homemade maple syrup, crepes, and a whole lot more.{/b} {w}And all with a whole lotta love!"
            c "Haha, really..."
            menu:
                "Then what about the secret ingredient everyone's been talking about?":
                    show agathatalking
                    ag "The secret ingredient huh... {w}It's certainly a big part but not all of it."
                    k "Then... {w}what is it?"
                    ag "THat's something I've gotta keep to myself kiddo. {w}Not much of a secret if I just told it to anyone who asked me right?"
                    if friend:
                        a "But she's not anyone! {w}She's Mrs. Nguyen's daughter!"
                        ag "Mrs. Nguyen's daughter? {w}"
                        scene dinerafternoon
                        show agathafrustrated
                        ag "She sent over her own daughter to find out what my secret ingredient was? {w}Ridiculous!"
                        k "Hey-"
                        c "Wait, wait, Mrs. Nguyen never sent her over! {w}We're detectives, we came to figure this out ourselves!"
                        show agathamad2
                        ag "Detectives? {w}I assure you, no one's gonna be figuring out what my secret ingredient is anytime soon."
                        c "Thats not what we meant! We uhh..."
                        menu:
                            "Came to resolve the misunderstanding between you and Mrs. Nguyen!":
                                ag "Misunderstanding? {w}I'm pretty sure there's no misunderstanding here."
                                a "No, no, Mrs. Nguyen said she never wanted to start a diner in the first place! {w}She said she would never tell anyone about your secret ingredient even if she knew!"
                                show agathatalking
                                ag "Huh. {w}Then why didn't she just tell me?"
                                k "Honestly, I don't know. {w}Mom didn't even tell {i}me{/i} until today!"
                                $ friendagain = True
                                ag "Well, I guess we have some catching up to do..."
                                jump agathasbegmean2
                            "Came to interview you!":
                                ag "Oh... {w}well, I don't really have time for that, so I'll see you guys later. {w}Thanks for the sentiments about my ingredients but, bye."
                                jump agathsbegmean2
                    else:
                        a "Oh..."
                        ag "Well, kids thanks for the sentiments, but I gotta go now."
                        jump agathasbegmean2
                "Wow, that's a lot of love.":
                    ag "Right! {w}I'm thanful for all of my staff, and my friends who helped me get this far!"
                    menu:
                        "Friends like who?":
                            a "My family! {w}My coworkers!"
                            k "{i}When did this turn into an interview?{/i}"
                            a "My husband!"
                            m "Oh, I didn't know you were married Agatha."
                            a "That's Mrs. Agatha to you kid. {w}Anyway, thanks for this interview, but I gotta go now."
                            jump agathasbegmean2
                        "Like the owners of Hoa Loa Ken?":
                            show agathamad2
                            ag "Definitely not them... {w}We're not on the best terms."
                            c "{i}So they're really not on the best terms...{/i}"
                            k "Why not?! {w}They're great people!"
                            ag "Yeah, before they decided to {b}compete with me in my business!{/b}"
                            k "Wait, what do you mean by that?"
                            show agathatalking
                            ag "Wait you look familiar kid... {w}Do I know you?"
                            k "Uhh..."
                            menu:
                                "I'm their daughter.":
                                    show agatha
                                    ag "Oh. {w}Well this is awkward. {w}Kurt right?"
                                    k "Uh, yeah. {w}How do you know my name?"
                                    show agathamad2
                                    ag "Surprisingly, I used to be friends with your mom... {w}but hey I can't talk about this type of stuff in front of kids..."
                                    k "Really?"
                                    ag "Ask your mom the rest kiddo. {w}I gotta go."
                                    jump agathasbegmean2
                                "People say that alot...":
                                    ag "Well, anyway, I got to go now... {w}See ya later kids."
                                    jump agathasbegmean2
                        "Family?":
                            ag "Yep, and the like!"
                            show agathatalking
                            ag "Well, anyway, I got to go now... {w}See ya later kids."
                            jump agathasbegmean2
        if deliv:
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
            scene dinerafternoon

            show demployee

            de "How can I help you?"
            c "Hi! {w}We were wondering if you had seen a cat somewhere nearby?"
            a "Gray fur, green-yellow eyes? {w}Also, kinda chub?" 
            de "Oh, sorry, no idea. {w}I barely go outside as is, I'm either waiting on tables all day! {w}The only cats I see are in those cat videos online. {w}Sorry to disappoint you."
            
            scene dinerafternoon
            show aj at slightleft
            show kurt at slightright
            show moe at right
            show christie at left

            c "Well that's unfortunate."
            m "I can't believe he wasn't here! {w}Guess we gotta go back on the map again..."
            call screen mapbeg

    else:
        $ agathasbegvisit = True
        if agathasbegvisit:
            $ visits += 1

        if ing: 
            show kurtmad at slightright
            k "Alright, let's get down to business. {w}We're at the scene of the crime already."
            show kurt at slightright
            show moedrop at right
            m "I don't think this qualifies as a crime?"
            show moe at right
            show kurtdisgust at slightright
            show ajdrop at slightleft
            k "You're missing the point. {w}{i}*Visible Shuddering*{/i} {w}I can't believe I'm even here. {w}My worst enemy's place."
            show moedrop at right
            m "I'm pretty sure Agatha has no clue who you are."
            show moe at right
            show cconfusedtalk at left
            c "Anyway, do you guys think we can get a hold of her? {w}What if she isn't here?"
            show christie at left
            show ajhappy at slightleft
            a "She's always here!"
            show kurtleftmad at slightright
            k "Really... {w}you're saying that like you come here often."
            show ajcaught at slightleft
            a "I have no idea what you're talking about."


            scene dinerafternoon

            show demployee
            with dissolve

            de "How can I help you? {w}Table for four?"
            k "We're looking for Agatha, owner of Agatha's diner?"
            de "Umm... {w} I'll call for her. {w} What's your relation to her?"
            k "Ene-"
            c "Haha, she means, we're just looking to ask some questions."
            de "Hmm...{w} ok.{w} I'll be just one second."

            scene dinerafternoon

            show agatha
            with dissolve

            ag "Hello? {w}You said you were looking to ask some questions?"
            c "Yes, thank you for coming to meet us!"
            k "{i}Agatha herself... we've gotta keep up our guard!{/i} {w}We were wondering why your pancakes, were, err, so good!"
            c "Yeah, everyone's been raving about them recently!"
            show agathahappy

            ag "Haha, I'm always happy to see people appreciate my art! {w}Honestly I just put all of my love into the pancakes, and hope for the best!"
            ag "But I think people forget we specialize in a lot of other things too as well... {w}we make{b} pancakes, hashbrowns, bacon, fries, sausages, ham, our homemade maple syrup, crepes, and a whole lot more.{/b} {w}And all with a whole lotta love!"
            c "Haha, really..."
            menu:
                "Then what about the secret ingredient everyone's been talking about?":
                    show agathatalking
                    ag "The secret ingredient huh... {w}It's certainly a big part but not all of it."
                    k "Then... {w}what is it?"
                    ag "THat's something I've gotta keep to myself kiddo. {w}Not much of a secret if I just told it to anyone who asked me right?"
                    if friend:
                        a "But she's not anyone! {w}She's Mrs. Nguyen's daughter!"
                        ag "Mrs. Nguyen's daughter? {w}"
                        scene dinerafternoon
                        show agathafrustrated
                        ag "She sent over her own daughter to find out what my secret ingredient was? {w}Ridiculous!"
                        k "Hey-"
                        c "Wait, wait, Mrs. Nguyen never sent her over! {w}We're detectives, we came to figure this out ourselves!"
                        show agathamad2
                        ag "Detectives? {w}I assure you, no one's gonna be figuring out what my secret ingredient is anytime soon."
                        c "Thats not what we meant! We uhh..."
                        menu:
                            "Came to resolve the misunderstanding between you and Mrs. Nguyen!":
                                ag "Misunderstanding? {w}I'm pretty sure there's no misunderstanding here."
                                a "No, no, Mrs. Nguyen said she never wanted to start a diner in the first place! {w}She said she would never tell anyone about your secret ingredient even if she knew!"
                                show agathatalking
                                ag "Huh. {w}Then why didn't she just tell me?"
                                k "Honestly, I don't know. {w}Mom didn't even tell {i}me{/i} until today!"
                                $ friendagain = True
                                ag "Well, I guess we have some catching up to do..."
                                jump agathasbegmean2
                            "Came to interview you!":
                                ag "Oh... {w}well, I don't really have time for that, so I'll see you guys later. {w}Thanks for the sentiments about my ingredients but, bye."
                                jump agathsbegmean2
                    else:
                        a "Oh..."
                        ag "Well, kids thanks for the sentiments, but I gotta go now."
                        jump agathasbegmean2
                "Wow, that's a lot of love.":
                    ag "Right! {w}I'm thanful for all of my staff, and my friends who helped me get this far!"
                    menu:
                        "Friends like who?":
                            a "My family! {w}My coworkers!"
                            k "{i}When did this turn into an interview?{/i}"
                            a "My husband!"
                            m "Oh, I didn't know you were married Agatha."
                            a "That's Mrs. Agatha to you kid. {w}Anyway, thanks for this interview, but I gotta go now."
                            jump agathasbegmean2
                        "Like the owners of Hoa Loa Ken?":
                            show agathamad2
                            ag "Definitely not them... {w}We're not on the best terms."
                            c "{i}So they're really not on the best terms...{/i}"
                            k "Why not?! {w}They're great people!"
                            ag "Yeah, before they decided to {b}compete with me in my business!{/b}"
                            k "Wait, what do you mean by that?"
                            show agathatalking
                            ag "Wait you look familiar kid... {w}Do I know you?"
                            k "Uhh..."
                            menu:
                                "I'm their daughter.":
                                    show agatha
                                    ag "Oh. {w}Well this is awkward. {w}Kurt right?"
                                    k "Uh, yeah. {w}How do you know my name?"
                                    show agathamad2
                                    ag "Surprisingly, I used to be friends with your mom... {w}but hey I can't talk about this type of stuff in front of kids..."
                                    k "Really?"
                                    ag "Ask your mom the rest kiddo. {w}I gotta go."
                                    jump agathasbegmean2
                                "People say that alot...":
                                    ag "Well, anyway, I got to go now... {w}See ya later kids."
                                    jump agathasbegmean2
                        "Family?":
                            ag "Yep, and the like!"
                            show agathatalking
                            ag "Well, anyway, I got to go now... {w}See ya later kids."
                            jump agathasbegmean2

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
            de "Oh, sorry, no idea. {w}I barely go outside as is, I'm either waiting on tables all day! {w}The only cats I see are in those cat videos online. {w}Sorry to disappoint you."
            
            scene dinerafternoon
            show aj at slightleft
            show kurt at slightright
            show moe at right
            show christie at left

            c "Well that's unfortunate."
            m "I can't believe he wasn't here! {w}Guess we gotta go back on the map again..."
            call screen mapbeg


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
                    jump agathasbegmean2
                    
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

    if ing:
        if friendagain:
            show ctalk at left
            c "Maybe there's chance for them to make up now..."
            show christie at left
            show kurtclosehappy at slightright
            k "And we'll finally figure out the secret ingredient!"
            c "Alright, then let's go!"
            call screen mapbeg
        else:
            k "Well we didn't learn anything about any secret ingredient! {w}Why'd we come here first? {w}Of course she wouldn't tell us!"
            c "Maybe we have a little bit more insight though... {w}On who to ask next."
            a "Back to the map then?"
            c "Yep."
            call screen mapbeg 
    if deliv:
        if deannoyance == 1:
            m "Well. {w}Wow. {w}That was abrupt."
            k "And not in a good way. {w} I {i}told{/i} you something weird was happening here. {w}It has to be something to do with their secret ingredient!"
            a "Which is {i}not{/i} what we're here for. {w}The deliveries Kurt, the deliveries."
            k "Right..."
            c "The only other place that sells anything to do with making pies is probably {b}Bake n' Take.{/b} {w}Wanna try our luck there?"
            m "Yeah, that sounds like a good idea."
            a "Let's go!"
            call screen mapbeg
        if deannoyance == 2:
            k "Well we didn't learn anything about any pie deliveries! {w}Only that Agatha's has had their signature homemeade pancakes stolen before too. {w}Of course they would only ever talk about themselves and their own problems!"
            m "Uhh... {w}I'm not sure if that has anything to do with self-obsession but okay."
            c "Hmm... {w}but maybe the two events could be related right?"
            m "Yeah, let's go find out."
            call screen mapbeg
        else:
            a "Bake n' Take huh? {w}Should we go there?"
            m "Probably."
            a "Let's go!"
            call screen mapbeg



label kurtsbeg:
    scene kenempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if kenvisit:
        show ajdropopen at slightleft
        a "Here again? {w}Alright then."
        scene kenhappy
        with dissolve
        kmom "Oh hey kids! {w}You have any more questions with your case?"
        a "Yes ma'am!"
        kmom "Alright, shoot!"
        if ing:
            menu:
                "We wanted to know if you know anyone who knows what Agatha's secret ingredient might be?":
                    kmom "Hmm... I'm not sure. Maybe {b}Emily{/b} at Bake n' Take knows. {w}She makes plenty of sweet stuff too, and pancakes technically fall under that category?"
                    kmom "That's all I know kids."
                    jump ken2
                "Why do you want to know about Agatha's secret ingredient?":
                    if friendagain:
                        scene kencon
                        kmom "Because we used to be friends, and I thought she would at least tell me... but it doesn't matter now since we're talking again...{w} by the way did you guys go to the diner earlier?"
                        m "Actually, yeah we did."
                        kmom "So it {i}was{/i} true. {w}She wanted to resolve the misunderstanding between us. {w}I was confused since it was out of nowehere... {w}I thought she didn't even want to talk to me anymore!"
                        c "Actually, we went to talk to her before this... {w}and we tried to explain the misunderstanding."
                        k "{i}Maybe mom knows the secret ingredient now!{/i} Did you guys make up?"
                        kmom "We did... and she told me about you coming over there!"
                        k "So you know the secret ingredient now?!"
                        scene kensmile
                        kmom "Hmm... {w}maybe I do... {w}but I'm not telling! {w}I said that before!"
                        k "Nooo, MOM!!!"
                        jump end1
                    else:
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
                        jump ken2
        if deliv:
            k "We're still on the missing pies..."
            scene kencon
            kmom "Missing pies... {w}That's definitely {b}Bake N' Take{/b}. {w}Sorry kids but I don't know anything about any missing pies-{w} I've never seen anything around here."
            jump ken2

        if cat:
            k "We're trying to find that missing cat on the newspaper!"
            scene kenmad2
            kmom "Missing cat? {w}Oh no... {w}I'm allergic to them. {w}Kurt, if you find it, do {i}not{/i} bring it here, okay?"
            k "Alright mom, I won't, I won't."
            scene kencon
            kmom "Anyway, I'm not sure if I can help you with that kids... {w}once cats go missing, it's hard to find them unless they're looking for you."
            k "Hmmm... {w}seems like you have a lot of experience with missing cats, mom."
            scene kenmad
            kmom "How do you think I found out I had an allergy in the first place? {w}By owning one!"
            k "Oh. {w}Yeah, I guess that makes sense."
            jump ken2    
    else:
        $ kenvisit = True
        if kenvisit:
            $ visits += 1
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
                            subtitle "Our protagonists sit and eat after being forcefully made to eat until their stomachs are full by Kurt's mother."
                            jump ken

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
                            jump ken


        if deliv:
            scene kensmile
            q "Hi, how can I help-"
            scene kenhappy
            kmom "Oh hey kids! {w}How's your detective agency going?"
            k "Pretty boring mom. {w}We're trying to find out about the missing pies in Esteredge!"
            scene kencon
            kmom "Missing pies... {w}That's definitely {b}Bake N' Take{/b}. {w}Sorry kids but I don't know anything about any missing pies-{w} I've never seen anything around here."
            c "Oh no... {w}Well thank you for the help Mrs. Nguyen!"
            scene kenhappy
            kmom "Of course! {w}Anyway, before you go, you should eat dinner!"
            m "Oh no, we wouldn't want to intrude Mrs. Nguyen."
            scene kenmad
            kmom "Nonsense! {w}Kurt was the one who dashed off before telling me that you kids were coming over later today! {w}Now you guys are hungry!"
            scene kenmad2
            "{i}They never said they were hungry.{/i}"
            k "How is that my fault mom?!"
            kmom "Just sit down and eat!"
            scene black
            subtitle "Our protagonists sit and eat after being forcefully made to eat until their stomachs are full by Kurt's mother."
            jump ken

        if cat:
            scene kensmile
            q "Hi, how can I help-"
            scene kenhappy
            kmom "Oh hey kids! {w}How's your detective agency going?"
            k "Pretty boring mom. {w}We're trying to find that missing cat on the newspaper!"
            scene kenmad2
            kmom "Missing cat? {w}Oh no... {w}I'm allergic to them. {w}Kurt, if you find it, do {i}not{/i} bring it here, okay?"
            k "Alright mom, I won't, I won't."
            scene kencon
            kmom "Anyway, I'm not sure if I can help you with that kids... {w}once cats go missing, it's hard to find them unless they're looking for you."
            k "Hmmm... {w}seems like you have a lot of experience with missing cats, mom."
            scene kenmad
            kmom "How do you think I found out I had an allergy in the first place? {w}By owning one!"
            k "Oh. {w}Yeah, I guess that makes sense."
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
            jump ken


label ken:
    scene kenempty

    show ajsmile at slightleft
    show kurtsmile at slightright
    show moesmile at right
    show csmile at left

    subtitle "Food always hits the spot."

    if ing:
        if visits >= 3:
            c "Do we know enough to go figure out what the secret ingredient is?"
            menu:
                "Yes.":
                    $ accuse = True
                    jump accuse1
                "No.":
                    $ accuse = False
                    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                    call screen mapbeg

    if deliv:
        if visits >=3:
            c "Do we know enough to go figure out who's stealing the pies is?"
            menu:
                "Yes.":
                    $ accuse = True
                    jump accuse1
                "No.":
                    $ accuse = False
                    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                    call screen mapbeg
        
    show ctalk at left
    c "Well at least now we have an idea of where to go next?"

    show ajhappy at slightleft
    a "Yep... {w}back to map?"

    show cchallenge at left
    c "Back to map."

    call screen mapbeg

label ken2:
    scene kenempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if visits >= 3:
        c "I think we know enough to go figure out what the secret ingredient is. {w}Agreed?"
        menu:
            "Yes.":
                $ accuse = True
                jump accuse1
            "No.":
                $ accuse = False
                c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                call screen mapbeg

    show ctalk at left
    c "Well at least now we have an idea of where to go next?"

    show ajhappy at slightleft
    a "Yep... {w}back to map?"

    show cchallenge at left
    c "Back to map."

    call screen mapbeg

#Bakery Scenes here

label bakery:
    scene bakeempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if bakevisit:
        show ajdropopen at slightleft
        a "Here again? {w}Alright then."
        scene bakesmile
        if ing:
            e "Hello, how can I help you? {w}Oh it's you kids again! {w}Careful watchers, huh?"
            a "Yep! {w}Here to solve the cases that matter the most!"
            e "Ya'll have any more questions for me?"
            c "Yes, actually,"
            menu:
                "Do you have any idea of what Agatha's secret ingredient could be?":
                    scene bakestalk
                    e "Honestly I have no idea what Agatha puts in her pancakes... {w} I've been trying to figure it out myself for years. {w}If ya'll figure out, let me know first!"
                    e "But...hmm... some common secret ingredients are lemon zest, ground cardamom, a lot more actually... {w}a quick search on the web that you youngsters use these days should bring it up..."
                    scene bakestalk2
                    e "But most of the time, remember this, it's usually what you least expect, but not because it's unusual, but because it's underneath our noses the whole time! {w}So obvious you wouldn't even think of it!"
                    $ obvious = True
                    jump bakery2
                "Do you know anyone else who would know Agatha's secret ingredient?":
                    e "Hmm... I'm not sure? {w}Maybe some of the other restaurants in the downtown mart know more than I do. {w}Sorry I can't help much kids."
                    jump bakery2
        if deliv:
            e "Hello, how can I help you? {w}Oh it's you kids again! {w}Thanks for helping out with the case... {w}Anymore questions you want to ask?"
            c "Yes, actually,"
            menu:
                "So it's only chocolate pies going missing?":
                    scene bakeuntalk
                    e "Yes, it's always {b}only the chocolate pies!{/b} {w}Frankly, those are the worst out of the batch, so I don't know why those are the ones being stolen!"
                    c "When are you walking in to see these pies gone?"
                    e "Early morning... like six?"
                    a "And the door is locked and everything when you walk in?"
                    e "Yes. {w}Everytime!"
                    jump bakedeliv
                "When are you walking in to see the pies going missing?":
                    e "Probably like six in the morning? {w}Whoever steals them {b}wakes up early...{/b}"
                    a "And the door is locked and everything when you walk in?"
                    e "Yes. {w}Everytime!"
                    jump bakedeliv


        if cat:
            e "Hello, how can I help you? {w}Oh it's you kids again! {w}Careful watchers, huh? {w}Ya'll have anymore questions for me?"
            c "Hi, we were wondering if you could tell us about any missing cats?"
            scene bakestalk
            e "Hmm... {w}Missing cats. {w}Sorry kids, but I'm not sure about that one... {w}My daughter is allergic to cats so we never have them in the house."
            e "You would be better off trying your shot somewhere else... {w}Maybe the taco truck? {w}Jose is always returning cats to their owners."
            m "Alright, thanks ma'am."
            jump bakery2
    else:
        $ bakevisit = True
        if bakevisit:
            $ visits += 1
        if ing:
            c "Maybe Bake n' Take knows something about the ingredient?"
            scene bakesmile
            e "Hello, how can I help you?"
            k "We were wondering if you knew anything about Agatha's Diner's secret ingredient? {w}The one they put in their pancakes???"
            scene bakestalk
            e "Uhh... {w}This is a little out of the blue. {w}Honestly I have no idea what Agatha puts in her pancakes... {w} I've been trying to figure it out myself for years."
            c "Ahh, man."
            menu: 
                "Do you have any idea of what it could be?":
                    e "Hmm... some common secret ingredients are lemon zest, ground cardamom, a lot more actually... {w}a quick search on the web that you youngsters use these days should bring it up..."
                    scene bakestalk2
                    e "But most of the time, remember this, it's usually what you least expect, but not because it's unusual, but because it's underneath our noses the whole time! {w}So obvious you wouldn't even think of it!"
                    $ obvious = True
                    jump bakery2
                "Do you know anyone else who would know?":
                    e "Hmm... I'm not sure? {w}Maybe some of the other restaurants in the downtown mart know more than I do. {w}Sorry I can't help much kids."
                    jump bakery2

        if deliv:
            c "Let's see what we can find out."
            scene bakesmile
            e "Hello, how can I help you?"
            c "Hi, we were wondering if you could tell us about any missing pie deliviers? {w}Is that here?"
            scene bakeun
            e "Yes, that's here, sadly. {w}I don't know who it is, why it's happening, all I know is I'm tired of walking in and seeing all my chocolate pies gone!"
            menu:
                "So it's only chocolate pies going missing?":
                    scene bakeuntalk
                    e "Yes, it's always {b}only the chocolate pies!{/b} {w}Frankly, those are the worst out of the batch, so I don't know why those are the ones being stolen!"
                    c "When are you walking in to see these pies gone?"
                    e "Early morning... like six?"
                    a "And the door is locked and everything when you walk in?"
                    e "Yes. {w}Everytime!"
                    jump bakedeliv
                "When are you walking in to see the pies going missing?":
                    e "Probably like six in the morning? {w}Whoever steals them {b}wakes up early...{/b}"
                    a "And the door is locked and everything when you walk in?"
                    e "Yes. {w}Everytime!"
                    jump bakedeliv
                    

        if cat:
            c "Let's see what we can find out."
            scene bakesmile
            e "Hello, how can I help you?"
            c "Hi, we were wondering if you could tell us about any missing cats?"
            scene bakestalk
            e "Hmm... {w}Missing cats. {w}Sorry kids, but I'm not sure about that one... {w}My daughter is allergic to cats so we never have them in the house."
            e "You would be better off trying your shot somewhere else... {w}Maybe the taco truck? {w}Jose is always returning cats to their owners."
            m "Alright, thanks ma'am."
            jump bakery2

label bakedeliv:
    scene bakeempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    show ctalk at left
    c "So if the door is locked everytime, only the chocalate pies are gone, and it's early morning everytime they're stolen..."
    a "It has to be someone who works there!"
    show kurtdisgust at slightright
    k "But who would wake up that early?"
    menu:
        "The people who open up shop?":
            a "But who is that? {w}That could be anyone... even an adult."
            m "Adults don't wake up that early right?"
            k "Mine do..."
            show ajdropopen at slightleft
            a "Well, your parents own a restuarant kurt."
            k "Wait... isn't it a little weird that she hasn't questioned the people who work at the bakery?"
            c "Well we don't know if she has or not? {w}Otherwise, yeah that would be pretty weird..."
            menu:
                "Must be someone close to her then?":
                    $ close = True
                    m "Yeah, that makes a lot more sense... Otherwise, how are they getting away with it?"
                    c "Back to map then?"
                    k "Yep!"
                    call screen mapbeg
                "They have to be breaking in then...":
                    a "Hmm... yeah, that must be the only option... {w}why would someone close to her steal her pies? {w}They could just ask her for them!"
                    c "Back to map then?"
                    a "Yep!"
                    call screen mapbeg

        "A student?":
            show ajmad at slightleft
            a "Exactly! {w}We have to wake up at five every day to go to our stupid school!"
            show moeopen at right
            m "He's not wrong."
            c "Maybe we'll find our culprit close to school..."
            $ close = True
            show ajdropopen at slightleft
            a "Back to map then?"
            c "Yep..."
            call screen mapbeg


label bakery2:
    scene bakeempty

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if ing:
        if visits >= 3:
            c "Do we know enough to go figure out what the secret ingredient is?"
            menu:
                "Yes.":
                    $ accuse = True
                    jump accuse1
                "No.":
                    $ accuse = False
                    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                    call screen mapbeg
        c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
        call screen mapbeg

    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
    call screen mapbeg


label taco1:
    scene tacomorning

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    $ weird = False

    if tacovisit:
        show ajdropopen at slightleft
        a "Here again? {w}Alright then."
        if ing:
            scene josehappy
            j "Hey kids! {w}Nice to see you again. {w}Have any more questions?"
            k "Do you have any speculations about Agatha's secret ingredient?"
            j "Some... {w}I think whatever she puts in her pancakes is an ingredient she makes herself... {w}Otherwise there's no way that no one else hasn't figured out what she puts in it."
            k "I knew it!"
            j "Think about something {b}uncoventional... {/b}{w}something you wouldn't expect to be in pancakes, but is..."
            $ strange = True
            m "Hmm... that makes a lot of sense actually."
            menu:
                "Would you happen to know some uncommon things that have been put in pancakes before?":
                    j "Pancakes, I'm not sure. {w}But for tacos, we put weird things all the time! {w}Maybe like mushroom powder, {w}or unsweetened cocao powder!"
                    a "Wait, seriously?"
                    j "Yeah, people put weird things in tacos all the time! {w}For all we know, the secret ingredients in the pancakes could just be {b}salt...{/b} but that's a common one."
                    jump taco2
                "Agatha doesn't seem like an uncovential person?":
                    $ weird = True
                    j "You never know kiddos, just by looking at someone. {w}People are weird... {w}and sometimes, they're always hiding something. {w}Nothing ever is really how it looks on the surface."
                    m "...{w}huh."
                    jump taco2
        if deliv:
            scene josehappy
            j "Hey kids! {w}Nice to see you again. {w}Have any more questions?"
            c "We just came by to ask about the pies again..."
            if close:
                menu:
                    "This truck is close to school. Have you seen any kids come here around 5-6 in the morning?":
                        j "We usually don't open then actually... {w}But sometimes when I try to park here early, or get here for breakfast serving time in case kids come early, {w}there'll be some kids here, most of them on their way to school."
                        c "Oh really, who?"
                        j "I only know a couple of them as regulars... particularly Eli, Mark, and Sandy, but the others not really. {w}One of them looks kind of like one of the other food places' kid in the downtown mart... and is always carrying some bags with her. {w}Again, not sure the name."
                        a "Hey, I know Eli! {w}Have you seen him lately?"
                        scene josehappy
                        j "Yeah, just yesterday actually! {w}Came to thank me for my tacos!"
                        k "Wait... there are only a few other food places' kid in the downtown mart, including me. {w}Agatha doesn't have any kids in Esteredge anymore... do they look like Emily by any chance?" 
                        scene josedrop
                        j "Yeah, I think so actually? {w}She could pass as a younger version of Emily..."
                        c "Hmm... okay. {w}Thanks Jose!"
                        jump taco2
                    "Yeah, have you seen or heard anything about it?":
                        j "Not really... {w}sorry kids. {w}Sweet things are not really my territory... {w}Maybe you should go ask the diner? {w}They make pancakes?"
                        c "Hmm... okay. {w}Thanks Jose."
                        jump taco2
            menu:
                "Yeah, have you seen or heard anything about it?":
                    j "Not really... {w}sorry kids. {w}Sweet things are not really my territory... {w}Maybe you should go ask the diner? {w}They make pancakes?"
                    c "Hmm... okay. {w}Thanks Jose."
                    jump taco2
    else:
        $ tacovisit = True
        if tacovisit:
            $ visits += 1
        if ing:
            show ajdropopen at slightleft
            a "Alright, this better be worth it. {w}We came all the way to school just to find out what Agatha puts in her pancakes!"
            show kurtleftmad at slightright
            k "A necessary decision! {w}We would make the papers if we really found out what she put in her pancakes!"
            show ajcaught2 at slightleft
            a "Really?"
            show ajhappy at slightleft
            a "Then i'm totally on board! {w}Lead the way kurt!"
            show cdrop at left
            show moedrop at right
            scene josemono
            q "Hello, how can I help you-"
            scene josehappy
            q "-Oh heya Christie! {w}Como estas? {w}How are the parents?"
            scene josesmile
            c "Estamos bien! {w}How are you Mr. Jose?"
            scene josehappy
            j "Great! {w}Haha, tell your mom I said hi, and that I'll be needing more of her cooking in the future!"
            scene josesmile
            c "Will do Mr. Jose!"
            scene josehappy
            j "So what can I do for you today? {w}Tacos? {w}On the house for you and your friends here!"
            scene josesmile
            a "Oh wow, we'll take you up on that Mr. Jose!"
            k "What we're {i}actually{/i} here for is about Agatha's secret ingredient!"
            scene josedrop
            j "Hmm... {w}Her secret ingredient huh? {w}Honestly I haven't heard much about it... Agatha's pretty tight-lipped about it."
            if visits >= 1:
                c "So you don't know either!"
                j "Hmmm, but I do have some speculations!"
            else:
                c "Do you have any speculations maybe?"
                j "Some."
            j "I think whatever she puts in her pancakes is an ingredient she makes herself... {w}Otherwise there's no way that no one else hasn't figured out what she puts in it."
            k "I knew it!"
            j "Think about something {b}uncoventional... {/b}{w}something you wouldn't expect to be in pancakes, but is..."
            $ strange = True
            m "Hmm... that makes a lot of sense actually."
            menu:
                "Would you happen to know some uncommon things that have been put in pancakes before?":
                    j "Pancakes, I'm not sure. {w}But for tacos, we put weird things all the time! {w}Maybe like mushroom powder, {w}or unsweetened cocao powder!"
                    a "Wait, seriously?"
                    j "Yeah, people put weird things in tacos all the time! {w}For all we know, the secret ingredients in the pancakes could just be {b}salt...{/b} but that's a common one."
                    jump taco2
                "Agatha doesn't seem like an uncovential person?":
                    $ weird = True
                    j "You never know kiddos, just by looking at someone. {w}People are weird... {w}and sometimes, they're always hiding something. {w}Nothing ever is really how it looks on the surface."
                    m "...{w}huh."
                    jump taco2
            
        if deliv:
            show ajdropopen at slightleft
            a "Alright, this better be worth it. {w}We came all the way to school just to find out where those missing pies are at!"
            scene josemono
            q "Hello, how can I help you-"
            scene josehappy
            q "-Oh heya Christie! {w}Como estas? {w}How are the parents?"
            scene josesmile
            c "Estamos bien! {w}How are you Mr. Jose?"
            scene josehappy
            j "Great! {w}Haha, tell your mom I said hi, and that I'll be needing more of her cooking in the future!"
            scene josesmile
            c "Will do Mr. Jose!"
            scene josehappy
            j "So what can I do for you today? {w}Tacos? {w}On the house for you and your friends here!"
            scene josesmile
            a "Oh wow, we'll take you up on that Mr. Jose!"
            c "What we're {i}actually{/i} here for is about the missing pies recently."
            scene josedrop
            j "The pies huh..."
            if close:
                menu:
                    "This truck is close to school. Have you seen any kids come here around 5-6 in the morning?":
                        j "We usually don't open then actually... {w}But sometimes when I try to park here early, or get here for breakfast serving time in case kids come early, {w}there'll be some kids here, most of them on their way to school."
                        c "Oh really, who?"
                        j "I only know a couple of them as regulars... particularly Eli, Mark, and Sandy, but the others not really. {w}One of them looks kind of like one of the other food places' kids in the downtown mart... and is always carrying some bags with her. {w}Again, not sure the name."
                        a "Hey, I know Eli! {w}Have you seen him lately?"
                        scene josehappy
                        j "Yeah, just yesterday actually! {w}Came to thank me for my tacos!"
                        k "Wait... there are only a few other food places' kid in the downtown mart, including me. {w}Agatha doesn't have any kids in Esteredge anymore... do they look like Emily by any chance?" 
                        scene josedrop
                        j "Yeah, I think so actually? {w}She could pass as a younger version of Emily..."
                        c "Hmm... okay. {w}Thanks Jose!"
                        jump taco2
                    "Yeah, have you seen or heard anything about it?":
                        j "Not really... {w}sorry kids. {w}Sweet things are not really my territory... {w}Maybe you should go ask the diner? {w}They make pancakes?"
                        c "Hmm... okay. {w}Thanks Jose."
                        jump taco2
            menu:
                "Yeah, have you seen or heard anything about it?":
                    j "Not really... {w}sorry kids. {w}Sweet things are not really my territory... {w}Maybe you should go ask the diner? {w}They make pancakes?"
                    c "Hmm... okay. {w}Thanks Jose."
                    jump taco2

        if cat:
            show ajdropopen at slightleft
            a "Alright, this better be worth it. {w}We came all the way to school just to find out where that missing cat is!"
            scene josemono
            q "Hello, how can I help you-"
            scene josehappy
            q "-Oh heya Christie! {w}Como estas? {w}How are the parents?"
            scene josesmile
            c "Estamos bien! {w}How are you Mr. Jose?"
            scene josehappy
            j "Great! {w}Haha, tell your mom I said hi, and that I'll be needing more of her cooking in the future!"
            scene josesmile
            c "Will do Mr. Jose!"
            scene josehappy
            j "So what can I do for you today? {w}Tacos? {w}On the house for you and your friends here!"
            scene josesmile
            a "Oh wow, we'll take you up on that Mr. Jose!"
            m "What we're {i}actually{/i} here for is about the missing cat on the newspaper recently."
            scene josedrop
            j "The missing cat? {w}Oh no, that's quite unfortunate, but you came to the right place... {w}I see cats around all the time here!"
            m "Really? What cats did you see?"
            j "Hmm... it's always the same one, gray fur, green-yellow eyes, kinda fat?"
            a "Wait, that's him! That's the cat we're looking for!"
            j "Well then... {w}I hate to break it to you but that cat goes missing every week. {w}I always find him and return him back to his owner, but then he's gone just like that the next day, and back near my taco truck."
            m "{i}So cats like tacos...{/i}"
            j "He's not really lost, but the owner keeps putting a request in the newspaper to find him again... {w}I don't think she understands he doesn't actually want to be found..."
            jump end1

label taco2:
    scene tacomorning

    show aj at slightleft
    show kurt at slightright
    show moe at right
    show christie at left

    if ing:
        if weird:
            m "That was pretty insightful I think. {w}I think I learned more about life then I actually did about any secret ingredient."
        c "Hmm... well now,"
        if visits >= 3:
            c "I think we know enough to go figure out what the secret ingredient is. {w}Agreed?"
            menu:
                "Yes.":
                    $ accuse = True
                    jump accuse1
                "No.":
                    $ accuse = False
                    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                    call screen mapbeg
        else:
            show ajsmile at slightleft
            a "Back to the map!"
            call screen mapbeg

    if deliv:
        if close:
            show ctalk at left
            c "A person who looks like a younger version of emily near the truck at 5-6 in the morning?"
            menu:
                "She was probably trying to get to school after stealing the pies!":
                    a "That's why she passed the taco truck!"
        
        if visits >= 3:
            c "I think we know enough to go figure out who stole the pies. {w}Agreed?"
            menu:
                "Yes.":
                    $ accuse = True
                    jump accuse1
                "No.":
                    $ accuse = False
                    c "Okay, then I guess it's back to more investigating... {w}where should we go next?"
                    call screen mapbeg
                    show ctalk at left

        show ajdrop at slightleft
        c "Back to the map again I guess..."
        a "Haah... we're not going anywhere with this!"
        call screen mapbeg


                    

label accuse1:
    if ing:
        scene dinerafternoon
        show aj at slightleft
        show kurt at slightright
        show moe at right
        show christie at left

        if ing: 
            show kurtmad at slightright
            k "Alright, let's get down to business. {w}Confrontation time."

            scene dinerafternoon

            show demployee
            with dissolve

            de "How can I help you? {w}Table for four?"
            k "We're looking for Agatha, owner of Agatha's diner?"
            de "Umm... {w} I'll call for her. {w} What's your relation to her?"
            k "Ene-"
            c "Haha, she means, we're just looking to confirm some questions."
            de "Hmm...{w} ok.{w} I'll be just one second."

            scene dinerafternoon

            show agatha
            with dissolve

            ag "Hello? {w}How can I help you?"
            k "We've figured out your secret ingredient!"
            scene dinerafternoon
            show agathafrustrated
            ag "Not this again... {w}Alright, shoot your best shot."
            scene dinerafternoon
            show agatha 
            if obvious:
                if strange:
                    menu:
                        "It was under our noses this entire time!":
                            menu:
                                "Maple Syrup!":
                                    $ answer = True
                                "Salt!":
                                    $ answer = False
                                "Cocoa powder!":
                                    $ answer = False
                                "Lemon Zest!":
                                    $ answer = False
                        "It was the strangest thing we could think of!":
                            menu:
                                "Mushroom powder!":
                                    $ answer = False

                                "Cocoa powder!":
                                    $ answer = False
                                "Tasty poison!":
                                    $ answer = False
                    
                    jump accuse2

                    k "It was under our noses this entire time!"
                    menu:
                        "Maple Syrup!":
                            $ answer = True
                        "Salt!":
                            $ answer = False
                        "Cocoa powder!":
                            $ answer = False
                        "Lemon Zest!":
                            $ answer = False
                    jump accuse2
            if strange:
                if obvious:
                    menu:
                        "It was under our noses this entire time!":
                            menu:
                                "Maple Syrup!":
                                    $ answer = True
                                "Salt!":
                                    $ answer = False
                                "Cocoa powder!":
                                    $ answer = False
                                "Lemon Zest!":
                                    $ answer = False
                        "It was the strangest thing we could think of!":
                            menu:
                                "Mushroom powder!":
                                    $ answer = False
                                "Cocoa powder!":
                                    $ answer = False
                                "Tasty poison!":
                                    $ answer = False
                jump accuse2
                k "It was the strangest thing we could think of!"
                menu:
                    "Mushroom powder!":
                        $ answer = False
                    "Cocoa powder!":
                        $ answer = False
                    "Tasty poison!":
                        $ answer = False
                jump accuse2


    if deliv:
        scene bakeempty
        show aj at slightleft
        show kurt at slightright
        show moe at right
        show christie at left

        c "Alright guys... {w}It's showdown!"

        scene bakesmile
        if close:
            e "Oh hello guys! {w}What can I help you with?"
            a "We've come to figure out who's stealing your pies Mrs!"
            scene bakestalk2
            e "Oh really? {w}Who?"
            menu:
                "It's someone close to you.":
                    e "Wait, who?"
                    c "Sorry to inform you maam, but someone who looks like \"a younger version of you\" you has been going to Esteredge high carrying bags of something in the morning from 5-6. {w}I believe it may be your:"
                    menu:
                        "Grandchild":
                            c "Who has been stealing your chocolate pies in the morning before going to school."
                            scene bakeuntalk
                            e "{i}Granddaughter?{/i} {w}I beg your pardon, but I do not have a granddaughter. {w}I do have a daughter who goes to highschool though."
                            k "Oh... {w}then it's probably her?"
                            e "Are you assuming I'm {i}old{/i}???"
                            show bakeun
                            a "Uh, no ma'am, not at all! {w}We just uhhh, wanted to show respect!"
                            k "Yes, you just look so distinguished as an, uhh, {w}elder."
                            scene bakeuntalk
                            e "Right, of course I do.{w} Anyway, you kids should be going home, not staying out this late investigating cases and accusing people's daughters... {w}I'll see you later."
                            scene bakeempty
                            show ajshook at slightleft
                            show kurtshook at slightright
                            show moedrop at right
                            show cdrop at left
                            k "...{w}did she just kick us out because we assumed she was old?"
                            c "...{w}I think so."
                            a "Well what were we supposed to think?! {w}Her hair is gray!"
                            m "My mom always tells me that women are sensitive about their age... {w}next time we've got to keep that in mind."
                            jump end2
                            
                        "Daughter":
                            c "Who has been stealing your chocolate pies in the morning before going to school."
                            scene bakeun
                            e "Celise? {w}Why would she be doing that?"
                            c "..."
                            e "Well, thank you for this information, i'll be sure to use it well. {w}That Celise... I'm going to have a good good talk with her tonight."
                            $ answer = True
                            jump end1
        else:
            e "Oh hello guys! {w}What can I help you with?"
            a "We've come to figure out who's stealing your pies Mrs!"
            scene bakestalk2
            e "Oh really? {w}Who?"
            k "It's someone in your inner circle... {w}The people who open the shop!"
            scene bakeun
            e "Ummm... {w}I already came to that conclusion and questioned all of them, even firing some... {w}It was {i}not{/i} them I assure you. {w}I appreciate your help, but I'm going to have to ask you all to leave now."
            jump end1


label accuse2:
    if answer:
        show agathamad2
        ag "I don't know what you're pulling, but this isn't funny. {w}Who told you this?"
        k "Are we right?"
        ag "..."
        ag "..."
        "{i}She doesn't want to admit it, but the Careful Watchers just struck gold.{/i}"
        ag "I'm not going to say its right... {w}But who?"
        a "No one, we figured it out ourselves!"
        scene dinerafternoon
        show agathafrustrated
        ag "Of course you did..."
        jump end1
    else:
        show agathamad2
        ag "You're wrong. {w}Just like everyone else. {w}Nice try though kids."
        jump end1


label end1:
    if friendagain:
        scene kenempty

        show ajdrop at slightleft
        show kurtshook at slightright
        show moedrop at right
        show cdrop at left

        k "I can't believe mom didn't tell us the secret ingredient!"
        c "I guess we'll never know Agatha's secret ingredient... {w}but hey, at least your mom knows, right kurt?"
        show kurtmad at slightright 
        k "I JUST WANNA KNOW, IS IT THAT HARD--"
        jump end2
    if answer:
        if ing:
            scene dinerafternoon

            show ajsmile at slightleft
            show kurtclosehappy at slightright
            show moedrop at right
            show cdrop at left
            k "So it was the custom homemade maple syrup this whole time..."
            k "..."
            k "..."
            k "Wait, but how do you make the custom homemade maple syrup?"
            show kurtshook at slightright
            show ajshook at slightleft
            a "Wait... {w}Another secret ingredient?"
            k "AHHHHHHHHHHHHHH-"
            jump end2
        if deliv:
            scene bakeempty
            show ajsmile at slightleft
            show kurtclosehappy at slightright
            show moedrop at right
            show cdrop at left

            a "Now we can rest in piece, with another case solved!"
            m "I'm not sure there was much case solving as there was case assumming, but...{w} yeah."
            a "Yeah!"
            jump end2
    else:
        if ing:
            scene dinerafternoon

            show ajdrop at slightleft
            show kurtmad at slightright
            show moedrop at right
            show cdrop at left
            k "I can't believe we were wrong!"
            c "I can't believe we thought we were going to be right..."
            m "I think this was more guessing than case solving..."
            show ajdropopen at slightleft
            a "Maybe we're not cut out for this..."
            show kurtleftmad at slightright
            k "I told you this whole thing was a stupid idea in the first place!"
            jump end2
        if deliv:
            scene bakeempty
            show ajdrop at slightleft
            show kurtmad at slightright
            show moedrop at right
            show cdrop at left
        
            m "Well... that was not a case solved."
            a "Uh... {w}yeah."
            jump end2
        if cat:
            scene tacomorning
            show ajdrop at slightleft
            show kurtmad at slightright
            show moedrop at right
            show cdrop at left

            a "So basically, we hopped onto a fake case?"
            k "Yep. {w}Man was this a waste of time!"
            m "Better luck next time?"
            jump end2


label end2:
    scene black
    subtitle "And so, the tale of the Careful Watchers ended... {w}version one."
    scene endscreen
    subtitle "See you next time."