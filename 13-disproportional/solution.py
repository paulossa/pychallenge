from xmlrpc.client import ServerProxy
conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.system.listMethods())
# Maybe we should call phone ? 
conn.system.methodHelp('phone')
conn.system.methodSignature('phone')
print(conn.phone('Bert'))