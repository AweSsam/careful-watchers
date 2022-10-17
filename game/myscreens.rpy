screen firstpage():
    imagemap:
        ground "newspage1.png"
        hover "newspage1hov.png"
        hotspot(1337, 858, 166, 61) action Jump("newspaper2")

screen secondpage():
    imagemap: 
        ground "newspage2.png"
        hover "newspage2hov.png"
        hotspot(341, 891, 133, 47) action Jump("newspaper1")
        hotspot(1344, 852, 168, 57) action Jump("newspaper3")

screen thirdpage():
    imagemap:
        ground "newspage3.png"
        hover "newspage3hov.png"
        hotspot(365, 862, 171, 59) action Jump("newspaper2")
        hotspot(931, 62, 604, 383) action Jump("ingredient")
        hotspot(922, 448, 611, 252) action Jump("deliveries")
        hotspot(925, 713, 614, 222) action Jump("thecat")

screen mapbeg():
    imagemap:
        ground "map1.png"
        hover "hovermap1.png"
        hotspot(561, 919, 377, 81) action Jump("mapforward1")
        hotspot(833, 576, 294, 168) action Notify("You can't access this yet!")
        hotspot(1641, 764, 179, 130) action Notify("You can't access this yet!")
        hotspot(241, 401, 149, 79) action Notify("You're already here!") #moes place
        hotspot(545, 292, 70, 112) action Notify("You can't access this yet!")

screen mapbeg2():
    imagemap:
        ground "map1-2.png"
        hover "hovermap1-2.png"
        hotspot(53, 68, 156, 90) action Jump("agathasbeg") #agatha's diner
        hotspot(638, 5, 441, 135) action Jump("kurtsbeg") #hoa loa ken
        hotspot(58, 451, 141, 125) action Notify("You can't access this yet!") #movies
        hotspot(790, 285, 208, 113) action Jump("bakery") #bake n' take
        hotspot(893, 642, 157, 118) action Notify("You can't access this yet!") #gym
        hotspot(272, 636, 210, 144) action Notify("You can't access this yet!") #supercenter
        hotspot(1271, 32, 185, 133) action Jump("taco1") #taco 2go
        hotspot(253, 12, 309, 61) action Jump("mapback1")