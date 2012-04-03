import httplib
import urllib2
import time
import sys

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}

    def run(self):
        start_timer = time.time()
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/home?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/account?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/account_comps?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/account_points?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/account_freeplay?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/disclaimer?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/Instructions_Account?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/Instructions_offers?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/offers?playerid=29154&pin=062581')
        resp = urllib2.urlopen('http://master.joingo.com/a/tjcr/scene/FoodFunds?playerid=29154&pin=062581')
        
        http://master.joingo.com/a/tjcr/scene/Account_Comps?playerid=29154&pin=062581
        http://master.joingo.com/a/tjcr/scene/Account_Comps?playerid=29154&pin=062581
        
        
        content = resp.read()
        latency = time.time() - start_timer

        self.custom_timers['Mega_UA_Switch'] = latency

        assert (resp.code == 200), 'Bad Response: HTTP %s' % resp.code
        assert ('MegaJackpots' in content), 'Text Assertion Failed'


if __name__ == '__main__':
	if len(sys.argv) > 2:	# If provided with more than two arguments exit
		sys.exit("Must not provide more than two arguments")
    trans = Transaction()
    trans.run()
