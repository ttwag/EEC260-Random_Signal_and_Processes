
## Counting Process
A stochastic process $N(t)$ is a **counting process** if:
1. $N(0) = 0$
2. $N(t)$ assumes nonnegative integer values.
3. If $t_1 < t_2$, then $N(t_1) \leq N(t_2)$
4. If $t_1 < t_2$, then $N(t_2) - N(t_1)$ counts the number of events that occur in the interval $(t_1, t_2]$.

A counting process starts at time 0 and counts the occurrences of events.

### Arrival Times
The $k^{th}$ arrival time, denoted by $T_k$, is the occurrence time of the $k^{th}$ event.

### Interarrival Times
The $k^{th}$ interarrival time, defined by $\Delta T_k$, is $\Delta T_k = T_k - T_{k-1}$ for $k \geq 2$ and<br>
$\Delta T_1 = T_1$

## Poisson Process
A counting process $N(t)$ is a **Poisson process** of rate $\lambda$ if

1. $N(0) = 0$.
2. $N(t)$ has **stationary independent increments**. $N(t_1) - N(t_0)$ and $N(t_1^{'}) - N(t_0^{'})$ respectively, are independent random variables.
3. $N(t)$, for any given $t > 0$, is Poisson($\lambda t$). That is, a Poisson random varible with mean $\lambda t$, where $\lambda > 0$ is constant, for $k = 0, 1, 2, \dots,$

The parameter $\lambda$ is the **rate** of the Poisson process.

## Poisson Process PMF
For a Poisson random variable, $M = N(t_1)-N(t_0)$, the PMF is
$$P_M(m) = 
\begin{cases}
\frac{[\lambda(t_1 - t_0)]^{m}}{m!}e^{-\lambda (t_1 - t_0)} & m = 0, 1,\dots, \\
0 & otherwise.
\end{cases}
$$

We could write a Poisson PMF for a set of time instants $t_1 < t_2 < \dots < t_k$

**Intuition:** we could think of this formula as a regular Poisson Distribution but with concept of time inside. If we revisit the Poisson Distribution from the Random Variable Chapter, we find that $\lambda$ is the average number of arrivals (expected value of binomial distribution) because it's $n * p$, where n is the number of trials and p is the success (arrival) probability. Here, we are restricting the trial to be within the time interval $t_1 - t_0$, and subsituting $\lambda$ to be arrivals/second ($\lambda$) times the time difference ($t_1 - t_0$). The product is the average number of arrival again.

### Property of Poisson Process
**Interarrival Time**

Let $N(t)$ be a Poisson process of rate $\lambda$. Then, the interarrival times $\Delta T_k, k = 1, 2, \dots,$ are independent Exponential($\lambda$) random variable, where $f_{X}(x) = \lambda e^{-\lambda x}$ for $x \geq 0$

**Distribution of Arrival Times of Poisson Process**

Let $N(t)$ be a Poisson process of rate $\lambda$. Then, the $k^{th}$ arrival time, $T_k$, has a PDF given by
$$
f_{T_k}(t) = 
\begin{cases}
0 & t < 0\\
\lambda e^{-\lambda t} \frac{(\lambda t)^{k-1}}{(k-1)!} & t \geq 0.
\end{cases}
$$


**Conditional Distribution of Arrival Times of Poisson Processes**

We consider the arrival times $T_1, T_2, \dots, T_n$ given that $N(t) = n$.
Note that $0 \leq T_1 \leq T_2 \leq \dots \leq T_n \leq t$

We have for $0 < t_1 < t_2 \dots < t_n < t$
$$f_{T_1, \dots, T_n | N(t)} (t_1, \dots, t_n | n) = \frac{n!}{t^n}$$