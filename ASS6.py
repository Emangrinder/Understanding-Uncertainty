# %% [markdown]
# # Assignment 6
# ### Do Question 6, and three more questions of your choice.

# %% [markdown]
# ### 1. Set review:
# 
# - Operations on sets (hints: sketch venn-type diagrams, and showing $A=B$ is the same as $A \subseteq B$ and $B \subseteq A$):
# - $ (A \backslash B) \cup (A \cap B) = A $
# - $ A \cup ( B \cap C) = (A \cup B) \cap (A \cup C)$
# - $ A \backslash (B \cup C) = A\backslash B \cap A \backslash C $ and $A \backslash (B \cap C) = A \backslash B \cup A \backslash C$
# 
# - Plot the following sets: 
#     - $A = \{x \in \mathbb{R}: x^2 -1 \ge 0 \}$ 
#     - $B = \{ (x,y) \in \mathbb{R}^2: 3x -2y \ge 0 \}$
#     - $C = \{ (x,y) \in \mathbb{R}^2: xy \ge 3 \}$
#     - $D = \{ (x_1,x_2) \in \mathbb{R}^2: x_1 \ge 0, x_2 \ge 0, x_1 + x_2 \le 1 \}$
# - The power set of $A$ is the set of all subsets of $A$, denoted $\mathcal{P}(A)$. What is the power set of $\{ 1, 2, 3 \}$? (Hint: The empty set is a subset of every set; the whole set is a subset of itself.)
#     - $\mathcal{P}(\{1, 2, 3\}) = \{ \emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\} \}$

# %%
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

def shade_background(ax, color='lightgray'):
    """Fills background for excluded regions."""
    ax.set_facecolor(color)

# 1 (A \ B) ∪ (A ∩ B) = A
plt.figure(figsize=(10, 4))
plt.suptitle(r"Identity 1: $(A \backslash B) \cup (A \cap B) = A$", fontsize=14)

# LHS
plt.subplot(1, 2, 1)
ax = plt.gca()
shade_background(ax)
v = venn2(subsets=(1, 1, 1), set_labels=('A','B'))
v.get_patch_by_id('10').set_color('skyblue')  # A\B
v.get_patch_by_id('11').set_color('skyblue')  # A∩B
v.get_patch_by_id('01').set_alpha(0.2)        # B only (excluded)
plt.title("LHS: (A \\ B) ∪ (A ∩ B)")

# RHS
plt.subplot(1, 2, 2)
ax = plt.gca()
shade_background(ax)
v = venn2(subsets=(1, 1, 1), set_labels=('A','B'))
v.get_patch_by_id('10').set_color('skyblue')
v.get_patch_by_id('11').set_color('skyblue')
v.get_patch_by_id('01').set_alpha(0.2)
plt.title("RHS: A")
plt.show()


# 2 A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
plt.figure(figsize=(10, 4))
plt.suptitle(r"Identity 2: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$", fontsize=14)

# LHS
plt.subplot(1, 2, 1)
ax = plt.gca()
shade_background(ax)
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A','B','C'))
for s in ['100','110','101','111','011']:  # A or (B∩C)
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_color('skyblue')
plt.title("LHS: A ∪ (B ∩ C)")

# RHS
plt.subplot(1, 2, 2)
ax = plt.gca()
shade_background(ax)
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A','B','C'))
for s in ['100','110','101','111','011']:
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_color('skyblue')
plt.title("RHS: (A ∪ B) ∩ (A ∪ C)")
plt.show()


# 3 A \ (B ∪ C) = (A \ B) ∩ (A \ C)
plt.figure(figsize=(10, 4))
plt.suptitle(r"Identity 3: $A \backslash (B \cup C) = (A \backslash B) \cap (A \backslash C)$", fontsize=14)

# LHS
plt.subplot(1, 2, 1)
ax = plt.gca()
shade_background(ax)
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A','B','C'))
for s in ['100']:  # Only A alone
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_color('skyblue')
for s in ['110','101','111','011','010','001']:
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_alpha(0.2)
plt.title("LHS: A \\ (B ∪ C)")

# RHS
plt.subplot(1, 2, 2)
ax = plt.gca()
shade_background(ax)
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A','B','C'))
for s in ['100']:
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_color('skyblue')
for s in ['110','101','111','011','010','001']:
    if v.get_patch_by_id(s): v.get_patch_by_id(s).set_alpha(0.2)
plt.title("RHS: (A \\ B) ∩ (A \\ C)")
plt.show()


# %% [markdown]
# ### The light blue is the final overlap, I didn't know how to add my images drawn, so I just graphed them above with chatGPT

# %%
# A = {x in R: x^2 - 1 >= 0}

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 1.5))

ax.get_yaxis().set_visible(False)
ax.set_xlim(-3, 3)

ax.hlines(0, -3, 3, color='black')
ax.hlines(0, -3, -1, color='skyblue', linewidth=6)
ax.hlines(0, 1, 3, color='skyblue', linewidth=6)

ax.plot([-1, 1], [0, 0], 'ro')  # red dots at the boundaries
ax.text(-1, 0.05, '-1', ha='center', va='bottom')
ax.text(1, 0.05, '1', ha='center', va='bottom')
ax.set_title(r"$A = \{x \in \mathbb{R} : x^2 - 1 \geq 0\}$", y=0.6)

plt.show()


# %%
# B = {(x,y) in R^2: 3x - 2y >= 0}

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Color in red

plt.plot(x, 3*x - 2*y)
plt.fill_between(x, 3*x - 2*y, where=3*x - 2*y >= 0, color='r') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('B = {(x,y) in R^2: 3x - 2y >= 0}')
plt.show()

# %%
# C = {(x,y) in R^2: xy >= 3}

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Color in red

plt.plot(x, x*y)
plt.fill_between(x, x*y, where=x*y >= 3, color='r') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('C = {(x,y) in R^2: xy >= 3}')
plt.show()

# %%
# D = {(x_1,x_2) in R^2: x_1 >= 0, x_2 >= 0, x_1 + x_2 >= 1}

import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(0, 2, 100)
x_2 = np.linspace(0, 2, 100)

# Color in red

plt.plot(x_1, x_2)
plt.fill_between(x_1, x_2, where=x_1 + x_2 <= 1, color='r') 
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title('D = {(x_1,x_2) in R^2: x_1 >= 0, x_2 >= 0, x_1 + x_2 <= 1}')
plt.show()

# %% [markdown]
# ### 2. Probability space basics:
# 
# - What are the outcomes for rolling a single, fair **THREE**-sided die? 
#     - The outcomes are {1, 2, 3}, assuming the values are 1, 2, and 3 for each side
# - What's the set of all events? 
#     - The set of all events is equal to E = {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
# - What are the probabilities of all the events?
#     - The probabilities of all the events are equal to P(E) = {0, 1/3, 1/3, 1/3, 2/3, 2/3, 2/3, 1} or for any event|size of that event|/4
# 
# 
# - What about flipping a fair coin twice? (Hint: There are 4 outcomes, and $2^{4} = 16$ events.)
#     - The outcomes are S = {HH, HT, TH, TT}
#     - The set of all events is equal to E = {{}, {HH}, {HT}, {TH}, {TT}, {HH, HT}, {HH, TH}, {HH, TT}, {HT, TH}, {HT, TT}, {TH, TT}, {HH, HT, TH}, {HH, HT, TT}, {HH, TH, TT}, {HT, TH, TT}, {HH, HT, TH, TT}} (16 events)
#     - The probabilities of all the outcomes are equal to P(S) = {1/4, 1/4, 1/4, 1/4}
#     - The probabilities of all the events are equal to P(E) = {0, 1/4, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 3/4, 3/4, 3/4, 3/4, 1} or for any event |size of that event|/4
# 
# - What about rolling the **THREE**-sided die twice, and adding the results? Don't write down the set of all the possible events, but describe briefly what it looks like and how large it is. (Hint: There are 5 outcomes, and $2^{5}=32$ possible events.)
#     - Assuming the die is fair and valued 1,2,3, the outcomes look like the sum of two dice, so the set of all summed outcomes is O = {2, 3, 4, 5, 6} with probabilities P(O) = {1/9, 2/9, 3/9, 2/9, 1/9}
#     - The outcomes are the possible sums {2,3,4,5,6}, each with probability as above. The event space is the power set of {2,3,4,5,6}, which has 32 subsets (events). An example event is ‘sum is even’ = {2,4,6}, with probability 1/9+3/9+1/9=5/9.
# 
# Obviously, a "three-sided die" doesn't exist, but this keeps you from spending a lot of time suffering in working out sets of events.

# %% [markdown]
# 
# ### 3. Random Variable Basics
# 
# - Imagine rolling a fair single six-sided die. There are 6 outcomes, all equally likely. Derive the sample space and the space of events. What are the probabilities of the outcomes and events? 
#     - The sample space is S = {1, 2, 3, 4, 5, 6}
#     - The space of events is E = {{}, {1}, {2}, ... {1,2,3,4,5,6}}
#     - The probabilities of all outcomes are equal to P(S) = {1/6, 1/6, 1/6, 1/6, 1/6, 1/6}
#     - The probabilities of all the events are equal to |size of that event|/6
# - Consider a random variable that assigns the square root of the number of pips on the die to each outcome. Write code to simulate rolling a single six-sided die and computing the value of the random variable. Simulate 5000 rolls and plot the mass function and ECDF of the random variable.
# - Imagine rolling two fair six-sided die. Consider a random variable that adds up the pips on the dice. There are 11 outcomes (2 , 3, ..., 12), but not all are equally likely. Derive the sample space and **describe** the space of events. What are the probabilities of the outcomes?
#     - The underlying sample space (before summing) is all ordered pairs, there are 36 equally likely outcomes, each with probability 1/36
# - Write code to simulate the random variable (rolling two six-sided die and adding the results together). Simulate 10000 rolls and plot the mass function and ECDF.

# %%
import numpy as np
import matplotlib.pyplot as plt

# simulate 5000 rolls of one fair d6
n = 5000
rolls = np.random.randint(1, 7, size=n)        
X = np.sqrt(rolls)                             

# --- Mass function estimate (PMF) ---
vals, counts = np.unique(X, return_counts=True)
pmf_est = counts / n

plt.figure(figsize=(6,4))
plt.stem(vals, pmf_est)
plt.xlabel("x (sqrt of die roll)")
plt.ylabel("Estimated P(X = x)")
plt.title("Estimated PMF of X = sqrt(roll)")
plt.grid(True)
plt.show()

# --- Empirical CDF (ECDF) ---
X_sorted = np.sort(X)
ecdf_y = np.arange(1, n+1) / n

plt.figure(figsize=(6,4))
plt.step(X_sorted, ecdf_y, where='post')
plt.xlabel("x")
plt.ylabel("ECDF of X")
plt.title("ECDF of X = sqrt(roll)")
plt.grid(True)
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt

# simulate 10000 rolls of two fair d6 and sum them
n = 10000
roll1 = np.random.randint(1, 7, size=n)
roll2 = np.random.randint(1, 7, size=n)
Y = roll1 + roll2   # random variable = sum

# PMF estimate
vals, counts = np.unique(Y, return_counts=True)
pmf_est = counts / n

plt.figure(figsize=(6,4))
plt.stem(vals, pmf_est)
plt.xlabel("Sum of two dice")
plt.ylabel("Estimated P(Y = y)")
plt.title("Estimated PMF of Y = die1 + die2")
plt.grid(True)
plt.show()

# ECDF
Y_sorted = np.sort(Y)
ecdf_y = np.arange(1, n+1) / n

plt.figure(figsize=(6,4))
plt.step(Y_sorted, ecdf_y, where='post')
plt.xlabel("Sum of two dice")
plt.ylabel("ECDF of Y")
plt.title("ECDF of Y = die1 + die2")
plt.grid(True)
plt.show()


# %% [markdown]
# ### 4. Roulette
# 
# #### Used chat to speed up soft dev process, as three above are me
# 
# This question will be easiest if you read the whole thing, and come up with a clear plan for how you'll write the code.
# 
# Roulette is a betting game. There are 37 possible outcomes: A green 0, and the numbers 1 to 36 in red and black. Here is a picture of the (American, not Euro, it has an extra green 00) betting board:
# 
# ![Roulette](./src/euro_roulette.jpg)
# 
# To bet, you must pay a dollar, but then you get payouts that depend on how many slots are in your bet
# - Basic bets:
#     - Red or Black slots
#     - Odd or Even slots
#     - A single slots, like 20
# - More complex bets:
#     - Split: Two adjacent slots (e.g. {1,2})
#     - Square: Four adjacent slots (e.g. {1,2,4,5})
#     - Street: Three slots in a row (e.g. {1,2,3})
#     - Line: Six slots (e.g. {1,2,3,4,5,6})
# In general, you can only bet on 1, 2, 3, 4, 6 slots, 12 slots, or 18 slots. If your bet occurs when the wheel is spun, you gain 36/K-1 where $K$ is the number of slots you bet on; if not, you lose a dollar and get -1.
# 
# - Write code to model spinning the roulette wheel, including the colors and numbers (you could make two lists of number and color and draw a random number between 0 and 37... or use a dataframe with color and number variables and sample it... or use a dict with key to number/color pairs...)
# - Describe the probability space associated with the roulette wheel: Outcomes, events, probabilities (If there are 37 outcomes, there are $2^{37}= 137,438,953,472$ events, by the way)
#     - The sample space of outcomes is S = {0, 1, ... 37}
#     - The probability space is P(S) = 1/37 for any outcome
#     - The event space is $2^{37}$ ~ E = {{}, {0}, ... {0,1,...37}}
#     - The probability for any event is |size of the event|/37
# - You wrote code to generate a spin of the roulette wheel. Now write a function that takes a basic or complex bet as an argument, and returns the result for the player (win or lose, and the payout 36/K-1 or -1)
# - Simulate betting on red, betting on odd, betting on 7, a split, and a line 1000 times each.
# - Compute the average values for the bets you just simulated. What are the expected average payoffs?
#     -  The negative payoffs show the return to the house on each, showed below.

# %%
import random
import numpy as np

# Define the wheel
# Standard European roulette colors for 1-36.
RED_NUMBERS = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
BLACK_NUMBERS = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

wheel = []
for n in range(37):  # 0 through 36
    if n == 0:
        color = "green"
        parity = None
    elif n in RED_NUMBERS:
        color = "red"
        parity = "odd" if (n % 2 == 1) else "even"
    elif n in BLACK_NUMBERS:
        color = "black"
        parity = "odd" if (n % 2 == 1) else "even"
    else:
        raise ValueError(f"Number {n} missing color assignment.")
    wheel.append({
        "number": n,
        "color": color,
        "parity": parity
    })

def spin_wheel():
    """Return a random outcome from the wheel as a dict."""
    return random.choice(wheel)


# %%
def get_bet_numbers(kind, values=None):
    """
    kind: 'red', 'odd', 'single', 'split', 'line'
    values: depends on kind
        - single: int like 7
        - split: tuple/list of 2 ints, e.g. (7,8)
        - line: list/tuple of 6 ints, e.g. (1,2,3,4,5,6)
    returns: set of winning numbers
    """
    if kind == "red":
        return {slot["number"] for slot in wheel if slot["color"] == "red"}
    if kind == "odd":
        return {slot["number"] for slot in wheel if slot["parity"] == "odd"}
    if kind == "single":
        return {values}  # single
    if kind == "split":
        return set(values)  # two
    if kind == "line":
        return set(values)  # six
    raise ValueError("Unknown bet type.")


def bet_outcome(bet_numbers, outcome_number):
    """
    bet_numbers: set of numbers you win on
    outcome_number: the rolled number (0..36)
    returns net winnings:
        hit  -> 36/K - 1
        miss -> -1
    """
    K = len(bet_numbers)
    if outcome_number in bet_numbers:
        return 36 / K - 1
    else:
        return -1


# %%
def simulate_bet(kind, values=None, trials=1000):
    bet_nums = get_bet_numbers(kind, values)
    results = []
    for _ in range(trials):
        outcome = spin_wheel()
        winnings = bet_outcome(bet_nums, outcome["number"])
        results.append(winnings)
    return np.array(results)

# Run simulations
np.random.seed(0)  # for reproducibility

res_red   = simulate_bet("red",   trials=1000)
res_odd   = simulate_bet("odd",   trials=1000)
res_single= simulate_bet("single",values=7, trials=1000)
res_split = simulate_bet("split", values=(7,8), trials=1000)
res_line  = simulate_bet("line",  values=(1,2,3,4,5,6), trials=1000)

def summarize(name, arr):
    mean_payoff = arr.mean()
    hit_rate = np.mean(arr > 0)
    return {
        "bet": name,
        "avg_net_per_bet": mean_payoff,
        "hit_pct": hit_rate
    }

summaries = [
    summarize("red",    res_red),
    summarize("odd",    res_odd),
    summarize("single 7", res_single),
    summarize("split (7,8)", res_split),
    summarize("line (1-6)",  res_line)
]

for s in summaries:
    print(s)


# %% [markdown]
# ### 5. CDF and PDF Basics
# 
# - Verified by hand and summarized below, used chat to plot. Top three problems above mine this one is bonus
# - Verify the following functions are distribution functions and compute their density functions. Plot the distribution and density.
# 
# 1. $F(x) = \begin{cases}
# 0, & x \le 0 \\
# \sqrt{x}, & 0 \le x \le 1 \\
# 1, & x \ge 1 
# \end{cases}
# $
# 2. $F(x) = \dfrac{1}{1+e^{-x}}$
# 3. For $ a < b < c$,
# $
# F(x) = \begin{cases}
# 0, & x \le 0 \\
# \frac{(x-a)^2}{(b-a)(b-c)}, & a \le x \le c \\
# 1 - \frac{(b-x)^2}{(b-a)(b-c)}, & c < x < b \\
# 1, & x \ge b
# \end{cases}
# $
# 4. $ F(x) = \begin{cases}
# 0, & x <0 \\
# 1 - e^{-x}, & x>0
# \end{cases}
# $
# 5. $ F(x) = \begin{cases}
# 0, & x \le 0 \\
# x, & 0 < x < 1\\
# 1, & x \ge 1
# \end{cases}
# $

# %% [markdown]
# - CDF if:
#     - Nondecreasing
#     - Right continuous
#     - Lim F(x) -> 0 as x -> -$\infty$
#     - Lim F(x) -> 1 as x -> $\infty$
# - Left 0, right 1 mean negative infinity on left and right infinity on right for x leads (apppoaching) to 0 and  1 respectively
# - (1) 
#     - Left 0, right 1, Continuous, as x increases overall increases (nondecreasing)
# - (2) 
#     - Left 0, right 1, as x increases, e decreases which increases overall (nondecreasing), continuous
# - (3) 
#     - Left 0, right 1, as long as c = (a+b)/2 then continuous else is not guarenteed, as x -> $\infty$ increases (nondecreasing)
# - (4) 
#     - Left 0, right 1, Continuous, as x increases, e decreases, as x -> $\infty$, e -> 0 which is increasing (nondecreasing)
# - (5) 
#     - Left 0, right 1, continuous, nondecreasing since x +

# %%
import numpy as np
import matplotlib.pyplot as plt

# --- CDF definitions ---

def F1(x):
    # 1. Piecewise sqrt distribution
    # F(x)=0 for x<=0
    # F(x)=sqrt(x) for 0<x<=1
    # F(x)=1 for x>1
    return np.piecewise(
        x,
        [x <= 0, (x > 0) & (x <= 1), x > 1],
        [0, lambda t: np.sqrt(t), 1]
    )

def F2(x, sigma=1.0):
    # 2. Logistic CDF with scale sigma
    return 1 / (1 + np.exp(-x / sigma))

def triangular_cdf(x, a, c, b):
    # 3. Triangular-style CDF from prompt
    # F(x) = 0,                                   x <= a
    #        (x-a)^2 / ((b-a)(b-c)),              a < x <= c
    #        1 - (b-x)^2 / ((b-a)(b-c)),          c < x < b
    #        1,                                   x >= b
    #
    # NOTE: this is only guaranteed to be valid if c = (a+b)/2
    # and a < c < b. Otherwise it will typically jump at c.
    return np.piecewise(
        x,
        [x <= a,
         (x > a) & (x <= c),
         (x > c) & (x <  b),
         x >= b],
        [
            0,
            lambda t: ((t - a)**2) / ((b - a)*(b - c)),
            lambda t: 1 - ((b - t)**2) / ((b - a)*(b - c)),
            1
        ]
    )

def F4(x, lam=1.0):
    # 4. Exponential CDF with rate λ
    # F(x)=0 for x<0
    # F(x)=1-exp(-λx) for x>=0
    return np.where(x < 0, 0, 1 - np.exp(-lam * x))

def F5(x):
    # 5. Uniform(0,1) CDF
    # F(x)=0 for x<=0
    # F(x)=x for 0<x<1
    # F(x)=1 for x>=1
    return np.piecewise(
        x,
        [x <= 0, (x > 0) & (x < 1), x >= 1],
        [0, lambda t: t, 1]
    )

# --- Domains to plot on ---
x1 = np.linspace(-1, 2, 400)    # for F1, F5
x2 = np.linspace(-8, 8, 400)    # for logistic
x3 = np.linspace(-0.5, 1.5, 400)  # for triangular-style
x4 = np.linspace(-1, 5, 400)    # for exponential

# Triangular parameters
a = 0.0
b = 1.0
c_good = 0.5   # midpoint -> continuous/"valid" CDF
c_bad  = 0.7   # not midpoint -> creates a jump at c

# --- Plot all six panels (the 5 dists, and two versions of #3) ---
fig, axs = plt.subplots(3, 2, figsize=(10, 10))
axs = axs.ravel()

# 1. sqrt-style on [0,1]
axs[0].plot(x1, F1(x1))
axs[0].set_title("1. CDF: piecewise sqrt on [0,1]")
axs[0].set_xlim(-1, 2)
axs[0].set_ylim(-0.1, 1.1)
axs[0].grid(True)

# 2. Logistic (σ=1)
axs[1].plot(x2, F2(x2, sigma=1.0))
axs[1].set_title("2. Logistic CDF (σ = 1)")
axs[1].set_xlim(-8, 8)
axs[1].set_ylim(-0.1, 1.1)
axs[1].grid(True)

# 3a. Triangular-style, continuous (c midpoint)
axs[2].plot(x3, triangular_cdf(x3, a, c_good, b))
axs[2].set_title(f"3a. Triangular CDF (a={a}, c={c_good}, b={b}) [continuous]")
axs[2].set_xlim(-0.5, 1.5)
axs[2].set_ylim(-0.1, 1.1)
axs[2].grid(True)

# 3b. Triangular-style, discontinuous (c not midpoint)
axs[3].plot(x3, triangular_cdf(x3, a, c_bad, b))
axs[3].set_title(f"3b. Triangular CDF (a={a}, c={c_bad}, b={b}) [discontinuous]")
axs[3].set_xlim(-0.5, 1.5)
axs[3].set_ylim(-0.1, 1.1)
axs[3].grid(True)

# 4. Exponential (λ=1)
axs[4].plot(x4, F4(x4, lam=1.0))
axs[4].set_title("4. Exponential CDF (λ = 1)")
axs[4].set_xlim(-1, 5)
axs[4].set_ylim(-0.1, 1.1)
axs[4].grid(True)

# 5. Uniform(0,1)
axs[5].plot(x1, F5(x1))
axs[5].set_title("5. Uniform(0,1) CDF")
axs[5].set_xlim(-1, 2)
axs[5].set_ylim(-0.1, 1.1)
axs[5].grid(True)

plt.tight_layout()
plt.show()


# %% [markdown]
# ### 6. Some Common Distributions
# 
# For the following distributions:
# - Determine the support
# - Compute the density from the distribution for the logistic and exponential distributions (take a derivative)
# - Plot the density and distribution for a variety of parameter values
# - Take a sample of 1000 draws $(x_1, x_2, ..., x_{1000})$ from the distribution, plot a KDE and ECDF, visually compare with the theoretical pdf/cdf
# - Find an example of this general type of PDF/CDF from the Metabric cancer data
# 
# You can use https://docs.scipy.org/doc/scipy/reference/stats.html to generate values for the pdf/cdf and generate samples of random variates.
# 
# 
# - Logistic distribution (similar to normal): 
# $$
# F(x; \sigma) = \dfrac{1}{1+e^{-x/\sigma}} 
# $$
# with $\sigma >0$.
# - Exponential distribution (similar to log-normal):
# $$
# F_X(x) = \begin{cases}
# 0, & x<0 \\
# 1 - e^{-\lambda x}, & x \ge 0,
# \end{cases}
# $$
# with $\lambda > 0$.
# - Negative Binomial (similar to Poisson): The probability mass function for positive integers is:
# $$
# f(k;r,p) = \dfrac{(k+r-1)!}{k!(r-1)!}(1-p)^k p^r, \quad \text{ for $k=0,...n$}
# $$
# You can interpret this as follows: Flip a coin that comes up heads with probability $p$ until you get $r$ heads, and then stop. What is the probability of stopping at each $k=0,1,2,...$?
# - Categorical (similar to Bernoulli): The probability mass function over $k = 1, 2, ..., K$ categories is
# $$
# f(k;p_1,...,p_K) = p_1^{k=1}p_2^{k=2}...p_K^{k=K}
# $$
# where $0 \le p_i \le 1$ and $ \sum_{k=1}^K p_k = 1$.
# 

# %% [markdown]
# ### Logistic distribution
# - Support
# $$
# x  \in (-\infty, \infty)
# $$
# - Density
# $$
# f(x; \sigma) = \dfrac{1}{\sigma} \dfrac{e^{-x/\sigma}}{(1+e^{-x/\sigma})^2} 
# $$
# - Plots for different parameter values (conceptually how / why)
#     - As sigma gets smaller, the curve gets steeper, and as sigma gets larger, the curve gets flatter. The shape of the curve depends on the value of sigma and the location of the peak due to the 1/sigma factor as well as the shape of the exponential term.
# - Sampling, KDE, ECDF and interpretation
#     - Visually, this is evidence that the sample we drew actually behaves like the logistic distribution and the theoretical formulas for PDF and CDF match what we see in data.
# - How this shows up in METABRIC (a breast cancer clinical/genetic dataset)
#     - Because there are only two possible outcomes, this variable follows a Bernoulli process, which is directly modeled by the logistic distribution. The logistic model estimates the probability that a patient received hormone therapy as a function of one or more predictors (e.g., tumor size, age, receptor status, or cancer stage). This function produces an S-shaped curve where the probability transitions smoothly from 0 to 1 as the predictors change, capturing how clinical or molecular factors increase or decrease the likelihood of hormone therapy being administered.

# %%
import numpy as np
import matplotlib.pyplot as plt

def logistic_cdf(x, sigma):
    return 1 / (1 + np.exp(-x / sigma))

def logistic_pdf(x, sigma):
    return (1 / sigma) * np.exp(-x / sigma) / (1 + np.exp(-x / sigma))**2

# Range of x-values to plot
x = np.linspace(-10, 10, 1000)

# Different scale values sigma to compare
sigmas = [0.5, 1.0, 2.0]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: PDFs
for s in sigmas:
    axes[0].plot(x, logistic_pdf(x, s), label=fr'$\sigma={s}$')
axes[0].set_title("Logistic PDF for different $\sigma$")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].grid(True)
axes[0].legend()

# Right: CDFs
for s in sigmas:
    axes[1].plot(x, logistic_cdf(x, s), label=fr'$\sigma={s}$')
axes[1].set_title("Logistic CDF for different $\sigma$")
axes[1].set_xlabel("x")
axes[1].set_ylabel("F(x)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sigma = 1.0

# Theoretical PDF and CDF for sigma=1 using our functions above
x = np.linspace(-10, 10, 1000)
pdf_true = logistic_pdf(x, sigma)
cdf_true = logistic_cdf(x, sigma)

# 1. Generate 1000 samples from the logistic distribution
#    scipy.stats.logistic uses 'scale' = sigma, 'loc' = mean
np.random.seed(0)  # for reproducibility
sample = stats.logistic.rvs(loc=0, scale=sigma, size=1000)

# 2. KDE estimate of the PDF from the sample
kde = stats.gaussian_kde(sample)
pdf_kde = kde.evaluate(x)

# 3. Empirical CDF (ECDF)
sample_sorted = np.sort(sample)
ecdf_y = np.arange(1, len(sample) + 1) / len(sample)

# --- Plot PDF comparison ---
plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.plot(x, pdf_true, label='True PDF ($\sigma$=1)')
plt.plot(x, pdf_kde, '--', label='KDE from sample')
plt.title("Logistic PDF: theory vs. KDE estimate")
plt.xlabel("x")
plt.ylabel("density")
plt.grid(True)
plt.legend()

# --- Plot CDF comparison ---
plt.subplot(1,2,2)
plt.plot(x, cdf_true, label='True CDF ($\sigma$=1)')
plt.step(sample_sorted, ecdf_y, where='post', linestyle='--', label='ECDF from sample')
plt.title("Logistic CDF: theory vs. ECDF")
plt.xlabel("x")
plt.ylabel("cumulative probability")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# %%
# Read the csv of the metabric dat in /data/metabric.csv

import pandas as pd
metabric = pd.read_csv("./data/metabric.csv")
metabric.head()

# %% [markdown]
# ### Exponential distribution
# - Support
# $$
# x  \in [ 0, \infty)
# $$
# - Density
# $$
# f(x; \lambda) = \lambda e^{-\lambda x}
# $$
# - Plots for different parameter values (conceptually how / why)
#     - Large lambda, the PDF spikes high near 0 and then drops fast; CDF rises fast.
#     - Small lambda PDF is lower and more spread-out; CDF rises slowly.
# - Sampling, KDE, ECDF and interpretation
#     - The dashed KDE curve closely matches the theoretical exponential PDF near x=0 and decays in a similar exponential fashion.
#         - Small deviations at the tails are normal — the exponential tail is thin, so random samples there are sparse
#     - The ECDF (step plot) hugs the theoretical CDF smoothly, confirming that the simulated data behaves as expected from an Exponential(lambda=1) process. The empirical distribution of simulated samples converges to the theoretical exponential distribution as sample size increases
# - How this shows up in METABRIC (a breast cancer clinical/genetic dataset)
#     - Tumor Size: Many patients have small tumors; large tumors are less common -> exponential-like decay.
#         - Positive, right-skewed clinical variables following exponential-like behavior.

# %%
# Plot exponential CDF and PDF for different parameters

import numpy as np
import matplotlib.pyplot as plt

def F4(x, lam):
    return 1 - np.exp(-lam * x)

def f4(x, lam):
    return lam * np.exp(-lam * x)

# Range of x-values to plot
x = np.linspace(0, 10, 1000)

# Different λ values to compare
lambdas = [0.5, 1.0, 2.0]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: PDFs
for lam in lambdas:
    axes[0].plot(x, f4(x, lam), label=fr'$\lambda={lam}$')
axes[0].set_title("Exponential PDF for different $\lambda$")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].grid(True)
axes[0].legend()

# Right: CDFs
for lam in lambdas:
    axes[1].plot(x, F4(x, lam), label=fr'$\lambda={lam}$')
axes[1].set_title("Exponential CDF for different $\lambda$")
axes[1].set_xlabel("x")
axes[1].set_ylabel("F(x)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set the exponential rate parameter
lam = 1.0

# Theoretical functions
def f_exp(x, lam): return lam * np.exp(-lam * x)
def F_exp(x, lam): return 1 - np.exp(-lam * x)

# Simulate 1000 draws from exponential(λ)
np.random.seed(0)
samples = np.random.exponential(scale=1/lam, size=1000)

# Define range for plotting
x = np.linspace(0, 10, 1000)
pdf_true = f_exp(x, lam)
cdf_true = F_exp(x, lam)

# --- Compute KDE for the sample ---
kde = stats.gaussian_kde(samples)
pdf_kde = kde.evaluate(x)

# --- Compute ECDF from the sample ---
samples_sorted = np.sort(samples)
ecdf_y = np.arange(1, len(samples_sorted) + 1) / len(samples_sorted)

# --- Plot PDF comparison ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, pdf_true, label='True Exponential PDF (λ=1)')
plt.plot(x, pdf_kde, '--', label='Sample KDE')
plt.title("Exponential PDF: True vs. KDE (1000 draws)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

# --- Plot CDF comparison ---
plt.subplot(1, 2, 2)
plt.plot(x, cdf_true, label='True Exponential CDF (λ=1)')
plt.step(samples_sorted, ecdf_y, where='post', linestyle='--', label='Empirical CDF')
plt.title("Exponential CDF: True vs. ECDF (1000 draws)")
plt.xlabel("x")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# %%
# Plot the tumor size from metabric

import numpy as np
import matplotlib.pyplot as plt

# import metabric

meta = pd.read_csv("./data/metabric.csv")

# Plot histogram
plt.figure(figsize=(6,4))
plt.hist(meta['Tumor Size'], bins=10, edgecolor='black')

# %% [markdown]
# ### Negative Binomial distribution
# - Support
# $$
# k \in \mathbb{N}  
# $$
# - Probability mass function
# $$
# f(k;r,p) = \dfrac{(k+r-1)!}{k!(r-1)!}(1-p)^k p^r, \quad \text{ for $k=0,...n$}
# $$
# - Plots for different parameter values (conceptually how / why)
#     - The Negative Binomial models the number of failures (k), before reaching r successes in repeated Bernoulli trials with success probability p. As p increases (success more likely), the distribution becomes more concentrated near k = 0. As r increases (more successes required), the distribution spreads out, reflecting a longer process before the stop condition. The CDF rises more slowly for larger r or smaller p.
# - Sampling, KDE, ECDF and interpretation
#     - The histogram (blue) aligns closely with the theoretical PMF (red dashed line), confirming that the sample data follows the Negative Binomial distribution. Small random fluctuations occur because of the finite sample size (1000). This verifies that simulated data matches theoretical probabilities of “failures before r successes.”
# - How this shows up in METABRIC (a breast cancer clinical/genetic dataset)
#     - The Negative Binomial is used for overdispersed count data — where the variance exceeds the mean. In METABRIC, this fits naturally for variables like "Lymph nodes examined positive" where the count variables that often exhibit overdispersion — many small counts, a few large ones — which the Poisson distribution can’t model well.

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parameter grid for Negative Binomial
params = [(3, 0.3), (5, 0.5), (10, 0.7)]  # (r, p)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

for r, p in params:
    # Support (possible k values)
    k = np.arange(0, 40)
    pmf = stats.nbinom.pmf(k, r, p)
    cdf = stats.nbinom.cdf(k, r, p)
    
    axes[0].stem(k, pmf, label=fr'$r={r}, p={p}$', basefmt=" ")
    axes[1].step(k, cdf, where='post', label=fr'$r={r}, p={p}$')

axes[0].set_title("Negative Binomial PMF for different $(r,p)$")
axes[0].set_xlabel("k (failures before r-th success)")
axes[0].set_ylabel("P(X=k)")
axes[0].grid(True)
axes[0].legend()

axes[1].set_title("Negative Binomial CDF for different $(r,p)$")
axes[1].set_xlabel("k")
axes[1].set_ylabel("F(X≤k)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()


# %%
# Example parameters
r, p = 5, 0.3

# Simulate 1000 draws
np.random.seed(0)
samples = stats.nbinom.rvs(r, p, size=1000)

# Theoretical PMF
k = np.arange(0, max(samples)+1)
pmf_theoretical = stats.nbinom.pmf(k, r, p)

# Empirical frequencies
counts, bins = np.histogram(samples, bins=np.arange(-0.5, max(samples)+1.5, 1), density=True)

# Plot comparison
plt.figure(figsize=(8,5))
plt.bar(bins[:-1], counts, alpha=0.6, label='Empirical (1000 samples)')
plt.plot(k, pmf_theoretical, 'r--', linewidth=2, label='Theoretical PMF')
plt.title(f"Negative Binomial (r={r}, p={p}) — Empirical vs Theoretical")
plt.xlabel("k (failures before r-th success)")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.show()


# %%
# Plot the mutation distribution

import numpy as np
import matplotlib.pyplot as plt

# import metabric

meta = pd.read_csv("./data/metabric.csv")

# Plot histogram
plt.figure(figsize=(6,4))
plt.hist(meta['Lymph nodes examined positive'], bins=10, edgecolor='black')

# %% [markdown]
# ### Categorical distribution
# - Support
# $$
# k \in \mathbb{N}  
# $$
# - Probability mass function
# $$
# f(k;p_1,...,p_K) = p_1^{k=1}p_2^{k=2}...p_K^{k=K}
# $$
# - Plots for different parameter values (conceptually how / why)
#     - The Categorical distribution represents probabilities across discrete outcomes. The PMF plot simply shows the height of each category’s probability. If one probability (e.g., p4=0.55) is dominant, it corresponds to the most common outcome. This is a generalization of the Bernoulli distribution (which has only 2 categories).
# - Sampling, KDE, ECDF and interpretation
#     - The empirical frequencies (right bars) are nearly identical to the theoretical probabilities (left bars). This confirms that random sampling reproduces the expected categorical proportions over many draws. Small mismatches arise from sampling randomness but vanish as n goes to infinity.
# - How this shows up in METABRIC (a breast cancer clinical/genetic dataset)
#     - The Categorical distribution fits variables that describe mutually exclusive classes — exactly one outcome per observation. In METABRIC, categorical variable Tumor Stage (I, II, III, IV) is an example of this. Each patient belongs to one and only one category, making categorical models ideal. Each category has its own probability, which allows modeling class probabilities or feeding them into multinomial logistic regression for prediction.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Category probabilities for two cases
p_sets = [
    [0.1, 0.2, 0.4, 0.3],
    [0.05, 0.15, 0.25, 0.55]
]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

for i, p in enumerate(p_sets):
    categories = np.arange(1, len(p)+1)
    ax[i].bar(categories, p, color='teal', alpha=0.7)
    ax[i].set_xticks(categories)
    ax[i].set_xlabel("Category")
    ax[i].set_ylabel("Probability")
    ax[i].set_ylim(0, 1)
    ax[i].set_title(f"Categorical PMF\np={p}")
    ax[i].grid(True, axis='y')

plt.tight_layout()
plt.show()



# %%
# True probabilities for 4 categories
p_true = [0.1, 0.2, 0.4, 0.3]
categories = np.arange(1, len(p_true)+1)

# Simulate 1000 samples
np.random.seed(0)
samples = np.random.choice(categories, size=1000, p=p_true)

# Empirical frequencies
counts = np.bincount(samples)[1:] / len(samples)

# Plot comparison
plt.figure(figsize=(8,5))
bar_width = 0.35
plt.bar(categories - bar_width/2, p_true, width=bar_width, label='True p_k', alpha=0.7)
plt.bar(categories + bar_width/2, counts, width=bar_width, label='Empirical freq', alpha=0.7)
plt.xticks(categories)
plt.xlabel("Category")
plt.ylabel("Probability / Frequency")
plt.title("Categorical Distribution — True vs Empirical (1000 draws)")
plt.legend()
plt.grid(True, axis='y')
plt.show()



