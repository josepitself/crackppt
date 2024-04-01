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

def generate_strings_with_separators_to_file(matrix, separators, file_path):
    """
    Generate strings where each string is formed by concatenating the words
    in each row of the matrix with all possible combinations of the given separators,
    and write these strings directly to a file.
    This approach is designed to work efficiently with large datasets by avoiding
    to keep all results in memory.
    """
    def all_combinations_to_file(words, sep, file, prefix=''):
        """Helper function to recursively find and write all combinations for a given list of words."""
        if len(words) == 1:
            file.write(prefix + words[0] + '\n')
            rows += 1
        else:
            # For each combination and separator, write the combination directly to the file
            for s in sep:
                all_combinations_to_file(words[1:], sep, file, prefix + words[0] + s)

    # Open the file once and pass the file object to the helper function
    rowcount = 0
    with open(file_path, 'a') as file:
        for row in matrix:
            rowcount += all_combinations_to_file(row, separators, file)
    return rowcount


