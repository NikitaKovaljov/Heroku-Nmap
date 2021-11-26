from flask import Flask,render_template, request
import flask
#import nmap3
  
app = Flask(__name__)

  
@app.route("/")
def pages():
    return render_template('/templates/index.html')

@app.route('/nmap.html', methods = ['POST','GET'])
def nmap():
    if request.method == "POST":
        nmap_request = request.form.get("nmap_request")
        if len(nmap_request) == 0:
            return "Problems with Request"
        else:
            return nmap_request
    else:
        return render_template('/templates/nmap.html')
  
if __name__ == "__main__":
  app.run()


