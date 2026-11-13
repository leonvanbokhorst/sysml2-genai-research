#!/usr/bin/env python3
"""Cohen's kappa and raw agreement for the two-coder classification study."""
import csv
from collections import Counter
from pathlib import Path

here = Path(__file__).parent
a = {r["sample_id"]: r for r in csv.DictReader(open(here / "coder-a.csv"))}
b = {r["sample_id"]: r for r in csv.DictReader(open(here / "coder-b.csv"))}
ids = sorted(a)
assert set(ids) == set(b), "sample ids differ"

pa = [a[i]["class"] for i in ids]
pb = [b[i]["class"] for i in ids]
n = len(ids)
agree = sum(x == y for x, y in zip(pa, pb))
po = agree / n
ca, cb = Counter(pa), Counter(pb)
pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
kappa = (po - pe) / (1 - pe)
print(f"n={n} raw agreement={agree}/{n} = {po:.3f}")
print(f"Cohen's kappa = {kappa:.3f}")
print("A distribution:", dict(ca), "B distribution:", dict(cb))
print("\nDisagreements:")
for i in ids:
    if a[i]["class"] != b[i]["class"]:
        print(f"  {i} {a[i]['class']} vs {b[i]['class']} | A note: {a[i].get('note','')[:120]} | B note: {b[i].get('note','')[:120]}")
print("\nConfusion (A rows):")
for x in sorted(set(pa) | set(pb)):
    print(" ", x, dict(Counter(y for xx, y in zip(pa, pb) if xx == x)))
