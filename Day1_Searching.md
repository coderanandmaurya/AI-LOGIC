---

# Part 1 – Introduction to AI Search Strategies

---

## 🔹 What is Search in AI?

Search is the process of **exploring possible states** to reach a **goal state** from an **initial state**.

* An AI problem is often formulated as a **search problem**.
* The AI agent navigates through a **state space** (graph or tree of states).
* Goal: find a sequence of actions (solution path) that leads from start to goal.

---

## 🔹 Example – Vacuum Cleaner World

Imagine a vacuum cleaner robot:

* **Initial state**: Vacuum at left, both rooms dirty.
* **Actions**: Move left, move right, suck.
* **Goal state**: Both rooms clean.

👉 The robot uses **search strategies** to decide the sequence of moves.

---

## 🔹 Why Study Search?

* Core foundation of **AI problem solving**.
* Used in **planning, robotics, games, pathfinding**.
* Helps understand **trade-offs** (speed, memory, optimality).

---

## 🔹 Types of Search in AI

1. **Uninformed Search (Blind Search)**

   * No extra knowledge about states.
   * Example: BFS, DFS, UCS, IDS.

2. **Informed Search (Heuristic Search)**

   * Uses heuristic/knowledge to guide.
   * Example: Greedy, A\*.

---

## 🔹 Search Problem Definition

A search problem is defined by:

* **Initial state (S0)** → Starting point.
* **Actions (A)** → Possible moves.
* **Transition model (T)** → Result of applying action.
* **Goal test (G)** → Checks if goal is reached.
* **Path cost (C)** → Numeric cost of path.

---

### Formal Notation

```
Problem = (S, A, T, S0, G, C)
```

Where:

* S = set of states
* A = set of actions
* T = transition model
* S0 = initial state
* G = goal test
* C = path cost

---

## 🔹 State Space Representation

### Example: 8-Puzzle Problem

```
Initial State: 
1 2 3
4 5 6
7 8 _

Goal State:
1 2 3
4 5 6
7 8 _
```

* State = configuration of tiles.
* Action = move blank tile (up, down, left, right).
* Path cost = number of moves.

---

## 🔹 Search Tree vs. State Space

* **Search Tree** → Data structure explored by search algorithm.
* **State Space** → The actual set of all states.

👉 One state can appear multiple times in the tree with different paths.

---

### Example Diagram

```
Initial State (S0)
    |
   Action1
    |
   State1
    |
   Action2
    |
   Goal State
```

---

## 🔹 Components of Search

1. **Nodes** – represent states.
2. **Edges** – represent actions.
3. **Frontier** – set of nodes yet to explore.
4. **Explored set** – already visited states.

---

## 🔹 Evaluating Search Algorithms

We compare algorithms using:

1. **Completeness** – Will it find a solution if one exists?
2. **Optimality** – Will it find the best (least cost) solution?
3. **Time complexity** – How long does it take?
4. **Space complexity** – How much memory does it use?

---

### Time & Space Complexity

Measured in terms of:

* **b** → branching factor (avg. successors).
* **d** → depth of shallowest solution.
* **m** → max depth.

---

## 🔹 Example – Simple Maze

```
S → A → B → G
 \       /
  → C →
```

* Start at S, goal is G.
* BFS will explore level by level.
* DFS may go deep via wrong path.

---

## 🔹 Types of Search Problems

1. **Single-state problems** (deterministic, fully observable).

   * Ex: 8-puzzle, route planning.

2. **Multiple-state problems** (uncertain state).

   * Ex: agent doesn’t know exact position.

3. **Contingency problems** (environment not predictable).

   * Ex: planning under uncertainty.

4. **Exploration problems** (environment not fully known).

   * Ex: robot exploring new area.

---

## 🔹 Roadmap of Search Strategies

```
Search
│
├── Uninformed Search
│   ├── Breadth-First Search (BFS)
│   ├── Depth-First Search (DFS)
│   ├── Depth-Limited Search (DLS)
│   ├── Iterative Deepening Search (IDS)
│   └── Uniform Cost Search (UCS)
│
└── Informed Search
    ├── Greedy Best-First Search
    ├── A* Search
    └── Variants (IDA*, SMA*)
```

---

## 🔹 Class Activity Suggestion

* Give students a **grid-based maze**.
* Ask them to manually perform BFS and DFS.
* Compare paths taken & nodes explored.

---

