from flask import *
import json, time

app = Flask(__name__)

@app.route('/', method=['GET'])
def home_page():
    data_set={'page': 'Homw', 'Message': 'Succesfull loaded home page', 'Timstamp': time.time()}
    json_dump =json.dumps(data_set)
    return json_dump


@app.route('/user/', method=['GET'])
def request_page():
    user_query= str(request.args.get('user'))

    data_set={'page': 'request', 'Message': f'Succesfull got request {user_query}', 'Timstamp': time.time()}
    json_dump =json.dumps(data_set)
    return json_dump


if __name__ =='__main__':
    app.run(port=7777)




