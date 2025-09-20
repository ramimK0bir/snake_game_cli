"""
This is a simple snake game .
auther : userAnonymousLoggedIn
github : https://github.com/ramimk0bir
"""
import asyncio
import time
import random
import keyboard
pressedKey=-1
operationalKey=-1
snake_body=[(1,5)]
food=-1
score=-1


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
    global pressedKey,operationalKey,snake_body,food,score
    while True:

        x=snake_body[0][0]
        y=snake_body[0][1]
        if pressedKey==0 and (abs(operationalKey-pressedKey)!=2) :
            snake_body.insert(0,(x,y-1))
            snake_body.pop()
            operationalKey=0
        elif pressedKey==1 and (abs(operationalKey-pressedKey)!=2):
            snake_body.insert(0,(x-1,y))
            snake_body.pop()
            operationalKey=1
        elif pressedKey==2 and (abs(operationalKey-pressedKey)!=2):
            snake_body.insert(0,(x,y+1))
            snake_body.pop()
            operationalKey=2
        elif pressedKey==3 and (abs(operationalKey-pressedKey)!=2):
            snake_body.insert(0,(x+1,y))
            snake_body.pop()
            operationalKey=3
        if food in snake_body:
            snake_body.insert(0,food  )
            food=-1


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
        if any(  (x[1] >=11 or not x[1] ) for x in snake_body     ) :
            print("\033[H\033[J", end="")  # ANSI escape code to clear screen
            print("\033[91m" +game_over+"\033[0m\n")
            break
        elif any(  (x[0] >=21 or not x[0] ) for x in snake_body     ) :
            print("\033[H\033[J", end="") 
            print("\033[91m" +game_over+"\033[0m\n")
            break
        main_base = score_bar(score)+ line+'\n'+temp_base+line
        print("\033[H\033[J", end="")  # ANSI escape code to clear screen
        print("\033[92m" +main_base+"\033[0m\n")
        await asyncio.sleep(0.5)  # prevent blocking CPU

async def check_keys():
    global pressedKey
    while True:
        if keyboard.is_pressed('up'):
            pressedKey=0
        elif keyboard.is_pressed('left'):
            pressedKey=1
        elif keyboard.is_pressed('down'):
            pressedKey=2
        elif keyboard.is_pressed('right'):
            pressedKey=3
        await asyncio.sleep(.1)

async def main():
    await asyncio.gather( check_keys(),print_loop())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program stopped.")












