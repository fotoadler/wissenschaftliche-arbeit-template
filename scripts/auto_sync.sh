#!/usr/bin/env bash
# ==============================================================================
# Automatisches Backup & Git-Sync Skript
# ==============================================================================
# Sichert automatisch alle Arbeitsfortschritte in Git und pusht zu GitHub,
# damit Studierende vor Datenverlust geschuetzt sind und eine lueckenlose
# Versionshistorie haben, ohne manuelle Git-Befehle tippen zu muessen.
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$SCRIPT_DIR"

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
DATE_ONLY=$(date "+%Y-%m-%d")

echo "----------------------------------------------------------------"
echo "[SYNC] Starte Git-Backup: $TIMESTAMP"
echo "----------------------------------------------------------------"

# Pruefen ob Git initialisiert ist
if [ ! -d ".git" ]; then
    echo "[FEHLER] Kein Git-Repository gefunden. Führe zuerst 'git init' aus."
    exit 1
fi

# Pruefen ob Aenderungen vorliegen
if git status --porcelain | grep -q .; then
    CHANGED_COUNT=$(git status --porcelain | wc -l | tr -d ' ')
    echo "[INFO] $CHANGED_COUNT geaenderte/neue Datei(en) erkannt."
    
    # Optional: Aenderungslog dokumentieren
    LOG_FILE="00_steuerung/aenderungslog.md"
    if [ -f "$LOG_FILE" ]; then
        CHANGED_SUMMARY=$(git status --short | head -n 5 | tr '\n' ', ' | sed 's/,$//')
        echo "| $DATE_ONLY | $CHANGED_COUNT Dateien | Automatisches Backup | Nachtsicherung via auto_sync.sh ($CHANGED_SUMMARY) |" >> "$LOG_FILE"
    fi

    # Git add, commit, push
    git add -A
    COMMIT_MSG="Auto-Backup: $TIMESTAMP ($CHANGED_COUNT geaenderte Dateien)"
    git commit -m "$COMMIT_MSG"
    
    # Push falls Remote konfiguriert ist
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
    if git remote | grep -q "origin"; then
        echo "[INFO] Pushe Aenderungen zu GitHub ($CURRENT_BRANCH)..."
        git push origin "$CURRENT_BRANCH" || echo "[WARNUNG] Push zu GitHub fehlgeschlagen (offline?). Lokaler Commit ist gesichert."
    else
        echo "[INFO] Kein Git-Remote 'origin' eingerichtet. Lokaler Commit erfolgreich gesichert."
    fi

    echo "[ERFOLG] Backup abgeschlossen: $COMMIT_MSG"
else
    echo "[INFO] Keine ungespeicherten Aenderungen vorhanden. Alles aktuell."
fi
echo "----------------------------------------------------------------"
