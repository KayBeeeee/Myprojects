ascii_art = """
       -=[ deserted on island ]=-  12/98
                    _
                   /_'. _
                 _   \\ / '-.
                < ``-.;),--'`
                 '--. |__
      /-/-/|o|-|\\-\\\\|\\\\   / | \\
       '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\\
             |-|                      |"\\ |__ ,_) \\_, |_| |__ |_/  o  o  o
             |-|O
             |-(\\\\,__
          ...|-|\\\\--,\\\\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Daniel C. Au


.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\\\o\\))     .                                   .
.     .-.    `  \\\\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.



                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \\O/                                      |\\
          X.a##a.   M                                       |_\\
       .aa########a.>>                                    __|__
    .a################aa.                                 \\   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                 David S. Issel



                                                   .       .
                                                    \\     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \\
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""

print(ascii_art)



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()

if direction == "right" or direction != "left":
   print("You fell into a hole. Game Over.")

elif direction == "left":
   print("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
   lake = input().lower()

   if lake == "swim" or lake != "wait":
      print("You were attacked by a trout. Game Over.")
   elif lake == "wait":
         print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
         door = input().lower()
         if door == "red":
            print("It's a room full of fire. Game Over.")
         elif door == "yellow":
            print("You found the treasure! You Win!")
         elif door == "blue":
            print("You enter a room of beasts. Game Over.")
         else:
            print("You chose a door that doesn't exist. Game Over.")






         
   





