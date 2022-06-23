from flask import Flask
app = Flask('hello-world')
@app.route('/')
def hello():
 return "Github Action CI/CD to Deploy Sample Python App on Google Cloud (Google Kubernetes Engine-GKE)\n"
if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 8080)
