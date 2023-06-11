# Flask-Store
This is a flask project for stores with items that has users engaging with them.

Users can register and then log in. By logging in they will get a JWT (JSON Web Token) to call APIs.

Only APIs with methods other than `GET` require these tokens.

# Demo
[![Watch on Youtube]([](https://img.youtube.com/vi/vt5fpE0bzSY/maxresdefault.jpg))](https://youtu.be/Ge1iNhwLefA)

# Setup
- Open your terminal
- Clone the project by:
  ```
    git clone https://github.com/sananqsh/Flask-Store.git
  ```
- Change directory to the project:
  ```
    cd Flask-Store/
  ```
- Have a [python](https://www.python.org/downloads/) version of `3.x`
- Create a virtual environment (Optional):
    ```
      virtualenv venv # if you don't have `virtualenv` run `pip install virtualenv`
    ```
    Activate the virtual environment:
    ```
    source venv/bin/activate` # your terminal prompt probably should include the name of the venv, if done correctly
    ```
    > You can exit the virtual environment anytime by `deactivate`

- Install the requirements by [`pip`](https://pip.pypa.io/en/stable/installation):
  ```
    pip install -r code/requirements.txt
  ```
- Change directory to `/code`:
  ```
    cd code/
  ```
- Run the app: `python3 app.py` (you might use a different python version so the running command might differ a bit. e.g `python app.py`)
> If you get an error similar to this after running the app:
> ```
> Traceback (most recent call last):                                                                                                                                                                         
>  File "/path-to/Flask-Store/code/app.py", line 3, in <module>                                                                                                                      
>    from flask_jwt import JWT                                                                                                                                                                              
>  File "/path-to/Flask-Store/venv/lib/python3.10/site-packages/flask_jwt/__init__.py", line 16, in <module>                                                                         
>    import jwt                                                                                                                                                                                             
>  File "/path-to/Flask-Store/venv/lib/python3.10/site-packages/jwt/__init__.py", line 19, in <module>                                                                               
>    from .api_jwt import (                                                                                                                                                                                 
>  File "/path-to/Flask-Store/venv/lib/python3.10/site-packages/jwt/api_jwt.py", line 5, in <module>                                                                                 
>    from collections import Mapping
> ImportError: cannot import name 'Mapping' from 'collections' (/usr/lib/python3.10/collections/__init__.py)
> ```  
> It's because of the incompability of your python with the libraries; the same problem that I encountered.
> This is fixable by using the patch files I wrote.
> 1. Take a look at the patch files, I wrote them for my python version: 3.10. If you have a different python version, modify the file.
> 2. In the `code/` directory, run patch:
>   ```
>     patch ../venv/lib/python3.10/site-packages/jwt/api_jwt.py < patches/api_jwt.patch
>   ```
>   ```
>     patch ../venv/lib/python3.10/site-packages/jwt/api_jws.py < patches/api_jws.patch
>   ```
> The app should work fine now. If any other error came along, let me know!
>
> Also, I tried to dockerize the project but after running its image, I had trouble calling the APIs! Checkout to `dockerize` branch and see if you can help with the issue.
