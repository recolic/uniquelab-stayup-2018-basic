#!/usr/bin/env python3
import hashlib, sys
# usage: python this.py example@example.com

obj = hashlib.sha256(('RecolicEncryptHead' + sys.argv[1]).encode())
print(obj.hexdigest())
