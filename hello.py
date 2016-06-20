from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    print "test"
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1' % name
	
	
@app.route('/api/charge' , methods=['POST'])
def charge():
    content = request.json
    print request
    return jsonify({"cctoken":"OK"})
    
    
	
	
if __name__ == '__main__':
    app.run(debug=True)

