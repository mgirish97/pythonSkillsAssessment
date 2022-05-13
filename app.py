from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data/patient_tb.csv')
no_dupl_df = df.drop_duplicates(subset=['PatientID', 'MostRecentTestDate', 'TestName'])


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/search_data', methods=['GET', 'POST'])
def get_data():
    name = request.form['patient']
    name = name.title()
    input_name_df = no_dupl_df[no_dupl_df['PatientFirstName'] == name]
    df_dict = input_name_df.to_dict('records')
    return render_template('search.html', df_dict=df_dict)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
