"""
Python 2020-2021 Assignment 06
"""

def read_file_to_dict(input_file):
    """
    Read in the contents of the input file in such a way 
    that you can retrieve the contents of columns 2, 3, and 4 
    by the (unique) values in column 1.
    """
    dct = {}
    with open(input_file) as f:
        for line in f:
            tokens = line.strip().split('\t')
            if len(tokens) == 4:
                key, val1, val2, val3 = tokens
                dct[key] = (val1, val2, val3)
    return dct


def simple_tokenizer(th_dict, sentence):
    """
    Simple tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data.
    """
    i, word, translate = 0, '', []
    while i < len(sentence):
        word += sentence[i]
        if word in th_dict:
            translate.append((word, *th_dict[word]))
            sentence = sentence[i + 1: ]
            i, word = 0, ''
        else:
            i += 1
    return translate


def th_tokens(th_dict, sentence):
    """
    Get the tokens of the Thai sentence using simple tokenizer.
    """
    return [x[0] for x in simple_tokenizer(th_dict, sentence)]


def th_translit(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using simple tokenizer.
    """
    return [x[1] for x in simple_tokenizer(th_dict, sentence)]


def th_pos(th_dict, sentence):
    """
    Get the list of part of speech tags 
    of Thai sentence tokens using simple tokenizer.
    """
    return [x[2] for x in simple_tokenizer(th_dict, sentence)]


def th_gloss(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using simple tokenizer.
    """
    return [x[3] for x in simple_tokenizer(th_dict, sentence)]


def greedy_tokenizer(th_dict, sentence):
    """
    Greedy tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data. 
    Always find the longest chunk of characters starting at the current position 
    which can be found in the dictionary ("greedy search").
    """
    i, j, word, translate = 0, 0, '', []
    while sentence:
        while i < len(sentence):
            word += sentence[i]
            if word in th_dict:
                longest = word
                j = i
            i += 1
        translate.append((longest, *th_dict[longest]))
        sentence = sentence[j + 1: ]
        i, word = 0, ''
    return translate


def th_tokens_greedy(th_dict, sentence):
    """
    Get the tokens of Thai sentence using greedy tokenizer.
    """
    return [x[0] for x in greedy_tokenizer(th_dict, sentence)]


def th_translit_greedy(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using greedy tokenizer.
    """
    return [x[1] for x in greedy_tokenizer(th_dict, sentence)]


def th_pos_greedy(th_dict, sentence):
    """
    Get the part of speech tags of Thai sentence tokens using greedy tokenizer.
    """
    return [x[2] for x in greedy_tokenizer(th_dict, sentence)]


def th_gloss_greedy(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using greedy tokenizer.
    """
    return [x[3] for x in greedy_tokenizer(th_dict, sentence)]

if __name__ == '__main__':
    file_name = "th-eng-dict.tsv"
    example = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
    #th_dict = read_file_to_dict(file_name)
    #print(simple_tokenizer(th_dict, example))
    #print(th_tokens(th_dict, "ดาวอังคารเป็น"))
    #print(th_translit(th_dict, "ดาวอังคารเป็น"))
    #print(th_pos(th_dict, "ดาวอังคารเป็น"))
    #print(th_gloss(th_dict, "ดาวอังคารเป็น"))
    #print(greedy_tokenizer(th_dict, "ดาวอังคารเป็น"))
    #print(th_tokens_greedy(th_dict, "ดาวอังคารเป็น"))
    #print(th_translit_greedy(th_dict, "ดาวอังคารเป็น"))
    #print(th_pos_greedy(th_dict, "ดาวอังคารเป็น"))
    #print(th_gloss_greedy(th_dict, "ดาวอังคารเป็น"))

