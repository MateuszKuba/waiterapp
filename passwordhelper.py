import hashlib
import os
import base64

class PasswordHelper:
    
    def get_hash(self,plain):
        return hashlib.sha512(plain).hexdigest()
    
    def get_salt(self):
        return base64.b64encode(os.urandom(20))
    
    def validate_password(self,plain,salt,expected):
        pw_bytes = plain.encode('utf-8')
        salt_bytes = salt.encode('utf-8')
        return self.get_hash(pw_bytes + salt_bytes) == expected
    
    