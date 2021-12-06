# Envirnment Setup

I have already install anaconda. Created python36 environmnt, installed gdal and everything. And was able to use GDAL from my notebook

# VSCode Configuraton

Selected the python interpreter as "python36" - which configured the settings json as

```
"python.pythonPath": "/Users/rajanp/opt/anaconda3/envs/python36/bin/python"
```

After this whenver I opened the terminal python36 env is activated by default.

```
#Logs

source /Users/rajanp/opt/anaconda3/bin/activate
(base) rajanp@rajanps-MBP docs % source /Users/rajanp/opt/anaconda3/bin/activate
(base) rajanp@rajanps-MBP docs % conda activate python36
(python36) rajanp@rajanps-MBP docs % 
```

### But I cannot refer gdal

```
(python36) rajanp@rajanps-MBP docs % python3
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import gdal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'gdal'
>>> ^D
(python36) rajanp@rajanps-MBP docs % 
```

On inspection, looks like python36 is not included in the path

```
(base) rajanp@rajanps-MBP abd % python3 -m site
sys.path = [
    '/Users/rajanp/work/abd',
    '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
    '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
    '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
    '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages',
]
USER_BASE: '/Users/rajanp/Library/Python/3.8' (doesn't exist)
USER_SITE: '/Users/rajanp/Library/Python/3.8/lib/python/site-packages' (doesn't exist)
ENABLE_USER_SITE: True
(base) rajanp@rajanps-MBP abd % 
```

Whereas referring the actual python path worked

```
(base) rajanp@rajanps-MBP abd % /Users/rajanp/opt/anaconda3/envs/python36/bin/python main.py
Hello
(base) rajanp@rajanps-MBP abd %
```

Suspected PATH & CONDA_ROOT ENv var

Conda Info returned correct values.

```
(python36) rajanp@rajanps-MBP docs % conda info

     active environment : python36
    active env location : /Users/rajanp/opt/anaconda3/envs/python36
            shell level : 2
       user config file : /Users/rajanp/.condarc
 populated config files : /Users/rajanp/.condarc
          conda version : 4.9.2
    conda-build version : 3.20.5
         python version : 3.8.5.final.0
       virtual packages : __osx=10.15.6=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /Users/rajanp/opt/anaconda3  (writable)
           channel URLs : https://conda.anaconda.org/conda-forge/osx-64
                          https://conda.anaconda.org/conda-forge/noarch
                          https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /Users/rajanp/opt/anaconda3/pkgs
                          /Users/rajanp/.conda/pkgs
       envs directories : /Users/rajanp/opt/anaconda3/envs
                          /Users/rajanp/.conda/envs
               platform : osx-64
             user-agent : conda/4.9.2 requests/2.24.0 CPython/3.8.5 Darwin/19.6.0 OSX/10.15.6
                UID:GID : 501:20
             netrc file : None
           offline mode : False

(python36) rajanp@rajanps-MBP docs % 
```
### Finally
set this in the settings json
"terminal.integrated.inheritEnv": false

# Use conda
```
# This step is not necessary - but its needed at the moment - Need to fix
# https://code.visualstudio.com/docs/editor/integrated-terminal#_why-are-there-duplicate-paths-in-the-terminals-path-environment-variable-andor-why-are-they-reversed


conda activate python36
```

# Install packages in the python36 env
conda install --name python36 pylint -y