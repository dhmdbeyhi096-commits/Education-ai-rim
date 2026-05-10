from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
subjects = ["Math", "Science", "History"]
resources = {
    "Math": ["Algebra Basics", "Calculus 101"],
    "Science": ["Physics for Beginners", "Chemistry Fundamentals"],
    "History": ["World History Overview", "Ancient Civilizations"]
}

@app.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify(subjects)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question', '')
    if question:
        # Here, you would process the question and return an answer
        return jsonify({"response": f"Received your question: {question}"}), 200
    return jsonify({"error": "Question is required!"}), 400

@app.route('/resources/<subject>', methods=['GET'])
def get_resources(subject):
    if subject in resources:
        return jsonify(resources[subject])
    return jsonify({"error": "Subject not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)