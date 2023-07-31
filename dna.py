# Program uses a database to match a DNA sample and identify the person
import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database.csv> <sequence.txt>")
        return -1

    # Read database file into a variable
    database = []
    with open(sys.argv[1], "r") as database_file:
        database_reader = csv.DictReader(database_file)
        for line in database_reader:
            database.append(line)

    # Store list of DNA subsequence
    subsequence_list = list(database[0].keys())[1:]

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dna_file:
        dna_sequence = dna_file.read().strip()

    str_count = {}

    # Find longest match of each STR in DNA sequence
    for subsequence in subsequence_list:
        str_count[subsequence] = str(longest_match(dna_sequence, subsequence))

    # Check database for matching profiles
    for person in database:
        match = True
        for subsequence in subsequence_list:
            if person[subsequence] != str_count[subsequence]:
                match = False
                break
        if match:
            print(person["name"])
            break
    if not match:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
