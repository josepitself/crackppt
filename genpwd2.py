import cracker

terms = ['darth', 'vader', 'vs', 'luke', 'skywalker']
separators = [ '', ' ' ]
fitxer = './passwords.txt'

print("Step1...")
tcases = cracker.all_case_combinations(terms)
all_words = cracker.generate_word_combinations(tcases)
all_combinations = cracker.generate_strings_with_separators(all_words, separators)

print("writing file...")
file = open(fitxer, 'w')
for item in all_combinations:
    file.write(f'{item}\n')

print("Step2...")
terms = [ 'luke', 'skywalker', 'vs', 'darth', 'vader' ]
separators = [ '', ' ' ]
tcases = cracker.all_case_combinations(terms)
all_words = cracker.generate_word_combinations(tcases)
all_combinations = cracker.generate_strings_with_separators(all_words, separators)
print("writing file...")
for item in all_combinations:
    file.write(f'{item}\n')

print("Done!")