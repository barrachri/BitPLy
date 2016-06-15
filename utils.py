import os

def get_env(name, default=None):
    '''Helper to generate a bool var from env'''
    env = os.getenv(name, default)
    if env == "True":
        env = True
    if env == "False":
        env = False
    return env
