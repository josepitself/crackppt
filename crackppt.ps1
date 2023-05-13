# Defineix el camí complet del fitxer de PowerPoint protegit amb contrasenya
$PowerPointFile = "C:\path\to\pptfile.pptx"

# Defineix el camí complet de l'arxiu de contrasenyes
$PasswordFile = "C:\path\to\passwords-file.txt"

# Crea un objecte PowerPoint per obrir el fitxer
Write-Host "Create object PowerPoint.Application... " -NoNewline
$PowerPoint = New-Object -ComObject PowerPoint.Application
Write-Host "OK"

# Llegeix la llista de contrasenyes des de l'arxiu de text
$trencat = 0
$pwds = 0

# Intenta obrir el fitxer de PowerPoint amb cada contrasenya de la llista
try {
    Write-Host "Opening passwords file '$($PasswordFile)... " -NoNewline
    $reader = [System.IO.StreamReader]::new($PasswordFile)
    Write-Host "OK"
    
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
