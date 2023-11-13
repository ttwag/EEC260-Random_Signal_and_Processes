# Markov Chain
## Introduction
A Markov Chain is a discrete-time Markov process. If X(0), X(1),... is a sequence of random variables, then this sequence is a Markove chain if
$$P(X(t+1) = i_{t+1}|X(t) = i_{t}, X(t-1) = i_{t-1},\dots,X(0)=i_{0})= P(X(t+1)=i_{t+1}|X(t)=i_{t})$$
for all nonnegative integers $t$ and all values $i_{t+1}, i_{t},\dots,i_{0}$ for $X(t + 1), X(t),\dots, X(0)$ respectively.

We consider only **finite-state** Markov chains. That is, the values assumed by the random variables form a finite set, $S$, which we take to be $\Set{1, 2,\dots,N}$.

$t$ denotes time. Intuitively, this means given the present, the duture is independent of the past.

The elements of $S$ are **states**. If $X(t) = i$, the state at time $t$ is $i$.

**Initiali State** refers to the random variable $X(0)$.

The Markove chain is **homogeneous** if $P(X(t+1) = j|X(t)=i)$, which means it deosn't depend on $t$.

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

The state distribution $\pi(0) of the initial state $X(0)$ is the **initial distribution** of the chain.

In addition, we have
$$\boldsymbol{\pi}(t+m) = \boldsymbol{\pi}(t)\bold{P}^{m}=\boldsymbol{\pi}(t)\bold{P}^{(m)}$$

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
