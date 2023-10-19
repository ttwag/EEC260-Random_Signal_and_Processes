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

![Figure1](./images/Figure1.png)

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

## Conditional CDF
The *conditional CDF* of a random variable $X$ given and event $E$, with $P(E) > 0$, is given by<br>
$F_X(x|E) = P(X \leq x|E) = \frac{P(X \leq x \cap E)}{P(E)}$ <br><br>
The *conditional PDF*, $f_X(x|E)$, of $X$ given $E$ is <br>
$F_X(x|E) = \int_{-\infty}^{x} f_X(x|E)dx$<br><br>
## Derived Random Variable
Let $X$ be a random variable and $Y = g(X)$, for some function $g:\mathbb{R} \to \mathbb{R}$.<br>
Then, $Y$ is a random variable.<br>
### CDF
Let $y$ be a real number and $S_ \leq y = \Set{x: g(x) \leq y}$. Then, $F_Y(y) = P(Y \leq y) = P(X \in S_\leq y)$ <br>
### PMF
If $X$ is discrete, then $ Y = g(X)$ is discrete.<br>
Let $S_=y = \Set{x: g(x) = y}$. We have $p_Y(y) = P(X \in S_=y)$
### Go from PDF of X to Y
Find the CDF of $Y$ from $X$ and differentiate it.

## Expected Value of a Random Variable
The *expected value*, $E[X]$, is defined as <br>
### Discrete $X$ with PMF
$m_X = E[X] = \sum_{x}x\thinspace p_X(x)$
### Continuous $X$ with PDF 
$E[X] = \int_{-\infty}^{\infty} g(x) \thinspace f_X(x)dx$
### Derived Y with PMF
$E[Y] = \sum_{x} g(x)p_X(x)$

## Variance, Moments, Moemnet Generating Function, and Characteristic Function of a Random Variable
### Moment
The $l^{th}$ moment of the random variable $X$, where $l$ is a positive integer, is given by $E[X^{l}]$. The first moment is the expectation.
### Variance
The *variance* of $X$ is $K = Var[X] = E[(X - m_X)^{2}] = E[X^{2}] - m^{2}_X$
### Moment Generating Function
The *moment generating function* of $X$ is $M_X(s) = E[e^{sX}]$ where s is in the region of nvergence (ROC) of the function.<br>
* Property: $E[X^{l}] = \frac{d^{l}}{ds^{l}} M_X(s)\large |_{s = 0}$

### Characteristic Function
The *characteristic function* of $X$ is obtained by evaluating $M_X(s)$ on the imaginary axis. That is, $\Phi_X(\omega) = E[e^{j\omega X}]$, where $j = \sqrt{-1}$. Since $|e^{j\omega X}| = 1$, the characteristic function always exists. 
* Discrete Fourier Transform Property of $X$: $\Phi_X(\omega) = \sum_x p_X(x)\space e^{j\omega x}$ and $p_X(\omega) = \frac{1}{2 \pi}{\large \int_{-\pi}^{\pi}}\Phi_X(\omega)e^{-j\omega x}d\omega$.
* Continuous Fourier Transform Property of $X$: $\Phi_X(\omega) = {\large \int_{-\infty}^{\infty}f_X(x)e^{j\omega x}dx}$ and $f_X(x) = \frac{1}{2 \pi}\int_{-\infty}^{\infty}\Phi_X(\omega)e^{-j\omega x}d\omega$.
* Important Properties
    1) $\Phi_X(\omega)$ is bounded. $|\Phi_X(\omega)| \leq \Phi(0) = 1$.
    2) $\Phi_X^{*}(\omega) = \Phi_X(-\omega)$.
    3) $E[X^{l}] = \frac{1}{j^{l}}\Phi_X^{(l)}(0)$, provided that the derivatives exist.
## Common Discrete Random Variables
### Bernoulli Random Variable
Denoted by Bernoulli($p$), is a discrete random variable which assumes two values, 0, and 1, with PMF: $p_X(0) = 1 - p$ and $p_X(1) = p$. We have
* $E[X] = p$
* $K_X = p(1 - p)$
* $M_X(s) = (1 - p) + pe^{s}$
* $\phi_X(\omega) = (1 - p) + pe^{j\omega}$.
### Binomial Random Variable
Denoted by Binomial($n, p$), is a discrete random variable which counts the number of successes in n independent trials where the probability of each success is $p$. It assumes the values $0, 1, 2, ..., n $ with PMF given by <br>
$$p_X(k) = {\binom {n}{k}}p^{k}(1 - p)^{n - k}$$
We have
* $E[X] = np$
* $K_X = np(1-p)$
* $M_X(s) = ((1 - p) + pe^{s})^{n}$
* $\phi_X(\omega) = ((1-p) + pe^{j\omega})^{n}$
### Poisson Random Variable
Denoted by Poisson($\lambda$), $\lambda > 0$, os a disrete random variable which assumes the values $0, 1, 2,...$ with PMF given by $$p_X(k) = e^{-\lambda}\frac {\lambda^{k}}{k!}$$
We have
* $E[X] = \lambda$
* $K_X = \lambda$
* $M_X(s) = e^{\lambda(e^{s} - 1)}$
* $\phi_X(\omega) = e^{\lambda (e^{j\omega} - 1)}$
* Poisson Random Variable could be used as an approxiation for Binomial Random Variable with $p = \frac{\lambda}{n}$ as $ n \to \infty$ 
### Geometric Random Variable
Denoted by Geometric($p$), $0 < p < 1$, is a discrete random variable which counts the number of trials required for the first success in independent trials, where the probability of each success is $p$. It assumes the values $1, 2, 3,...$ with the PMF given by $p_X(k) = (1 - p)^{k-1}p$.
* $E[X] = \frac{1}{p}$
* $K_X = \frac{1-p}{p^{2}}$
* $M_X(s) = \frac{p}{e^{-s}-(1-p)}$, where real part of $s < ln(1-p)$.
* $\phi_X(\omega) = \frac{p}{e^{-j\omega} - (1 - p)}$.
## Common Continuous Random Variables
### Uniform Random Variable
A uniform random variable, $X$, over the interval $[a, b]$, denoted by Uniform(a, b), where a < b, has PDF and CDF
$$
f_X(x) = 
\begin{cases}
    \frac{1}{b - a} & \text{for} \space a \leq x \leq b\\
    0 & \text{otherwise.}
\end{cases}
$$

$$
F_X(x) = 
\begin{cases}
    0 & x < a\\
    \frac{x - a}{b - a} & a \leq x \leq b\\
    1 & x > b    
\end{cases}
$$
* $E[X] = \int_{a}^{b} \frac{x}{b-a}dx = \frac{1}{2}(b + a)$
### Exponential Random Variable
An exponential random variable, $X$, with parameter $\lambda > 0$, denoted by Exponential ($\lambda$), has PDF and CDF

$$
f_X(x) = 
\begin{cases}
    0 & x < 0\\
    \lambda e^{-\lambda x} & x \geq 0\\
\end{cases}
$$

$$
F_X(x) = 
\begin{cases}
    0 & x < 0\\
    1- e^{-\lambda x} & x \geq 0\\
\end{cases}
$$
* $E[X] = \frac{1}{\lambda}$
* $E[X^{2}] = \frac{1}{\lambda^{2}}$

The exponential random variable is memoryless, which means 
* $P(X > a + b | X > b) = P(X > a)$.
* $P(X > a + b) = P(X > a)P(X > b)$.

### Gaussian Random Variable
A *Gaussian*, also called *normal*, random variable, $X$, denoted by Gaussian($m, K$), $K > 0$, is a continuous random variable with PDF and CDF given by
$$ f_X(x) = \frac{1}{\sqrt{2 \pi K}}e^{-\frac{(x-m)^{2}}{2K}}$$

$$F_X(x) = \frac{1}{\sqrt{2 \pi K}} \int_{-\infty}^{x}e^{-\frac{(x-m)^{2}}{2K}}dx$$
Important Properties:
* If $X$ is Gaussian($m, K$), then $Y = aX + b$, where $a ≠ 0$, is Gaussian($am + b, |a|^{2}K$).
* $E[X] = m$
* $K_X = K$
* $M_X(s) = e^{ms + \frac{Ks^{2}}{2}}$
* $\phi_X(\omega) = e^{m\omega + \frac{K\omega^{2}}{2}}$

Let $\phi(x)$ be the CDF of Gaussian(0, 1), that is
$$\phi = \frac{1}{2 \pi} \int_{-\infty}^{x} e^{\frac{-u^{2}}{2}}du$$
If $X$ is Gaussian($m, K$), then $$F_X(x) =  \frac{x - m}{\sqrt{K}}$$
and $$\phi(z) = 1 - \phi(-z)$$
due to the symmetry of the Normal Distribution.

#### Important Properties
* The sum of two independent Gaussian($m_X, K_X$) and Gaussian($m_Y, K_Y$) is Gaussian($m_X+m_Y, K_X+K_Y$ )
## Joint Distribution of Random Variables
Consider the discrete random variables $X$ and $Y$. The **joint probability mass function** of $X$ and $Y$ is the probability $P(X = x, Y = y)$ that $X$ takes the value $x$ and 
$Y$ takes the value $y$ for any possible values $x$ and $y$ assumed by $X$ and $Y$.
The probability is denoted by $p_{X, Y}(x, y)$.

For continuous random variables, the **joint cumulative distribution function (joint CDF)**
is the probability $P(X \leq x, Y \leq y)$ for real $x$ and $y$. This is denoted by $F_{X,Y}(x, y)$.

We say that $X$ and $Y$ are **jointly continuous** if there exists a function $f_{X,Y}(x, y) such that for all $x, y \in \mathbb{R}$,
$$F_{X, Y}(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{X,Y}(u, v)dvdu$$
This PDF is called the **joint probability density function (joint PDF)** of $X$ and $Y$. If $F_{X, Y}(x, y)$ is differentiable, then
$$f_{X,Y}(x, y) = \frac{\partial^{2}}{\partial x \partial y}F_{X,Y}(x, y)$$

### Properties of the Joint CDF
1) $F_{X,Y}(x, -\infty) = F_{X,Y}(-\infty, y) = 0, F_{X,Y}(\infty, \infty)=1.$
2) $F_{X,Y}(x, \infty) = F_X(x)$ and $F_{X, Y}(\infty, y) = F_Y(y)$
3) $F_{X,Y}(x,y)$ is nondecreasing in the two variables $x$ and $y$, that is, $F_{X,Y}(x_1, y_1) \leq F_{X,Y}(x_2, y_2)$ for $x_1 \leq x_2$ and $y_1 \leq y_2$

### Marginal CDF
We integrate one of the variable to accumulate the probability of that variable at every region in real number.

$$f_X(x) = \int_{-\infty}^{\infty} f_{X, Y}(x, y)dy$$
$$f_Y(y) = \int_{-\infty}^{\infty} f_{X, Y}(x, y)dx$$

Now, the variable left would have probability that depends on its own distribution.

$X$ and $Y$ are independent iff $$F_{X,Y}(x, y) = F_{X}(x)F_{Y}(x)$$
or equivalently, 
$$f_{X,Y}(x, y) = f_X(x)f_Y(y)$$
for all real numbers $x$ and $y$.

### Conditional CDF and PDF
The **conditional cumulative distribution function** of the continuous random variable $X$ given the continuous random variable $Y$ is
$$F_{X|Y}(x|y)=\frac{F_{X,Y}(x,y)}{F_Y(y)}$$
provided that $F_Y(y) \neq 0$.

The **conditional probability density function** of the continuous random variable $X$ given the continuous random variable $Y$ is
$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$
provided that $f_Y(y) \neq 0$

### Covariance of $X$ and $Y$
The **covariance** of $X$ and $Y$ is $$K_{X,Y} = E[(X-E[X])(Y-E[Y])]$$
If $X$ and $Y$ are independent, then $$K_{X,Y} = 0$$
If $K_{X,Y} = 0$, then $X$ and $Y$ are **uncorrelated**

### Conditional Expectation
Let $X$ and $Y$ be random variables. The **conditional expectation** of $X$ given that $Y = y$ is 
$$E[X|Y=y] = \sum_x xp_{X|Y}(x|y)$$
or 
$$E[X|Y=y] = \int_{-\infty}^{\infty}xf_{X|Y}(x|y)dx$$

Special Property:
$E[E[X|Y]] = E[X]$

## Random Vectors
Let $X_1, X_2,..., X_n$ be random variables. Then, $\bold{X} = (X_1, X_2,...,X_n)$, is a (row) *random vector*
### Discrete
If $X_1, X_2,...,X_n$ are discrete, then $\bold{X}$ is a discrete random vector with joint PMF
$$p_{\bold{X}}(\bold{x})=P(X_1=x_1, X_2=x_2,...,X_n = x_n)$$
where $\bold{x} = (x_1, x_2,...,x_n)$ and $x_1, x_2,...,x_n$ are values assumed by $X_1, X_2,...,X_n$

### Continuous
If $X_1, X_2,...,X_n$ are continuous, then $\bold{X} = (X_1, X_2,...,X_n)$ is a continuous random vector with joint CDF given by
$$F_{\bold{X}}(\bold{x}) = P(X_1 \leq x_1, X_2 \leq x_2,..., X_n \leq x_n)$$
where $\bold{x} = (x_1, x_2,...,x_n) \in \mathbb{R}^{n}$

The joint PDF of $\bold{X}$, denoted by $f_{\bold{X}}(\bold{x})$, is given by

$$F_{\bold{X}}(\bold{x}) = \int_{-\infty}^{x_n}...\int_{-\infty}^{x_2}\int_{-\infty}^{x_1}f_{X_1, X_2,...,X_n}(u_1, u_2,...,u_n)du_1du_2...du_n$$

### Mean Vector
Let $\bold{X} = (X_1, X_2,\dots,X_n)$ be a random vector. Then $$\bold{m_X}=(m_1, m_2,\dots,m_n)$$
is called the **mean vector** of $\bold{X}$ and 
$$
\bold{K_X}=
\begin{pmatrix}
  K_{X_1} & K_{X_1, X_2} & \dots & K_{X_1, X_n} \\
  K_{X_2, X_1} & K_{X_2} & \dots & K_{X_2, X_n} \\
  \vdots & \vdots & \ddots & \vdots\\
  K_{X_n, X_1} & K_{X_n, X_2} & \dots & K_{X_n} \\
\end{pmatrix}
$$
is called the **covariance matrix** of $\bold{X}$. 

### Gaussian Random Vectors
The vector $\bold{X} = (X_1, X_2, \dots, X_n)$ of random variables is called a **Gaussian random vector** if
$$f_{\bold{X}}(\bold{x})=\frac{1}{\sqrt{(2 \pi)^{n}\det(\bold{K_{\bold{X}}})}}e^{-\frac{1}{2}((\bold{x-m_X})\bold{K_{\bold{X}}}^{-1}(\bold{x-m_X})^{T})}$$
$X_1, X_2, \dots, X_n$ are *jointly Gaussian*.

**The joint distribution of two Gaussian is not necessarily a Gaussian**

**The joint distribution of two indipendent Gaussian is a Gaussian**