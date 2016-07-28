import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_environment = jinja2.Environment(
      loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('event.html')
        self.response.out.write(template.render())

class PromHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('eventprompage.html')
        self.response.out.write(template.render())

class WeddingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('eventweddingpage.html')
        self.response.out.write(template.render())

class GraduationHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('eventgraduationpage.html')
        self.response.out.write(template.render())

class BirthdayHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('eventbirthdaypage.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/prom', PromHandler),
    ('/wedding', WeddingHandler),
    ('/graduation', GraduationHandler),
    ('/birthday', BirthdayHandler),
], debug=True)
