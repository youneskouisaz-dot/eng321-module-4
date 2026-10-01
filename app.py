
import streamlit as st
import pandas as pd

from iteration import solve_tank


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Cylindrical Tank Goal Seek",
    page_icon="📐",
    layout="wide"
)


# TITLE
st.title("Cylindrical Tank Diameter Goal Seek")

st.write(
    "An iterative engineering solver that automatically "
    "adjusts the tank diameter to reach a target volume."
)


# SIDEBAR INPUTS
st.sidebar.header("Engineering Inputs")

target_volume = st.sidebar.number_input(
    "Target Volume (ft³)",
    value=100.0,
    format="%.3f"
)

height = st.sidebar.number_input(
    "Tank Height (ft)",
    value=5.0,
    format="%.3f"
)

starting_diameter = st.sidebar.number_input(
    "Starting Diameter (ft)",
    value=3.0,
    format="%.3f"
)

tolerance = st.sidebar.number_input(
    "Tolerance (ft³)",
    value=0.05,
    format="%.5f"
)

max_iterations = st.sidebar.number_input(
    "Maximum Iterations",
    min_value=1,
    value=50,
    step=1
)


# RUN BUTTON
if st.sidebar.button("Calculate", type="primary"):

    result = solve_tank(
        target_volume=target_volume,
        height=height,
        starting_diameter=starting_diameter,
        tolerance=tolerance,
        max_iterations=max_iterations
    )

    st.header("Solver Results")

    status = result["status"]

    # CONVERGED
    if status == "CONVERGED":

        st.success("CONVERGED: Target reached successfully.")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Final Diameter",
            f"{result['diameter']:.4f} ft"
        )

        col2.metric(
            "Calculated Volume",
            f"{result['volume']:.4f} ft³"
        )

        col3.metric(
            "Final Error",
            f"{result['error']:.6f} ft³"
        )

        col4.metric(
            "Iterations",
            result["iterations"]
        )

    # NOT CONVERGED
    elif status == "NOT CONVERGED":

        st.warning("NOT CONVERGED")

        st.write(result["message"])

        st.write(
            f"Iterations completed: {result['iterations']}"
        )

        st.write(
            f"Last calculated error: {result['error']:.6f} ft³"
        )

        st.info(
            "No successful engineering solution was produced. "
            "Try a different starting diameter or increase "
            "the maximum iteration limit."
        )

    # INVALID INPUT
    else:

        st.error("INVALID INPUT")

        st.write(result["message"])


    # ITERATION HISTORY
    if result["history"]:

        st.subheader("Iteration History")

        history_df = pd.DataFrame(result["history"])

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        # PROGRESS CHART
        st.subheader("Iteration Progress")

        chart_df = history_df.set_index("Iteration")

        st.line_chart(
            chart_df[
                [
                    "Calculated Volume (ft³)",
                    "Error (ft³)"
                ]
            ]
        )


# ASSUMPTIONS AND LIMITATIONS
with st.expander("Engineering Assumptions & Limitations"):

    st.write("""
    - The tank is assumed to be a perfect cylinder.
    - All dimensions are expressed in feet.
    - Volume is calculated in cubic feet.
    - Tank height remains constant.
    - Only the diameter is adjusted.
    - The solver uses Newton's iterative method.
    - Convergence occurs when absolute error is
      less than or equal to the selected tolerance.
    - Maximum iterations prevent an unlimited loop.
    - This is a synthetic educational engineering example.
    """)
