# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:31:02 2017

@author: Rightleft
"""

import hmac, hashlib

secret_key = "HelloWorld"
message = "The quick brown fox jumps over the lazy dog"

digest = hmac.new(secret_key, message, hashlib.md5).hexdigest()
print(str(digest))
