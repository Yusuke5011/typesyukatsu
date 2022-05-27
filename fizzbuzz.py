for num in range(1, 101):
    string = ''

    # ここから記述
    
    if num % 3 == 0 and i % 5 == 0:　
    # numが３の倍数かつ５の倍数（15の倍数）の時
        print("FizzBuzz")
    elif num % 3 == 0:
    # numが15の倍数ではなく3の倍数の時
        print("Fizz")
    elif num % 5 == 0:
    # numが15の倍数でも、３の倍数でもなく、5の倍数の時
        print("Buzz")
    else:
    # それ以外の時
        print(i) 
        
    # ここまで記述

    print(string)
