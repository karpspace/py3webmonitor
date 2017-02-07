import sys
import urllib2
import urllib
class Py3status:
    urls = [
            'youUrl.com']
    status = ''

    def websitesStatus(self):
        self.status = ''
        color = self.py3.COLOR_LOW
        error = 0
        for url in self.urls:
            req = urllib2.Request('http://'+url)
            resCode = '';
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError as e:
                resCode = '404'
            if resCode == '404':
                if (not error):
                    self.status = ''
                color = self.py3.COLOR_HIGH
                self.status = '[' + url + ']' + self.status
                error=1
            else:
                if(not error):
                    self.status = 'All websites are up.'
        return {
                'full_text':self.status,
                'color': color,
                'cached_until': 10
                }
