def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Знижка має бути від 0 до 100")

    return price - (price * discount_percent / 100)



assert calculate_discount(200.0, 15.0) == 170.0
assert calculate_discount(100.0, 50.0) == 50.0
assert calculate_discount(100.0, 0.0) == 100.0
assert calculate_discount(100.0, 100.0) == 0.0
assert calculate_discount(0.0, 50.0) == 0.0


try:
    calculate_discount(-100, 10)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100, 150)
    assert False
except ValueError:
    pass

print("Автотести пройшли успішно")