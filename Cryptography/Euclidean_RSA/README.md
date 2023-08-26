### Euclidean RSA
This is the first cryptography challenge. The code itself is not very lengthy, but its functionality is quite "uncommon" as it utilizes an external function to generate four integers a, b, c, and d, which have a relationship with n: `a^2 + b^2 = n`, `c^2 + d^2 = n`
```py
while True:
	try:
		key = RSA.generate(2048)
		a,b,c,d = magic(key)
		break
	except:
		pass
assert a**2 + b**2 == key.n
assert c**2 + d**2 == key.n
```
At this point, by using the `Brahmagupta–Fibonacci` method, you can solve the equation following these steps:

$$
\begin{align*}
& a^2 + b^2 = c^2 + d^2 = n \\
& (a^2 + b^2)(c^2 + d^2) = n^2 = (pq)^2 \\
& (ac + bd)^2 + (ad - bc)^2 = p^2 q^2 \\
& q^2 = s^2 + t^2 \\
& (ac + bd)^2 + (ad - bc)^2 = (p \cdot s)^2 + (p \cdot t)^2 \\
& ps = a \cdot c + b \cdot d \\
& pt = a \cdot d - b \cdot c \\
& p = \text{gcd}(ps, pt) \\
& q = \frac{n}{p} \\
\end{align*}
$$
