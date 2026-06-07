#!/usr/bin/env python3
"""
Pragmata Save Editor – Edit resources and inventory.
Open source – no game memory modification.
"""

import os
import json
import shutil
from datetime import datetime

SAVE_FILE = os.path.expandvars(r"%USERPROFILE%\Documents\Pragmata\SaveGames\savegame.sav")
BACKUP_DIR = os.path.expanduser("~/Pragmata_Backups")

def backup_save():
    if not os.path.exists(SAVE_FILE):
        print("❌ Save file not found. Play the game first.")
        return False
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"save_{timestamp}.sav")
    shutil.copy2(SAVE_FILE, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return True

def edit_stats():
    print("⚠️ This script is a placeholder. The full trainer is in Releases.")
    print("📦 The trainer supports editing health, jetpack fuel, ammo, and more.")

if __name__ == "__main__":
    if backup_save():
        edit_stats()
        input("Press Enter to exit...")