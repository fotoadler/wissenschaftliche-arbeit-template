#!/usr/bin/env bash
# ==============================================================================
# Automatische Einrichtung des naechtlichen Backups (Cronjob)
# ==============================================================================
# Richtet einen taeglichen Cronjob ein, der jede Nacht um 23:00 Uhr
# das Skript scripts/auto_sync.sh ausfuehrt.
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SYNC_CMD="$SCRIPT_DIR/scripts/auto_sync.sh >> $SCRIPT_DIR/scripts/sync.log 2>&1"
CRON_SCHEDULE="0 23 * * *" # Jeden Tag um 23:00 Uhr

echo "----------------------------------------------------------------"
echo "[SETUP] Richte naechtliches Backup ein..."
echo "Projektpfad: $SCRIPT_DIR"
echo "Zeitplan:    Jeden Abend um 23:00 Uhr"
echo "----------------------------------------------------------------"

# Pruefen ob der Job bereits in der Crontab existiert
CURRENT_CRON=$(crontab -l 2>/dev/null || true)

if echo "$CURRENT_CRON" | grep -Fq "$SCRIPT_DIR/scripts/auto_sync.sh"; then
    echo "[INFO] Naechtlicher Cronjob ist bereits registriert:"
    echo "$CURRENT_CRON" | grep -F "$SCRIPT_DIR/scripts/auto_sync.sh"
else
    # Neuen Cronjob anhaengen
    (echo "$CURRENT_CRON"; echo "$CRON_SCHEDULE $SYNC_CMD") | crontab -
    echo "[ERFOLG] Cronjob erfolgreich hinzugefuegt!"
    echo "Befehl: $CRON_SCHEDULE $SYNC_CMD"
fi

echo "----------------------------------------------------------------"
echo "Tipp: Du kannst das Backup jederzeit auch manuell ausfuehren mit:"
echo "      ./scripts/auto_sync.sh"
echo "----------------------------------------------------------------"
