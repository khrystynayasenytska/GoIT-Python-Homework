import timeit

# Knuth-Morris-Pratt (KMP)

def kmp_search(pattern, text):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0

    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    # Search
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  # found
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

# Rabin-Karp

def rabin_karp_search(pattern, text, prime=101):
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    base = 256
    hpattern = 0
    htext = 0
    h = 1

    for i in range(m-1):
        h = (h * base) % prime

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % prime
        htext = (base * htext + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            htext = (base*(htext - ord(text[i])*h) + ord(text[i+m])) % prime
            if htext < 0:
                htext += prime
    return -1

# Boyer-Moore

def boyer_moore_search(pattern, text):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    last = {c: i for i, c in enumerate(pattern)}
    i = m - 1
    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i += m - min(j, lo + 1)
            j = m - 1
    return -1

# Load texts

def load_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='utf-16') as f:
            return f.read()

# Benchmark function

def benchmark(algorithm, pattern, text):
    return timeit.timeit(lambda: algorithm(pattern, text), number=1)

# Paths to your two text files

text1_path = 'стаття 1.txt'
text2_path = 'стаття 2 (1).txt'

text1 = load_text(text1_path)
text2 = load_text(text2_path)

# Choose two patterns: one exists, one does not
pattern_exist = "алгоритми"   # exists in both texts
pattern_fake = "xyznotfound"  # fake pattern

algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search,
    "Boyer-Moore": boyer_moore_search
}

texts = {
    "Text1": text1,
    "Text2": text2
}

patterns = {
    "Existing": pattern_exist,
    "Fake": pattern_fake
}

results = {}

for tname, tcontent in texts.items():
    results[tname] = {}
    for pname, pvalue in patterns.items():
        times = {}
        for aname, afunc in algorithms.items():
            t = benchmark(afunc, pvalue, tcontent)
            times[aname] = t
        # find fastest
        fastest = min(times, key=times.get)
        results[tname][pname] = {
            "times": times,
            "fastest": fastest
        }

for tname in results:
    print(f"\nResults for {tname}:")
    for pname in results[tname]:
        print(f"  Pattern ({pname}):")
        for alg, t in results[tname][pname]["times"].items():
            print(f"    {alg}: {t:.6f}s")
        print(f"    Fastest: {results[tname][pname]['fastest']}")
