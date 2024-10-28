from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Kode untuk menangani data yang dikirimkan
    username = request.form['username']
    password = request.form['password']
    # Simpan data ke database atau kirimkan melalui email
    return "Data telah diterima"

if __name__ == '__main__':
    app.run(debug=True)
