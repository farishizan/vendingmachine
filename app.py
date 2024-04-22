from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    balance = int(request.form['money'])
    drinks = request.form['drinks']
    notesArr = []
    if drinks == 'pepsi':
        balance = balance - 3
    elif drinks == 'coke':
        balance = balance - 4
    elif drinks == 'mountaindew':
        balance = balance - 2
    else:
        balance = balance - 4
    money = balance
    if balance > 50:
        note50 = balance // 50
        balance = balance % 50
        notesArr.append(['50',note50])

    if balance > 20:
        note20 = balance // 20
        balance = balance % 20
        notesArr.append(['20',note20])

    if balance > 10:
        note10 = balance // 10
        balance = balance % 10
        notesArr.append(['10',note10])
    
    if balance > 5:
        note5 = balance // 5
        balance = balance % 5
        notesArr.append(['5',note5])

    if balance > 1:
        note1 = balance // 1
        balance = 0
        notesArr.append(['1',note1])

    return render_template('submission.html', money=money, notesArr=notesArr)

if __name__ == '__main__':
    app.run(debug=True)
