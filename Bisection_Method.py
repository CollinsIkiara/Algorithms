# Bisection Method for finding roots of a function

# The bisection method is a numerical method for finding roots of continuous functions. It works by repeatedly bisecting an interval and then selecting a subinterval in which a root must lie. This method is guaranteed to converge if the function changes signs over the interval.
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target in (0, 1):
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid ** 2

        if abs(high - low) <= tolerance:
            root = mid
            break
        elif square_mid < square_target:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

    print(f"The square root of {square_target} is approximately {root}")
    return root


# Example uses
square_root_bisection(0)
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(0.25, 1e-7, 50)
square_root_bisection(1)
square_root_bisection(81, 1e-3, 50)
square_root_bisection(225, 1e-3, 100)
square_root_bisection(225, 1e-5, 100)
square_root_bisection(225, 1e-7, 100)
square_root_bisection(225, 1e-7, 10)

## Output:
# The square root of 0 is 0
# The square root of 0.001 is approximately 0.03162277660168379
# The square root of 0.25 is approximately 0.5
# The square root of 1 is 1
# The square root of 81 is approximately 9.000000000000002
# The square root of 225 is approximately 15.000200271606445
# The square root of 225 is approximately 15.000002458691597
# The square root of 225 is approximately 15.000000022700988
# Failed to converge within 10 iterations