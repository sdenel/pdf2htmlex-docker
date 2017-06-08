import os, socket, sys
from subprocess import call
os.chdir("/tmp/")

from subprocess import Popen, PIPE

file_in = sys.stdin.buffer.read()

filename_in = "coucou.pdf"
file_path = os.path.join("/tmp/", filename_in)

file = open(file_path, "wb") 
file.write(file_in) 
file.close()

assert filename_in.endswith('.pdf')

filename_out = filename_in + '.html'


p = Popen(["pdf2htmlEX", filename_in, filename_out], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()
rc = p.returncode


#r = send_from_directory('/tmp/', filename_out)

f = open(filename_out, 'r')
bytes = f.read()
f.close()

print(bytes)

os.remove(filename_out)



