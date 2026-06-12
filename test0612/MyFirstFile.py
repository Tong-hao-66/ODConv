import random
 
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("猜一个1到100之间的数字。")
 
    while True:
        guess = int(input("你的猜测: "))
        attempts += 1
 
        if guess < number_to_guess:
            print("太小了！")
        elif guess > number_to_guess:
            print("太大了！")
        else:
            print(f"恭喜你，猜对了！你一共用了{attempts}次。")
            break
 
if __name__ == "__main__":
    guess_number()
