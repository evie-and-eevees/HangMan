import random
from flask import Flask, request, session
E = ['able', 'carpenter', 'damage', 'forever', 'helmet', 'mountain', 'record', 'total']
M = ['activity', 'calendar', 'currency', 'famous', 'industry', 'mention', 'picture', 'reduce', 'televise', 'wrist']
H = ['achieve', 'calculator', 'exasperating', 'leather', 'propel', 'territory']

app = Flask(__name__)
app.config["SECRET_KEY"] = "akljsghakljsehakljslaksjhdfalksedf"
app.config['DEBUG'] = True

@app.route("/", methods=["POST", "GET"])
def hangMan():
    finish = ''
    message = ''
    if "guesses" not in session:
        session["guesses"] = []
    if request.method == "GET":
        session.clear()
        return '''
            <html>
                <body>
                    <form method="POST" action=".">
                        <p>Choose Difficulty:</p>
                        <input type="radio" id="easy" name="easy" value="difficulty">
                        <label for="easy">Easy</label><br>
                        <input type="radio" id="medium" name="medium" value="difficulty">
                        <label for="medium">Medium</label><br>
                        <input type="radio" id="hard" name="hard" value="difficulty">
                        <label for="hard">Hard</label><br>
                        <input type="submit">
                    </form>
                </body>
            </html>
        '''
    if "word" not in session:
        session["word"] = ''
    if 'easy' in request.form:
        bank = E
    elif 'medium' in request.form:
        bank = M
    else:
        bank = H
    if "setup" not in session:
        session["word"] = bank[random.randint(0,len(bank)-1)]
        session["setup"] = True
    length = len(session['word'])
    if "answers" not in session:
        session["answers"] = []
        for x in range(0, length):
            session['answers'].append('_')
    if "r" not in session:
        session["r"] = 5
    if "output" not in session:
        session['output'] = ''
    if "Keep Going" in request.form:
        session['r'] = -1
    if "Stop" in request.form:
        session['r'] = -2
        finish = 'n'
    errors = ''
    if "letter" in request.form and session['r'] != 0:
        if len(request.form["letter"]) != 1 and request.form["letter"].lower() != session["word"]:
            errors += "<p>Please only enter 1 letter at a time</p>"
        elif not request.form['letter'].isalpha():
            errors += "<p>Please enter letters only</p>"
        elif request.form['letter'] in session["guesses"]:
            errors += "<p>You have already guessed {!r}</p>".format(request.form["letter"])
        else:
            letter = str(request.form['letter']).lower()
            session["guesses"].append(letter)
            if letter in session['word']:
                i = 0
                for x in session['word']:
                    if x == letter:
                        session['answers'][i] = letter
                    i += 1
                if ('_' not in session['answers'] or letter == session['word']) and session['r'] > 0:
                    return '''
                        <html>
                            <body>
                                <p>Letters guessed: {letters}</p>
                                <p>Word: {answers}</p>
                                <p>You win! Play again?</p>
                                <form method="GET" action="/">
                                    <button type="submit">Click here to play again!</button>
                                </form>
                            </body>
                        </html>
                    '''.format(letters=session['guesses'], answers=(''.join(session['answers'])))
                if session['r'] < 0 and ('_' not in session['answers'] or letter == session['word']):
                    finish = 'n'
                message += "Good Guess!\n"
            elif letter not in session['word']:
                session['r'] = session['r'] - 1
                if session['r'] < 0:
                    session['r'] = -1
                message += "Good try\n"
    if session['r'] != 0 and finish != 'n':
        session['answers'] = session['answers']
        return '''
            <html>
                <body>
                    {errors}
                    <p>Word: {answers}</p>
                    <p>Letters guessed: {guesses}</p>
                    <p>{message}</p>
                    <p>Attempt(s) remaining: {r}</p>
                    <p>Enter a letter:</p>
                    <form method="POST" action=".">
                        <p><input name="letter" /></p>
                        <p><input type="submit" name="action" value="Submit Letter" /></p>
                    </form>
                </body>
            </html>
        '''.format(errors=errors, answers=(' '.join(session['answers'])), guesses=session['guesses'], r=session['r'], message=message, word=session['word'])
    if session['r'] == 0:
        return '''
            <html>
                <body>
                    {errors}
                    <p>Word: {answers}</p>
                    <p>Letters guessed: {guesses}</p>
                    <p>{message}</p>
                    <p>Attempt(s) remaining: {r}</p>
                    <p>You lost! Would you like to keep playing?</p>
                    <form method="POST" action=".">
                        <p><input type="submit" id="Keep Going" name="Keep Going" value="Keep Going" /></p>
                        <p><input type="submit" id="Stop" name="Stop" value="Stop" /></p>
                    </form>
                </body>
            </html>
        '''.format(errors=errors, answers=' '.join(session['answers']), guesses=session['guesses'], r=session['r'], message=message)
    if finish == 'n':
        return '''
            <html>
                <body>
                    {errors}
                    <p>Word: {answers}</p>
                    <p>Letters guessed: {guesses}</p>
                    <p>{message}</p>
                    <p>Game over</p>
                    <form method="GET" action="/">
                        <button type="submit">Click here to play again!</button>
                    </form>
                </body>
            </html>
        '''.format(errors=errors, answers=' '.join(session['answers']), guesses=session['guesses'], message=message)
