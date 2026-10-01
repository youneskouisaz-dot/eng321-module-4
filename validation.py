
import math


def validate_inputs(target_volume, height, starting_diameter,
                    tolerance, max_iterations):
    """
    Validate user inputs before running the solver.

    Raises ValueError if any input is invalid.
    """

    inputs = {
        "Target volume": target_volume,
        "Tank height": height,
        "Starting diameter": starting_diameter,
        "Tolerance": tolerance
    }

    # All engineering values must be positive and finite
    for name, value in inputs.items():

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a number.")

        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be positive and finite.")

    # Maximum iterations must be a positive whole number
    if (isinstance(max_iterations, bool)
            or not isinstance(max_iterations, int)
            or max_iterations <= 0):

        raise ValueError(
            "Maximum iterations must be a positive integer."
        )

    return True


# Quick validation check
if __name__ == "__main__":

    validate_inputs(
        target_volume=100,
        height=5,
        starting_diameter=3,
        tolerance=0.05,
        max_iterations=50
    )

    print("All inputs are valid.")
