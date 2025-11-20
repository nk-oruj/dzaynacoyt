import re
import csv
from collections import defaultdict

pattern = r'(?:((?<![աէոօեիը])ւ)|(?:[աէոօեիը]+վ(?![աէոօեիը]|$)|[աէոօեիը]+[ւյ]?))' # vowels
# pattern = r'[^\n\sաէոօեիըւ0-9]+' # consonants
allow_overlap = False

def count_unique_matches(text, pattern):
    counts = defaultdict(int)

    for match in re.finditer(pattern, text):
        s = match.group(0)
        counts[s] += 1

    return counts


def run_calculator(file, output):
    # read the input file
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # count matches
    results = count_unique_matches(text, pattern)

    # sort by frequency descending
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # write csv file
    with open(output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["string", "count"])  # header row
        for substring, count in sorted_results:
            writer.writerow([substring, count])

    print(f"dataset of {file} written to: {output}")

if __name__ == "__main__":
    run_calculator("bible.txt", "dzaynakoyt_bible.csv")
    run_calculator("dictionary.txt", "dzaynakoyt_dictionary.csv")
