"""
This is a simple snake game .
Author : userAnonymousLoggedIn
GitHub : https://github.com/ramimk0bir
"""
import asyncio
import random
pressedKey=-1
operationalKey=-1
snake_body=[(1,5)]
food=-1
score=-2


base = """|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
|++++++++++++++++++++|
"""
line="----------------------"


def score_bar(score):

    return f"""
----------------------
|{ f"score :{score+1}".center(20) }|
----------------------

"""

isGamePaused=0

class custom_keyboard :
    def __init__(self):
        from pynput import keyboard
        
        self.keyboard=keyboard
        self.pressed_keys = set()

        self.listener = self.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
    def on_press(self,key):
        self.pressed_keys.add(key)

    def on_release(self,key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)


    def is_pressed(self,key_name):
        # Convert string like "space" to pynput Key or character
        from pynput.keyboard import Key
        try:
            key = getattr(Key, key_name)
        except AttributeError:
            # Not a special key, check char key
            key = key_name

        return key in self.pressed_keys

def base_replace(base_text,text,x,y):
    x-=1
    y-=1
    base=base_text

    base2=[]
    for index,line in enumerate(base.split('\n')):
        if index == y:

            line= line [:x+1]+text+ line[x+2:]
        base2.append(line)
    return  '\n'.join(base2)



async def print_loop():
    global pressedKey,operationalKey,snake_body,food,score,isGamePaused
    while True:
        
        lastNode=snake_body[-1]
        x=snake_body[0][0]
        y=snake_body[0][1]
        print(abs(operationalKey-pressedKey), file=open("test.txt", "a"))
        if isGamePaused  :
            pass
        elif (abs(operationalKey-pressedKey)==2)  :
            X=x
            Y=y
            if pressedKey==0:
                Y+=1
            elif pressedKey==2:
                Y-=1
            elif pressedKey==1:
                X+=1
            elif pressedKey==3:
                X-=1
            snake_body.insert(0,(X,Y))
            snake_body.pop()
        elif pressedKey==0  :
            snake_body.insert(0,(x,y-1))
            snake_body.pop()
            operationalKey=0
        elif pressedKey==1:
            snake_body.insert(0,(x-1,y))
            snake_body.pop()
            operationalKey=1
        elif pressedKey==2 :
            snake_body.insert(0,(x,y+1))
            snake_body.pop()
            operationalKey=2
        elif pressedKey==3 :
            snake_body.insert(0,(x+1,y))
            snake_body.pop()
            operationalKey=3




        temp_base=base_replace(base,"+",0,0)
        for index,item in enumerate (snake_body):
            if index == 0:
                temp_base=base_replace(temp_base, "@", item[0], item[1])
                continue
            temp_base=base_replace(temp_base,"=", item[0], item[1])
        if food == -1 :
            food=( random.randint(1,20),random.randint(1,10)       )
            score+=1
        else :
            temp_base=base_replace(temp_base,   "\033[31m*\033[32m"      , food[0], food[1])

        game_over = f"""
----------------------
|     Game Over      |
|{ f"score :{score+1}".center(20) }|
----------------------
"""
        if snake_body[0][1] >=11 or not snake_body[0][1] :
            print("\033[H\033[J", end="")  # ANSI escape code to clear screen
            print("\033[91m" +game_over+"\033[0m\n")
            break
        elif snake_body[0][0] >=21 or not snake_body[0][0]  :
            print("\033[H\033[J", end="") 
            print("\033[91m" +game_over+"\033[0m\n")
            break
        elif any( not snake_body.count(x)<=1  for x in snake_body  ) :
            print("\033[H\033[J", end="") 
            print("\033[91m" +game_over+"\033[0m\n")
            break
        if food in snake_body:
  
            snake_body.insert(-1,snake_body[-1])
            food=-1
        main_base = score_bar(score)+ line+'\n'+temp_base+line
        print("\033[H\033[J", end="")  # ANSI escape code to clear screen
        print("\033[92m" +main_base+"\033[0m\n")
        await asyncio.sleep(0.5)  # prevent blocking CPU

async def check_keys():
    global pressedKey,isGamePaused,custom_keyboard
    custom_keyboard=custom_keyboard()
    while True:
        if custom_keyboard.is_pressed('up'):
            pressedKey=0
        elif custom_keyboard.is_pressed('left'):
            pressedKey=1
        elif custom_keyboard.is_pressed('down'):
            pressedKey=2
        elif custom_keyboard.is_pressed('right'):
            pressedKey=3
        elif custom_keyboard.is_pressed('space') :
            isGamePaused = not isGamePaused
        await asyncio.sleep(.1)

async def main():
    await asyncio.gather( check_keys(),print_loop())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program stopped.")



