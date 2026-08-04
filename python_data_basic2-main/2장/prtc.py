temperature = 0
if temperature > 0:
    print("Ice Americano")
elif temperature == 0:
    print("plain Americano")
else:
    print("Hot Americano")


climate = "맑음"
if climate == "맑음":
    if temperature > 0:
        print("AA")
    elif temperature == 0:
        print("MA")
    else:
        print("DDA")
else:
    print("CPPCN")


mathScore = 10
engScore = 19

if engScore >= 90 or mathScore >= 90:
    print("MoneyInc")
elif 80 >= engScore or 80 >= mathScore:
    print("MoneyDec")
else:
    print("asIs")



scores = [80, 90, 70, 65, 85, 95, 90, 80, 75, 80, 100]
newScores = []

# for s in scores:
#     new = s + 5
#     newScores.append(new)
# print(newScores)
# scores.clear()

# for s in scores:
#     if s < 100:
#         new = s + 5
#     else:
#         new = s
#     newScores.append(new)
# print(newScores)

newScore2 = [s + 5 if s < 100 else s for s in scores]
print(newScore2)

scores = [80, 90, 70, 65, 95, 100, 90, 80, 75, 80, 100]
new_score = []
index = 0

while index < len(scores):#scores리스트 길이보다 작은 동안,
    if scores[index] < 100:#해당 인덱스의 점수가 100보다 작다면,
        new = scores[index] + 5 #해당 인덱스 아이템에 +5 한다음 new에 할당
    else:
        new = scores[index]#100이상이면 그대로
    new_score.append(new)
    index += 1
print(new_score)


time = 0
use = 0
while time < 300:
    time += 50
    print(time)
print("중단")