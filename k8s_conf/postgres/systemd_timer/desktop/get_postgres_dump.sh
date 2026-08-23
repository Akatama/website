#!/usr/bin/env bash
set -euo pipefail

DEST="/var/backups/postgres"

if [ ! -d "$DEST" ]; then
  sudo mkdir -p "$DEST"
fi

tailscale file get "$DEST"
