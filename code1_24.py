kg = int(input("身長(cm)を入力>>"))
cm = int(input("体重(kg)を入力>>"))
cm /= 100
bmi = kg / cm / cm
print(f"あなたのBMIは{bmi}です。")