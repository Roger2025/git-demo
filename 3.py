# 1.加入例外處理  try_except Exception as e
# 2.重複輸入,直到a=>exit 離開,使用while true

while True:
    try:
        a = input("請輸入a:")
        if a == "exit":
            print("離開程式")
            break
        a = eval(a)
        b = eval(input("請輸入b:"))
        if a == b:
            print("a跟b一樣大")
        elif a > b:
            print(f"a>b,相差:{a-b}")
        else:
            print(f"a<b,相差:{b-a}")
    except Exception as e:
        print(f"輸入錯誤!錯誤訊息為:{e}")
