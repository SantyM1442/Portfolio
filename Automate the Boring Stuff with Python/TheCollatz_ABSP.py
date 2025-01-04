def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    elif number%2==1:
        answer=3*number+1
        print(answer)
        return answer
num=int(input('Type a number: '))
while num!=1:
    num=collatz(int(num))
