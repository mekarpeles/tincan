import web
import random
import hashlib
import base64

class ApiKey:
    def GET(self):
        """
        Simple API key generator
        jetfar.com/simple-api-key-generation-in-python
        
        """
        return base64.b64encode(hashlib.sha256( str(random.getrandbits(256)) ).digest(),
                                random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')

