'''
check module exits, 
if not install 
'''

def checkPythonmod(mod):
    try:
        op = find_module(mod)
        return([mod, True])
    except ImportError:
        pip.main(['install', mod])
        
  
