import cracker

terms = ['darth', 'vader', 'vs', 'luke', 'skywalker']
separators = [ '', ' ' ]
pwdfile = './passwords.txt'

print("Step1... ")
print("\t[case combinations] ")
tcases = cracker.all_case_combinations(terms)
n=0
for i in range(0, len(tcases)):
    n += len(tcases[i])
print(f"{n}\n\t[all words] ", end='')
print("\n")

all_words = cracker.generate_word_combinations(tcases)
n = len(all_words)
print(f"{n}\n\t[passwords] ", end='')

pwds = cracker.generate_strings_with_separators_to_file(all_words, separators, pwdfile)

print("Step2...")
print("\t[case combinations] ")
tcases = cracker.all_case_combinations(terms)
n=0
for i in range(0, len(tcases)):
    n += len(tcases[i])
print(f"{n}\n\t[all words] ", end='')
print("\n")

all_words = cracker.generate_word_combinations(tcases)
n = len(all_words)
print(f"{n}\n\t[passwords] ", end='')

pwds += cracker.generate_strings_with_separators_to_file(all_words, separators, pwdfile)

print(f"DONE! {pwds} passwords generated")