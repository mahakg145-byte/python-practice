snake = -1
water = 1
Gun = 0
a = int(input("player1: "))
b = int(input("player2: "))


if a==b:
    print("Draw")
elif(a == snake and b == water) or \
    (a == water and b == Gun) or \
      (a == Gun and b == snake):   
   print("player 1 wins")
else:
    print("Player 2 wins")