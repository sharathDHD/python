def ceaser_encrypt( plain_text , key = 3 , wspace = True ,character_set = 127):
	cipher = []

	if wspace:
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) if ord(x) != 32 else cipher.append(chr(32)) for x in list(plain_text)]
	else:	
		[ cipher.append( chr(abs( ord( x ) + key ) % character_set )) for x in list( plain_text ) ]

	return "".join( cipher )
