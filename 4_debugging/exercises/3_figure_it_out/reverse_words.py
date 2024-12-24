#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for reversing a sentence word-by-word.
This function may be buggy!

Module contents:
    - reverse_words: Reverses a sentence word-by-word

Created on 2024-12-06
Author: Claude AI
"""

def reverse_words(text: str) -> str:
    """Reverses the order of words in a string.
    Words are separated by single spaces.
    
    Parameters:
        text: str, the input string
        
    Returns -> str: string with words in reverse order
    
    >>> reverse_words("hello world")
    'world hello'
    >>> reverse_words("one")
    'one'
    >>> reverse_words("")
    ''
    """
    assert isinstance(text, str), "input must be a string"

    words = text.split(" ")
    result = ""
    
    for word in words:
        if result:  # Add a space only if result is not empty
            result = word + " " + result
        else:  # For the first word, just add it without a space
            result = word

    return result
