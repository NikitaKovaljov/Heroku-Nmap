from flask import Flask,render_template, request
import os
import json
  
app = Flask(__name__)
  
@app.route("/")
def pages():
    return render_template('/templates/index.html')

@app.route('/nmap', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        #nmap_args = request.form.get("args")
        #nmap_host = request.form.get("host")

        nmap_host = "scanme.nmap.org"
        nmap_args = "-v"

        if len(nmap_host) == 0 and len(nmap_args) == 0:
            return "Problems with Request"
        else:
            path = "/app/nmap/bin/"
            os.chdir(path)
            
            os.system("./nmap -v -p 22 -oX output.xml scanme.nmap.org")
            return("success")
    else:
        return render_template('/templates/nmap.html')
  
if __name__ == "__main__":
  app.run()


