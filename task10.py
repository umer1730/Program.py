questions = [
    [
        "Which language is used to craete fb?","Python",
        "French","Java script",
        "Php","None",4
    ],
    [
        "Which cricketer is called the god of cricket?","Sachin",
        "Imran","Virat",
        "Don bradman","Sir Viv Richards",4
    ],
    [
        "Which is the first prime minister of Pakistan?","Liagat Ali Khan",
        "Quaid-e-azam","Allama Iqbal",
        "Nawaz Sharif","Imran khan",4
    ],
    [
        "Who scored most fifties in international career?","Sachin",
        "Babar","Virat Kohli",
        "","None",4
    ],
    [
        "Which language is used to create fb?","Python",
        "French","Java script",
        "Php","None",4
    ],
    [
        "Which language is used to create fb?","Python",
        "French","Java script",
        "Php","None",4
    ],
    [
        "Which language is used to create fb?","Python",
        "French","Java script",
        "Php","None",4
    ],
]
levels = [1000,2000,3000,4000,10000,20000,40000,80000,160000,320000,10000000]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter Your number(1 - 4):"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
             money = 10000
        elif (i== 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break
print(f"Your take home money is {money}")