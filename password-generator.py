import itertools
import argparse
import sys
import math
from tqdm import tqdm

def variacions_maj_min(terme):
    return [''.join(v) for v in itertools.product(*([c.lower(), c.upper()] for c in terme))]

# Defineix els arguments de la línia de comandes
parser = argparse.ArgumentParser()
parser.add_argument("-O", "--output-file", help="File where to write all the passwords", required=True)
parser.add_argument("-t", "--terms", help="Terms to combine to produce passwords", nargs='+', required=True)
parser.add_argument("-s", "--separators", help="Separators to use to join terms", nargs='+', required=True)
parser.add_argument("-c", "--calc-only", help="Calculate the number of passwords to generate but not generate them", action='store_true')
args = parser.parse_args()

# Calcula el nombre total de combinacions
total_combinacions = math.factorial(len(args.terms)) * len(args.separators)**(len(args.terms) - 1) * math.prod([2**len(t) for t in args.terms])

# Imprimeix el total de combinacions generades
print(f"Number of combinations to be produced: {total_combinacions:,}")

if not args.calc_only:
    # Genera les variacions de majúscules i minúscules
    variacions = [variacions_maj_min(terme) for terme in args.terms]

    progress_bar = tqdm(total=total_combinacions, desc="Producing combinations", ncols=70)
    # Genera i escriu les combinacions
    with open(args.output_file, 'w') if args.output_file != '-' else sys.stdout as f:
        for producte in itertools.permutations(variacions):
            for sep_comb in itertools.product(args.separators, repeat=len(producte)-1):
                for p in itertools.product(*producte):
                    combinacio = ''.join(p[i//2] if i%2 == 0 else sep_comb[i//2] for i in range(len(p)*2-1))
                    f.write(f"{combinacio}\n")
                    progress_bar.update()

progress_bar.close()
