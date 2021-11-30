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

        if len(nmap_host) == 0 and len(nmap_args) == 0:
            return "Problems with Request"
        else:
            path = "/app/nmap/bin/"
            os.chdir(path)
            x = subprocess.check_output(f"./nmap {nmap_args} -oX output.xml {nmap_host}", shell=True).decode("utf8")
            #test = os.path.exists("./output.xml")
            return render_template("./output.xml")
    else:
        return render_template('/templates/nmap.html', PageTitle= "NMAP")
  
if __name__ == "__main__":
  app.run()


