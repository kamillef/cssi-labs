#main.py
# the import section
import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello!</h1>Hello, CSSI!') #the response
class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('You found the secret page!')


# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secret', SecretPage),
], debug=True)
