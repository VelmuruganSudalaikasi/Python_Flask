from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# In-memory storage for students
students = [
    {"id": str(uuid.uuid4()), "name": "John Doe", "age": 20, "grade": "A"},
    {"id": str(uuid.uuid4()), "name": "Jane Smith", "age": 21, "grade": "B"},
]

@app.route('/')
def list_students():
    search = request.args.get('search')
    filtered_students=[]
    if search:
        for student in students:
            if search.lower() in student['name'].lower():
                filtered_students.append(student)
    else:
        filtered_students = students
    return render_template('list.html', students=filtered_students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        new_student = {
            "id": str(uuid.uuid4()),
            "name": request.form['name'],
            "age": int(request.form['age']),
            "grade": request.form['grade']
        }
        students.append(new_student)
        flash('Student added successfully!', 'success')
        return redirect(url_for('list_students'))
    return render_template('add.html')

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student is None:
        flash('Student not found!', 'error')
        return redirect(url_for('list_students'))
    
    if request.method == 'POST':
        student['name'] = request.form['name']
        student['age'] = int(request.form['age'])
        student['grade'] = request.form['grade']
        flash('Student updated successfully!', 'success')
        return redirect(url_for('list_students'))
    return render_template('edit.html', student=student)

@app.route('/delete/<string:id>')
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('list_students'))


if __name__ == '__main__':
    app.run(debug=True)





































































































































































































