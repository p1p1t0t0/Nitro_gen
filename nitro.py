import os
import random
import string
import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii():
    fig = Figlet(font="slant")
    print(Fore.CYAN + fig.renderText("SOLIX"))
    print(Fore.YELLOW + "               By p1p1t0t0\n")

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_code(code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}"
    response = requests.get(url)
    return response.status_code == 200

def main():
    clear_console()
    print_ascii()

    try:
        total = int(input(Fore.WHITE + "Combien de codes voulez-vous générer ? " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "❌ Nombre invalide !")
        return

    use_webhook = input(Fore.WHITE + "Voulez-vous utiliser un webhook ? [O/N] " + Style.RESET_ALL).strip().upper()
    webhook_url = None

    if use_webhook == "O":
        webhook_url = input(Fore.CYAN + "Veuillez entrer le lien du webhook : " + Style.RESET_ALL).strip()
        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            print(Fore.RED + "❌ Le lien n'est pas valide. Veuillez réessayer !")
            return

    valid_count = 0
    invalid_count = 0

    print("\n" + Fore.MAGENTA + "📦 Génération des liens Nitro...\n")

    for i in range(1, total + 1):
        code = generate_code()
        full_link = f"https://discord.gift/{code}"

        if check_code(code):
            print(Fore.GREEN + f"Valide   | {i:<3} | {full_link}")
            valid_count += 1
            if webhook_url:
                requests.post(webhook_url, json={"content": f"🎉 Code Nitro Valide trouvé : {full_link}"})
        else:
            print(Fore.RED + f"Invalide | {i:<3} | {full_link}")
            invalid_count += 1

    print("\n" + "-"*42)
    print(Fore.RED + f"❌ Codes invalides : {invalid_count}")
    print(Fore.GREEN + f"✅ Codes valides   : {valid_count}")
    print("-"*42)

if __name__ == "__main__":
    main()
