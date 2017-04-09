"""
Problem B. Tidy Numbers
"""


def solve(N):
    digit = len(N)
    N = [int(x) for x in N]
    for i in range(digit - 1):
        if N[i] > N[i + 1]:
            N[i] -= 1
            t = digit - 1
            while t > i:
                N[t] = 9
                t -= 1
            while t > 0 and N[t] < N[t - 1]:
                N[t] = 9
                N[t - 1] -= 1
                t -= 1
            break
    return int("".join([str(x) for x in N]))

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        N = f.readline().strip()
        solution = solve(N)
        print("Case #{0}: {1}".format(case, solution))
