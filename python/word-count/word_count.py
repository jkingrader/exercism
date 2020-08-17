def count_words(sentence):
    import re

    # substitute a blank space for non-alphanumeric characters or non-apostrophe
    lower_sentence = re.sub("[^0-9a-zA-Z']+"," ", sentence.lower())
    
    # replace apostrophes at beginning or end of words
    lower_sentence = lower_sentence.replace("' ", " ").replace(" '", " ")
    
    # brute force - remove all apostrophes at beginning or end of string
    while len(lower_sentence) > 0 and lower_sentence[0] == "'":
        lower_sentence = lower_sentence[1:]
    while len(lower_sentence) > 0 and lower_sentence[-1] == "'":
        lower_sentence = lower_sentence[:-1]

    # remove all apostrophes at beginning or end of string
    # lower_sentence.lstrip("'").rstrip("'")

      # initialize dictionary mapping words to counts
    result = {}
    words = lower_sentence.split()
    for word in set(words):
        result.update( {word : words.count(word)} )
    
    return result
