print("Welcome to my first game")
name = input("what is your name? ")
age = int(input("what is your age? "))
 

health = 10

if age >= 18:
    print("You are old enough to play")

    want_to_play = input("do you want to play? ").lower()
    if want_to_play == "yes":
        print("you are starting with", health , "health")
        print("let's play")

        left_or_right = input("first choice... Left or Right (left/right?) ")

        if left_or_right == "left":
          ans = input("Nice, you follow the path amd reach a lake... Do you go across or go around (across/around)? ").lower()

          if ans == "around":
            print("you went around and reached the orther side of the lake")

          elif ans == "across":
            print("you managed to get across, but you bit by a fish and lost 5 health.")
            health -= 5
          
          ans = input("you notice a house and a river. which do you go to (house/river)? ")
          if ans == "house":
            print("you go to the house and are greted by the owner... He doesn't like you and you lose 5 health")
            health -= 5

            if health <= 0:
              print("you now have 0 health and you lost the game..")
            else:
             print("you now have", health, "you have survived, You WIN") 


          else:
            print("you fell in the river and lost")




        else: 
          print("you fell down and lost")
          
          
          
    else:
        print("cya...")




else:
    print("you are not old enough to play")

 

























'''
*
/
+
-
%
//
'''

x = 9 
y = 8
x = x + y
# x += y


'''
variable
You can't start a variable with a number
'''''
'''''
str     "hello" 'hi' '89'
int 8, 7, -9, 100000
float  6.0, 7.5, -9.8, -100.0
bool True, False
'''
# or use 