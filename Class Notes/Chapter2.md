# Chapter 2 -  Random Variable

## Formal Definition of the Random Variable

A random variable, $X$, is a function from the sample space $\Omega$ to the real line $\mathbb{R}$ which associates to each outcome $\omega$ a real value $X(\omega)$, such that for any subset $R \subset \mathbb{R}$, obtained by taking unions, intersections, and complements of a discrete number (finite or infinite) of open or closed intervals in $\mathbb{R}$, the set $X^{-1}(R) = \Set{\omega : X(\omega) \in R}$ is an event in $F$; $F$ is  the set of all events and $X^{-1}(R)$ maps the subset $R$ back to the outcomes in the sample space. 
<br>
<br>
We use $P(X \in R)$ to denote the probability of this event, that is, 

$P(X \in R) = P(X^{-1}(R)) = P(\Set{\omega : X(\omega) \in R})$
<br>
This shows that the probability of the random variable and $\omega$ are associated.
<br>
<br>

For any real number $x$,
<br>
$X^{-1}((-\infty, x]) = \Set{\omega : X(\omega) \leq x}$ 
<br>
is an event with probability $P(X \leq x)$. 
<br>
![Figure1](./images/Figure1.png)
<br>
Note that, $R$ is the interval $(-\infty, x]$. This means that we are summing the probability of every outcomes in the interval to obtain the probability that the event representing that interval occurs.
<br>
<br>
This probability, denoted by $F_X(x)$, is the *cumulative distribution function* (CDF) of $X$.
<br>

## Properties of the CDF
1) $F_X(-\infty)$ = 0, $F_X(\infty)$ = 1.
2) $F_X(x)$ is nondecreasing.
3) $F_X(x)$ is right continuous. That is, $\lim_{x \to x_0^{+}}F_X(x) = F_X(x_0)$
4) $P(X = x_0) = F_X(x_0) - F_X(x_0^{-})$.<br>
Thus, $X$ takes the vaue $x_0$ with nonzero probability iff $F_X(x)$ is discontinuous at $x_0$

## Discrete Random Variable
The CDF of a discrete random variable is a staircase function with discontinuities.<br>
The probability that $X$ assumes the value $x_0$ is <br>
$p_X(x_0) = P(X = x_0) = P(\Set{\omega : X(\omega) = x_0}) = F_X(x_0) - F_X(x_0^{-})$<br>
This is the *probability mass function* (PMF) of the random variable $X$.

## Continuous Random Variables
A random variable $X$ is continuous if there is a function $f_X(x)$ such that for all $x_0 \in \mathbb{R}$, 
$F_X(x_0)$ = $\int_{-\infty}^{x_0} f_X(x) \, dx$<br><br>
The function $f_X(x)$ is the *probability density function* (PDF) of the random variable $X$.<br><br>
Since $F_X(\infty) = 1$, we have $\int_{-\infty}^{\infty} f_X(x) dx = 1$<br>
If $F_X(x)$ is differentiable, then $f_X(x)$ is its derivative.
