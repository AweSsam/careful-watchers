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