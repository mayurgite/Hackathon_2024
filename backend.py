from flask import Flask, render_template, request, jsonify

app = Flask(__name__,template_folder='template')

@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/predict", methods=['POST'],)
def predict():

    data = request.json  # Get the array of data from the request
    print(f"Received data: {data}")
    
    # You can process the data here as needed

    return jsonify({'message': 'Data received successfully', 'received_data': data}), 200

    # if coordinates.len > 10:
    #     return render_template('index.html', pred='Not good')
    # else:
    #     return render_template('index.html', pred='All good')

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=8090)