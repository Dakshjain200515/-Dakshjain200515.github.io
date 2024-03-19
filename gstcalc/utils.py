# Inside gstcalc/utils.py

def calculate(weight, rate):
    amount = (weight * rate / 10)
    gst = (amount * 0.03)
    tds = (amount * 0.001)
    final_amount = amount + gst - tds
    return amount, gst, tds, final_amount
