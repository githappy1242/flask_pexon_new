from flask import Flask, request, jsonify

app = Flask(__name__)

movies_list = [
    {
        "id": 0,
        "author": "George Lucas",
        "language": "English",
        "title": "Star Wars",
    },
    {
        "id": 1,
        "author": "George Lucas",
        "language": "English",
        "title": "Star Wars 2",
    },
{
        "id": 2,
        "author": "George Lucas",
        "language": "English",
        "title": "Star Wars 3",
    }

]

@app.route('/')
def hello():

    return 'Hello Pexon'


@app.route('/movies', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(movies_list) > 0:
            return jsonify(movies_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = movies_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        movies_list.append(new_obj)
        return jsonify(movies_list), 201

@app.route('/movie/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_movie(id):
    if request.method == 'GET':
        for movie in movies_list:
            if movie['id'] == id:
                return jsonify(movie)
            pass
    if request.method == 'PUT':
        for movie in movies_list:
            if movie['id'] == id:
                movie['author'] = request.form['author']
                movie['language'] = request.form['language']
                movie['title'] = request.form['title']
                updated_movie = {
                    'id': id,
                    'author': movie['author'],
                    'language': movie['language'],
                    'title': movie['title']
                }
                return jsonify(updated_movie)

    if request.method == 'DELETE':
        for index, movie in enumerate(movies_list):
            if movie['id'] == id:
                movies_list.pop(index)
                return jsonify(movies_list)


if __name__ == '__main__':
    app.run()