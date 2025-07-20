import time
from collections import deque

# Check if placing a queen at (row, col) is safe
def is_safe(queens, row, col):
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


# BFS approach to solve N-Queens
def solve_bfs(n):
    results = []
    q = deque([[]])  # Start with an empty state

    while q:
        state = q.popleft()
        row = len(state)

        if row == n:
            results.append(state)
        else:
            for col in range(n):
                if is_safe(state, row, col):
                    q.append(state + [col])

    return results


# DFS approach using backtracking
def solve_dfs(n, queens=[], row=0, results=[]):
    if row == n:
        results.append(queens[:])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve_dfs(n, queens, row + 1, results)
            queens.pop()

    return results


# Just to print one solution in a readable chessboard form
def show_board(solution, n):
    print("\nHere's one of the possible solutions:\n")
    for r in range(n):
        row = ['.'] * n
        row[solution[r]] = 'Q'
        print(" ".join(row))
    print()


# The main function to run the solver
def start():
    print("Welcome to the N-Queens Solver! ")
    try:
        n = int(input("Enter the number of queens (N): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"\nSolving the {n}-Queens problem... \n")

    # Solve with BFS
    t1 = time.time()
    bfs_results = solve_bfs(n)
    bfs_duration = (time.time() - t1) * 1000

    # Solve with DFS
    t2 = time.time()
    dfs_results = solve_dfs(n)
    dfs_duration = (time.time() - t2) * 1000

    # Show stats
    print(f"BFS found {len(bfs_results)} solutions in {bfs_duration:.2f} ms")
    print(f"DFS found {len(dfs_results)} solutions in {dfs_duration:.2f} ms")

    # Display sample board
    if bfs_results:
        show_board(bfs_results[0], n)
    else:
        print("No solutions found! ")

    # Compare results
    print("Comparison Summary:")
    print(f" BFS Time: {bfs_duration:.2f} ms")
    print(f" DFS Time: {dfs_duration:.2f} ms")

    print("\nThanks for trying the N-Queens Solver!")
    print("Made with ❤️ by Ziyad Azzaz 🧠 (AI Course Project)")


# Entry point
if __name__ == "__main__":
    start()
