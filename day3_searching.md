---

# Part 3 – Informed Search (Heuristic-Based Search)

---

## 🔹 What is Informed Search?

* **Definition**: Search strategies that use **extra information (heuristics)** about the problem to guide the search process.
* **Heuristic (h(n))**: An estimate of the cost from node **n** to the goal.

👉 Example: In route-finding, heuristic could be **straight-line distance** to destination.

### Why Informed Search?

* Uninformed search wastes time exploring irrelevant states.
* Informed search uses **domain knowledge** to reduce search time.
* Often finds optimal solution faster than BFS/UCS.

---

## 🔹 Key Characteristics

1. Uses a **heuristic function h(n)**.
2. Explores nodes that **seem promising**.
3. Can be **faster** than uninformed methods.
4. May or may not be optimal (depends on heuristic).

---

## 🔹 Types of Informed Search

1. **Greedy Best-First Search (GBFS)**
2. **A\* Search**

---

## 1. Greedy Best-First Search (GBFS)

* Expands the node that **appears closest to goal**.
* Uses heuristic **h(n)** only.
* Ignores cost so far (g(n)).

### Evaluation Function

```
f(n) = h(n)
```

### Algorithm (Pseudocode)

```
GreedyBestFirst(initial_state, goal_test, h):
    frontier ← PriorityQueue()   # ordered by h(n)
    frontier.insert(initial_state, h(initial_state))
    explored ← ∅

    while frontier not empty:
        node ← frontier.pop()   # node with lowest h
        if goal_test(node):
            return solution(node)
        explored.add(node)
        for child in expand(node):
            if child not in frontier and child not in explored:
                frontier.insert(child, h(child))
```

### Example – Romania Map

* Task: Go from Arad → Bucharest.
* Heuristic: straight-line distance to Bucharest.
* GBFS always picks the city with **smallest h(n)**.

👉 Fast but may take **longer path** because it ignores actual cost.

### Properties

* **Completeness**: No (may loop).
* **Optimality**: No.
* **Time Complexity**: O(b^m).
* **Space Complexity**: O(b^m).

---

## 2. A\* Search

* Combines **UCS (actual cost)** and **Greedy (heuristic cost)**.
* Expands the node with lowest **f(n) = g(n) + h(n)**.

👉 This makes A\* both **complete** and **optimal** (if heuristic is admissible).

### Evaluation Function

```
f(n) = g(n) + h(n)
```

* **g(n)** = cost from start to node n.
* **h(n)** = estimated cost from n to goal.

### Algorithm (Pseudocode)

```
A*(initial_state, goal_test, h):
    frontier ← PriorityQueue()   # ordered by f(n)
    frontier.insert(initial_state, g=0, f=h(initial_state))
    explored ← ∅

    while frontier not empty:
        node ← frontier.pop()   # lowest f(n)
        if goal_test(node):
            return solution(node)
        explored.add(node)
        for child in expand(node):
            g_child = g(node) + cost(node, child)
            f_child = g_child + h(child)
            if child not in frontier or g_child < old_g(child):
                frontier.insert(child, f_child)
```

### Example – Romania Map

* Start = Arad, Goal = Bucharest.
* Uses both **distance traveled so far (g)** + **straight-line estimate (h)**.
* Finds the **shortest route**.

### Properties

* **Completeness**: Yes (if step cost ≥ ε).
* **Optimality**: Yes (if heuristic admissible).
* **Time Complexity**: Exponential in worst case, but usually much better than BFS/UCS.
* **Space Complexity**: O(b^d).

---

## 🔹 Heuristic Properties

### 1. Admissible Heuristic

* Never overestimates true cost.
* Ensures A\* is **optimal**.

👉 Example: Straight-line distance is admissible because actual road distance ≥ straight-line distance.

### 2. Consistent (Monotonic) Heuristic

* For every node n and successor n’:

```
h(n) ≤ cost(n, n’) + h(n’)
```

* Ensures **non-decreasing f(n)** along a path.

---

## 🔹 Example – 8 Puzzle Problem

### Puzzle Layout

```
Start:         Goal:
1 2 3          1 2 3
4 5 6          4 5 6
7 8 _          7 8 _
```

### Heuristics

1. **Misplaced Tiles**: Count of tiles not in place.
2. **Manhattan Distance**: Sum of tile distances from goal position.

👉 A\* with Manhattan distance is more efficient.

---

## 🔹 Comparison of GBFS vs A\*

| Feature      | GBFS             | A\*                |
| ------------ | ---------------- | ------------------ |
| Function     | f(n) = h(n)      | f(n) = g(n) + h(n) |
| Completeness | No               | Yes                |
| Optimality   | No               | Yes (admissible h) |
| Time         | Fast (but risky) | Slower but safer   |
| Memory       | High             | High               |

---

## 🔹 Class Activity

1. Give students Romania map distances.

   * Ask them to solve with GBFS and A\*.
   * Compare paths and node expansions.

2. 8-Puzzle problem.

   * Try with misplaced tiles vs Manhattan distance.

👉 This shows how heuristics **improve efficiency**.

---

Do you want me to move on and prepare **Part 4** now?
