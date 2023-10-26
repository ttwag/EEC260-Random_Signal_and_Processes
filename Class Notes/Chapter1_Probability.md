
## Conditional Probability
$$P(A \cap B) = P(A | B)P(B)$$
or
$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

Given the event B has occurred, the probability that event A occurs is $P(A | B)$. Note that this is a fundamental definition in probability theory.

**Intuition:** The first formula is more intuitive and tells us that to get $P(A \cap B)$, we need to get the probability of the first event that happened, $P(B)$, then multiply it to the second event (given that event B occurred), $P(A | B)$. To get an idea of why we need multiplication here, think of $P(B) = \frac{1}{2}$. We would have a half of a probability pie. If we have another event A given B has occured and $P(A | B) = \frac{1}{2}$, then we could cut the half pie in half again by multiplying $P(A | B)$ with $P(B)$. This product is the probability that both events happened. A tree diagram is also useful to illustrate the concept.

To get the second formula, rearrange the first one.

In general, the conditional probability updates the sample space given an event has occured.
### Independent Event vs. Dependent Event
$P(A | B) = P(A)P(B)$ if and only if the two events are independent because if you put this back to the conditional probabliity equation, $P(A | B) = P(A)$, which means knowing B has occured tell us nothing about the probability of the event A occuring.

$P(A | B) ≠ P(A)P(B)$ if and only if events are dependent, so they affect each other.

