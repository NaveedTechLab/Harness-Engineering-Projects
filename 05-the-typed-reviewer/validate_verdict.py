#!/usr/bin/env python3
"""
validate_verdict.py — validates a reviewer's JSON verdict.

Does TWO kinds of checking, and the second kind is the whole point of
this project:

1. Structural: does the JSON match schema.json? (right fields, right
   types, verdict is one of the allowed values, confidence is 0-1)
2. Consistency: does the verdict actually make internal sense? A model
   can produce perfectly well-typed JSON that is still self-contradictory
   — e.g. verdict: "PASS" while tests_passed: false. Structural
   validation alone would let that through. This is why a typed output
   is necessary but not sufficient — you still need to check the
   RELATIONSHIPS between fields.

Usage:
    python3 validate_verdict.py verdict.json
    echo '{...}' | python3 validate_verdict.py -
"""

import json
import sys


def load_input(arg: str) -> dict:
    if arg == "-":
        raw = sys.stdin.read()
    else:
        with open(arg) as f:
            raw = f.read()
    return json.loads(raw)


def check_structure(data: dict) -> list[str]:
    errors = []
    required = ["verdict", "tests_run", "tests_passed", "issues", "confidence"]
    for field in required:
        if field not in data:
            errors.append(f"missing required field: {field}")

    if "verdict" in data and data["verdict"] not in ("PASS", "FAIL"):
        errors.append(f"verdict must be 'PASS' or 'FAIL', got: {data['verdict']!r}")

    if "tests_run" in data and not isinstance(data["tests_run"], bool):
        errors.append("tests_run must be a boolean")

    if "tests_passed" in data and not isinstance(data["tests_passed"], bool):
        errors.append("tests_passed must be a boolean")

    if "issues" in data and not isinstance(data["issues"], list):
        errors.append("issues must be an array")

    if "confidence" in data:
        c = data["confidence"]
        if not isinstance(c, (int, float)) or not (0.0 <= c <= 1.0):
            errors.append(f"confidence must be a number between 0 and 1, got: {c!r}")

    return errors


def check_consistency(data: dict) -> list[str]:
    errors = []

    verdict = data.get("verdict")
    tests_run = data.get("tests_run")
    tests_passed = data.get("tests_passed")
    issues = data.get("issues", [])

    if verdict == "PASS":
        if tests_run is not True:
            errors.append("verdict is PASS but tests_run is not true — a PASS requires the reviewer to have actually run the tests")
        if tests_passed is not True:
            errors.append("verdict is PASS but tests_passed is not true — contradiction")
        if issues:
            errors.append(f"verdict is PASS but issues is non-empty: {issues} — a real PASS should have no open issues")

    if verdict == "FAIL":
        if not issues:
            errors.append("verdict is FAIL but issues is empty — a FAIL must explain what's wrong")
        if tests_passed is True:
            errors.append("verdict is FAIL but tests_passed is true — contradiction")

    return errors


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 validate_verdict.py <file.json | ->", file=sys.stderr)
        sys.exit(1)

    try:
        data = load_input(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"❌ INVALID JSON: {e}", file=sys.stderr)
        sys.exit(1)

    structural_errors = check_structure(data)
    if structural_errors:
        print("❌ STRUCTURAL ERRORS:")
        for e in structural_errors:
            print(f"   - {e}")
        sys.exit(1)

    consistency_errors = check_consistency(data)
    if consistency_errors:
        print("❌ CONSISTENCY ERRORS (well-formed JSON, but self-contradictory):")
        for e in consistency_errors:
            print(f"   - {e}")
        sys.exit(1)

    print(f"✅ VALID — verdict: {data['verdict']}, confidence: {data['confidence']}")
    sys.exit(0)


if __name__ == "__main__":
    main()
