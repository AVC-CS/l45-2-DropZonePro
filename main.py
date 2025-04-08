import random


def main():
    total = 0
    numbers = []

    i = 0

    while i < 100:
        randnum = random.randint(1, 100)
        numbers.append(randnum)
        i += 1
        if sum(numbers) > 100:
            numbers.pop()
            break

    total = sum(numbers)

    numbers = numbers + [randnum]

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
