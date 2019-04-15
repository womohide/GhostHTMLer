import os

__name__ == "__main__":

def getcurrentlist():
    pathlist=os.listdir(os.path.dirname(os.path.abspath(__file__)))
    return pathlist