import sys


def factorize_number(n):
    """Factorize a number into two smaller numbers.

    Args:
        n (int): The number to factorize.

    Returns:
        list[int]: A list containing the factorization of the number.
                   The first two elements are the smaller factors.

    """
    factors = []
    for index in range(2, n):
        if n % index == 0:
            factors.append(index)
            factors.append(n // index)
            break
    return factors


def factorize_file(file_name):
    """Factorize numbers from a file and print the factorizations.

    Args:
        file_name (str): The path to the file containing numbers to factorize.

    """
    with open(file_name, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_number(number)
            factorization = f"{number}={factors[0]}*{factors[1]}"
            print(factorization)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    factorize_file(file_name)
