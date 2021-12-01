from flask import Flask,render_template, request
import os
import json
import subprocess
import shutil
  
app = Flask(__name__)
  
@app.route("/")
def pages():
    return render_template('/templates/index.html', PageTitle = "Tools")

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
            #x = subprocess.check_output(f"./nmap {nmap_args} -oX - {nmap_host}", shell=True).decode("utf8")
            subprocess.check_output(f"./nmap {nmap_args} -oX output.xml {nmap_host}", shell=True)      
            shutil.move("output.xml", "/app/templates/templates/")
            path1 = "/app/templates/templates/"
            os.chdir(path1)
            test = os.path.exists("./output.xml")
            ### Code above working, file is creating ###
            ### Code below is trying to convert .xml to html file ###
            os.system("xsltproc nmap.xsl output.xml -o new.html")
            lets = os.path.exists("./new.html")
            print(test)
            return("ok")
    else:
        return render_template('/templates/nmap.html', PageTitle = "NMAP")
  
if __name__ == "__main__":
  app.run()


