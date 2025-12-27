from pathlib import Path

# Projekt-Root (ein Ordner über /src)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Standardordner
DATA_DIR = PROJECT_ROOT / "data"
FIG_DIR = PROJECT_ROOT / "figures"

# Pfad zur CSV
DATA_FILE = DATA_DIR / "credit_data.csv"
