#!/usr/bin/env python
import os

print(os.getenv('GREETING_CONFIGMAP'))
print(os.getenv('GREETING_SECRET'))