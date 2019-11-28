from flask import Flask, render_template, request, url_for, redirect,flash, session,jsonify
import requests
import json
server = Flask(__name__)

from app.routes import *    