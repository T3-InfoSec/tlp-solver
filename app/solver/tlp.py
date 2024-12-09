import gmpy2
import time

class PrimeGenerator:
    def __init__(self, bits):
        self.bits = bits
        gmpy2.get_context().precision = bits
        self.state = gmpy2.random_state(int(time.time()))

    def generate_base(self):        
        return gmpy2.mpz_rrandomb(self.state, self.bits)

    def generate_prime(self):
        prime = gmpy2.mpz_rrandomb(self.state, self.bits)
        prime = gmpy2.next_prime(prime)
        return prime

    def calculate_totient(self, p1, p2):
        p1_minus_1 = p1 - 1
        p2_minus_1 = p2 - 1
        return p1_minus_1 * p2_minus_1

    def calculate_carmichael(self, p1, p2):
        p1_minus_1 = p1 - 1
        p2_minus_1 = p2 - 1
        lcm = gmpy2.lcm(p1_minus_1, p2_minus_1)
        return lcm

    def mod_exp(self, base, exp, mod):
        return gmpy2.powmod(base, exp, mod)
