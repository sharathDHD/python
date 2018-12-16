def ceaser_encrypt( plain_text , key = 3 , wspace = True ,character_set = 127):
	cipher = []

	if wspace:
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) if ord(x) != 32 else cipher.append(chr(32)) for x in list(plain_text)]
	else:	
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) for x in list( plain_text ) ]

	return "".join( cipher )

def ceaser_decrypt( cipher_text , key = 3 , wspace = True , character_set = 127 ):
	plain_text = []
	if wspace:
		[ plain_text.append( chr(( abs( ord( x ) - key ) % character_set ))) if ord(x) != 32 else plain_text.append(chr(32)) for x in cipher_text ]
	else:
		[ plain_text.append( chr(( abs( ord( x ) - key ) % character_set )))  for x in cipher_text ]	
	return "".join(plain_text)

