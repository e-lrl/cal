from flask import render_template, session, redirect, url_for

from . import main_bp


@main_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('main/index.html')
