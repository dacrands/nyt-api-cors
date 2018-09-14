from app import app
from flask import jsonify
import requests

@app.route('/')
@app.route('/index')
def index():
  res = requests.get('https://api.nytimes.com/svc/archive/v1/1915/10.json?api-key=1e2e8c3de5ee427c835460f4a58a4792')
  return res.text

@app.route('/api/archives/<month>/<year>')
def archives(month, year):
  res = requests.get('https://api.nytimes.com/svc/archive/v1/{0}/{1}.json?api-key={2}'.format(month, year, app.config['API_KEY']))
  print(res.status_code)
  if res.status_code != 200:
    errData = {'status': res.status_code, 'error': 'There was an error'}
    return jsonify(errData)

  archivesData =  jsonify(res.json())  
  
  return archivesData