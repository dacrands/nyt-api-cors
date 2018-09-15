from app import app
from flask import jsonify
import requests

@app.route('/api/popular')
def popular():
  res = requests.get('https://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/1.json?api-key={0}'.format(app.config['API_KEY']))
  if res.status_code != 200:
    errData = {'status': res.status_code, 'error': 'There was an error'}
    return jsonify(errData), res.status_code    
  
  popularData = jsonify(res.json())
  return popularData

@app.route('/api/best')
def best():
  res = requests.get('https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json?api-key={0}'.format(app.config['API_KEY']))
  if res.status_code != 200:
    errData = {'status': res.status_code, 'error': 'There was an error'}
    return jsonify(errData), res.status_code    
  
  bestData = jsonify(res.json())
  return bestData

@app.route('/api/archives/<month>/<year>')
def archives(month, year):
  res = requests.get('https://api.nytimes.com/svc/archive/v1/{0}/{1}.json?api-key={2}'.format(month, year, app.config['API_KEY']))
  if res.status_code != 200:
    errData = {'status': res.status_code, 'error': 'There was an error'}
    return jsonify(errData), res.status_code    

  archivesData =  jsonify(res.json())  
  return archivesData