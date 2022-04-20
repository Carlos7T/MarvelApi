import requests,json
from flask import Flask, render_template, make_response, jsonify 
from decouple import config

app = Flask(__name__)
PORT=5001

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#GET METHOD
@app.route('/searchComics/', methods=['GET'])
def searchComics():
    url="https://gateway.marvel.com/v1/public/characters?orderBy=name&ts=1&apikey="+config('API_KEY')+"&hash="+config('HASH_KEY')
    r= requests.get(url)
    response = json.loads(r.text)
    character=[]
    try:
        for item in response['data']['results']:
            id= item['id']
            name= item['name']
            image = item['thumbnail']['path']+"."+item['thumbnail']['extension']
            appearances = item['comics']['available']
            character_json = {'id':id, 'name':name, 'image':image, 'appearances':appearances}
            character.append(character_json)

        return  json.dumps(character)
    except:
        return {"error": "No se encontraron resultados"}

if __name__ == '__main__':
    print('Starting server on port {}'.format(PORT))
    app.run(port=PORT)
