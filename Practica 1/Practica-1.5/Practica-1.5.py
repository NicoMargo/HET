#!/usr/bin/env python3
import base64
from pathlib import Path

b64_data = Path("passwd64").read_bytes()
raw = base64.b64decode(b64_data)
print(raw.decode("utf-8", errors="replace"), end="")

