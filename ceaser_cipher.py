import nltk
def ceaser_encrypt( plain_text , key = 3 , wspace = True ,character_set = 127):
	""" Encrypts based on ASCII table of 127 elements with given key """
	cipher = []
	if wspace:
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) if ord(x) != 32 else cipher.append(chr(32)) for x in list(plain_text)]
	else:	
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) for x in list( plain_text ) ]

	return "".join( cipher )

def ceaser_decrypt( cipher_text , key = 3 , wspace = True , character_set = 127 ):
	""" Decrypts ceaser cipher with key as of ASCII table"""
	plain_text = []
	if wspace:
		[ plain_text.append( chr(( abs( ord( x ) - key ) % character_set ))) if ord(x) != 32 else plain_text.append(chr(32)) for x in cipher_text ]
	else:
		[ plain_text.append( chr(( abs( ord( x ) - key ) % character_set )))  for x in cipher_text ]	
	return "".join(plain_text)

def get_vocab():
	""" generates vocab"""
	for word in nltk.corpus.words.words():
		yield word.lower()

def ceaser_brute_decrypt( cipher_text ):
	""" decrypts ceaser cipher even if there is no key """
	vocab = set(get_vocab())
	plain_text = []
	for y in cipher_text.split():
		for key in range(128):
			x = ceaser_decrypt(y,key)
			if x in vocab:
				plain_text = ceaser_decrypt(cipher_text,key)
				return plain_text


if __name__ == '__main__':
	choice = 0
	while(choice == 0):
		print(" 1 . Encrypt \n 2 . Decrypt\n 3.Brute force Decrypt \n 4.Exit")
		choice = int( input( "Enter choice:" ))
		if choice == 1 :
			print( ceaser_encrypt( input( " Enter plain Text " ) , int( input( "Enter key:" )) , 1 != abs( int( input( "Enter 1 to encrypt along with spaces" )))))
		elif choice == 2 :					     
			print(ceaser_decrypt( input( " Enter cipher Text " ) , int( input( "Enter key:" )) , 1 != abs( int( input( "Enter 1 to decrypt along with spaces " )))))
		elif choice == 3 :
			_ = ceaser_brute_decrypt( input( " Enter cipher Text : " ))
			print(" : decrypted to : ", _ )
		elif choice == 4 :
			exit(0)
		else :	
			print(" Enter valid input ")
		choice = 0	
