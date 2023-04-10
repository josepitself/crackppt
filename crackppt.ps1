# Path to the password protected ppt file
$PowerPointFile = "C:\path\to\pptfile.pptx"

# path to the dictionary with passworks to try
$PasswordFile = "C:\path\to\passwords-list.txt"

#----------------------------------------
# Create a PPT Application object
$PowerPoint = New-Object -ComObject PowerPoint.Application

# Load password lists into memory
$Passwords = Get-Content $PasswordFile

$trencat = 0
$pwds = 0

# Let's try each password to open the ppt file
foreach ($Password in $Passwords) {
    $pwds++
    try {
        $Presentation = $PowerPoint.ProtectedViewWindows.Open($PowerPointFile, $Password)
        Write-Host "\rTrying key # $pwds: '$Password'"
        $Presentation.Close()
        $PowerPoint.Quit()
        $trencat = 1
        break
    }
    catch {
    }
}

# cleanup
try {
    $PowerPoint.Quit()
}
catch {
}

if ($trencat) {
    Write-Host "\rYeehah! '$PowerPointFile' has been cracked! Password: '$Password'\n"
} else {
    Write-Host "\rOooooh, couldn't crack the file '$PowerPointFile'\n"
}
