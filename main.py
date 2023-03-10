def sum_list(lst):  # this finds the sum
    sum = 0
    for i in lst:
        sum += i
    return sum

def product_list(lst):  # this finds the product
    product = 1
    for i in lst:
        product *= i
    return product

def reverse_list(lst):
    return list(reversed(lst))

def main():  # This calls above functions
    response = ""
    numbers = []
    while response.lower() != 'x':
        response = input("Enter a number or x to stop\n")
        if response.lower() == 'x':
            break
        numbers.append(int(response))
    print(f'Sum of Numbers: {sum_list(numbers)}')
    print(f'Product of Numbers: {product_list(numbers)}')
    print(f'Reverse of Numbers: {reverse_list(numbers)}')

if __name__ == "__main__":
    main()