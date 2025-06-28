from flask import Flask, render_template, redirect, request

app = Flask(__name__)

tasks = {}

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks )

@app.route('/add-task', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        tasks[name] = 'u'
        
        return redirect('/')
    return render_template('/add-task.html')
    
@app.route('/change/<name>')
def change(name):
    if tasks[name] == 'u':
        tasks[name] = 'f'
    else:
        tasks[name] = 'u'
    return redirect('/')
    
@app.route('/edit/<name>', methods = ['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        new_name = request.form['name']
        
        if tasks[name] == 'u':
            tasks[new_name] = 'u'
        else:
            tasks[new_name] ='f'
            
        tasks.pop(name)
        
        return redirect('/')
    return render_template('edit-task.html', name = name)
    
@app.route('/delete/<name>')
def remove(name):
    tasks.pop(name, None)
    
    return redirect('/')
    
     

if __name__ == '__main__':
	app.run(debug = True, port = 5001)