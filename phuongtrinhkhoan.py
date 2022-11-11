import math

def f(p , q , r , s , t , u , x):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

def solve():
    while True:
        try:
            p, q, r, s, t, u = map(float, input().split(' '))

            if f(p, q, r, s, t, u, 1.0) > 1e-9 or p + r + u < 0:
                print("No solution")
                continue

            res = -1
            tung = 0.000
            trang = 1.000
            for i in range(50):
                love = (tung + trang) / 2.0
                F = f(p, q, r, s, t, u, love)
                if F > 0:
                    tung = love
                else:
                    trang = love
            print('{:0.4f}'.format(tung))
        except EOFError:
            break

solve()