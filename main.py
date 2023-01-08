from distutils.log import debug
from fileinput import filename
from flask import *
import socket
import pyqrcode


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


local_ip_address = get_local_ip()
url = "http://"+local_ip_address+":80"
qr = pyqrcode.create(url)
qr_ascii = qr.terminal(quiet_zone=1)
print(qr_ascii)
app = Flask(__name__)


@app.route('/')
def main():

    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(f.filename)
        # save file in /sdcard/Download+ f.filename)
        return render_template("Acknowledgement.html", name=f.filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
