import os


def splitEnvPath(envVar: str):
    user_paths = []
    try:
        user_paths = os.environ[envVar].split(os.pathsep)
    except KeyError:
        user_paths = []
    return user_paths


def splitPythonPath():
    return splitEnvPath("PYTHONPATH")
