cat << 'EOF' > aee.py
import sys
def get_inverse(a, n):
    a_orig, n_orig = a, n
    x0, x1 = 1, 0
    while n != 0:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1, x0 - q * x1
    if a != 1: return None
    return x0 % n_orig

if __name__ == "__main__":
    if len(sys.argv) != 3: sys.exit(1)
    try:
        val_a, val_n = int(sys.argv[1]), int(sys.argv[2])
        inv = get_inverse(val_a, val_n)
        print(inv if inv is not None else "No existe inverso (gcd != 1)")
    except: sys.exit(1)
EOF