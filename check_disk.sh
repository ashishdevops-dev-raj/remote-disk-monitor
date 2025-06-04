#!/bin/bash

THRESHOLD=60
USER="your_ssh_user"
REPORT="disk_report_$(date +%F).txt"

echo "Disk Usage Report - $(date)" > $REPORT
echo "----------------------------------" >> $REPORT

while IFS= read -r IP; do
  echo "Checking $IP..."
  USAGE=$(ssh -o ConnectTimeout=5 -o BatchMode=yes $USER@$IP "df / | tail -1 | awk '{print \$5}' | sed 's/%//'")

  if [ -z "$USAGE" ]; then
    echo "$IP - ❌ Could not connect" >> $REPORT
    python3 sms.py "❌ ALERT: Cannot connect to $IP"
    continue
  fi

  if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "$IP - 🚨 High Disk Usage: $USAGE%" >> $REPORT
    python3 sms.py "🚨 ALERT: $IP disk usage at ${USAGE}%"
  else
    echo "$IP - ✅ Normal: $USAGE%" >> $REPORT
  fi
done < servers.txt

echo "Report saved to $REPORT"
