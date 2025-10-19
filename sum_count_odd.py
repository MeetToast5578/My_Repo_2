# Daxil edilmiş natural ədədin tək rəqəmlərinin
# sayına bərabər olan rəqəmlərin cəmini çıxışa
# verən proqram tərtib edin.

# Məsələn, 234522 - burda 3 və 5 təkdir,
# sayı 2 edir. Ədəddə olan 2-lərin cəmi çıxışa gedir 2+2+2 = 6

def sum_count_odd(number):
    digit_list = []
    count_odd = 0
    sum = 0

    while number > 0:
        digit = number % 10
        if digit % 2 == 1:
            count_odd+=1
        digit_list.append(digit)
        number//=10
    for item in digit_list:
        if item == count_odd:
            sum += item
    print(sum)


number_ = 234522
sum_count_odd(number_)