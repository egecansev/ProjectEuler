# Check https://arxiv.org/pdf/1302.0521.pdf

def offline():


    def chk_n_add (serie, nn, jj):
        if nn*nn+jj not in serie and nn*nn+jj < 10000:
            serie.append(nn*nn+jj)
        return serie


    odd=[]
    even=[]
    for n in range(1,100):
        odd = chk_n_add(odd, n, 1)

    for n in range(1,100):
        for j in range(2,n+1):
            if float(int(2*n/j)) == float(2*n/j):
                even = chk_n_add(even, int(n), int(j))

    j=4
    for n in range(1,100):
        if n % 2:
            odd = chk_n_add(odd, int(n), int(j))
        else:
            even = chk_n_add(even, int(n), int(j))

    for n in range(2,100):
        j = 2 * n - 1
        even = chk_n_add(even, int(n), int(j))

    for n in range(4,100):
        j = 2 * n - 3
        even = chk_n_add(even, int(n), int(j))

    for k in range(1,50):
        # RULE ODD 1
        n = 5 * k + 1
        j = (4 * n + 1) / 5
        odd = chk_n_add(odd, int(n), int(j))

        # RULE ODD 2
        n = 5 * k + 3
        j = (6 * n + 2) / 5
        odd = chk_n_add(odd, int(n), int(j))

        # RULE EVEN 1
        n = 6 * k + 5
        j = (2 * n - 1) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 2
        n = 9 * k + 4
        j = n - 2
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 3
        n = 5 * k + 4
        j = (8 * n + 3) / 5
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 4
        n = 3 * k + 2
        j = (5 * n + 2) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 5
        n = 3 * k + 2
        j = (4 * n + 1) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 6
        n = 2 * k + 1
        j = (3 * n + 1) / 2
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 7
        n = 5 * k + 2
        j = n - 1
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 8
        n = 6 * k + 1
        j = (5 * n + 1) / 6
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 9
        n = 10 * k + 7
        j = (2 * n + 1) / 5
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 10
        n = 3 * k + 1
        j = (2 * n + 1) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 11
        n = 3 * k + 1
        j = n + 1
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 12
        n = 7 * k + 3
        j = n + 2
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 13
        n = 6 * k + 4
        j = (7 * n + 2) / 6
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 14
        n = 3 * k + 1
        j = (4 * n + 2) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 15
        n = 7 * k + 5
        j = (8 * n + 2) / 7
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 16
        n = 6 * k + 2
        j = (2 * n - 1) / 3
        even = chk_n_add(even, int(n), int(j))

        # RULE EVEN 17
        n = 3 * k + 2
        j = 2 * n - 2
        even = chk_n_add(even, int(n), int(j))

    return [odd, even]
