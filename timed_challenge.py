# Timed Challenge: First Repeated Value
# Return the first value that repeats in the collection.
#
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    if not isinstance(values, list):
        return None

    seen = set()

    for value in values:
        if value in seen:
            return value

        seen.add(value)

    return None


# Tests
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))
print(first_repeated_value([1, 2, 3, 4, 5]))
print(first_repeated_value([]))
print(first_repeated_value([5, 5]))
print(first_repeated_value("not a list"))