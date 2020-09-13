hours_raw = input("Enter Hours: ")
hours = float(hours_raw)
rate_raw = input("Enter Rate: ")
rate = float(rate_raw)
pay = 0

if hours > 40:
  pay = (hours - 40) * 1.5 * rate + (40 * rate)
else:
  pay = hours * rate

print pay
