# Iterative Engineering Solver

This project replaces a manual spreadsheet goal-seek process with a Python-based iterative solver.

The program calculates the diameter required for a cylindrical tank to reach a target volume.

## Features

- Deterministic cylindrical tank calculation
- Iterative solver using Newton's Method
- User-defined starting diameter
- User-defined tolerance
- Maximum iteration limit
- Input validation
- Convergence detection
- Iteration history
- Streamlit user interface
- Automated tests with pytest

## Engineering Formula

The tank volume is calculated using:

V = π × r² × h

Where:

- V = Volume
- r = Radius
- h = Height
- Diameter = 2 × Radius

## Project Structure

```text
Engineering-Solver/
│
├── app.py
├── calculation.py
├── iteration.py
├── validation.py
├── requirements.txt
│
└── tests/
    └── test_solver.py
