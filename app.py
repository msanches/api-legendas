from flask import Flask, jsonify #, render_template
import series

app = Flask(__name__)

@app.route('/')
def home():
  html = '<h1>Página inicial</h1>'
  html += '<ul>'
  html += '<li><a href= "../categoria/serie/1">Para buscar series<a></li>'
  html += '<li><a href= "../categoria/filmes/1">Para buscar filmes<a></li>'
  html += '<li><a href= "../buscar/ncis/1">Para por uma legenda específica<a></li>'
  return html
  
@app.route('/buscar/<serie>/<page>')
def search(serie, page):
  dados = series.buscar(serie, page)
  
  response = jsonify(dados)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/categoria/<categoria>/<page>')
def api(categoria, page):
    dados = series.scraping(categoria, page)

    response = jsonify(dados)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  
@app.route('/legenda/<nome>')
def legenda(nome):
  dados = series.buscaLegenda(nome) 

  response = jsonify(dados)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

if __name__ == '__main__':
    #app.run(debug=False)
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)