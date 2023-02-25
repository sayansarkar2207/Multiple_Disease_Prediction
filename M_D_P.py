from flask import Flask, render_template, request
import output
import json
import base64

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index_html():
    return render_template('mdp.html',flag="False")


@app.route('/send', methods=['POST'])
def get_data_from_html1():
    ou = request.get_json()
    result = json.loads(ou)
    result = result[result.index(',')+1:]
    imgdata = base64.b64decode(result)
    filename = './static/images/input.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return render_template('mdp.html', flag="False")



@app.route('/send_data', methods=['POST'])
def get_data_from_html():
    x = output.predict()
    if x!="":
        print(x)
        return render_template('mdp.html', flag="True", prediction=x)
    else:
        return render_template('mdp.html', flag="False")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
