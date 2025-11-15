
define e = Character("Eileen")


label start:
    jump game1
    
    "Choose Game"

    menu:
        "Guess The Dish":
            jump game1


    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
