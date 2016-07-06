from flask import Flask, request, jsonify
import stripe
import json,httplib
import requests
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
    stripe.api_key = "sk_test_GHr5dXDw5KyZXmEYUghkBezc"
    content = request.json
    token = content['stripeToken']
    amountInCents = content['amountInCents']
    print "token********"
    print token
    try:
        charge = stripe.Charge.create(
            amount = amountInCents,
            currency = "usd",
            source = token,
            description = "Example charge"
        )
        print "charge*********"
        print charge
        return jsonify({"chargeID":charge.id})
    except stripe.error.CardError as e:
        print "The card has been declined"
        body = e.json_body
        err  = body['error']
        print err
        print e
        
    return jsonify({"chargeID":"failed"})

    
    
	
	
if __name__ == '__main__':
    app.run(debug=True)

