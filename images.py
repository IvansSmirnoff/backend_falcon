import falcon
import matplotlib.pyplot as plt
import msgpack
import pandas as pd

import os
import time
import uuid

def _ext_to_media_type(ext):
    return 'image/' + ext

class Resource(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        
        #taking x, y from params. Can be complicated:
        x = int(req.params['xaxis'])
        x2 = int(req.params['x2axis'])
        y= int(req.params['yaxis'])
        y2= int(req.params['y2axis'])

        x= [x, x2]

        y = [y, y2]

        #Not needed, but can be used if the input is not that simple
        #x= pd.Series(x1,x2)
        #y=pd.Series(y1,y2)

        #plotting and saving to the project folder. Repository can be changed:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        name ='my_plot.png'
        fig.savefig('my_plot.png')


        ext = os.path.splitext(name)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        #For the repository to be optional
        image_path = os.path.join(self.storage_path, name)
        
        #Opening the file as response
        resp.stream = open(image_path, 'rb')
        resp.stream_len = os.path.getsize(image_path)
