import os, socket, sys
from subprocess import call

from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_file():
    assert 'file' in request.files
    file = request.files['file']
    filename_in = file.filename
    assert filename_in.endswith('.pdf')
    file_path = os.path.join("/tmp/", filename_in)
    file.save(file_path)
    filename_out = filename_in + '.html'
    call(["pdf2htmlEX", filename_in, filename_out])
    r = send_from_directory('/tmp/', filename_out)
    os.remove(filename_out)
    return r

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    print("server IP:", ip, file=sys.stderr)
    os.chdir("/tmp/")
    app.run(host='0.0.0.0', port=80)
