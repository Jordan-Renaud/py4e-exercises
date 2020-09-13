
def computepay(h,r):
    if hours < 40:
        return hours * rate
    return (hours - 40) * 1.5 * rate + (40 * rate)


hours_raw = input("Enter Hours: ")
rate_raw = input("Enter Rate: ")

hours = float(hours_raw)
rate = float(rate_raw)

pay_total = computepay(hours, rate)
print("Pay",pay_total)
