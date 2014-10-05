#!/usr/bin/env python

import sys

#Compute all primes between 0 and max
#Input:
#max: maximum size of primes. Type: Integer
#Output:
#primes: ordered list of the primes between 1 and max
def computePrimes(max):
    # [YOUR TASK STARTS HERE]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

    # [YOUR TASK ENDS HERE]
    return primes

# Compute a public key
# Input:
# p, q: primes. Type: integer. Constraints: p, q < 300, p != q
# Output:
# (n, e): tupel of integers representing the public key
def computePubKey(p, q):
        assert (p < 300)
        assert (q < 300)
        assert (p != q)
    # Note: we do not do any primality tests here!

    # [YOUR TASK STARTS HERE]

        n = p * q
        phi_n = computePhi(p, q)
        for prime in computePrimes(300):
                if gcd(prime, phi_n) == 1:
                        e = prime
                        break

        # [YOUR TASK ENDS HERE]

        # n and e must be integers!
        return (n, e)

        
# e and phi(n) are input, both integers
# Compute a private key
# Input:
# e, phi(n): as in lecture. Type: integer.
# Output:
# d: private key. Type: integer
def computePrivKey(e, phi):
    # [YOUR TASK STARTS HERE]

    # from e*d == 1 mod phi_n, we have that e*d - k*phi = 1,
    # hence e*d - k*phi = gcd(e, phi), because e and phi_n are relativly prime
    # the Extended Euclidian Algorithm returns [d, -phi], hence we get only the first item of the tuple
    d, _ = eea(e, phi)

    # [YOUR TASK ENDS HERE]
    # d is the private key, an integer
    return d


# gcd() uses eea()
# Input:
# a, b: numbers to work on. Type: integer
# Output:
# gcd: the gcd. Type: integer
def gcd(a, b):
    # [YOUR TASK STARTS HERE]

    x, y = eea(a, b)
    gcd = a*x + b*y

    # [YOUR TASK ENDS HERE]
    return gcd


# eea is the Extended Euclidean Algorithm
# Input:
# a, b: numbers to work on. Type: integer
# Output:
# (x, y): numbers for which ax + by = gcd(a,b) holds. Type: tupel of integers
def eea(a, b):
    # [YOUR TASK STARTS HERE]

        x, x1 = 1, 0
        y, y1 = 0, 1
        while b:
                quotient = a // b
                x, x1 = x1, x - quotient * x1
                y, y1 = y1, y - quotient * y1
                a, b = b, a - quotient * b

        # [YOUR TASK ENDS HERE]
        return (x, y)



# Compute phi(n) if input is a product of two primes
# Input:
# p, q: primes. Type: integer
# Output:
# o: phi(n). Type: integer
def computePhi(p, q):
    # [YOUR TASK STARTS HERE]

    o = (p - 1) * (q - 1)

    # [YOUR TASK ENDS HERE]
    return o



# Compute an encrypted message
# Input:
# m: the message. Type: integer. Constraint: m < n
# pubkey: public key. Type: tupel of integers (n, e)
# Output:
# ciphertext: encrypted message. Type: integer
def encrypt(m, pubkey):
    # [YOUR TASK STARTS HERE]
        n, e = pubkey
        assert(m < n)
        ciphertext = (m**e) % n

        # [YOUR TASK ENDS HERE]
        return ciphertext


# Decrypt an encrypted message
# Input:
# d: the private key. Type: integer
# n: the product of p and q. Type: integer
# Output:
# decryptedtext: the decrypted message. Type: integer
def decrypt(c, d, n):
    # [YOUR TASK STARTS HERE]

        decryptedtext = (c**d) % n

        # [YOUR TASK ENDS HERE]
        return decryptedtext


# Use this if you want to test your program
# DO NOT CHANGE THE FORMAT OF COMMAND LINE CALL
def main():
    # we read from stdin
    # first prime number
    p1 = int(sys.argv[1])
    # second prime number
    p2 = int(sys.argv[2])
    # message to encode, given as an integer m < n = p1 * p2
    m = int(sys.argv[3])

    # DO NOT CHANGE THE OUTPUT FORMAT
    (n, e) = computePubKey(p1, p2)
    print "Pubkey:" + str(n) + "," + str(e)
    phi = computePhi(p1, p2)
    print "Phi:" + str(phi)
    d = computePrivKey(e, phi)
    print "PrivKey:" + str(d)
    c = encrypt(m, (n, e))
    print "m:" + str(m) + "->" + str(c)
    print "c:" + str(c) + "->" + str(decrypt(c, d, n))

# main()
if __name__ == "__main__":
    main()
