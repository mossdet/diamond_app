from flask import Flask
import ml_framework

# Name the Flask app
app = Flask('ping')

# Use a declarator to add extra functionalities to core functions
# The extra functionality that will be added wil allow turning the app into a web service 

# @app.route() specifies in which address this function will live (in this cases the /ping address)
@app.route('/pingole', methods=['GET'])
def pingoleta():
    return "PONGOLETA\n"


@app.route('/ping', methods=['GET'])
def ping():
    return "PONG\n"



# the Flask app must run from main
# In order to start this app, simply run python ping.py on a terminal, the app will then be accesible at the specified address and port
# The access to the app can be tested using curl , e.g. curl http://192.168.4.20:9696/ping
# The access to the app can also be tested using a browser and typing http://192.168.4.20:9696/ping or http://localhost:9696/ping
if __name__ == '__main__':
    # host address 0.0.0.0, port is 9696
    app.run(debug=True, host='0.0.0.0', port='9696')

