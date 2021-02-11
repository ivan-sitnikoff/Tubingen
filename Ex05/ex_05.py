"""
Python 2019 Assignment 05
"""


def read_frequency_file(freq_file_name):
    """
    Loads (token,frequency) pairs from a file with line format "<token> <frequency>".
    """
    frequencies = []
    with open(freq_file_name, encoding='utf8') as f:
        for j, line in enumerate(f):
            token = line.split()
            frequencies.append((token[0], int(token[1])))
    return frequencies


def determine_decile_thresholds(frequencies):
    """
    Returns a vector of 9 thresholds delineating 10% of overall token coverage,
    i.e. the number of tokens that are needed to cover 10%, 20%, 30%, etc. of all tokens.
    """
    total = sum([x[1] for x in frequencies])
    deciles = []
    part, summa = 0.1, 0
    for number, word_freq in enumerate(frequencies):
        _, freq = word_freq
        summa += freq
        if summa >= total * part:
            #deciles.append(number + 1)
            #part += 0.1
            deciles.append(number) ###
            summa = 0 ###
    #return deciles[:-1]
    return deciles ###


def get_prefix_frequencies(frequencies):
    """
    Computes a list of (prefix,frequency) pairs from a list of (token,frequency) pairs
    by counting every prefix [0:i] of each token, and adding the counts for each prefix.
    """
    prefix_freq = {}
    for word, freq in frequencies:
        prefix = ''
        for letter in word:
            prefix += letter
            if prefix in prefix_freq:
                prefix_freq[prefix] += freq
            else:
                prefix_freq[prefix]  = freq
    return sorted(list(prefix_freq.items()))


def store_frequencies_alphabetically(frequencies, freq_file_name):
    """
    Writes a list of (string,frequency) pairs to a new file, with string in alphabetical order.
    Each pair is only written if frequency >= 1000.
    """
    with open(freq_file_name, 'w', encoding='utf8') as f:
        for prefix, freq in frequencies:
            if freq >= 1000:
                print(f'{prefix} {freq}', file=f)

            

if __name__ == "__main__":
    freq_file_name = "freq_en_50k.txt"
    prefix_freq_file_name = "freq_en_prefixes.txt"
    
    frequencies = read_frequency_file(freq_file_name)
    print(frequencies[0:3])
    
    deciles = determine_decile_thresholds(frequencies)
    print(deciles)
     
    prefix_freq = get_prefix_frequencies(frequencies)
    print(prefix_freq[10383:10387])
     
    store_frequencies_alphabetically(prefix_freq, prefix_freq_file_name)
