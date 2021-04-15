from flask import Flask, render_template, request
from keras.models import load_model
app = Flask(__name__)

model = load_model('model_inception.h5')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print("method executed............", file)
    return "best in the world"


# keras used == 2.4.3
# tensorflow used 2.4.1
