temp = float(input("what's the temp today (in celcius)?"))
print(f"{'Freezing' if temp < 0 else 'normal' if temp < 20 else 'Hot'}")