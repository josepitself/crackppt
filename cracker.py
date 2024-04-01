from itertools import product

def toogle_case(s):
    """
    Function to return all possible combinations of uppercase and lowercase letters of a given string.
    """
    if len(s) == 0:
        return ['']
    # Get combinations for the substring
    sub_combinations = toogle_case(s[1:])
    # For each combination, add both the lowercase and uppercase version of the first character
    result = []
    for combination in sub_combinations:
        result.append(s[0].lower() + combination)
        result.append(s[0].upper() + combination)
    return result

def all_case_combinations(termsvector):
    result = []
    for i in range(0, len(termsvector)):
        result.append(toogle_case(termsvector[i]))
    return result

def generate_word_combinations(matrix):
    """
    Generate all possible combinations of words from different vectors in the given matrix,
    where each word appears exactly once in each combination.
    """
    # Generate the cartesian product of lists in the matrix
    combinations = list(product(*matrix))
    return [list(comb) for comb in combinations]

def generate_strings_with_separators(matrix, separators):
    """
    Generate a list of strings where each string is formed by concatenating the words
    in each row of the matrix with all possible combinations of the given separators.
    Each pair of words can only be separated by one separator, but different separators
    can be used within the same string.
    """
    def all_combinations(words, sep):
        """Helper function to recursively find all combinations for a given list of words."""
        if len(words) == 1:
            return words
        # Recur for the rest of the words
        rest_combinations = all_combinations(words[1:], sep)
        result = []
        # For each combination and separator, prepend the first word and separator to the combination
        for combination in rest_combinations:
            for s in sep:
                result.append(words[0] + s + combination)
        return result

    result_list = []
    # Generate combinations for each row in the matrix
    for row in matrix:
        result_list.extend(all_combinations(row, separators))
    
    return result_list
