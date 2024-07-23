from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data['name']
    dob = data['dob']
    cutoff = data['cutoff']
    location = data['location']
    interest = data['interest']

    # Example guidance logic
    message = f"Hello {name}, based on your interest in {interest}, here are some suggestions:"

    if interest.lower() == "engineering":
        message += " Consider applying to IITs, NITs, and state engineering colleges. Prepare for exams like JEE Main and Advanced."
    elif interest.lower() == "medicine":
        message += " Consider applying to medical colleges like AIIMS, and prepare for exams like NEET."
    else:
        message += " Explore courses and colleges related to your interest area. Research the scope and entrance exams accordingly."

    return jsonify(name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
