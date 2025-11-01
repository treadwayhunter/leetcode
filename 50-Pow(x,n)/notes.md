# Problem 50

## Python solution was too trivial
x**n. Python can handle this kind of situation in a built-in way. This would probably not look good on an interview???

## C. This was a pain.
I tried to implement it in C. My initial solution passed almost all test cases, with the exception of a handful of cases in the end where the power was -2^31, or any other extremely large power.
Ultimately C can't handle that, so my solution also could not. I had to find a look around.

After fighting for the lookaround, I ended up defaulting to Chatgpt. But I was able to learn something.

Given a number n and an exponent x, it turns out x has a binary representation.

For example
n^13 is actually just n^(8+4+1), or n^8 * n^4 * n^1.
These binary representations are also extremely easy to solve for. It essentially enables us to keep squaring n, which can be done simply by a computer. I want to continue doing this.