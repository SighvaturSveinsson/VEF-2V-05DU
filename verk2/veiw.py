from flask.views import View

class MyRequest(View):
    methods = ['POST']

    def dispatch_request(self):
        # request.method == 'POST'
        name = request.form.get('name', 'Damyan')
        return 'Hello, %s!' % name