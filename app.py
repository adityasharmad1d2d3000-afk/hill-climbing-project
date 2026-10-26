import streamlit as st

st.set_page_config(page_title="Hill Climbing Search Visualizer", layout="wide")
st.title("Hill Climbing Search Visualizer")
st.caption("Artificial Intelligence & Soft Computing | Python + Streamlit")

STATES = {
    "A": {"value": 2, "neighbors": ["B", "C"]},
    "B": {"value": 5, "neighbors": ["A", "D", "E"]},
    "C": {"value": 3, "neighbors": ["A", "F"]},
    "D": {"value": 7, "neighbors": ["B", "G"]},
    "E": {"value": 6, "neighbors": ["B", "G"]},
    "F": {"value": 4, "neighbors": ["C", "G"]},
    "G": {"value": 8, "neighbors": ["D", "E", "F"]},
}
EDGES = [("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("D","G"),("E","G"),("F","G")]

def initialize():
    st.session_state.current = "A"
    st.session_state.visited = ["A"]
    st.session_state.moves = 0
    st.session_state.done = False
    st.session_state.log = ["Start at A (value 2)."]
    st.session_state.message = "Start at A. Compare its neighbors and move to a better one."

def hill_climbing_step():
    if st.session_state.done:
        return
    current = st.session_state.current
    current_value = STATES[current]["value"]
    neighbors = STATES[current]["neighbors"]
    candidates = sorted(neighbors, key=lambda sid: STATES[sid]["value"], reverse=True)
    best_neighbor = candidates[0]
    best_value = STATES[best_neighbor]["value"]
    if best_value <= current_value:
        st.session_state.done = True
        st.session_state.message = f"Stop at {current} (value {current_value}): no neighbor has a higher value."
        st.session_state.log.insert(0, f"No neighbor improves {current}. Search stops at value {current_value}.")
        return
    st.session_state.current = best_neighbor
    st.session_state.visited.append(best_neighbor)
    st.session_state.moves += 1
    st.session_state.message = f"Move from {current} ({current_value}) to {best_neighbor} ({best_value}), the highest-valued neighbor."
    st.session_state.log.insert(0, f"Move {current} -> {best_neighbor}: {current_value} -> {best_value}.")

if "current" not in st.session_state:
    initialize()

current = st.session_state.current
m1, m2, m3 = st.columns(3)
m1.metric("Current state", current)
m2.metric("State value", STATES[current]["value"])
m3.metric("Moves made", st.session_state.moves)

left, right = st.columns([1.4, 1])
with left:
    st.subheader("State graph")
    st.write("Each node has a value. Higher values are better in this example.")
    lines = ["graph Search {", 'graph [bgcolor="transparent", overlap=false];',
             'node [shape=circle, style=filled, fontname="Arial", fontsize=12, width=1.0, height=1.0];',
             'edge [color="#B8C7D6", penwidth=2];']
    for sid, data in STATES.items():
        if sid == current and st.session_state.done:
            fill, border = "#FFE7C9", "#C47A19"
        elif sid == current:
            fill, border = "#D5F4ED", "#15947E"
        elif sid in st.session_state.visited:
            fill, border = "#DCE9F8", "#3976B8"
        else:
            fill, border = "#FFFFFF", "#7890A8"
        lines.append(f'{sid} [label="{sid}\nValue: {data["value"]}", fillcolor="{fill}", color="{border}", penwidth=2];')
    for a, b in EDGES:
        color = "#23A18D" if a in st.session_state.visited and b in st.session_state.visited else "#B8C7D6"
        lines.append(f'{a} -- {b} [color="{color}"];')
    lines.append("}")
    st.graphviz_chart("\n".join(lines), use_container_width=True)

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("Next Step", use_container_width=True, disabled=st.session_state.done):
            hill_climbing_step()
            st.rerun()
    with b2:
        if st.button("Run to End", use_container_width=True, disabled=st.session_state.done):
            for _ in range(20):
                if st.session_state.done:
                    break
                hill_climbing_step()
            st.rerun()
    with b3:
        if st.button("Reset", use_container_width=True):
            initialize()
            st.rerun()

with right:
    st.subheader("Algorithm status")
    st.info(st.session_state.message)
    st.markdown("**Rule:** Choose the highest-valued neighbor, but move only if it improves the current value.")
    st.subheader("Execution log")
    for i, entry in enumerate(st.session_state.log, start=1):
        st.write(f"**{i}.** {entry}")

st.divider()
st.subheader("How it works")
st.markdown("1. Start at an initial state.\n2. Check its neighboring states.\n3. Select the neighbor with the highest value.\n4. Move only if that value is higher than the current state's value.\n5. Stop when no neighbor is better.\n\n**Expected path:** A (2) -> B (5) -> D (7) -> G (8)\n\n**Limitation:** Hill Climbing can get stuck at a local optimum and does not guarantee the global optimum.")

with st.expander("View the core Python algorithm"):
    st.code("candidates = sorted(neighbors, key=lambda sid: STATES[sid]['value'], reverse=True)\nbest_neighbor = candidates[0]\n\nif STATES[best_neighbor]['value'] <= current_value:\n    done = True\nelse:\n    current = best_neighbor\n", language="python")
