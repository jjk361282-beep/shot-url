import base64
import hashlib

def shorten(original_url:str)->str:
    
    url_hash = hashlib.md5(original_url.encode('utf-8')).digest()
    
    # 2. On l'encode en Base64 URL-Safe
    base64_encoded = base64.urlsafe_b64encode(url_hash).decode('utf-8')
    
    # 3. On nettoie les '=' de remplissage et on tronque (ex: 8 caractères)
    short_code = base64_encoded.rstrip('=')[:8]
    
    return short_code
    