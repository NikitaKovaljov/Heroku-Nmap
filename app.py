from flask import Flask,render_template, request
import nmap3
import os
  
app = Flask(__name__)
  
@app.route("/")
def pages():
    return render_template('/templates/index.html')

@app.route('/nmap.html', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        nmap_args = request.form.get("args")
        nmap_host = request.form.get("host")

        #all_together = (nmap_args + ' ' + nmap_host)

        if len(nmap_host) == 0:
            return "Problems with Request"
        else:
            #username = getpass.getuser()
            local = os.getuid()
            tut = local 
            return tut
            """
            nmap = nmap3.Nmap()
            result = nmap.scan_top_ports(nmap_host, args=nmap_args)
            x = 1
            return x
            """
        
    else:
        return render_template('/templates/nmap.html')
  
if __name__ == "__main__":
  app.run()


