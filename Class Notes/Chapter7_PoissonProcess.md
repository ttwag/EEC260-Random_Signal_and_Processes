
## Counting Process
A stochastic process $N(t)$ is a **counting process** if for every sample function, $n(t, s) = 0$ for $t < 0$ and $n(t, s)$ is integer-valued and nondecreasing with time.

A counting process starts at time 0 and counts the occurrences of events.
## Poisson Process
A counting process $N(t)$ is a **Poisson process** of rate $\lambda$ if

(a) The number of arrivals in any interval $(t_0, t_1]$, $N(t_1) - N(t_0)$, is a Poisson random variable with expected value $\lambda (t1-t_0)$

(b) For any pair of nonoverlapping intervals $(t_0, t_1]$ and $(t_0^{'}, t_1^{'}]$, the number of arrivals in each interval, $N(t_1) - N(t_0)$ and $N(t_1^{'}) - N(t_0^{'})$ respectively, are independent random variables.


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

## Poisson Process Joint PMF
For a **Poisson process $N(t)$** of rate $\lambda$, the joint PMF of 
