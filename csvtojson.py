import csv
import json
from datetime import datetime
import sys

def convert_csv_to_json(input_file, output_file):
    """
    Convertit un fichier CSV de taux de change en format JSON API-like.
    
    Args:
        input_file (str): Chemin vers le fichier CSV d'entrée
        output_file (str): Chemin vers le fichier JSON de sortie
    """
    exchange_rates = []
    
    try:
        with open(input_file, 'r') as csv_file:
            # Utiliser le module csv pour lire le fichier
            csv_reader = csv.reader(csv_file)
            
            # Lire l'en-tête pour le sauter
            header = next(csv_reader)
            
            # Traiter chaque ligne
            for row in csv_reader:
                if len(row) >= 3:  # Vérifier que la ligne a au moins 3 colonnes
                    date_str, currency, rate = row
                    
                    # Convertir le format de date de MM/DD/YYYY à YYYY-MM-DD
                    try:
                        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        iso_date = date_obj.strftime('%Y-%m-%d')
                    except ValueError:
                        # Si le format de date est déjà bon ou différent, utiliser tel quel
                        iso_date = date_str
                    
                    # Convertir le taux en nombre flottant
                    try:
                        rate_float = float(rate)
                    except ValueError:
                        print(f"Avertissement: Impossible de convertir le taux '{rate}' en nombre pour {currency} à la date {date_str}")
                        rate_float = rate  # Garder comme chaîne si la conversion échoue
                    
                    # Ajouter l'entrée au tableau des taux de change
                    exchange_rates.append({
                        "date": iso_date,
                        "currency": currency,
                        "rate": rate_float
                    })
            
        # Créer la structure JSON finale
        json_data = {
            "exchange_rates": exchange_rates
        }
        
        # Écrire le résultat dans le fichier de sortie
        with open(output_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)
            
        print(f"Conversion réussie. Résultat écrit dans {output_file}")
        
    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return False
        
    return True

def main():
    """Fonction principale pour exécuter le script."""
    if len(sys.argv) != 3:
        print("Usage: python convert_exchange_rates.py input.csv output.json")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_csv_to_json(input_file, output_file)

if __name__ == "__main__":
    main()