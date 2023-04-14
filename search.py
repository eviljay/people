from flask import Flask, request

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # do something with the search query
    return 'Search results'

if __name__ == '__main__':
    app.run()
