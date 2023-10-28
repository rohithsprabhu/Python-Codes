import random

def games():
    user  = input("Odd or Even : ").lower()
    if user=="odd":
        machine="I'm even"
        print(machine)
        while True:
            odd = int(input("ready 3 2 1 ....go : "))
            if odd > 0 and odd < 11:
                break
            else:
                print("You've entered number not in range")
        comp = random.randint(1, 10)
        playing_choice = odd + comp
        if(playing_choice%2==0):
            system = random.choice(["bat", "bowl"])
            print("I choose to " +system)
            if system=="bat":
                print("'>>>'- when this symbol arrives that's your turn to bowl")
                print("Let's start the game")
                off_ground(True)
            if system=="bowl":
                print("'>>>'- when this symbol arrives that's your turn for bating")
                print("Let's start the game")
                on_ground(True)
        else:
            print("You have the hell of luck")
            user_opinion = input("You won by your choice. Do you choose to bat or bowl?").lower()
            if user_opinion=="bat":
                print("You choose to bat. Best of luck!")
                print("'>>>'- when this symbol arrives that's your turn for bating")
                print("Let's start the game")
                on_ground(True)
            if user_opinion=="bowl":
                print("you choose to bowl. Becareful I'm a good batsman")
                print("'>>>'- when this symbol arrives that's your turn to bowl")
                print("Let's start the game")
                off_ground(True)
    elif user=="even":
        machine="I'm odd"
        print(machine)
        even = int(input("Are you ready? then press the number"))
        mach = random.randint(1, 10)
        gaming_choice = even+mach
        if (gaming_choice%2==0):
            print("You have the hell of luck")
            user_opinion = input("You won by your choice. Do you choose to bat or bowl?").lower()
            if user_opinion=="bat":
                print("You choose to bat. Best of luck, boy!")
                print("'>>>'- when this symbol arrives that's your turn for bating")
                print("Let's start the game")
                on_ground(True)
            if user_opinion=="bowl":
                print("you choose to bowl. Becareful I'm a good batsman")
                print("'>>>'- when this symbol arrives that's your turn to bowl")
                print("Let's start the game")
                off_ground(True)
        else:
            system = random.choice(["bat", "bowl"])
            print("I choose to " +system)
            if system=="bat":
                print("'>>>'- when this symbol arrives that's your turn to bowl")
                print("Let's start the game")
                off_ground(True)
            if system=="bowl":
                print("'>>>'- when this symbol arrives that's your turn for bating")
                print("Let's start the game")
                on_ground(True)



def on_ground(bool):
    count = 0
    over = 0
    run = 0
    runs = 0
    wicket = 0
    print("note: number should be in 1 - 10")
    while True:
        player = int(input(">>> "))
        if player < 1 or player > 10:
            print("You've entered the number not in range")
            continue
        player_2 = random.randint(1, 10)
        print(player_2)
        count = count+1
        if(count%6==0):
            over = over+1
            print(f"hey {over} is ended")
        if player==player_2:
            runs=runs+player
            wicket=wicket+1
            wick=11-wicket
            print(f"you have {wick} more wicket")
        if player!=player_2:
            run=run+player
            final_score=run-runs
            if (final_score%100==0):
                print(f"You scored {final_score} runs")
        if wicket==11:
            if final_score>200:
                print(f"Well played bro. You scored  *{final_score}*")
            else:
                print(f"hey buddy, You just scored {final_score} number of runs")
            break
    if bool:
        print("It's your turn to bowl")
        off_ground(False)


def off_ground(bool):
    count_1 = 0
    over_1 = 0
    run_1 = 0
    run_2 = 0
    wicket_1 = 0
    print("note: number should be in 1 - 10")
    while True:
        batsman = random.randint(1, 10)
        bowler = int(input(">>> "))
        if bowler < 1 or bowler >  10:
            print("You've entered the number not in range")
            continue
        print(batsman)
        count_1=count_1+1
        if(count_1%6==0):
            over_1=over_1+1
            print(f"my {over_1} are ended")
        if batsman==bowler:
            run_2=run_2+batsman
            wicket_1=wicket_1+1
        if batsman!=bowler:
            run_1=run_1+batsman
            final_score=run_1-run_2
        if wicket_1==11:
            if final_score>200:
                print(f"yeah! I scored  *{final_score}* runs")
            else:
                print(f"I just scored  *{final_score}* runs")
            break
    if bool:
        print("it's your turn to bat")
        on_ground(False)

if __name__ == '__main__':
    games()