"""
Python 2019 Assignment 05
"""


def read_frequency_file(freq_file_name):
    """
    Loads (token,frequency) pairs from a file with line format "<token> <frequency>".
    """
    count = []
    with open(freq_file_name, 'r') as fi:
        for line in fi:
            token = line.split(' ')
            for word in token:
                if word not in count:
                    count.append(word)
    return (count[0:3])

print(read_frequency_file("freq_en_50k.txt"))

def determine_decile_thresholds(frequencies):
    """
    Returns a vector of 9 thresholds delineating 10% of overall token coverage,
    i.e. the number of tokens that are needed to cover 10%, 20%, 30%, etc. of all tokens.
    """
    pass

def get_prefix_frequencies(frequencies):
    """
    Computes a list of (prefix,frequency) pairs from a list of (token,frequency) pairs
    by counting every prefix [0:i] of each token, and adding the counts for each prefix.
    """
    pass

def store_frequencies_alphabetically(frequencies, freq_file_name):
    """
    Writes a list of (string,frequency) pairs to a new file, with string in alphabetical order.
    Each pair is only written if frequency >= 1000.
    """
    pass

if __name__ == "__main__":
   freq_file_name = "freq_en_50k.txt"
   prefix_freq_file_name = "freq_en_prefixes.txt"

