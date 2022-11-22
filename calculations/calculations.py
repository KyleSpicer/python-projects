#!/usr/bin/env python
import math


def main():  # try/except takes user input and casts to correct function.
    user_provided = input('\nEnter a word or number: ')

    try:
        value = float(user_provided)
        temp = int(value)
        if value == temp:
            value = temp

    except ValueError:
        demo_text(user_provided)

    else:
        calculations(value)
        more_calculations(value)
        print('#' * 73)
        print('With the calculations working better, \
lets move on to some word problems:')
        print('#' * 73)
        print()
        siblings()
        utilities()
        subway()
        print(f'{user_provided} was your original input.')


def calculations(val):  # takes user provided integer to complete equations.
    print(f'{val} is the number you entered.\n')
    
    dec = val / 19

    print(f'{dec:<30}')
    print(f'{dec:>30}')
    print(f'{dec:^30}')
    print()

    if type(val) is int:
        print(f'-{val} =', -val)
        print(f'{val}² =', val ** 2)
        print(f'Hex value of {val} is {hex(val)}.')
        print(f'Hex value can also be shown as {val:x}.')
        print(f'Octal value can be shown as {val:o}'.format(val))

    print(f'{val} + 35 = {val + 35}.')
    print(f'{val} - 91 = {val - 91}.')
    print(f'{val} ÷ 3 = {val / 3}.')
    print(f'{val} × 100 = {val * 100}.')
    print()

    solution_2 = (17 - 5 / (4/5) * 4 + 12)
    print(f'The equation: 17 - 5 ÷ ⅘ × 4 + 12 evaluates to: {solution_2}.\n')

    print('When a number becomes large, it is often beneficial \
to include a thousands separator.')
    larger = dec * 1000000
    print(f'The number {larger} with separators looks like: {larger:,.2f}')
    print()

    a, b, c, d, e = 7, 8, 3, 2, 4
    solution = (a - b) ** 2 + c * d - e ** 2
    print(f'The equation ({a} - {b})² + {c} x {d} - {e}² evaluates \
to: {solution}.')
    print()


def more_calculations(val):  # takes user provided integer in equations below.
    print('In mathematical notation ⌊x] represents the floor of a number.')
    print('which is the largest integer no larger than x')
    print(f'⌊{val} ÷ 3⌋ =', math.floor(val / 3))
    print(f'⌊{val} ÷ 7⌋ =', math.floor(val / 7))
    print()

    print('In mathematical notation ⌈x⌉ represents the ceiling of a number.')
    print('which is the smallest integer no smaller than x')
    print(f'⌈{val} ÷ 3⌉ =', math.ceil(val / 3))
    print(f'⌈{val} ÷ 7⌉ =', math.ceil(val / 7))
    print()

    original = val
    val += 17
    print(f'The value "val" is increased by 17 and has a new value of {val}.')
    val -= 17
    print(f'The value "val" is decrease by \
17 back to its oringal value of {original}.')
    print()
    print(f'The following shows 3 times the absolute value of {val} minus 1:')
    print(f'3 × |{val}| - 1 = {3 * abs(val) - 1}')
    print()

    a = b = c = d = val
    print('id of a =', id(a))
    print('id of b =', id(b))
    print('id of c =', id(c))
    print('id of d =', id(d))
    print('id of val =', id(val))
    print(f'''From the id's above it is apparent that there is 1 instance of \
{val} in memory.''')
    print()


def siblings():  # determines how old Frankie's sibling is
    print('When Frankie was 2 years old,')
    young_frankie = 2
    print('Frankie had a sibling who was 3 times as old.')
    sibling = young_frankie * 3
    print('If Frankie is now 50, how old is the sibling?')
    old_frankie = 50
    old_sibling = (sibling - young_frankie) + old_frankie
    print(f'''That would make Frankie's sibling {old_sibling} years old.''')
    print()


def utilities():  # determines discounted amount owed by one of the roomates.
    print('''It's the beginning of the month and \
time to pay rent and utilities.''')
    print('The four roomates normally split the bills evenly, but this month \
all are in agreement that the one roomate who is between jobs will only be \
responsible for paying 3/4ths of the original monthly obligation.')

    roommates = 4
    discount = (3/4)

    print('Rent is $2,400.00, Water is $57.56, \
Gas and Electric combined is $315.82, \
having cut the cord, internet & streaming \
services come to a total of $95.\n')

    rent = 2400
    water = 57.56
    gas_electric = 315.82
    internet_stream = 95
    total_due = rent + water + gas_electric + internet_stream
    amount_due = (total_due / 3.75) * 0.75

    print(f'The total amount due comes to: \
${total_due}')
    print('The amount that the roommate between jobs \
owes is', f'${amount_due:.2f}.')
    print()


def subway():  # calculates averages for New York subway rides in a given year.
    print('According to Wikipedia: \
"https://en.wikipedia.org/wiki/New_York_City_Subway"')

    print('The New York subway offers service 24 \
hours per day, every day of the year.')

    service_hours = 24  # hours in a day
    day_per_week = 7  # 7 days in a week
    weeks_in_year = 52  # days in a year
    print('Averaging approximately 5.6 million daily rides on weekdays.')
    weekdays = 5600000  # 5.6 mil rides
    print('3.2 million on Saturdays')
    saturdays = 3200000  # 3.2 mil rides
    print('2.5 million on Sundays')
    sundays = 2500000  # 2.5 mil rides
    print()

    hour_avg = (((weekdays * 5) + saturdays + sundays) /
                day_per_week / service_hours)
    total_rides = ((weekdays * 5) + saturdays + sundays) * weeks_in_year

    print(f'For any given week, the average rides per hour \
are {hour_avg:,.0f}.')
    print(f'The average rides per weekday are {weekdays:,}.')
    print(f'Based on the above figures, there \
are approxiamately, {total_rides:,} rides each year.')


def demo_text(val):  # will run if the user provides a word instead of number.
    print(f'{val} is the word you entered')
    print(f'{val} is', len(val), 'characters long')
    print(f'{val}{val}{val} is', val + val + val)
    print('Calculating the character after the letter \
A can be done as: chr(ord("A") + 1). Which will return \
the result:', chr(ord("A") + 1))
    print(f'If the length of your word is, {len(val)}, \
Then the character, {len(val)}, more than the letter X is',
          chr(ord('X') + len(val)))
    print(f'The type and id of your word are as follows: \
type is {type(val)} and id is {id(val)}')


if __name__ == '__main__':
    main()
