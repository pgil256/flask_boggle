from boggle import Boggle
from flask import Flask, session, render_template, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'asdhgf'

boggle_game = Boggle()

@app.route('/'):
def start():
    '''Shows page at start'''

    game_board = boggle_game.make_board()
    session[board] = board

    return render_template('index.html', board = board)

@app.route('/test-word')
def test_word():
    '''Test if word exists'''

    word = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board,word)

    return jsonify({'result': response})

@app.route('/post-score')
def post_score():
    '''Recieve score and update'''

    score = request.json['score']

    return jsonify({'score': score})