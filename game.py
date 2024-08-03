# Kaun Banega Crorepati Game
questions = [
    [
        "Which animal is known as the 'Ship of the Desert",
        "Dog",
        "Cat",
        "Camel",
        "Cow",
        3,
    ],
    ["How many days are there in a week?", "7", "8", "10", "5", 1],
    ["How many hours are there in a day?", "18", "20", "12", "24", 4],
    ["How many letters are there in the English alphabet?", "24", "26", "22", "25", 2],
    ["Rainbow consist of how many colours?", "6", "8", "7", "5", 3],
    [
        "How many days are there in a year(not leap year)?",
        "365",
        "340",
        "325",
        "320",
        1,
    ],
    ["How many minutes are there in an hour?", "30", "45", "70", "60", 4],
    ["How many seconds make one hour?", "3600", "3000", "6000", "4200", 1],
    ["Baby frog is known as.......?", "Catterpillar", "Tadpole", "Larva", "cub", 2],
    [
        "How many consonants are there in the English alphabet?",
        "20",
        "18",
        "22",
        "21",
        4,
    ],
    ["Name the National bird of India?", "Parrot", "Sparrow", "Peacock", "Crow", 3],
    ["Name the National animal of India?", "Lion", "Tiger", "Elephant", "Giraffe", 2],
    ["Name the national flower of India?", "Lotus", "Lily", "Sunflower", "Hibiscus", 1],
    [
        "Name the National tree of India?",
        "Mango Tree",
        "Banyan Tree",
        "Coconut Tree",
        "Banana Tree",
        2,
    ],
    [
        "Name the National river of India?",
        "Yamuna",
        "Ganga",
        "Brahmaputra",
        "Saraswati",
        2,
    ],
    [
        "Name the biggest continent in the world?",
        "South America",
        "Europe",
        "Africa",
        "Asia",
        4,
    ],
]

levels = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
    70000000,
]
money = 0
print(
    '\n\n***** Namaskaar, Deviyon or Sajjanon, "KAUN BANEGA CROREPATI" mei aapka swaagat hai! *****'
)
print("          Ummed hai aap yaha se bahut bhaari raashi jeet ke jaayenge!")
count = 1
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Mahashay, {count} prashn {levels[i]} rupay ka ye raha aapke screen pe")
    print(question[0])
    print("Aapke options hain :")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    reply = int(input("Uttar Dijiye (0 for quit)\n"))
    if reply == 0 and count == 1:
        money = 0
        break
    if reply == 0:
        money = levels[i - 1]
        break
    if reply == question[-1]:
        print(f"Bilkul Sahi jaawab {levels[i]} rupay jeet gaye aap\n")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
        elif 16:
            money = 70000000
    else:
        print("Ye ek galat jawaab hai!")
        break
    count = count + 1
if money != 0:
    print(f"Ye raha aapaka {money} Rupay Cheque!!!")
print("KAUN BANEGA CROREPATI khelne ke liye bahut bahut Dhanyawaad")
