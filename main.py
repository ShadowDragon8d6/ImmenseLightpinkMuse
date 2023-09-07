def isfloat(num):
  period = 0
  for a in num:
    if a == ".":
      period = period + 1
    elif a.isdigit():
      pass
    else: 
      return False
  if period <= 1:
    if float(num) >= 0:
      return True
    else:
      return False
  else:
    return False
print(isfloat("02."))
body_fat_percentage = 0.12645
print(f"{body_fat_percentage:.2f}")