import web

urls = (
    '/', 'Hello'
)

app = web.application(urls, globals())

class Hello:
    def GET(self):
        web.header('content-type', 'text/json')
        return 'Hello,world!'


if __name__ == '__main__':
    app.run()