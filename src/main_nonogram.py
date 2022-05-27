from functools import reduce
 
def gen_row(w, s):
    def gen_seg(o, sp):
        if not o:
            return [[2] * sp]
        return [[2] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]
 
 
def deduce(hr, vr):
    def allowable(row):
        return reduce(lambda a, b: [x | y for x, y in zip(a, b)], row)
 
    def fits(a, b):
        return all(x & y for x, y in zip(a, b))
 
    def fix_col(n):
        c = [x[n] for x in can_do]
        cols[n] = [x for x in cols[n] if fits(x, c)]
        for i, x in enumerate(allowable(cols[n])):
            if x != can_do[i][n]:
                mod_rows.add(i)
                can_do[i][n] &= x
 
    def fix_row(n):
        c = can_do[n]
        rows[n] = [x for x in rows[n] if fits(x, c)]
        for i, x in enumerate(allowable(rows[n])):
            if x != can_do[n][i]:
                mod_cols.add(i)
                can_do[n][i] &= x
 
    def show_gram(m):
        for x in m:
            print(" ".join("x#.?"[i] for i in x))
        print()
 
    w, h = len(vr), len(hr)
    rows = [gen_row(w, x) for x in hr]
    cols = [gen_row(h, x) for x in vr]
    can_do = list(map(allowable, rows))
 

    mod_rows, mod_cols = set(), set(range(w))
 
    while mod_cols:
        for i in mod_cols:
            fix_col(i)
        mod_cols = set()
        for i in mod_rows:
            fix_row(i)
        mod_rows = set()
 
    if all(can_do[i][j] in (1, 2) for j in range(w) for i in range(h)):
        print("Unica solucion")  # Podria ser incorrecto!
    else:
        print("Puede haber más de una ,Hacer busqueda:")
 
    out = [0] * h
 
    def try_all(n = 0):
        if n >= h:
            for j in range(w):
                if [x[j] for x in out] not in cols[j]:
                    return 0
            show_gram(out)
            return 1
        sol = 0
        for x in rows[n]:
            out[n] = x
            sol += try_all(n + 1)
        return sol
 
    n = try_all()
    if not n:
        print("No tiene solucion.")
    elif n == 1:
        print("Unica solution.")
    else:
        print(n, "solutiones.")
    print()
 
 
def solve(s, show_runs=True):
    s = [[[ord(c) - ord('A') + 1 for c in w] for w in l.split()]
         for l in p.splitlines()]
    if show_runs:
        print("Horizontal:", s[0])
        print("Vertical:", s[1])
    deduce(s[0], s[1])