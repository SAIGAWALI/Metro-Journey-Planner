import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from metro_graph import create_metro_graph, get_cities
from dijkstra import dijkstra
from interchanges import get_interchanges

st.set_page_config(page_title="Metro Journey Planner", layout="centered")

# Sidebar
st.sidebar.title("🧭 Navigation")
selected_map_city = st.sidebar.selectbox("View Metro Map for City:", get_cities())
show_map_only = st.sidebar.checkbox("Show Map Only")

st.sidebar.title("ℹ️ Instructions")
st.sidebar.markdown("""
- Select a city to plan your metro journey.
- Choose source and destination stations.
- round trip is also available.
- Use the sidebar to view only the metro map.
""")

# Assign colors to lines
line_colors = {
    "B": "blue",
    "Y": "#FFD700",
    "R": "red",
    "G": "green",
    "P": "purple",
    "O": "orange"
}

# Get edge color
def get_edge_color(u, v):
    u_line = u.split("~")[-1]
    v_line = v.split("~")[-1]
    if u_line == v_line:
        return line_colors.get(u_line, "black")
    return "gray"  # its for interchanges or unmatched lines




# Draw map function
def draw_metro_map(graph, highlight_path=None):
    G = nx.Graph()

    # Add edges with weights
    for u in graph:
        for v, w in graph[u].items():
            G.add_edge(u, v, weight=w)

    # Assign colors to each edge based on the station lines
    edge_colors = [get_edge_color(u, v) for u, v in G.edges()]

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(16, 12))

    # Draw base network
    nx.draw_networkx_nodes(G, pos, node_size=50)
    nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color=edge_colors)
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)

    # Highlight path if given
    if highlight_path:
        path_edges = list(zip(highlight_path, highlight_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="black", width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_path, node_color="red", node_size=80)

    st.pyplot(plt)

# Show only map
if show_map_only:
    graph = create_metro_graph(selected_map_city)
    draw_metro_map(graph)
    st.stop()

# Main planner
st.title("🚇 Metro Journey Planner")

city = st.selectbox("Select City:", get_cities())
graph = create_metro_graph(city)
stations = sorted(graph.keys())

src = st.selectbox("Select Source Station:", stations)
dst = st.selectbox("Select Destination Station:", stations)
opt_type = st.radio("Optimize For:", ["distance", "time"])
round_trip = st.checkbox("Plan Round Trip")

if st.button("Get Shortest Path"):
    if src == dst:
        st.warning("Source and destination cannot be the same.")
    else:
        result = dijkstra(graph, src, dst, optimize_for=opt_type)
        if result:
            st.success("Path Found!")
            st.markdown("**Path:**")
            st.code(" → ".join(result["path"]))

            if opt_type == "time":
                original = result['time_minutes']
                st.markdown(f"**Estimated Time:** {original} min")
            else:
                st.markdown(f"**Total Distance:** {result['cost']} km")

            interchanges = get_interchanges(result["path"])
            st.markdown(f"**Interchanges:** {len(interchanges)}")
            for i, (from_station, to_station) in enumerate(interchanges, 1):
                st.code(f"{i}. {from_station} ==> {to_station}")

            draw_metro_map(graph, result["path"])

            if round_trip:
                st.markdown("---")
                st.subheader("🔁 Return Trip")
                return_result = dijkstra(graph, dst, src, optimize_for=opt_type)
                if return_result:
                    st.code(" → ".join(return_result["path"]))
                    if opt_type == "time":
                        original_back = return_result['time_minutes']
                        st.markdown(f"**Estimated Time:** {original_back} min")
                    else:
                        st.markdown(f"**Total Distance:** {return_result['cost']} km")

                    interchanges_back = get_interchanges(return_result["path"])
                    st.markdown(f"**Interchanges:** {len(interchanges_back)}")
                    for i, (from_station, to_station) in enumerate(interchanges_back, 1):
                        st.code(f"{i}. {from_station} ==> {to_station}")
                else:
                    st.warning("Return path not found.")
        else:
            st.error("No path found between selected stations.")
