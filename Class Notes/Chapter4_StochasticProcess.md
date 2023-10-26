# Stochastic Processes

Stochastic means random, and process means function of time.

A **stochastic process** $X(t)$ consists of an experiment with a probability measure $P[.]$ defined on a sample space $S$ and a function that assigns a time function $x(t, s)$ to each outcome $s$ in the sample space of the experiment.

Just as a random variable assigns a real number to each outcome, a stochastic process assigns a sample function to each outcome.

![Figure3](./images/Figure3.png)

A sample function $x(t, s)$ is the time function associated with outcome $s$ of an experiment. A sample function corresponds to an outcome of a stochastic process experiment. It's one of the possible time functions that can result from the experiment. The **ensemble** of a stochastic process is the set of all possible time functions that can result from an experiment.

Given the process has different random variables a different time, it's a two-dimensional model with two kinds of averages.
With $t$ fixed at $t = t_0$, $X(t_0)$ is a random variable, and we could find its expected value and variance. This is the **ensemble averages**. There is also a **time average** of the sample function.

To characterize a random process, we could find the joint PDF of its random variables at different time, $f_{X(t_1), \dots, X(t_k)}(x_1,\dots,x_k)$ for all $k$

## Bernoulli Process
A Bernoulli (p) process $X_n$ is an independent and identically distributed random sequence in which each $X_n$ is a Bernoulli (p) random variable.
 
For a single sample $X_i$, the Bernoulli PMF is:
$$ P_{X_i}(x_i) = 
\begin{cases}
p^{x_i}(1-p)^{1-x_i} & x_i \in \Set{0, 1} \\
0 & otherwise.
\end{cases}
$$

The joint PMF of the process is
$$P_\bold{X}(\bold{x}) = 
\begin{cases}
\prod_{i = 1}^{n}p^{x_i}(1-p)^{1-x_i} = p^{k}(1-p)^{n-k} & x_i \in \Set{0, 1}, i = 1, \dots, n, \\
0 & otherwise.
\end{cases}
$$
where $k = x_1 + \dots + x_n$ and $\bold{X} = [X_1, \dots, X_n]^T$

## Counting Process
A stochastic process $N(t)$ is a **counting process** if for every sample function, $n(t, s) = 0$ for $t < 0$ and $n(t, s)$ is integer-valued and nondecreasing with time.

## Poisson Process


 The mean of the process is a function of time that could increase and decrease.
