#!/usr/bin/env bash
set -uo pipefail

pytest /tests/test_outputs.py --ctrf=/tmp/ctrf-report/ctrf.json
status=$?

mkdir -p /logs/verifier
cp /tmp/ctrf-report/ctrf.json /logs/verifier/ctrf.json 2>/dev/null || true

if [ "$status" -eq 0 ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

exit 0
