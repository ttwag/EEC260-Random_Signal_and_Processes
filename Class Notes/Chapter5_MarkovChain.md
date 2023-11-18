# Markov Chain
## Introduction
A Markov Chain is a discrete-time Markov process. If X(0), X(1),... is a sequence of random variables, then this sequence is a Markove chain if
$$P(X(t+1) = i_{t+1}|X(t) = i_{t}, X(t-1) = i_{t-1},\dots,X(0)=i_{0})= P(X(t+1)=i_{t+1}|X(t)=i_{t})$$
for all nonnegative integers $t$ and all values $i_{t+1}, i_{t},\dots,i_{0}$ for $X(t + 1), X(t),\dots, X(0)$ respectively.

We consider only **finite-state** Markov chains. That is, the values assumed by the random variables form a finite set, $S$, which we take to be $\Set{1, 2,\dots,N}$.

$t$ denotes time. Intuitively, this means given the present, the future is independent of the past.

The elements of $S$ are **states**. If $X(t) = i$, the state at time $t$ is $i$.

**Initiali State** refers to the random variable $X(0)$.

The Markov chain is **homogeneous** if $P(X(t+1) = j|X(t)=i)$, which means i and j deosn't depend on $t$.

## Transition Probability Matrix
The matrix P is called the (one-step) transition probability matrix.

$$
P =
\begin{pmatrix}
p_{1, 1} & p_{1,2} & \dots & p_{1,N}\\
p_{2,1} & p_{2,2} & \dots & p_{2,N}\\
\vdots & \vdots & \ddots & \vdots \\
p_{N, 1} & p_{N, 2} & \dots & p_{N,N} \\
\end{pmatrix}
$$

All its elements are nonnegative and the sum of elements in any row is 1.

## The m-Step Transition Probability
We define the m-step transition probability $p_{i, j}^{(m)}$, for $m \geq 1$ to be the probability that $X(t + m) = j$ given that $X(t) = i$, that is $p_{i, j}^{(m)} = P(X(t + m) = j | X(t) = i)$.

## The Chapman-Kolmogorov Equations
The Chapman-Kolmogorov Equation tells us that to get the $m$ step transition matrix, we could get the $m = 1$ transition matrix and raise it to the power $m$.
$$P^{(m)} = P^{m}$$

## State Distribution
The PMF of $X(t)$ is represented by the vector $\boldsymbol{\pi(t)} = (\pi_1(t), \pi_2(t),\dots, \pi_{N}(t))$, in which $\pi_{i}(t) = P(X(t) = i)$. This vector is the state distribution of the Markov Chain $X(t)$ at time $t$.

The state distribution $\pi(0)$ of the initial state $X(0)$ is the **initial distribution** of the chain.

In addition, we have
$$\boldsymbol{\pi}(t+m) = \boldsymbol{\pi}(t)\boldsymbol{P}^{m}=\boldsymbol{\pi}(t)\boldsymbol{P}^{(m)}$$

## Stationary Distribution
A distribution $\pi$ is **stationary** if $\boldsymbol{\pi} = \boldsymbol{\pi} \bold{P}$

Every Markov chain has at least one stationary distribution.

## Limiting Distribution
A Markov chain has a **limiting distribution** if for every initial distribution $\boldsymbol{\pi}(0)$, the limit $\lim_{t \to \infty} \boldsymbol{\pi}(t)$ exists and is independent of $\boldsymbol{\pi}(0)$.
This limit is $\boldsymbol{\pi}(\infty)$, and it's the limiting distribution of the chain.

A Markob chain has a limiting distribution if and only if for any initial distribution $\boldsymbol{\pi}(0)$, $\lim_{t \to \infty}\boldsymbol{\pi}(0)\bold{P}^{t}$ exists and is independent of $\boldsymbol{\pi}(0)$.
The limit is a matrix, denoted by $\bold{P}^{\infty}$, and all of its rows are identical. The limiting distribution is the common row in $\bold{P}^{\infty}$.

## Classification of States
### Communicating Class
We say that state $j$ is **accessible** from state $i$ if $p_{i, j}^{(m)} > 0$ for some $m \geq 0$. That is, it's possible
to reach state $j$ from state $i$ in some nonnegative number of steps. This is written as $i \to j$. 
Note that $p_{i, i}^{(0)} = 1$ and $p_{i, j}^{(0)} = 0$ if $i \neq j$.

$i$ and $j$ **communicates** if $j$ is accessible from $i$ and $i$ is accessible from $j$. This is $i \leftrightarrow j$.
$$i \leftrightarrow j \iff (i \rightarrow j \land j \rightarrow i)$$
Properties of Communicativity
* $i \leftrightarrow i$
* $i \leftrightarrow j \implies j \leftrightarrow i$.
* $(i \leftrightarrow j \land  j \leftrightarrow k) \implies i \leftrightarrow k$

Two states that communicate with each other are said to be in the same **communicating class**.

### Irreduciblility
We say that the Markov chain is **irreducible** if it has only one communicating class, thus all states in the Markov chain communicate with each other.
The Markov chain is **irreducible** if and only if for all $i, j \in S, p_{i,j}^{(m)} > 0$ for some $m \geq 0$.

### Period
The **period** of a state $i$ is defined as
$$d_i = gcd\Set{m \geq 1 : p_{i, i}^{(m)} > 0}$$
if there is a positive integer $m$ for which $p_{i, i}^{(m)} > 0$.
In other words, 
If starting from state $i$, it is possible to revisit state $i$ at some future time with positive probability.

Otherwise, if $p_{i, i}^{(m)} = 0$ for all $m \geq 1$, then we define $d_i = \infty$.

We say that a Markov chain is **aperiodic** if every state has period equal to 1.

**If two distinct states $i$ and $j$ communicates, $i \leftrightarrow j$, then they have the same period.**

**Important Theorem: Every irreducible aperiodic Markov chain has a limiting distribution.**

### Recurrent and Transient States
We say that state $i$ is **recurrent** if it is accessible from every state $j$ which is accessible from $i$. That is $i \to j$ implies $j \to i$.

A finite state Markov Chain has at least one recurrent state.

A state $i$ is **transient** if it is not recurrent. That is, there exists at least one stae $k$ that can be reached from $i$ but from which there is no return to $i$.


## Absorbing State and Absorbing Markov Chain
$f_{i, j} = \sum_{m = 1}^{\infty} f_{i,j}^{(m)}$ is the probability of accessing state $j$ given that the chain starts in state $i$, in a positive number of steps.

* A state is absorbing if $p_{i,i}^{(1)} = 1$. That is, once the chain reaches state $i$, it never leaves that state.
* A Markov chain is **absorbing** if it has at least one accessible absorbing state and from any state, there is at least one accessible absorbing state.
* Thus, the Markov chain is absorbing if and only if **every recurrent state is absorbing**, since a recurrent state needs to be able to reached back again.
The rest of the state will be transient states.

## Probability To Reach An Absorbing State
Let $j$ be an **absorbing state** in an absorbing Markov chain. 
<br>Let $A_j$ be the event that the Markov chain is **eventually absorbed** in state $j$.
Then $f_{i,j}$ is the probability of this event given that the Markov chain starts at the transient state $i$.
$$f_{i,j} = p_{i, j} + \sum_{k \in S_{Tr}}p_{i, k} f_{k, j}$$
Where   $S_{Tr}$ is the set of transient states.

Note: $p_{i, j}$ without superscript denotes the one-step probability.

## Time to Be Absorbed in an Absorbing State
Let $T_{absorb}$ be the time it takes to be absorbed in some absorbing state and $\mu_i$ be the average of this time if the Markov chain starts at the transient state $i$. We have
$$\mu_i = 1 + \sum_{j \in S_{Tr}}p_{i,j}\mu_{j}$$
