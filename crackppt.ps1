# Defineix el camí complet del fitxer de PowerPoint protegit amb contrasenya
# Defineix el camí complet de l'arxiu de contrasenyes
$PowerPointFile = "C:\devel\crackppt\data\viatge2021.pptx"
$PasswordFile = "C:\devel\crackppt\data\passwords.txt"
$VerboseBatch = 5000
$ResumeFile = $PowerPointFile + ".resume"

# Crea un objecte PowerPoint per obrir el fitxer
Write-Host "Creating PowerPoint object to crack file <$($PowerPointFile)>... " -NoNewline
$PowerPoint = New-Object -ComObject PowerPoint.Application
Write-Host "OK"

# Llegeix la llista de contrasenyes des de l'arxiu de text
$trencat = 0
$pwds = 0

Write-Host "Opening passwords file <$($PasswordFile)>... " -NoNewline
$reader = [System.IO.StreamReader]::new($PasswordFile)
Write-Host "OK"

# Si estava a mitges, continua
if (Test-Path -Path $ResumeFile) {
    Write-Host "Resume file found, catching up... "
    $continue = Get-Content -Path $ResumeFile
    Write-Host "Skipping $($continue) passwords... " -NoNewline
    while ( ($line = $reader.ReadLine()) -and $pwds -le $continue) {
        $pwds++
        if ($pwds % $VerboseBatch -eq 0) {
            Write-Host "`rSkipping $($continue) passwords... $($pwds)" -NoNewline 
        }
    }
    Write-Host "`nContinuing from $($pwds)"
}

# Intenta obrir el fitxer de PowerPoint amb cada contrasenya de la llista
$continue = $true
try {
    [console]::TreatControlCAsInput = $true
    while ( ($line = $reader.ReadLine()) -and $continue) {
        $Password = $line
        if ($pwds % $VerboseBatch -eq 0) {
            Write-Host "`rTrying key #$($pwds): '$Password'                                    " -NoNewline
        }
        # Intenta obrir el fitxer de PowerPoint 
        try {
            $Presentation = $PowerPoint.ProtectedViewWindows.Open($PowerPointFile, $Password)
            $Presentation.Close()
            $PowerPoint.Quit()
            $trencat = 1
            $continue = $false
            break
        }
        catch {
        }

        if ([console]::KeyAvailable)
        {
            $key = [system.console]::readkey($true)
            if (($key.modifiers -band [consolemodifiers]"control") -and ($key.key -eq "C"))
            {
                $answer = Read-Host "`nProcessing paused at point #$($pwds). Continue? [S/n]"
                if ($answer.ToLower() -eq 'n') {
                    Write-Host "Bye!"
                    $continue = $false
                    $reader.Dispose()
                    break
                } else {
                    Write-Host "Resuming cracking process, point #$($pwds)."
                    [console]::TreatControlCAsInput = $true
                }
            }
        }
        $pwds++
    }

    # Tanca l'objecte PowerPoint
    try {
        $PowerPoint.Quit()
    }
    catch {
    }
} 
finally {
    $pwds = $pwds - 1
    Write-Host "`nSaving resume file to point $($pwds)..." -NoNewline
    $pwds | Out-File -FilePath $ResumeFile
    Write-Host "OK"

    if ($trencat) {
        Write-Host "`n'$PowerPointFile' cracked with password '$Password'"
    } else {
        Write-Host "`nSorry, couldn't crack file '$PowerPointFile'"
    }
}
