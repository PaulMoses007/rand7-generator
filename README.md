## Number Generation (1–7 using 1–5)

This program generates numbers from 1 to 7 with equal probability
using a random function that produces numbers from 1 to 5.

### Approach:
- Combine two rand5() calls → range 1–25
- Reject values above 21
- Map remaining values to 1–7

This ensures uniform distribution.
