def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total_sum = 0

    for i, char in enumerate(isbn):
        if char == 'X' and i == 9:
            total_sum += 10 * (i + 1)
        elif char.isdigit():
            total_sum += int(char) * (i + 1)
        else:
            return False

    return total_sum % 11 == 0
