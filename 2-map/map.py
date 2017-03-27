# coding: utf-8

from string import ascii_letters, ascii_lowercase

class CCTranslator:
	def __init__(self, key):
		"""Creates a Ceasar Cipher Translator"""
		self.key = key
	
	def translate(self, encripted):
		decripted = ""
		for char in encripted:
			idx = ascii_lowercase.find(char.lower())
			
			if (idx == -1):
				decripted += char
			else: #character is a letter. 
				shiftedPosition = idx + self.key
				if (shiftedPosition >= len(ascii_lowercase)):
					shiftedPosition -= len(ascii_lowercase)
				decripted += ascii_lowercase[shiftedPosition]
		print decripted
	
def main():	
	translator = CCTranslator(2)
	stringToSolve = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
	translator.translate(stringToSolve)
	
	print "Applying to the url (map): " ,
	translator.translate("map")
 
if __name__ == "__main__":
	main()
