from flask import Flask, request, url_for, redirect, render_template

@app.route('/', method=['GET', 'POST'])
def index():
    
