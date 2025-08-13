# 🚇 Metro Journey Planner

A Python-based web application to find the most **time-efficient** routes between metro stations using **Dijkstra's Algorithm**.  
Built with **Streamlit** for an interactive and user-friendly experience.

---

## ✨ Features
- **Route Optimization**:  
  - **Time Mode** – Calculates the fastest route considering travel and transfer times.  
  - **Distance Mode** – Calculates the shortest route based on distance.
- **Interactive Graph Visualization** – Displays the metro map with stations and lines.
- **Interchange Detection** – Shows where a passenger needs to change lines.

---

## 📂 Project Structure
- app.py # Streamlit app interface
- dijkstra.py # Dijkstra's algorithm implementation
- interchanges.py # Function to detect line interchanges
- metro_graph.py # Reads CSV files and generates metro graph
- delhi_metro.csv # Station details
- mumbai_metro.csv # Station details
- requirements.txt # Python dependencies
- README.md # Project documentation

---

## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **NetworkX**
- **Matplotlib**
---

## 📊 Algorithm – Dijkstra's
- Uses a priority queue (`heapq`) to always expand the node with the smallest current cost.
- Supports two optimization modes:
  - **Time**
  - **Distance**

---

## 🔄 Interchange Detection
- Compares the line of the current station with the previous one.
- Marks points where the line changes as interchange stations.

---

## 🌐 Access the App
You can try the live Metro Journey Planner here:  
**[🔗 Click to Open App](https://metro-journey-planner.streamlit.app/)**

---
