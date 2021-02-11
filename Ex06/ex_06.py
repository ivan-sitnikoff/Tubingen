"""
Python 2020-2021 Assignment 06
"""

def read_file_to_dict(input_file):
    """
    Read in the contents of the input file in such a way 
    that you can retrieve the contents of columns 2, 3, and 4 
    by the (unique) values in column 1.
    """
    pass


def simple_tokenizer(th_dict, sentence):
    """
    Simple tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data.
    """
    pass


def th_tokens(th_dict, sentence):
    """
    Get the tokens of the Thai sentence using simple tokenizer.
    """
    pass


def th_translit(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using simple tokenizer.
    """
    pass


def th_pos(th_dict, sentence):
    """
    Get the list of part of speech tags 
    of Thai sentence tokens using simple tokenizer.
    """
    pass


def th_gloss(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using simple tokenizer.
    """
    pass


def greedy_tokenizer(th_dict, sentence):
    """
    Greedy tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data. 
    Always find the longest chunk of characters starting at the current position 
    which can be found in the dictionary ("greedy search").
    """
    pass


def th_tokens_greedy(th_dict, sentence):
    """
    Get the tokens of Thai sentence using greedy tokenizer.
    """
    pass


def th_translit_greedy(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using greedy tokenizer.
    """
    pass


def th_pos_greedy(th_dict, sentence):
    """
    Get the part of speech tags of Thai sentence tokens using greedy tokenizer.
    """
    pass


def th_gloss_greedy(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using greedy tokenizer.
    """
    pass

if __name__ == '__main__':
    file_name = "th-eng-dict.tsv"
    example = "ดาวอังคารเป็นดาวเคราะห์ลำดับที่สี่จากดวงอาทิตย์"
