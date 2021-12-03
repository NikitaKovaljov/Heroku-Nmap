from flask import Flask,render_template, request, send_from_directory
from os.path import exists
import os
import subprocess
import shutil

file_name = 1
new_file_name = 1

app = Flask(__name__)

@app.route("/")
def pages():
    return render_template('/templates/index.html', PageTitle = "Tools")

@app.route('/nmap', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        try:
            nmap_args = request.form.get("args")
            nmap_host = request.form.get("host")
            path = "/app/nmap/bin/"
            path1 = "/app/templates/templates/"
            global file_name
            global new_file_name
        except:
            return("Something wrong in start block")
        if len(nmap_host) == 0 or nmap_host == " " and len(nmap_args) == 0 or nmap_args == " ":
            return "Problems in inputs"
        else:
            os.chdir(path)
            if os.path.exists("nmap.xsl"):
                pass
            else:
                os.system("wget https://svn.nmap.org/nmap/docs/nmap.xsl")
            if os.path.exists(f"output{file_name}.xml"):
                pass
            else:
                try:
                    subprocess.check_output(f"./nmap {nmap_args} -oX output{file_name}.xml --stylesheet nmap.xsl {nmap_host}", shell=True)
                except subprocess.CalledProcessError:
                    return("Sudo args is not allowed")
            if os.path.exists(f"new{new_file_name}.html"):
                pass
            else:
                os.system(f"xsltproc output{file_name}.xml -o new{new_file_name}.html")    
            if os.path.exists(f"/app/templates/templates/new{new_file_name}.html"):
                pass
            else:
                shutil.move(f"new{new_file_name}.html", "/app/templates/templates/")
            try:
                #os.chdir(path1)
                final_name = new_file_name
                file_name += 1
                new_file_name += 1
            except:
                return("something went wrong in counter block")
            return send_from_directory('/app/templates/templates',f'new{final_name}.html')
    else:
        return render_template('/templates/nmap.html', PageTitle = "NMAP")
if __name__ == "__main__":
    app.run()


