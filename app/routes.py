from app import Flask, render_template, request, url_for, redirect,flash, server, session, jsonify
from flask_login import logout_user
import requests, json
from datetime import timedelta

@server.route('/', methods=['GET', 'POST'])
def index():
    return render_template('landing.html')