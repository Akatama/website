#!/usr/bin/env bash
set -euo pipefail

: "${NTFY_URL:?Set NTFY_URL in the service environment}"
: "${MONITOR_UNIT:=unknown unit}"
: "${MONITOR_SERVICE_RESULT:=unknown}"
: "${MONITOR_EXIT_CODE:=unknown}"
: "${MONITOR_EXIT_STATUS:=unknown}"

message="Unit: ${MONITOR_UNIT}
Result: ${MONITOR_SERVICE_RESULT}
Exit: ${MONITOR_EXIT_CODE} (${MONITOR_EXIT_STATUS})"

exec /usr/bin/curl \
  --fail --silent --show-error --max-time 15 \
  -H "Title: Postgres backup reception to desktop failed" \
  -H "Priority: high" \
  --data-binary "$message" \
  "$NTFY_URL"

