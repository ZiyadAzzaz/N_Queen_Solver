# ♟️ N-Queens Solver (BFS & DFS)

A Python-based solver for the classic N-Queens problem — implemented using both **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.  
This project compares the performance of the two algorithms and prints a sample solution on the board.

🎯 Developed as part of an AI fundamentals course by **Ziyad Azzaz**.

---

## 📋 Overview

The **N-Queens problem** asks:  
> Can you place N queens on an N×N chessboard so that no two queens attack each other?

This project:
- ✅ Explores both BFS and DFS approaches  
- ✅ Measures time taken by each algorithm  
- ✅ Displays one possible solution on the board  
- ✅ Shows how constraint satisfaction works in AI search  

---

## 🧠 Features

- 🔎 **BFS Search**: Iterative search using queues  
- 🧭 **DFS with Backtracking**: Recursive and memory-efficient  
- ⏱️ **Performance Timer**: Measures execution time of each approach  
- 🎨 **Board Display**: Text-based board output with queen positions  
- 💻 **CLI Interaction**: User inputs `N` directly from terminal  

---

## 📂 Files

| File Name            | Description                            |
|----------------------|----------------------------------------|
| `n_queens_solver.py` | Main Python script                     |
| `README.md`          | Project documentation (this file)      |


👉 **[View the Full Code Here](https://github.com/ZiyadAzzaz/N_Queen_Solver/blob/main/n_queens_solver.py)**

---

## ▶️ How to Run

1. Make sure Python is installed (>= 3.6)

2. Clone this repo:
```bash
git clone https://github.com/ZiyadAzzaz/n-queens-solver.git
cd n-queens-solver
```

3. Run the program:
```bash
python3 n_queens_solver.py
```
## 🧪 Example Output (N = 4)

Welcome to the N-Queens Solver!
Enter the number of queens (N): 4

Solving the 4-Queens problem...

BFS found 2 solutions in 1.85 ms
DFS found 2 solutions in 0.42 ms

Here's one of the possible solutions:

. Q . .. . . QQ . . .. . Q .

Comparison Summary:
BFS Time: 1.85 ms
DFS Time: 0.42 ms

Thanks for trying the N-Queens Solver!
Made with ❤️ by Ziyad Azzaz 🧠 (AI Course Project)

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Modules:** `collections`, `time`

---

## 💡 Educational Purpose

This project was built to demonstrate:

- Basic constraint satisfaction  
- AI search strategies (DFS vs BFS)  
- Recursive and iterative problem solving  
- Performance trade-offs between search methods

---

## 👨‍💻 Author

**Ziyad Azzaz**  
🔗 GitHub: [ZiyadAzzaz](https://github.com/ZiyadAzzaz)

---

## 🪪 License

This project is open-source under the **MIT License**.  
✅ Free to use, modify, and share — especially for learning purposes!

