from flask import Flask, render_template

app = Flask(__name__)

from mail import views
from mail import admin_view