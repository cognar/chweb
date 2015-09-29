from flask import render_template, url_for
from app import app
from random import randrange
from datetime import date

backgroundTemplates = (	(url_for('.static', filename='images/2.jpg'), 'DAC9C8', 'D3D599'),
						('/static/images/3.jpg', 'DFE3B9', 'D2D1CD'),
						('/static/images/4.jpg', 'B3AEDE', 'D5A48E'),
						('/static/images/5.jpg', 'A4A1A4', 'FEFEF1'),
						('/static/images/6.jpg', 'B59DA6', '94ABA1'),
						('/static/images/7.jpg', 'CAC5C6', 'D7D2D2'),
						('/static/images/8.jpg', 'C5939C', 'AAA79D'))

@app.route('/')
@app.route('/index')
def index():
    bgTemp = backgroundTemplates[randrange(0,len(backgroundTemplates))]
    bgTemp = backgroundTemplates[0]
    return render_template('index.html',
							title = 'Home',
							bgImageUrl = bgTemp[0],
							bgColor = bgTemp[1],
							fColor = bgTemp[2],
							year = date.today().year)

@app.route('/plants')
def plants():
    bgTemp = backgroundTemplates[randrange(0,len(backgroundTemplates))]
    return render_template('plants.html',
							title = 'Plants',
							bgImageUrl = bgTemp[0],
							bgColor = bgTemp[1],
							fColor = bgTemp[2],
							year = date.today().year)
