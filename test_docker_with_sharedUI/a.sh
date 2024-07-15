#!/usr/bin/env sh
if [ -z "$SCRIPT_PATH" ]; then
  echo "SCRIPT_PATH environment variable is required"
  exit 1
fi
python3 $SCRIPT_PATH
echo PyQT5 application closed. Keeping container running...
tail -f /dev/null

