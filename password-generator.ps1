function Generate-CasingCombinations {
    param (
        [string]$term
    )

    $combinations = @()
    $length = $term.Length
    $max = [math]::Pow(2, $length) - 1

    for ($i = 0; $i -le $max; $i++) {
        $combination = ""
        for ($j = 0; $j -lt $length; $j++) {
            $char = $term[$j]
            if (($i -shl -$j) -band 1) {
                $char = [char]::ToUpperInvariant($char)
            }
            else {
                $char = [char]::ToLowerInvariant($char)
            }
            $combination += $char
        }
        $combinations += $combination
    }

    return $combinations
}

function Generate-Phrases {
    param (
        [string[]]$terms,
        [string[]]$separators,
        [string]$currentPhrase,
        [int]$currentIndex
    )

    if ($currentIndex -eq $terms.Count) {
        $currentPhrase | Add-Content -Path $output_file
        $script:counter++
        Write-Host "`rCombinacions generades: $($script:counter)" -NoNewline
    }
    else {
        $termCombinations = Generate-CasingCombinations -term $terms[$currentIndex]
        foreach ($termCombination in $termCombinations) {
            foreach ($separator in $separators) {
                $newPhrase = $currentPhrase + $termCombination
                if ($separator -ne "") {
                    $newPhrase += $separator
                }

                Generate-Phrases -terms $terms -separators $separators -currentPhrase $newPhrase -currentIndex ($currentIndex + 1)
            }
        }
    }
}

# file to contain a line per each password generated
$output_file = "passwords2.txt"

# terms to use and separators to use. Will produce every combination of upper and lower case characters 
# of the terms, with every combination of separators (or no separator) to join terms
$terms = "luke", "skywalker", "vs", "darth", "vader"
$separators = " ", ".", "-"

if (Test-Path $output_file) {
    Remove-Item $output_file
}

$script:counter = 0
Generate-Phrases -terms $terms -separators $separators -currentPhrase "" -currentIndex 0

Write-Host ""


