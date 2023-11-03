password1 = input("لطفاً پسورد اول را وارد کنید: ")
password2 = input("لطفاً پسورد دوم را وارد کنید: ")

while password1 != password2:
    print("پسوردها متفاوت است!")
    password1 = input("لطفاً پسورد اول را دوباره وارد کنید: ")
    password2 = input("لطفاً پسورد دوم را دوباره وارد کنید: ")

print("پسوردها یکسان هستند!")
