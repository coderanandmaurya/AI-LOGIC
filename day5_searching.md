--

# Part 5 – Constraint Satisfaction Problems (CSPs)

---

## 🔹 What is a CSP?

* A **Constraint Satisfaction Problem (CSP)** is a problem defined by:

  1. **Variables** → e.g., X1, X2, X3.
  2. **Domains** → possible values for each variable.
  3. **Constraints** → restrictions on variable assignments.

👉 Goal: Assign values to variables such that **all constraints are satisfied**.

---

## 🔹 Examples of CSPs

1. **Map Coloring**

   * Variables: Each region (A, B, C …).
   * Domain: {Red, Green, Blue}.
   * Constraints: Adjacent regions must have different colors.

2. **N-Queens Problem**

   * Variables: Position of queens on board.
   * Domain: Row/column positions.
   * Constraints: No two queens attack each other.

3. **Sudoku Puzzle**

   * Variables: Each cell.
   * Domain: {1,2,…,9}.
   * Constraints: Row, column, and 3×3 box must contain unique digits.

---

## 🔹 Why CSPs are Important?

* General-purpose framework for **many real-world problems**.
* Efficient algorithms exist → **faster than blind search**.
* Common in **AI planning, scheduling, reasoning, resource allocation**.

---

## 🔹 Characteristics of CSPs

1. **Discrete variables**.
2. **Finite domains**.
3. **Constraints can be binary (between two vars) or global (many vars)**.
4. Representable as a **graph** (Constraint Graph).
5. Often solved with **backtracking + heuristics**.

---

## 🔹 CSP State Space

* States: Partial assignments.
* Initial state: Empty assignment.
* Goal state: Assignment satisfying all constraints.
* Successor function: Assign a value to an unassigned variable.

---

## 🔹 Backtracking Search

* Basic algorithm for CSPs.

```
Backtrack(assignment):
    if assignment is complete: return assignment
    var ← select_unassigned_variable()
    for each value in domain(var):
        if consistent(var, value, assignment):
            add {var = value} to assignment
            result ← Backtrack(assignment)
            if result ≠ failure: return result
            remove {var = value}
    return failure
```

👉 Same as DFS but with constraints checking.

---

## 🔹 Improving Backtracking

### 1. Variable Ordering

* **Minimum Remaining Values (MRV)** – choose variable with fewest legal values left.
* **Degree heuristic** – choose variable with most constraints on remaining vars.

### 2. Value Ordering

* **Least Constraining Value (LCV)** – choose value that rules out the fewest options for other variables.

### 3. Constraint Propagation

* **Forward Checking** – eliminate inconsistent values as soon as variable assigned.
* **Arc Consistency (AC-3)** – ensure every value in domain has a legal supporting value.

---

## 🔹 Example – Map Coloring with Backtracking

1. Assign Color(A).
2. Apply forward checking to restrict neighbors.
3. Continue until all regions colored or conflict found.

---

## 🔹 Complexity

* Worst-case: Exponential.
* With heuristics: Drastically reduced.

---

## 🔹 Local Search for CSPs

* Alternative to backtracking.
* Example: **Min-Conflicts Heuristic**

  * Start with random assignment.
  * At each step, change value of a variable causing conflicts.
  * Works well for problems like **N-Queens** (1000 queens solvable quickly).

---

## 🔹 Applications of CSPs

1. **Scheduling** – classes, exams, airline flights.
2. **Resource allocation** – CPU scheduling, memory management.
3. **Puzzles** – Sudoku, crosswords.
4. **Design problems** – VLSI design, timetabling.
5. **Configuration** – setting options for products.

---

## 🔹 CSP vs. Traditional Search

| Aspect               | Traditional Search  | CSP                               |
| -------------------- | ------------------- | --------------------------------- |
| State Representation | Paths / nodes       | Variable-value assignments        |
| Goal Test            | Reaching goal state | All constraints satisfied         |
| Search Type          | BFS, DFS, A\*       | Backtracking + heuristics         |
| Efficiency           | Often exponential   | More efficient (with propagation) |

---

## 🔹 Class Activities

1. **Map Coloring Exercise** – students color a map with 3 colors.
2. **Sudoku Puzzle Demo** – solve using backtracking.
3. **N-Queens Problem** – solve with min-conflicts heuristic.

---

