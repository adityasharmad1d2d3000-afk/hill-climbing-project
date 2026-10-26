HILL CLIMBING SEARCH VISUALIZER - PYTHON + STREAMLIT

FILES
- app.py: Python algorithm and Streamlit interface
- requirements.txt: dependency list
- README.txt: setup and viva notes

RUN LOCALLY
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run: python -m pip install -r requirements.txt
4. Run: python -m streamlit run app.py
5. Open the local URL shown in the terminal if a browser does not open automatically.

IMPLEMENTATION
- Each state has a value and a list of neighbors.
- The algorithm sorts the current state's neighbors by value, highest first.
- It moves to the highest-valued neighbor only when that value exceeds the current value.
- It stops when no neighbor improves the current value.
- Expected path: A(2) -> B(5) -> D(7) -> G(8), then stop.

VIVA NOTES
- Language: Python; UI framework: Streamlit.
- Hill Climbing is a heuristic/local-search algorithm.
- State: a possible position or solution.
- Neighbor: a state reachable in one move.
- Evaluation value: a score used to compare states; this example maximizes the score.
- Advantage: simple and memory-efficient.
- Limitation: can get stuck at a local optimum, plateau, or ridge; does not guarantee the global optimum.
- This is a fixed teaching example, not a general-purpose solver.
