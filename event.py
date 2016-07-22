import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_environment = jinja2.Environment(
      loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Choose an event!!')
        template = jinja_environment.get_template(
            'event.html')
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
