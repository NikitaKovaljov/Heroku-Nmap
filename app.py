from flask import Flask,render_template, request
import flask
#import nmap
  
app = Flask(__name__)

  
@app.route("/")
def pages():
    return render_template('/templates/index.html')

@app.route('/nmap.html', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        nmap_host = request.form.get("host")
        nmap_args = request.form.get("args")

        all_together = nmap_host + nmap_args

        if len(nmap_host) == 0:
            return "Problems with Request"
        else:
            return all_together

            #return nmap_request
            nm.scan(hosts=ip)
    else:
        return render_template('/templates/nmap.html')
  
if __name__ == "__main__":
  app.run()


