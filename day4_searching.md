---

# Part 4 – Local Search & Optimization

---

## 🔹 Why Local Search?

* So far, we studied **systematic search (BFS, DFS, A\*, etc.)** which explores **state space as a tree/graph**.
* Problem:

  * Requires huge memory (O(b^d)).
  * Slow in large/continuous state spaces.
* **Local Search** is different:

  * Uses a **single current state**.
  * Moves to a neighboring state.
  * Suitable for **optimization problems**.

👉 Example: **Traveling Salesman Problem (TSP)**, **n-Queens problem**, scheduling, machine learning hyperparameter tuning.

---

## 🔹 Characteristics of Local Search

1. Works with **one current node** (not full tree).
2. Uses **objective (fitness) function** instead of path cost.
3. Can handle **large/infinite state spaces**.
4. Memory efficient (stores only few states).
5. May get stuck in **local optima**.

---

## 🔹 Hill Climbing

* Analogy: Imagine climbing a hill in the fog.

  * You don’t see the whole landscape.
  * You take steps **uphill** until no higher step exists.

* **Greedy algorithm** – always move to neighbor with **better value**.

### Algorithm

```
HillClimb(problem):
    current ← initial_state
    loop:
        neighbor ← best_neighbor(current)
        if value(neighbor) ≤ value(current):
            return current   # local optimum
        current ← neighbor
```

### Example – 8 Queens Problem

* Place 8 queens on a chessboard so none attack each other.
* Hill climbing: Move queen with **least conflicts**.
* May reach a **local minimum** (stuck).

### Variants

1. **Steepest Ascent Hill Climbing**: Choose best neighbor among all.
2. **Stochastic Hill Climbing**: Choose random better neighbor.
3. **Random Restart Hill Climbing**: Restart with random states until success.

---

## 🔹 Problems with Hill Climbing

1. **Local Maxima** – state better than neighbors but not global max.
2. **Plateaus** – flat area, all neighbors equal.
3. **Ridges** – slope with diagonal ascent hard to follow.

---

## 🔹 Simulated Annealing

* Inspired by **annealing in metallurgy** (cooling metal slowly).
* Allows **downhill moves** with some probability to escape local maxima.

### Key Idea

* At high "temperature", algorithm explores widely.
* As temperature decreases, it behaves like hill climbing.

### Algorithm

```
SimulatedAnnealing(problem, schedule):
    current ← initial_state
    for t = 1 to ∞:
        T ← schedule(t)   # temperature
        if T = 0: return current
        neighbor ← random_successor(current)
        ΔE ← value(neighbor) - value(current)
        if ΔE > 0: current ← neighbor
        else with probability e^(ΔE/T):
            current ← neighbor
```

### Example – Traveling Salesman Problem

* Path with cities.
* Simulated Annealing can accept **longer path temporarily** to escape poor solutions.

---

## 🔹 Local Beam Search

* Instead of one state, keep **k states**.
* In each step:

  * Generate successors of all k states.
  * Select best k to continue.

👉 More robust than hill climbing.

---

## 🔹 Genetic Algorithms (GA)

* Inspired by **natural evolution**.
* Works with a **population of states**.
* Uses operators:

  1. **Selection** – choose best candidates.
  2. **Crossover** – combine two parents.
  3. **Mutation** – random change.

### Algorithm

```
GeneticAlgorithm(population):
    repeat:
        fitness ← evaluate(population)
        new_population ← select(population, fitness)
        crossover(new_population)
        mutate(new_population)
        population ← new_population
    until stopping_condition
```

### Example – Function Optimization

* Maximize f(x).
* Represent solutions as binary strings.
* GA evolves population until reaching near-optimal solution.

---

## 🔹 Comparison of Local Search Algorithms

| Algorithm           | Pros                            | Cons                                       |
| ------------------- | ------------------------------- | ------------------------------------------ |
| Hill Climbing       | Simple, fast                    | Gets stuck in local maxima                 |
| Simulated Annealing | Escapes local maxima            | Needs careful temperature schedule         |
| Local Beam Search   | Uses multiple states, parallel  | Still may converge early                   |
| Genetic Algorithm   | Good for large/complex problems | Requires tuning population, mutation rates |

---

## 🔹 Applications of Local Search

1. **N-Queens problem**
2. **Travelling Salesman Problem (TSP)**
3. **Job Scheduling**
4. **Neural Network weight optimization**
5. **Game AI strategies**
6. **Feature selection in Machine Learning**

---

## 🔹 Class Activities

1. **Hill Climbing on 8 Queens** – students try manually moving queens.
2. **Simulated Annealing demo** – show how random acceptance helps.
3. **GA exercise** – evolve binary strings for maximizing function.

---

Do you want me to prepare **Part 5** now?
