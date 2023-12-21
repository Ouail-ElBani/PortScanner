# Importation des modules nécessaires
import argparse
import socket
import threading
from datetime import datetime

# Définition de constantes
MAX_PORT = 65535  # Port maximum à scanner
TIMEOUT = 1  # Délai d'attente pour la connexion à un port

# Fonction pour scanner un port particulier sur la cible
def scan_port(target, port):
    try:
        # Création d'une socket pour la connexion TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(TIMEOUT)
        
        # Tentative de connexion au port spécifié
        result = s.connect_ex((target, port))
        
        # Vérification du résultat de la connexion
        if result == 0:
            print(f"Port {port} is open")
        
        # Fermeture de la socket
        s.close()
    except Exception as e:
        pass  # En cas d'erreur, ignorer et continuer

# Fonction principale pour scanner tous les ports de la cible
def scan_target(target):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    # Création d'une liste de threads pour le scanning des ports
    threads = []
    for port in range(1, MAX_PORT + 1):
        # Création d'un thread pour chaque port
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Attente de la fin de tous les threads
    for thread in threads:
        thread.join()

# Fonction principale du programme
def main():
    # Analyse des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    args = parser.parse_args()

    try:
        # Résolution de l'adresse IP à partir du nom d'hôte
        target = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved !!!!")
        return

    # Appel de la fonction pour scanner les ports de la cible
    scan_target(target)

# Point d'entrée du programme
if __name__ == "__main__":
    main()
