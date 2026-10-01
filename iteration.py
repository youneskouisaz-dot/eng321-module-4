
import math

from calculation import calculate_volume
from validation import validate_inputs


def solve_tank(target_volume, height, starting_diameter,
               tolerance, max_iterations):

    """
    Iterative goal-seek solver for cylindrical tank diameter.
    """

    history = []

    # STEP 1: Validate inputs before iteration begins
    try:
        validate_inputs(
            target_volume,
            height,
            starting_diameter,
            tolerance,
            max_iterations
        )

    except ValueError as error:
        return {
            "status": "INVALID INPUT",
            "message": str(error),
            "diameter": None,
            "volume": None,
            "error": None,
            "iterations": 0,
            "history": []
        }

    # STEP 2: Start with the user's diameter guess
    diameter = starting_diameter

    # STEP 3: Iterative goal-seek process
    for i in range(1, max_iterations + 1):

        volume = calculate_volume(diameter, height)

        # Absolute difference from the target
        error = abs(target_volume - volume)

        # Save every attempt
        history.append({
            "Iteration": i,
            "Diameter (ft)": diameter,
            "Calculated Volume (ft³)": volume,
            "Error (ft³)": error
        })

        # STEP 4: Check convergence
        if error <= tolerance:

            return {
                "status": "CONVERGED",
                "message": "Target reached within tolerance.",
                "diameter": diameter,
                "volume": volume,
                "error": error,
                "iterations": i,
                "history": history
            }

        # STEP 5: Adjust the diameter using Newton's method
        derivative = (math.pi * height * diameter) / 2

        diameter = diameter + (
            target_volume - volume
        ) / derivative

        # Prevent invalid numerical updates
        if not math.isfinite(diameter) or diameter <= 0:
            break

    # STEP 6: If the solver did not converge
    last = history[-1]

    return {
        "status": "NOT CONVERGED",
        "message": "Maximum iterations reached or unsafe update.",
        "diameter": None,
        "volume": last["Calculated Volume (ft³)"],
        "error": last["Error (ft³)"],
        "iterations": len(history),
        "history": history
    }


# Quick example from the Excel workbook
if __name__ == "__main__":

    result = solve_tank(
        target_volume=100,
        height=5,
        starting_diameter=3,
        tolerance=0.05,
        max_iterations=50
    )

    print("STATUS:", result["status"])
    print("ITERATIONS:", result["iterations"])

    if result["status"] == "CONVERGED":
        print(f"Final Diameter: {result['diameter']:.4f} ft")
        print(f"Final Volume: {result['volume']:.4f} ft³")
        print(f"Final Error: {result['error']:.4f} ft³")

    print("\nITERATION HISTORY")

    for step in result["history"]:
        print(step)
