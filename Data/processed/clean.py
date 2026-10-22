#!/usr/bin/env python3
"""
Extract the Australian state/territory code from an address column in a CSV
and write it to another column.

Reads addresses from Column B, writes state codes to Column E.

Usage:
    python clean.py input.csv output.csv
    python clean.py input.csv output.csv --no-header
"""

import argparse
import csv
import re

STATES = ["VIC", "NSW", "QLD", "SA", "WA", "TAS", "ACT", "NT"]

# Whole-word, case-sensitive match so "SA" doesn't match inside "SAINT" or "Wa" in "Wagga".
STATE_PATTERN = re.compile(r"\b(" + "|".join(STATES) + r")\b")

ADDRESS_COL = 1  # Column B (0-indexed)
STATE_COL = 4    # Column E (0-indexed)


def extract_state(address: str) -> str:
    """Return the state code found in the address, or '' if none.

    If several codes appear (e.g. a street called "NT Road"), the LAST one
    wins, since the state normally comes at the end of an Australian address
    (e.g. "12 Smith St, Richmond VIC 3121").
    """
    matches = STATE_PATTERN.findall(address or "")
    return matches[-1] if matches else ""


def main():
    parser = argparse.ArgumentParser(description="Extract AU state codes from addresses.")
    parser.add_argument("input", help="Input CSV path")
    parser.add_argument("output", help="Output CSV path")
    parser.add_argument("--no-header", action="store_true",
                        help="Use if the CSV has no header row")
    args = parser.parse_args()

    found = missing = 0

    with open(args.input, newline="", encoding="utf-8-sig") as f_in, \
         open(args.output, "w", newline="", encoding="utf-8") as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        if not args.no_header:
            header = next(reader, None)
            if header is not None:
                header += [""] * (STATE_COL + 1 - len(header))  # pad to column E
                header[STATE_COL] = "State"
                writer.writerow(header)

        for row in reader:
            row += [""] * (STATE_COL + 1 - len(row))  # pad short rows
            state = extract_state(row[ADDRESS_COL])
            row[STATE_COL] = state
            writer.writerow(row)

            if state:
                found += 1
            else:
                missing += 1

    print(f"Done. States found: {found}, no state found: {missing}")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()