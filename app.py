from flask import Flask,render_template, request
import nmap3
  
app = Flask(__name__)
  
@app.route("/")
def pages():
    return render_template('/templates/index.html')

@app.route('/nmap', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        #nmap_args = request.form.get("args")
        #nmap_host = request.form.get("host")

        nmap_host = "10.9.104.240"
        nmap_args = "-sV"

        if len(nmap_host) == 0 and len(nmap_args) == 0:
            return "Problems with Request"
        else:
            return nmap_host
            """
            nmap = nmap3.Nmap()
            result = nmap.scan_top_ports(nmap_host, args=nmap_args)
            """
        
    else:
        return render_template('/templates/nmap.html')
  
if __name__ == "__main__":
  app.run()


