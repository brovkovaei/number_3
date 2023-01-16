from flask import render_template, request, Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        line = request.form.get('str')
        new_line = ''

        for i in line:
            new_line += chr(ord(i) + 1)
        return render_template('index.html', res=new_line)

    return render_template('index.html', res=None)


if __name__ == "__main__":
    app.run(debug=True)