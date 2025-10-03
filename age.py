
# SI JAMAIS TU VEUX UN ENVIRONNEMENT DE DEVELOPPEMENT PYTHON, TU PEUX SUIVRE CES INSTRUCTIONS, sinon tu peux ignorer cette partie.
# Tout d'abord installe Visual Studio Code-Insiders avec ce lien : https://code.visualstudio.com/insiders/ (Si tu as visual studio code classique, ça marche aussi)
# Ensuite installe Python 3.13 ou supérieur avec ce lien : https://www.python.org/downloads/
# Ensuite fais ctrl + shift + x pour ouvrir les extensions et recherche python et installe l'extension officielle de Microsoft.
# Ensuite crée un nouveau fichier age.py et copie-colle ce code dedans.
# Fais windows puis tape python et accède à l'emplacement du fichier.
# Copie le chemin en haut (ex: D:\Aymeric\Git\python)
# Retourne sur ton fichier age.py et fais 'run python file'
# il devrait te demander de choisir un debugger, tu choisis browse et tu colles le chemin que tu as copié avant et tu sélectionnes .

# Pour exécuter ce programme, il suffit de lancer le fichier age.py avec un exécuteur Python (ctrl + F5 puis python debugger).

# Si jamais quelque chose ne fonctionne pas, n'hésite pas à m'appeler au 06 52 80 40 44.
# Si tu as des questions on peut éventuellement prévoir un petit point ensemble pour que j'y réponde.

# Un programme python est divisé en plusieurs groupes.
# En premier : les importations de modules (bibliothèques) externes. (from math import *, import datetime, etc.)
# En deuxième : les définitions de fonctions.
    # Chaque fonction est un bloc de code qui peut être réutilisé plusieurs fois dans le programme.
    # Une fonction est définie par le mot-clé 'def' suivi du nom de la fonction et de parenthèses ().
    # Les parenthèses peuvent contenir des paramètres, qui sont des valeurs d'entrée pour la fonction.
    # Le code de la fonction est indenté (décalé vers la droite) pour indiquer qu'il fait partie de la fonction.
    # Chaque fonction peut contenir des variables locales, qui ne sont accessibles que dans la fonction.
    # Une fonction peut retourner une valeur avec le mot-clé return.
    # Une fonction peut être appelée (exécutée) en écrivant son nom suivi de parenthèses ().
# En troisième : le code principal qui exécute le programme.
# Les commentaires définis par des hashtags # sont des lignes de texte qui ne sont pas exécutées par le programme.

# Ceci est une fonction qui calcule l'âge d'une personne en fonction de son année de naissance.
def level_1(): # Ici on définit une fonction appelée level_1
    print("Level 1: Age by Year of Birth") # l'attribut print sert à afficher du texte à l'écran. Ici on affiche "Level 1: Age by Year of Birth"
    year_of_birth = int(input("Enter your year of birth: ")) # Ceci est une entrée utilisateur (variable) pour l'année de naissance
    current_year = 2025  # Ceci est une entrée utilisateur (variable) pour l'année actuelle
    age = current_year - year_of_birth # Ici on calcule l'âge en soustrayant l'année de naissance (current_year) de l'année actuelle (year_of_birth)
    print(f"You are {age} years old.\n") # Ici on affiche l'âge calculé grace au print et au texte "You are {age} years old."
    # les accolades {} permettent d'insérer la valeur de la variable age dans la chaîne de caractères.

def level_2():
    print("Level 2: Exact Age by Birthdate")
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    # Ceci sont des variables pour la date actuelle (à mettre à jour à la main)
    current_year = 2025
    current_month = 6
    current_day = 10

    age_years = current_year - birth_year
    age_months = current_month - birth_month
    age_days = current_day - birth_day

    if age_days < 0:
        age_months -= 1
        prev_month_days = 31 if current_month in [5, 7, 8, 10, 12] else 30
        if current_month == 3:
            prev_month_days = 29 if (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)) else 28
        age_days += prev_month_days

    if age_months < 0:
        age_years -= 1
        age_months += 12

    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.\n")

def level_3():
    print("Level 3: Exact Age in Years, Months, Days, Hours, Minutes, Seconds")
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))
    birth_hour = int(input("Enter your birth hour (0-23): "))
    birth_minute = int(input("Enter your birth minute (0-59): "))
    birth_second = int(input("Enter your birth second (0-59): "))

    # Current date and time (update if needed)
    current_year = 2024
    current_month = 6
    current_day = 10
    current_hour = 12
    current_minute = 0
    current_second = 0

    # Calculate total seconds
    def to_seconds(y, mo, d, h, mi, s):
        days = y * 365 + mo * 30 + d  # Approximate months as 30 days
        hours = days * 24 + h
        minutes = hours * 60 + mi
        seconds = minutes * 60 + s
        return seconds

    birth_seconds = to_seconds(birth_year, birth_month, birth_day, birth_hour, birth_minute, birth_second)
    current_seconds = to_seconds(current_year, current_month, current_day, current_hour, current_minute, current_second)
    diff = current_seconds - birth_seconds

    years = diff // (365 * 24 * 3600)
    diff %= (365 * 24 * 3600)
    months = diff // (30 * 24 * 3600)
    diff %= (30 * 24 * 3600)
    days = diff // (24 * 3600)
    diff %= (24 * 3600)
    hours = diff // 3600
    diff %= 3600
    minutes = diff // 60
    seconds = diff % 60

    # Ici on affiche l'âge exact en années, mois, jours, heures, minutes et secondes.
    print(f"Your exact age is:")
    print(f"{years} years")
    print(f"{months} months")
    print(f"{days} days")
    print(f"{hours} hours")
    print(f"{minutes} minutes")
    print(f"{seconds} seconds\n")

# Ceci est la fonction principale qui gère le programme.
def main(): # Ici on définit une fonction appelée main
    print("Choose a level:") # Ici on affiche "Choose a level:" pour demander à l'utilisateur de choisir un niveau.
    print("1. Age by year of birth") # Ici on affiche "1. Age by year of birth" pour indiquer le premier niveau.
    print("2. Exact age by birthdate") # Ici on affiche "2. Exact age by birthdate" pour indiquer le deuxième niveau.
    print("3. Exact age in years, months, days, hours, minutes, seconds") # Ici on affiche "3. Exact age in years, months, days, hours, minutes, seconds" pour indiquer le troisième niveau.
    level = input("Enter level (1/2/3): ") # Ici on demande à l'utilisateur de saisir le niveau qu'il souhaite exécuter.
    if level == "1": # Ici on vérifie si l'utilisateur a choisi le niveau 1.
        level_1() # Si c'est le cas, on appelle la fonction level_1 pour exécuter le code correspondant.
    elif level == "2": # Ici on vérifie si l'utilisateur a choisi le niveau 2.
        level_2() # Si c'est le cas, on appelle la fonction level_2 pour exécuter le code correspondant.
    elif level == "3": # Ici on vérifie si l'utilisateur a choisi le niveau 3.
        level_3() # Si c'est le cas, on appelle la fonction level_3 pour exécuter le code correspondant.
    else:
        print("Invalid level.")

main() # Ici on appelle la fonction main pour exécuter le programme principal.

