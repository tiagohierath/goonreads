import csv
import json
import sys

if len(sys.argv) != 3:
    print("Usage: python storygraph_to_jsonl.py input.csv output.jsonl")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, newline="", encoding="utf-8") as csvfile, \
     open(output_file, "w", encoding="utf-8") as jsonlfile:

    reader = csv.reader(csvfile)

    next(reader)  # skip header

    for row in reader:
        if len(row) < 6:
            continue

        book = {
            "title": row[0].strip(),
            "author": row[1].strip(),
            "status": row[5].strip(),
        }

        jsonlfile.write(json.dumps(book, ensure_ascii=False) + "\n")

print(f"Wrote {output_file}")
