try:
	from googlesearch import search
except ImportError:
	print('Not Found')
import time

dork = ['site:', 'inurl:', 'intitle:"index of" "wp-config.php.bak"']
query = 'ibm.com'

	
for x in range(len(dork)):
	print('This is' + ' ' +dork[x])
	for j in search(dork[x]+query,  tld=('co.in'),  num=10,  stop=10, pause=10):
		print(j)
time.sleep(20)
	
