from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH'])
def main(path):
    print 'Path requested: %s' % path
    for key, value in request.headers:
        print "%s: %s" % (key, value)
    print request.json
    return "200"


if __name__ == '__main__':
    app.run(debug=True)
