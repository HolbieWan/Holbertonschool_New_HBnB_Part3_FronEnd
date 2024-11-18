"""
Front-End Controller Module

This module defines routes for rendering HTML templates associated with 
the front-end of the application. It provides endpoints for serving various 
pages such as the home page, place details, login page, and the add review page.

Blueprints:
    home_bp (Blueprint): A Flask blueprint for front-end related routes.

Routes:
    /HBnB: Renders the main home page.
    /place: Renders the place details page.
    /login: Renders the login page.
    /add_review: Renders the add review page.
"""

from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    """
    Renders the main home page.

    Returns:
        Response: The HTML content of the home page.
    """
    return render_template('index.html')

@home_bp.route('/place')
def home_place():
    """
    Renders the place details page.

    Returns:
        Response: The HTML content of the place details page.
    """
    return render_template('place.html')

@home_bp.route('/login')
def home_login():
    """
    Renders the login page.

    Returns:
        Response: The HTML content of the login page.
    """
    return render_template('login.html')

@home_bp.route('/logout')
def home_logout():
    """
    Renders the add review page.

    Returns:
        Response: The HTML content of the add review page.
    """
    return render_template('logout.html')