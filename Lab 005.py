def is_valid_part(part):
    if not isinstance(part, str):
        return False
    num = int(part)
    if not 0<=num<=255:
        return False
    if part != str(num):
        return False

    return True

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False

    return True

def decimal_to_binary(n):
    if n == 0:
        return "0"
    def rec(n):
        if n == 0:
            return ""
        quotient = n // 2
        remainder = n % 2
        return rec(quotient) + str(remainder)
    return rec(n) or "0"

def binary_to_decimal(b):
    if b == "":
        return 0
    left = int(b[0])
    pos = len(b) - 1
    return left * (2 ** pos) + binary_to_decimal(b[1:])

print(binary_to_decimal("11111111"))