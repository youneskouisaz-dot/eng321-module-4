
import math
import pytest

from calculation import calculate_volume
from iteration import solve_tank


# TEST 1: Verify the engineering calculation
def test_volume_calculation():
    result = calculate_volume(3, 5)
    expected = math.pi * (3 / 2) ** 2 * 5

    assert result == pytest.approx(expected)


# TEST 2: Solver reaches the target
def test_solver_convergence():
    result = solve_tank(
        target_volume=100,
        height=5,
        starting_diameter=3,
        tolerance=0.05,
        max_iterations=50
    )

    assert result["status"] == "CONVERGED"
    assert result["error"] <= 0.05


# TEST 3: Invalid input is rejected
def test_invalid_input():
    result = solve_tank(
        target_volume=-100,
        height=5,
        starting_diameter=3,
        tolerance=0.05,
        max_iterations=50
    )

    assert result["status"] == "INVALID INPUT"


# TEST 4: Solver respects maximum iterations
def test_max_iterations():
    result = solve_tank(
        target_volume=100,
        height=5,
        starting_diameter=1,
        tolerance=0.000001,
        max_iterations=1
    )

    assert result["status"] == "NOT CONVERGED"
    assert result["iterations"] == 1


# TEST 5: Iteration history is recorded
def test_iteration_history():
    result = solve_tank(
        target_volume=100,
        height=5,
        starting_diameter=3,
        tolerance=0.05,
        max_iterations=50
    )

    assert len(result["history"]) == result["iterations"]
    assert result["history"][0]["Iteration"] == 1
