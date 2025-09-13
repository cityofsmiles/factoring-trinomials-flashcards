





import sympy as sp
import random
import json
import os
import math

# Variables (typical algebra vars)
vars_pool = ["a", "b", "c", "m", "n", "p", "q", "x", "y", "z"]

flashcards = []


def format_poly(expr):
    """Format polynomial for display: replace ** with ^, remove *."""
    s = sp.sstr(expr, order='lex')
    s = s.replace("**", "^").replace("*", "")
    return s


def format_term(coef, var=None, exp=1, hide_one=True):
    """Format a term given coef, variable, and exponent."""
    if var is None:  # constant term
        return str(coef)

    if coef == 1 and hide_one:
        c_str = ""
    elif coef == -1 and hide_one:
        c_str = "-"
    else:
        c_str = str(coef)

    if exp == 1:
        return f"{c_str}{var}"
    return f"{c_str}{var}^{exp}"


def pick_vars():
    """Pick two distinct variables, alphabetical order."""
    v1, v2 = random.sample(vars_pool, 2)
    return tuple(sorted([v1, v2]))


def pick_coef_coprime(base_coef, limit=5):
    """Pick coefficient c or d relatively prime to base_coef."""
    while True:
        k = random.randint(1, limit)
        if math.gcd(k, base_coef) == 1:
            return k


def generate_case(case_type):
    x_name, y_name = pick_vars()
    x = sp.Symbol(x_name)
    y = sp.Symbol(y_name)

    if case_type == 1:
        # (x ± c)(x ± d)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        s1, s2 = random.choice([1, -1]), random.choice([1, -1])
        expr = (x + s1 * c) * (x + s2 * d)
        q = f"({x} {'+' if s1 == 1 else '-'} {c})({x} {'+' if s2 == 1 else '-'} {d})"

    elif case_type == 2:
        # (x ± cy)(x ± dy)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        s1, s2 = random.choice([1, -1]), random.choice([1, -1])
        expr = (x + s1 * c * y) * (x + s2 * d * y)
        q = f"({x} {'+' if s1 == 1 else '-'} {format_term(c, y)})({x} {'+' if s2 == 1 else '-'} {format_term(d, y)})"

    elif case_type == 3:
        # (ax ± c)(bx ± d)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = pick_coef_coprime(a)
        d = pick_coef_coprime(b)
        s1, s2 = random.choice([1, -1]), random.choice([1, -1])
        expr = (a * x + s1 * c) * (b * x + s2 * d)
        q = f"({format_term(a, x)} {'+' if s1 == 1 else '-'} {c})({format_term(b, x)} {'+' if s2 == 1 else '-'} {d})"

    else:  # case_type == 4
        # (ax ± cy)(bx ± dy)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = pick_coef_coprime(a)
        d = pick_coef_coprime(b)
        s1, s2 = random.choice([1, -1]), random.choice([1, -1])
        expr = (a * x + s1 * c * y) * (b * x + s2 * d * y)
        q = f"({format_term(a, x)} {'+' if s1 == 1 else '-'} {format_term(c, y)})({format_term(b, x)} {'+' if s2 == 1 else '-'} {format_term(d, y)})"

    return {"question": format_poly(sp.expand(expr)), "answer": q}


# Generate 200 flashcards (50 per case)
for case_type in range(1, 5):
    for _ in range(50):
        flashcards.append(generate_case(case_type))

# Save to ./public/flashcards.json
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")


