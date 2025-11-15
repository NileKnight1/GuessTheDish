default g1_l = g1_l1
default q_max = 10

label game1:
    play music "g1.ogg"
    scene bg g1 with pixellate


    menu:
        "Choose the level"
        "Easy":
            $ g1_l = g1_l1
        "Medium":
            $ g1_l = g1_l2
        "Hard":
            $ g1_l = g1_l3

    menu:
        "Choose number of questions"
        "5":
            $ q_max = 5
        "10":
            $ q_max = 10
        "15":
            $ q_max = 15
        "20":
            $ q_max = 20


    jump g1_start

screen hud():
    frame:
        background "#0008"
        padding (15, 10)
        xalign 0.02
        yalign 0.02
        xminimum 250
        yminimum 60
        

        vbox:
            spacing 5
            text "Score: [score]" size 30 color "#2cc054" bold True
            text "Health: [health]" size 30 color "#c32f14" bold True
            text "Question: [qn + 1]/[len(questions)]" size 30 color "#d1d1d1"


label g1_start:
    $ score = 0
    $ health = 3
    # scene bg g1 with pixellate
    show screen hud

    $ questions = random.sample(g1_l, q_max)
    $ qn = 0
    $ qn2 = 0
    
    jump g1_question



label g1_question:
    if qn2 == len(questions):
        jump g1_end

    $ cur_q = questions[qn]
    $ c_name = cur_q["name"]
    $ c_img = cur_q["img"]

    python:
        others = [f["name"] for f in g1_l if f["name"] != c_name]

        wrong = random.sample(others, 2)

        choices = [c_name] + wrong

        random.shuffle(choices)

    scene bg g1 
    show expression c_img 

    

    pause 1.0



    menu:
        "[choices[0]]":
            $ choice = choices[0]
            
        "[choices[1]]":
            $ choice = choices[1]

        "[choices[2]]":
            $ choice = choices[2]
    
    jump answer

label answer:
    # pause 1.0

    if choice == c_name:
        $ score = score + 1
        play sound "correct.ogg"
        show text "{color=#00ff44}{size=80}{b}Correct!{/b}{/size}{/color}" at truecenter with dissolve


    else:
        $ health = health - 1
        play sound "wrong.ogg"
        show text "{color=#ff3333}{size=60}{b}No it's [c_name].{/b}{/size}{/color}" at truecenter with dissolve


    # pause 1.0

    if health == 0:
        jump dead

    if(qn < q_max - 1):
        $ qn = qn + 1
    $ qn2 = qn2 + 1 

    hide expression c_img
    jump g1_question

label dead:
    # pause 1.0
    "You ran out of health."
    jump g1_end

label g1_end:
    # pause 1.0
    "Game over!"

    "Final score: [score] and you have [health] health points."
    




