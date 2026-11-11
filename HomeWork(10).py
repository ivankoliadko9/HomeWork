def digital_root(n):
    n = abs(n)

    if n < 10:
        return n

    digit_sum = sum(int(digit) for digit in str(n))

    return digital_root(digit_sum)


# Автотесты
assert digital_root(9875) == 2
assert digital_root(123) == 6
assert digital_root(9999) == 9
assert digital_root(5) == 5
assert digital_root(0) == 0

print("Цифровий корінь", digital_root(9875))
print("Автотест пройшов успішно")