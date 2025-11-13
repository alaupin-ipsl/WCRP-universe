#!/usr/bin/env python3
"""
Ajouter "sub_experiment_id": "none" aux fichiers JSON d'un dossier
si la clé n'existe pas encore. Insère juste après "start_year" si présent,
sinon ajoute à la fin.

Usage:
    python add_sub_experiment_id.py --dir CMIP7_experiment [--backup]
"""

import json
from pathlib import Path
import shutil
import argparse

def process_file(path: Path, backup: bool = False) -> bool:
    """
    Retourne True si le fichier a été modifié (clé ajoutée), False sinon.
    """
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"ERROR: impossible de lire {path}: {e}")
        return False

    # Si la clé existe déjà, on ne touche pas au fichier
    if "sub_experiment_id" in data:
        print(f"SKIP (already present): {path.name}")
        return False

    # Construire un nouveau dict en conservant l'ordre et en insérant la clé
    new_obj = {}
    inserted = False
    for k, v in data.items():
        new_obj[k] = v
        if k == "start_year":
            # insérer immédiatement après start_year
            new_obj["sub_experiment_id"] = "none"
            inserted = True

    if not inserted:
        # pas de start_year : ajouter à la fin
        new_obj["sub_experiment_id"] = "none"

    # backup si demandé
    if backup:
        bak = path.with_suffix(path.suffix + ".bak")
        try:
            shutil.copy(path, bak)
            print(f"Backup créé: {bak.name}")
        except Exception as e:
            print(f"WARNING: backup failed for {path}: {e}")

    # Écrire de façon atomique possible (écrire dans un fichier temporaire puis renommer)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    try:
        with temp_path.open("w", encoding="utf-8") as fh:
            json.dump(new_obj, fh, indent=4, ensure_ascii=False)
        temp_path.replace(path)
        print(f"UPDATED: {path.name}")
        return True
    except Exception as e:
        print(f"ERROR: impossible d'écrire {path}: {e}")
        # nettoyer le temporaire si présent
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)
        return False


def main(target_dir: str, backup: bool = False, recursive: bool = False):
    p = Path(target_dir)
    if not p.exists() or not p.is_dir():
        print(f"Le dossier cible n'existe pas ou n'est pas un répertoire: {target_dir}")
        return

    pattern = "**/*.json" if recursive else "*.json"
    files = list(p.glob(pattern))
    if not files:
        print("Aucun fichier JSON trouvé.")
        return

    created = 0
    skipped = 0
    errors = 0
    for f in files:
        modified = process_file(f, backup=backup)
        if modified:
            created += 1
        else:
            # si traitement non modifié et la clé existait déjà → skip
            # si erreur → count erreur
            # process_file imprime déjà le détail, on catégorise simplement :
            if "sub_experiment_id" in ( (lambda: (json.load(f.open("r", encoding="utf-8")) if f.exists() else {}))() ):
                skipped += 1
            else:
                # On ne peut pas distinguer toujours skip vs error facilement sans relire;
                # comptons skipped si la fonction a retourné False et le fichier est lisible.
                try:
                    _ = json.load(f.open("r", encoding="utf-8"))
                    skipped += 1
                except Exception:
                    errors += 1

    print(f"\nRésumé: ajoutés: {created}, skipped: {skipped}, erreurs: {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ajouter sub_experiment_id aux JSON d'un dossier.")
    parser.add_argument("--dir", "-d", default=".", help="Dossier cible contenant les fichiers .json")
    parser.add_argument("--backup", "-b", action="store_true", help="Créer un .bak avant modification")
    parser.add_argument("--recursive", "-r", action="store_true", help="Traiter récursivement les sous-dossiers")
    args = parser.parse_args()

    main(args.dir, backup=args.backup, recursive=args.recursive)
