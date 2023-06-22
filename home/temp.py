import os

imgs = os.listdir('static/img/caro')

print("{% static 'img/caro/"+ imgs[0] +"' %}")