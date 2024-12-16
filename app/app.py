from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas de ejemplo
tasks = [
    {
        'id': 1,
        'title': 'Ejemplo de Tarea 1',
        'description': 'Esto es una tarea de ejemplo.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Ejemplo de Tarea 2',
        'description': 'Otra tarea de ejemplo.',
        'done': True
    }
]

# Ruta principal (mostrar tareas)
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Ruta para agregar una nueva tarea (POST)
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if title and description:
        new_task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'done': False
        }
        tasks.append(new_task)
    
    return redirect(url_for('index'))

# Ruta para marcar tarea como completada (POST)
@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task:
        task['done'] = True
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

