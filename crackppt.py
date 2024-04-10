import os
import comtypes.client
import time

# Defineix el camí complet del fitxer de PowerPoint protegit amb contrasenya
# Defineix el camí complet de l'arxiu de contrasenyes
powerpoint_file = r"C:\tmp\demo.pptx"
password_file = r"C:\tmp\x.txt"
verbose_batch = 1
resume_file = powerpoint_file + ".resume"

# Aquí hauríem de crear l'objecte PowerPoint si fos possible
print(f"Creating PowerPoint object to crack file <{powerpoint_file}>... ", end="")
# Aquí s'iniciaria PowerPoint si fos possible en Python
powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
# powerpoint.Visible = True
print("OK")

# Llegeix la llista de contrasenyes des de l'arxiu de text
cracked = 0
pwds = 0

print(f"Opening passwords file <{password_file}>... ", end="")
with open(password_file, 'r') as file:
    print("OK")
    
    # Si estava a mitges, continua
    if os.path.exists(resume_file):
        print("Resume file found, catching up... ")
        with open(resume_file, 'r') as f_resume:
            continue_from = int(f_resume.read())
        print(f"Seting resume position to {continue_from}... ", end="")
        file.seek(continue_from, 0)
    else:
        continue_from = 0
    
    # Intenta obrir el fitxer de PowerPoint amb cada contrasenya de la llista
    try:
        for line in file:
            password = line
            pwds += 1
            if pwds % verbose_batch == 0:
                print(f"\rTrying key #{pwds}: '{password}'", end="")
            # Aquí hauries d'intentar obrir el fitxer PowerPoint si fos possible en Python
            try:
                # Simula l'obertura del fitxer PowerPoint amb la contrasenya
                ppt = powerpoint.Presentations.Open(powerpoint_file, WithWindow=True, Password = password)
                # Si es pot obrir, marca com a trencat i surt del bucle
                cracked = 1
                break
            except:
                pass

            time.sleep(1)
    except KeyboardInterrupt:
        if pwds > 0:
            continue_from = file.tell()
            print(f"\nSaving resume file to point {continue_from}...", end="")
            with open(resume_file, 'w') as f_resume:
                f_resume.write(str(continue_from))
            print("OK")

if cracked:
    print(f"\n'{powerpoint_file}' cracked with password '{password}'")
    ppt.Close()
else:
    print(f"\nSorry, couldn't crack file '{powerpoint_file}'")

powerpoint.Quit()