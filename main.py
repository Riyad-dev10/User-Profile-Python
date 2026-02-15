import random
from datetime import datetime  # باش نجيبو العام الحالي

# 1. نجيبو العام الحالي بطريقة أوتوماتيكية
current_year = datetime.now().year

# 2. نديرو حلقة (Loop) باش لو كان يغلط في العمر البرنامج ما يحبسش
while True:
    try:
        name = input("What is your name? ")
        age_input = input("How old are you? ")
        age = int(age_input)  # هنا نحولو النص لرقم
        break  # إذا فات هنا يعني الرقم صحيح، نخرجوا من الحلقة
    except ValueError:
        print("❌ خطأ: لازم تكتب العمر بالأرقام (مثلا: 17)!")

country = input("Where are you from? ")

# حساب سنة الميلاد بالدقة
birth_year = current_year - age

# القائمة تاعك راهي هايلة
motivations = [
    "Keep pushing, you got this!",
    "Every day is a new chance to improve!",
    "Believe in yourself, always!",
    "Small steps lead to big results!"
]
message = random.choice(motivations)

# 3. العرض باستعمال f-strings (أنقى وأوضح)
print(f"\n--- Your Info ---")
print(f"Name:       {name.capitalize()}") # يخلي أول حرف كبير
print(f"Age:        {age}")
print(f"Birth Year: {birth_year}")
print(f"Country:    {country.capitalize()}")
print(f"\nMotivational Message: {message}")
print("-" * 17)
