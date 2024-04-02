# Defineix el camí complet del fitxer de PowerPoint protegit amb contrasenya
# Defineix el camí complet de l'arxiu de contrasenyes
$PowerPointFile = "C:\devel\crackppt\data\viatge2021.pptx"
$PasswordFile = "C:\devel\crackppt\data\passwords.txt"

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
    while ( ($line = $reader.ReadLine()) -and $pwds -le $continue) {
        $pwds++
        Write-Host "`rSkipping $($continue) passwords... $($pwds)" -NoNewline 
    }
    Write-Host " "
}

# Intenta obrir el fitxer de PowerPoint amb cada contrasenya de la llista
try {
    while ( ($line = $reader.ReadLine()) ) {
        $Password = $line
        $pwds++
        Write-Host "`rTrying key #$($pwds): '$Password'                                    " -NoNewline
        # Intenta obrir el fitxer de PowerPoint 
        try {
            $Presentation = $PowerPoint.ProtectedViewWindows.Open($PowerPointFile, $Password)
            $Presentation.Close()
            $PowerPoint.Quit()
            $trencat = 1
            break
        }
        catch {
        }
    }
}
finally {
    if ($null -ne $reader) {
        if ($pwds -gt 0 -and -not $reader.EndOfStream) {
            Write-Host "`nSaving resume file..." -NoNewline
            $pwds = $pwds - 1
            $pwds | Out-File -FilePath $ResumeFile
            Write-Host "OK"
        }
        $reader.Dispose()
    }
}


# Tanca l'objecte PowerPoint
try {
    $PowerPoint.Quit()
}
catch {
}

if ($trencat) {
    Write-Host "`n'$PowerPointFile' cracked with password '$Password'"
} else {
    Write-Host "`nSorry, couldn't crack file '$PowerPointFile'"
}
