import binascii

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

class Wallet:

	def __init__(self):
		##set

		key = RSA.generate(2048)
		self.public_key = key.publickey().export_key(format = 'PEM')
		self.private_key = key.export_key(format = 'PEM')
		#self_address
		#self.transactions
