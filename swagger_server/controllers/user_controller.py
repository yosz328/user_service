import connexion
import six
import requests
import json
import socket
import os
 # noqa: E501
from swagger_server import util



def get_estimated(body):  # noqa: E501
    """obtener tiempo estimado

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    
    if connexion.request.is_json: 
        
        body = connexion.request.get_json()  # noqa: E501
        headers = {'Content-Type': 'application/json'}
        r = requests.post("http://52.168.132.142/get_latlon", data=json.dumps(body), headers=headers) #google
        data = requests.post("http://52.168.132.142/get_time", data=r, headers=headers) #uber
        
    return  data.json()
