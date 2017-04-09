"""
Problem A. Oversized Pancake Flipper
"""


def solve(S, K):
    flip = 2 ** K - 1
    num = 0
    for s in S:
        num = num << 1 | (s == '+')

    ans = 0
    for i in range(len(S) - K + 1):
        if not num & 1:
            num = (num >> K << K) | ((num & flip) ^ flip)
            ans += 1
        num >>= 1
    return ans if num == flip >> 1 else "IMPOSSIBLE"

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        S, K = f.readline().strip().split()
        solution = solve(S, int(K))
        print("Case #{0}: {1}".format(case, solution))
