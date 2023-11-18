# Wiener Process
## The Wiener Process
A continuous-valued stochastic process $W(t)$, $t \geq 0$, is a **Wiener process** if
1. $W(0) = 0$.
2. $W(t)$ has stationary independent increments.
3. $W(t)$ is Gaussian($0, \alpha^2t$). That is, a Gaussian random varibale with  zero mean and variance $\alpha^2t$.

The parameter $\alpha^2$, where $\alpha > 0$, is called the **variance rate**.
### Important Properties
* $W(t_2) - W(t_1), W(t_3)-W(t_2), \dots$ are independent for all $t_1 < t_2 < \dots$. Therefore, the process $W(t)$ has independent increments.
* The distribution of $W(t_2)-W(t_1)$ is the same as that of $W(t_2 - t_1) - W(0) = W(t_2 - t_1)$.

## Mean and Autocorrelation Function of the Wiener Process
* $E[W(t)] = 0$ for $t \geq 0$.
* For $0 \leq t_1 \leq t_2$, we have $R_W(t_1, t_2) = E[(W(t_1))^{2}] = \alpha^{2}t_1$
* For all $t_1, t_2$, $$R_W(t_1, t_2) = \alpha^2min\set{t_1, t_2}$$

