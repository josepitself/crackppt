
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
