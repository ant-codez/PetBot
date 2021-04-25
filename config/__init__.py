import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://fmlhlahbtfonwl:b39b8847a5036a2530975f1a366b7901178d3fcfe43d9679532af802010d1553@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d6ecpf8hf6sdte'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret'