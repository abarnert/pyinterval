# Copyright (c) 2008, Stefano Taschini <taschini@ieee.org>
# All rights reserved.
# See LICENSE for details.

"""Mathematical function library for intervals.

This module provides transcendental functions with interval argument.
"""

try:
    import crlibm
except ImportError:
    import sys
    sys.stderr.write("Cannot load crlibm extension. The imath functions will not be available.\n")
    del sys
else:

    from . import interval, fpu

    class monotonic(object):
        def __init__(self, domain=None, rd=None, ru=None):
            self.domain = domain or interval[-fpu.infinity, fpu.infinity]
            self.rd = rd
            self.ru = ru

        def __call__(self, f):
            from functools import wraps
            self.rd = self.rd or getattr(crlibm, f.__name__ + '_rd')
            self.ru = self.ru or getattr(crlibm, f.__name__ + '_ru')
            @wraps(f)
            def wrapper(x):
                return interval._canonical(type(c)(self.rd(c.inf), self.ru(c.sup))
                                           for c in interval.cast(x) & self.domain)
            return wrapper

    @monotonic()
    def exp(x):
        "Exponential."

    @monotonic()
    def expm1(x):
        "exp(x) - 1."

    @monotonic(domain = interval[0, fpu.infinity])
    def log(x):
        "Natural logarithm."

    @monotonic(domain = interval[0, fpu.infinity])
    def log2(x):
        "Logarithm in base 2."

    @monotonic(domain = interval[0, fpu.infinity])
    def log10(x):
        "Logarithm in base 10."

    @monotonic(domain = interval[-1, fpu.infinity])
    def log1p(x):
        "log(1+x)."

    @monotonic()
    def atan(x):
        "Arc tangent."

    @monotonic()
    def atanpi(x):
        "atan(x)/pi."

    @monotonic()
    def sinh(x):
        "Hyberbolic sine."

    @interval.function
    def cosh(c):
        "Hyberbolic cosine."
        if c.inf > 0:
            return (crlibm.cosh_rd(c.inf), crlibm.cosh_ru(c.sup)),
        if c.sup < 0:
            return (crlibm.cosh_rd(c.sup), crlibm.cosh_ru(c.inf)),
        else:
            return (1.0, fpu.max(crlibm.cosh_ru(x) for x in c)),

    pi = 4 * atan(1)
    e = exp(1)

    def tanh():
        one_rd = crlibm.log_rd(crlibm.exp_rd(1))

        def tanh_rd(x):
            if x < 0:
                return -tanh_ru(-x)
            if x == fpu.infinity:
                return 1.0
            s, c = crlibm.sinh_rd(x), crlibm.cosh_ru(x)
            if fpu.infinity in (s, c):
                return one_rd
            return fpu.down(lambda: s/c)

        def tanh_ru(x):
            if x < 0:
                return -tanh_rd(-x)
            if x == fpu.infinity:
                return 1.0
            s, c = crlibm.sinh_ru(x), crlibm.cosh_rd(x)
            if fpu.infinity in (s, c):
                return 1.0
            return fpu.up(lambda: s/c)

        @monotonic(rd=tanh_rd, ru=tanh_ru)
        def tanh(c):
            "Hyberbolic tangent."

        return tanh

    tanh=tanh()

    del monotonic

if __name__  == '__main__':
    import doctest
    doctest.testmod()
