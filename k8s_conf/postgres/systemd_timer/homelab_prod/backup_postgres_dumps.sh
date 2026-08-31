#!/usr/bin/env bash
set -euo pipefail

DEST="desktop:"
SRC_DIR="/var/backups/postgres"
STATE="/var/backups/postgres/.tailscale_last_sent"

latest="$(ls -1t "${SRC_DIR}"/blog_db-*.backup 2>/dev/null | head -n 1 || true)"
[ -n "$latest" ] || exit 0

basename="$(basename "$latest")"

if [ -f "$STATE" ] && [ "$(cat "$STATE" || true)" = "$basename" ]; then
	  exit 0
fi

tailscale file cp "$latest" "${DEST}"

echo "$basename" > "$STATE"
