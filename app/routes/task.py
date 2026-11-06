from flask import Blueprint, render_template, session, url_for, request, redirect, flash
from app import db
from app.models import Task

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def view_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='pending')
        db.session.add(new_task)
        db.session.commit()
        flash('task added successfully')

    return redirect(url_for('task.view_task'))

@task_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    task = Task.query.get_or_404(task_id)

    if task.status == 'pending':
        task.status = 'working'
    elif task.status == 'working':
        task.status = 'Done'
    else:
        task.status = 'pending'

    db.session.commit()
    return redirect(url_for('task.view_task'))

@task_bp.route('/clear', methods=['POST'])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('all tasks cleared !')
    return redirect(url_for('task.view_task'))