from flask import Flask,render_template, request
import os
import json
import subprocess
  
app = Flask(__name__)
  
@app.route("/")
def pages():
    return render_template('/templates/index.html', PageTitle= "Tools")

@app.route('/nmap', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        nmap_args = request.form.get("args")
        nmap_host = request.form.get("host")

        #nmap_host = "scanme.nmap.org"
        #nmap_args = "-v"

        if len(nmap_host) == 0 and len(nmap_args) == 0:
            return "Problems with Request"
        else:
            path = "/app/nmap/bin/"
            os.chdir(path)
            x = subprocess.check_output(f"./nmap {nmap_args} -oX - {nmap_host}", shell=True).decode("utf8")
            with open('readme.txt', 'x') as f:
                f.write('Create a new text file!')
                
            return(x)

            # subprocess.check_output(f"./nmap {nmap_args} -oX - {nmap_host}", shell=True).decode("utf8") - kid
            # return json.loads(json.dumps(subprocess.check_output(f"./nmap {nmap_args} {nmap_host}", shell=True).communicate())) - parent
    else:
        return render_template('/templates/nmap.html', PageTitle= "NMAP")
  
if __name__ == "__main__":
  app.run()


