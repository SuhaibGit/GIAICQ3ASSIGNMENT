import random
def play():
    user=input("What's your choice rock(R), paper(P), scissor(S): ").lower()
    computer=random.choice(['r','p','s'])
    if user==computer:
        return f"The can Ties the computer also choosen{computer}"
    result=isWin(user,computer)
    return result
def isWin(player, opponent):
    #return true if player wins
    if(player=='r' and opponent=='s' )or(player=='p' and opponent=='r') or ( player=='s' and opponent=='p'):
        return "Player Wins"
    else:
        return "Computer Wins" 
print(play())
