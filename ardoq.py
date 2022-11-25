import sys


def highest_product_short_version(numbers: list) -> int:
    """
    arg numbers: a list of integers
    Returns an integer that is the product of the 3 biggest list elements
    """
    if len(numbers) < 3:
        print("Not enough numbers to compute a result.Exiting gracefully...")
        sys.exit(0)

    numbers.sort()
    return max(
        numbers[-1] * numbers[-2] * numbers[-3], numbers[0] * numbers[1] * numbers[-1]
    )


def highest_product_optimized(numbers: list) -> int:
    """
    arg numbers: a list of integers
    Returns an integer that is the product of the 3 biggest list elements
    """
    if len(numbers) < 3:
        print("Not enough numbers to compute a result.Exiting gracefully...")
        sys.exit(0)

    smallest_two = [float("inf")] * 2
    largest_three = [float("-inf")] * 3
    for num in numbers:
        if num <= smallest_two[0]:
            smallest_two[0] = num
            smallest_two.sort(reverse=True)
        if num >= largest_three[0]:
            largest_three[0] = num
            largest_three.sort()
    return max(
        smallest_two[0] * smallest_two[1] * largest_three[2],
        largest_three[0] * largest_three[1] * largest_three[2],
    )


if __name__ == "__main__":
    assert highest_product_short_version([1, 2, 3]) == 6
    assert highest_product_short_version([1, 3, 5, 2, 6]) == 90
    assert highest_product_short_version([-1, -4, 5, -3]) == 60
    assert highest_product_optimized([1, 2, 3]) == 6
    assert highest_product_optimized([1, 3, 5, 2, 6]) == 90
    assert highest_product_optimized([-1, -4, 5, -3]) == 60
