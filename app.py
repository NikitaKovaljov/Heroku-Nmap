from flask import Flask,render_template, request, send_from_directory
from os.path import exists
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
        path = "/app/nmap/bin/"
        path1 = "/app/templates/templates/"
        file_name = 1
        new_file_name = 1

        if len(nmap_host) == 0 and len(nmap_args) == 0:
            return "Problems with Request"
        else:
            os.chdir(path)
            if os.path.exists("nmap.xsl"):
                pass
            else:
                os.system("wget https://svn.nmap.org/nmap/docs/nmap.xsl")
            if os.path.exists(f"output{file_name}.xml"):
                pass
            else:
                subprocess.check_output(f"./nmap {nmap_args} -oX output{file_name}.xml --stylesheet nmap.xsl {nmap_host}", shell=True)
            if os.path.exists(f"new{new_file_name}.html"):
                pass
            else:
                os.system(f"xsltproc output{file_name}.xml -o new{new_file_name}.html")    
            if os.path.exists(f"/app/templates/templates/new{new_file_name}.html"):
                pass
            else:
                shutil.move(f"new{new_file_name}.html", "/app/templates/templates/")
            os.chdir(path1)
            final = new_file_name
            new_file_name += 1
            file_name += 1
            print(file_name)
            return send_from_directory('/app/templates/templates',f'new{final}.html')

    else:
        return render_template('/templates/nmap.html', PageTitle = "NMAP")
  
if __name__ == "__main__":
  app.run()


