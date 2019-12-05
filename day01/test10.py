import web

urls = (
    '/', 'Tmp',
    '/aaa', 'Hello'

)

app = web.application(urls, globals())

class Hello:
    def GET(self):
        web.header('content-type','text/json')
        return 'Hello, world!'

class Tmp:
    def GET(self):
        web.header('content-type','text/json')
        return 'Hello, aaa!'

if __name__ == "__main__":
    app.run()