import gmpy2
from app.solver.tlp import PrimeGenerator
import asyncio


async def tlp_solver(baseg, t, product):
    """Asynchronous TLP solver using gmpy2 for modular exponentiation."""
    def compute_slow_power():
        prime_gen = PrimeGenerator(bits=256)
        baseg_mpz = gmpy2.mpz(baseg)
        product_mpz = gmpy2.mpz(product)
        t_mpz = gmpy2.mpz(t)
        slow_power = baseg_mpz
        for _ in range(int(t_mpz)):
            slow_power = prime_gen.mod_exp(slow_power, gmpy2.mpz(2), product_mpz)
        return slow_power

    # Run the compute_slow_power function in a thread pool using run_in_executor
    loop = asyncio.get_event_loop()
    slow_power = await loop.run_in_executor(None, compute_slow_power)
    return slow_power
