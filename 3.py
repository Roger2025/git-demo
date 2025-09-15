lis = ["a", "b"]
num = []

print("請使用者輸入a跟b兩個數字 判斷a,b的關係!")

for i in lis:
    print(f"使用者請輸入{i}:", end="")
    i = float(input())
    num.append(i)

if num[0] > num[1]:
    print(f"a比b大{num[0]-num[1]:.2f}")
elif num[0] == num[1]:
    print(f"a跟b一樣大")
else:
    print(f"b比a大{num[1]-num[0]:.2f}")
