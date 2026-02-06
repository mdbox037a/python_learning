def fast_pow(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half = fast_pow(base, exponent // 2)
        return half * half
    else:
        return base * fast_pow(base, exponent - 1)
