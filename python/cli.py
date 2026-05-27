#!/usr/bin/env python3
"""
DevOps Maturity Self-Assessment — CLI
Swift Tech Co. — https://swifttechco.com
"""

from calculator import QUESTIONS, calculate


def interactive():
    print("\nDevOps Maturity Self-Assessment")
    print("Swift Tech Co. — https://swifttechco.com")
    print("=" * 48)
    print("Rate your DevOps practices across 7 dimensions.\n")

    answers = {}
    for i, q in enumerate(QUESTIONS, 1):
        print(f"{i}. {q['label']}")
        for j, opt in enumerate(q["options"]):
            print(f"   {j}. {opt}")
        ans = int(input("   Your answer (0/1/2): ").strip())
        answers[q["id"]] = max(0, min(2, ans))
        print()

    result = calculate(answers)
    print("=" * 48)
    print(f"Score: {result['pct']} / 100 — {result['level']} DevOps Maturity")
    if result["gaps"]:
        print("\nTop areas to improve:")
        for g in result["gaps"][:4]:
            print(f"  -> {g}")
    print("\nGet a DevOps improvement plan: https://swifttechco.com/contact")


if __name__ == "__main__":
    interactive()
