from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

@app.route('/hill_stations')
def hill_stations():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redirect to login if not logged in

    data = [
        {'name': 'Shimla', 'state': 'Himachal Pradesh', 'description': 'Known for its colonial architecture and scenic views.'},
        {'name': 'Manali', 'state': 'Himachal Pradesh', 'description': 'Famous for its beautiful landscapes and adventure sports.'},
        {'name': 'Nainital', 'state': 'Uttarakhand', 'description': 'A popular hill station known for its lake.'},
    ]
    
    return render_template('hill_stations.html', stations=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically validate the credentials
        if username == 'admin' and password == 'password':  # Replace with your logic
            session['logged_in'] = True
            return redirect(url_for('hill_stations'))
    return render_template('login.html')  # Render the login page

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
