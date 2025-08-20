# Part 2 – Uninformed Search (Blind Search)

---

## 🔹 What is Uninformed Search?

* **Definition**: Search strategies that **do not use domain-specific knowledge**.
* They only use information available in the **problem definition** (initial state, actions, goal test).
* Also called **Blind Search** because they explore without heuristics.

👉 They are useful as **baseline methods** to understand search but are inefficient in large spaces.

---

## 🔹 Key Characteristics

1. **No heuristic knowledge** (no guidance about goal location).
2. Search systematically (level-by-level or depth-first).
3. May explore unnecessary states.
4. Guaranteed solution only if algorithm is complete.
5. Performance depends on **branching factor (b)** and **solution depth (d)**.

---

## 🔹 Types of Uninformed Search

1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
3. **Depth-Limited Search (DLS)**
4. **Iterative Deepening Search (IDS)**
5. **Uniform Cost Search (UCS)**

---

## 1. Breadth-First Search (BFS)

* Explores **level by level** from root.
* Uses **queue (FIFO)** data structure.
* Guaranteed to find **shallowest solution**.

### Algorithm (Pseudocode)

```
BFS(initial_state, goal_test):
    frontier ← Queue()
    frontier.enqueue(initial_state)
    explored ← ∅

    while frontier not empty:
        node ← frontier.dequeue()
        if goal_test(node):
            return solution(node)
        explored.add(node)
        for child in expand(node):
            if child not in frontier and child not in explored:
                frontier.enqueue(child)
```

### Example – Simple Graph

```
Start → A → B → Goal
       → C → D
```

* BFS explores: `Start → A, C → B, D → Goal`

### Properties

* **Completeness**: Yes (if b is finite).
* **Optimality**: Yes (for uniform step cost).
* **Time Complexity**: O(b^d)
* **Space Complexity**: O(b^d) (stores frontier).

---

## 2. Depth-First Search (DFS)

* Explores **deepest node first**.
* Uses **stack (LIFO)** or recursion.
* May go deep into wrong path.

### Algorithm (Pseudocode)

```
DFS(initial_state, goal_test):
    frontier ← Stack()
    frontier.push(initial_state)
    explored ← ∅

    while frontier not empty:
        node ← frontier.pop()
        if goal_test(node):
            return solution(node)
        explored.add(node)
        for child in expand(node):
            if child not in frontier and child not in explored:
                frontier.push(child)
```

### Example

```
Start → A → B → Goal
       → C → D
```

* DFS path may go: `Start → A → B → Goal`
* Or wrongly: `Start → C → D → dead end`

### Properties

* **Completeness**: No (fails in infinite depth).
* **Optimality**: No.
* **Time Complexity**: O(b^m) (m = max depth).
* **Space Complexity**: O(bm) (linear memory).

---

## 3. Depth-Limited Search (DLS)

* DFS with a **depth cutoff (L)**.
* Avoids infinite loops by limiting exploration depth.

### Example

* If cutoff = 2, search only explores 2 levels deep.

### Properties

* **Completeness**: No (if cutoff < d).
* **Optimality**: No.
* **Time Complexity**: O(b^L).
* **Space Complexity**: O(bL).

---

## 4. Iterative Deepening Search (IDS)

* Combines **BFS completeness** with **DFS low memory**.
* Runs DFS with increasing depth limit until goal is found.

### Process

1. Run DLS with limit = 0.
2. Run DLS with limit = 1.
3. Run DLS with limit = 2.
4. Continue until solution found.

### Example

```
Iteration 1: depth 0
Iteration 2: depth 1
Iteration 3: depth 2
Goal found at depth d
```

### Properties

* **Completeness**: Yes.
* **Optimality**: Yes (for uniform cost).
* **Time Complexity**: O(b^d).
* **Space Complexity**: O(bd).

👉 Used in practice (e.g., chess programs).

---

## 5. Uniform Cost Search (UCS)

* Variant of BFS that expands **lowest-cost node first**.
* Uses **priority queue** (based on path cost).
* Equivalent to **Dijkstra’s Algorithm**.

### Algorithm (Pseudocode)

```
UCS(initial_state, goal_test):
    frontier ← PriorityQueue()   # ordered by path cost
    frontier.insert(initial_state, cost=0)
    explored ← ∅

    while frontier not empty:
        node ← frontier.pop()   # node with lowest cost
        if goal_test(node):
            return solution(node)
        explored.add(node)
        for child in expand(node):
            if child not in frontier or lower cost found:
                frontier.insert(child, cost(child))
```

### Example

```
Path A → B (cost 5)
Path A → C → D → Goal (cost 3)
```

* UCS will find cheaper path even if longer in steps.

### Properties

* **Completeness**: Yes (if step cost ≥ ε > 0).
* **Optimality**: Yes (finds least-cost solution).
* **Time Complexity**: O(b^(1+⌊C\*/ε⌋))
* **Space Complexity**: O(b^(1+⌊C\*/ε⌋))

---

## 🔹 Comparison Table – Uninformed Search

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity |
| --------- | ------------ | ---------- | --------------- | ---------------- |
| BFS       | Yes          | Yes        | O(b^d)          | O(b^d)           |
| DFS       | No           | No         | O(b^m)          | O(bm)            |
| DLS       | No           | No         | O(b^L)          | O(bL)            |
| IDS       | Yes          | Yes        | O(b^d)          | O(bd)            |
| UCS       | Yes          | Yes        | O(b^(C\*/ε))    | O(b^(C\*/ε))     |

---

## 🔹 Class Activity Suggestion

1. Give students a simple graph:

```
     S
   / | \
  A  B  C
 / \     \
D   G     E
```

* Ask them to run BFS and DFS manually.
* Compare path and nodes explored.

2. Modify edges with different **costs**.

* Run UCS and see difference.

---
