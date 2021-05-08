import random
from flask import Flask, request, session
E = ('able', 'carpenter', 'damage', 'forever', 'helmet', 'mountain', 'record', 'total')
M = ('activity', 'calendar', 'currency', 'famous', 'industry', 'mention', 'picture', 'reduce', 'televise', 'wrist')
H= ['achieve', 'calculator', 'exasperating', 'leather', 'propel', 'territory']

app = Flask(__name__)
app.config["SECREt_KEY"] = "akljsghakljsehakljslaksjhdfalksedf"

@app.route("/", methods=["POST", "GET"])
def hangMan():
    if "guesses" not in session:
        session["guesses"] = []
    if request.method == "GET":
        return '''
            <html>
                <body>
                    <form method="post" action=".">
                        <p>Choose Difficulty:</p>
                        <input type="radio" id="easy" name="difficulty" value="easy">
                        <label for="easy">Easy</label><br>
                        <input type="radio" id="medium" name="difficulty" value="medium">
                        <label for="medium">Medium</label><br>
                        <input type="radio" id="hard" name="difficulty" value="hard">
                        <label for="hard">Hard</label><br>
                    </form>
                </body>
            </html>
        '''
    if "word" not in session:
        session["word"] = ''
    if request.form == "easy":
        bank = E
    elif request.form == "medium":
        bank = M
    else:
        bank = H
    if "setup" not in session:
        session["word"] = bank[random.randint(0,len(bank))]
        length = len(session['word'])
        session["setup"] = True
    if "answer" not in session:
        session['answers'] = []
        for x in range(0, length):
            session['answers'].append('_')

    if "r" not in session:
        session["r"] = 5
    if "output" not in session:
        session['output'] = ''
    errors = ''
    if request.form["action"] == "Submit Letter":
        if len(request.form["letter"]) != 1 and request.form["letter"] != session["word"]:
            errors += "Please only enter 1 letter at a time\n"
        if not request.form['letter'].isalpha():
            errors += "Please enter letters only\n"
        if request.form['letter'] in session["guesses"]:
            errors += "You have already guessed {!r}\n".format(request.form["letter"])
        if (len(request.form['letter']) == 1 or request.form['letter'] == session['word']) and request.form['letter'].isalpha() and request.form['letter'] not in session['guesses']:
            session["guesses"].append(request.form['letter'])
            if request.form['letter'] in session['word']:
                for x in session['word']:
                    index = session['word'].index(x)
                    session['answers'][index] = request.form['letter']
                if '_' not in session['answers']:
                    return '''
                        <html>
                            <body>
                                <p>Letters guessed: {letters}</p>
                                <p>Word: {answers}</p>
                                <p>'''
                print(f"{' '.join(session['answers'])} Good job!")
            elif request.form['letter'] not in session['word']:
                session['r'] = session['r'] - 1
                if session['r'] > 0:
                    session['r'] = 0
                print(f"{' '.join(session['answers'])} Good try.")
    while session['r'] != 0:
        return '''
            <html>
                <body>
                    <p>{errors}</p}
                    <p>Word: {answers}</p>
                    <p>Letters guessed: {guesses}</p>
                    <p>Attempt(s) remaining: {r}</p>
                    <p>Enter a letter:</p>
                    <form method="post" action=".">
                        <p><input name="letter" /></p>
                        <p><input type="submit" name="action" value="Submit Letter" /></p>
                    </form>
                </body>
            </html>
        '''.format(errors=errors, answers=' '.join(session['answers']), guesses=session['guesses'], r=session['r'])
