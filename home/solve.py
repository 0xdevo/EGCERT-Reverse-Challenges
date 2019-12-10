def getHashes():
	base_address = 0x7301E0	
	for address in range(0,0x4B8,0x10):
		ptr = base_address + address
		ptr = ptr		
		address_of_hash = Dword(ptr)
		hash_value = GetManyBytes(address_of_hash,64,True)
		if(hash_value != ""):
			print hash_value



