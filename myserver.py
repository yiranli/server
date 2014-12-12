#! /usr/bin/python2
# -*- coding:utf-8 -*-
# myserver.py
import tornado.web
import tornado.ioloop
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            self.write('<html><body><form action="/" method="post">'
                       '<input type="text" name="message">'
                       '<input type="submit" value="Submit">'
                       '</form></body></html>')
        except:
            self.write_error(404)
    def post(self):
        self.set_header("Content-Type","text/plain")
        self.write("You wrote "+self.get_argument('message').decode('utf-8'))

    def write_error(self,status_code,**kwargs):
        if status_code==404: raise tornado.web.HTTPError(404)
        elif status_code==500: raise tornado.web.HTTPError(500)
        else:
            self.write('error:'+str(status_code))
        
application=tornado.web.Application([
    (r"/",MainHandler),
])

if __name__=='__main__':
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
  

        
    
