import web


urls = (
    # '/(.*)', 'hello',
    '/hello_1[/]?.*', 'hello_1',
    '/hello_2/(.*)', 'hello_2',
)

app = web.application(urls, globals())
render=web.template.render('templates')

class hello_1:

    def GET(self):
        return render.index_1()


class hello_2:

    def GET(self, name):
        return render.index_2("Lisa")

if __name__ == "__main__":
    app.run()