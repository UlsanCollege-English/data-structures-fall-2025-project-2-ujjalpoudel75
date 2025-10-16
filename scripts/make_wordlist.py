# Generate a 50,000‑word frequency snapshot using wordfreq.
# Run locally once, commit the output to data/words.csv. Not used by tests at runtime.


from __future__ import annotations


import csv
from pathlib import Path


# Optional: import inside main to avoid import error when module is inspected without wordfreq installed.


def main():
    try:
        from wordfreq import top_n_list, zipf_frequency
    except Exception as e:
        raise SystemExit("Install wordfreq first: pip install wordfreq") from e


    words = top_n_list('en', 50_000)
    out_path = Path(__file__).resolve().parent.parent / 'data' / 'words.csv'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for w in words:
            writer.writerow([w, f"{zipf_frequency(w, 'en'):.6f}"])


        print(f"Wrote {len(words)} rows to {out_path}")


if __name__ == '__main__':
    main()