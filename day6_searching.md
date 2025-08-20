---

# Part 6 – Game Playing: Minimax & Alpha-Beta Pruning

---

## 🔹 Why Game Playing in AI?

* Many real-world problems can be seen as **competitive environments**.
* Games like **Chess, Checkers, Go, Tic-Tac-Toe** → test AI reasoning & strategy.
* AI must:

  1. **Plan ahead** (search).
  2. **Handle uncertainty** (opponent’s moves).
  3. **Act optimally** under competition.

---

## 🔹 Game Search Problems

A game is modeled as a **search tree**:

* **States** → configurations of the board.
* **Initial state** → starting position.
* **Players** → MAX (AI) & MIN (opponent).
* **Actions** → legal moves.
* **Transition model** → how moves change state.
* **Terminal test** → game over?
* **Utility function (payoff)** → win = +1, lose = -1, draw = 0 (simplest case).

---

## 🔹 Minimax Algorithm

* **Idea**:

  * MAX player tries to **maximize score**.
  * MIN player tries to **minimize score**.
* AI assumes opponent plays optimally.

### Pseudocode

```
function MINIMAX(state, depth, maximizingPlayer):
    if depth == 0 or state is terminal:
        return utility(state)
    
    if maximizingPlayer:
        maxEval = -∞
        for each child in successors(state):
            eval = MINIMAX(child, depth-1, false)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = +∞
        for each child in successors(state):
            eval = MINIMAX(child, depth-1, true)
            minEval = min(minEval, eval)
        return minEval
```

---

## 🔹 Example – Tic-Tac-Toe

* AI checks all possible future moves.
* Assigns scores:

  * Win = +1
  * Lose = -1
  * Draw = 0
* Chooses move that maximizes AI’s final outcome.

---

## 🔹 Problem with Minimax

* Game trees are **huge**.
* Example: Chess ≈ 10^120 possible states (too large!).
* Naïve Minimax is infeasible.

---

## 🔹 Alpha-Beta Pruning

* Optimized Minimax.
* **Prunes branches** that cannot affect final decision.
* Maintains two values:

  * **α (alpha)** → best value MAX can guarantee.
  * **β (beta)** → best value MIN can guarantee.
* If branch is worse than α or β, stop exploring.

### Pseudocode

```
function ALPHA-BETA(state, depth, α, β, maximizingPlayer):
    if depth == 0 or state is terminal:
        return utility(state)

    if maximizingPlayer:
        value = -∞
        for each child in successors(state):
            value = max(value, ALPHA-BETA(child, depth-1, α, β, false))
            α = max(α, value)
            if β <= α:
                break   // prune
        return value
    else:
        value = +∞
        for each child in successors(state):
            value = min(value, ALPHA-BETA(child, depth-1, α, β, true))
            β = min(β, value)
            if β <= α:
                break   // prune
        return value
```

---

## 🔹 Benefits of Alpha-Beta

* Same result as Minimax.
* Explores far fewer nodes.
* **Best case**: Cuts search space in half.
* Enables deeper lookahead in games.

---

## 🔹 Heuristics in Game Search

* Depth is limited → cannot search to end in big games.
* Use **heuristic evaluation functions**:

  * Chess → piece values, board control, king safety.
  * Tic-Tac-Toe → number of 2-in-a-rows.
* These functions approximate the "goodness" of a state.

---

## 🔹 Example Walkthrough

Tic-Tac-Toe with depth limit:

1. AI = MAX, Opponent = MIN.
2. Expand tree up to 2 levels.
3. Apply heuristic evaluation at leaf nodes.
4. Backpropagate scores using Minimax/Alpha-Beta.
5. AI chooses move with best score.

---

## 🔹 Game Tree Illustration (simplified)

```
        MAX
       /   \
     MIN   MIN
    /  \   /  \
   +1  -1  0   +1
```

* MAX picks left branch → worst case is +1.

---

## 🔹 Complexity

* Without pruning: O(b^d)
* With pruning: O(b^(d/2)) (in best case)
* b = branching factor, d = depth.

---

## 🔹 Applications

1. **Classic board games** – Chess, Checkers, Go.
2. **Video games AI** – decision-making for NPCs.
3. **Strategic planning** – military simulations.
4. **Business competition models** – bidding, auctions.

---

## 🔹 Class Activities

1. **Tic-Tac-Toe Demo** – implement Minimax manually.
2. **Alpha-Beta Exercise** – show how pruning cuts branches.
3. **Chess Evaluation Discussion** – how to design heuristics.

---

## 🔹 Summary

* Minimax → optimal play, but slow.
* Alpha-Beta → speeds up search, deeper lookahead.
* Heuristic evaluations → practical for large games.
* Game playing AI balances **optimality vs efficiency**.

---

