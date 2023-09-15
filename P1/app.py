from flask import Flask
from flask import request, jsonify, make_response
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        
        return f(*args, **kwargs)

@app.route('/group01')
def group01():
    return jsonify({'result': 'este es el grupo 01'})

@app.route('/group02')
def group02():
    return jsonify({'result': 'este es el grupo 02'})

# Selected
@app.route('/group03')
def group03():
    return jsonify({'result': 'este es el grupo 03'})

@app.route('/group04')
def group04():
    return jsonify({'result': 'este es el grupo 04'})

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == '000000111111':
        token = jwt.enconde({ 
            'user': auth.username, 
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

if _name_ == "__main__":
    app.run(debug=True, port=5000)