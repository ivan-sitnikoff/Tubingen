# -*- coding: UTF-8 -*-
"""
Universität Tübingen - Seminar für Sprachwissenschaft
VL 'Programming and Data Analysis' WS 2019-2020
© Johannes Dellert, Gerhard Jäger

Assignment 08: Experiments with German N-grams
Template
"""

import re


class Ngram:
    """
    A class for n-gram models based on a text file.

    :attr filename: the name of the file  that the model is based on
    :type filename: str
    :attr n: the number of tokens in the tuples
    :type n: int
    :attr raw_counts: the raw counts of the n-gram tuples
    :type raw_counts: dict[tuple[str*], int]
    :attr prob: the probabilities of the n-gram tuples
    :type prob: dict[tuple[str*], int]
    :attr cond_prob: the probability distributions over the respective next tokens for each n-1-gram
    :type cond_prob: dict[tuple[str*], dict[str, int]]
    """

    # Task 1
    def __init__(self, filename="", n=0):
        """
        Initialize an Ngram object.

        :param filename: The name of the file to base the model on.
        :param n: The number of tokens in the n-gram tuples.
        """
        pass

    # Task 2
    def extract_raw_counts(self):
        """
        Compute the raw counts for each n-gram occurring in the text.
        """
        pass
    
    # Task 3
    def extract_probabilities(self):
        """
        Compute the probability of an n-gram occurring in the text.
        """
        pass

    # Task 4
    def extract_conditional_probabilities(self):
        """
        Compute the probability distribution over the next tokens given an n-1-gram.
        """
        pass

    # Task 5
    def generate_random_token(self, mgram):
        """
        Generate a random next token based on an n-1 gram,
        taking into account the probability distribution over the possible next tokens for that n-1-gram.

        :param mgram: the n-1 gram to generate the next token for.
        :type mgram: a tuple (of length n-1) of strings.
        :return a random next token for the n-1-gram.
        :rtype str
        """
        pass

    # Task 6
    def generate_random_sentence(self):
        """
        Generate a random sentence.

        :return a random sentence
        :rtype list[str]
        """
        pass


def tokenize_smart(sentence):
    """
    Tokenize the sentence into tokens (words, punctuation).

    :param sentence: the sentence to be tokenized
    :type sentence: str
    :return: list of tokens in the sentence
    :rtype: list[str]
    """
    tokens = []

    for word in re.sub(r" +", " ", sentence).split():
        word = re.sub(r"[\"„”“»«`\(\)]", "", word)
        if word != "":
            if word[-1] in ".,!?;:":
                if len(word) == 1:
                    tokens += [word]
                else:
                    tokens += [word[:-1], word[-1]]
            else:
                tokens.append(word)

    return tokens


def list2str(sentence):
    """
    Convert a sentence given as a list of strings to the sentence as a string separated by whitespace.
    
    :param sentence: the string list to be joined
    :type sentence: list[str]
    :return: sentence as a string, separated by whitespace
    :rtype: str
    """
    sentence = " ".join(sentence)
    sentence = re.sub(r" ([\.,!\?;:])", r"\1", sentence)
    return sentence


if __name__ == '__main__':
    # Task 1
    ngram_model = Ngram("de-sentences-tatoeba.txt", 2)
    print(ngram_model.n, ngram_model.filename)
    print(ngram_model.raw_counts, ngram_model.prob, ngram_model.cond_prob)
    # Task 2
    ngram_model.extract_raw_counts()
    print(ngram_model.raw_counts[("kaltes", "Land")])
    print(ngram_model.raw_counts[("schönes", "Land")])
    # Task 3
    ngram_model.extract_probabilities()
    print(ngram_model.prob[("kaltes", "Land")])
    print(ngram_model.prob[("schönes", "Land")])
    # Task 4
    ngram_model.extract_conditional_probabilities()
    print(ngram_model.cond_prob[(" beobachteten ",)])
    print(ngram_model.cond_prob[("schönes",)][("Land")])
    # Task 5
    print(ngram_model.generate_random_token(("den",)))
    print(ngram_model.generate_random_token(("den",)))
    print(ngram_model.generate_random_token(("den",)))
    # Task 6
    print(list2str(ngram_model.generate_random_sentence()))
    print(list2str(ngram_model.generate_random_sentence()))
