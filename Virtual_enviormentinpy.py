## all the things appeared below are from terminal session
# this is the work should be done for making virtual environment and installing different versions of pandas in it 

Last login: Wed Oct 22 17:22:21 on ttys000
(base) admin@Admins-MacBook-Pro-2 ~ % cd Desktop
(base) admin@Admins-MacBook-Pro-2 Desktop % cd python
(base) admin@Admins-MacBook-Pro-2 python % cd python venv
cd: no such file or directory: /Users/admin/Desktop/venv
(base) admin@Admins-MacBook-Pro-2 python % cd 2
cd: no such file or directory: 2
(base) admin@Admins-MacBook-Pro-2 python % cd python-venv
(base) admin@Admins-MacBook-Pro-2 python-venv % python3 -m venv myenv
(base) admin@Admins-MacBook-Pro-2 python-venv % pip3 install pandas
Requirement already satisfied: pandas in /opt/anaconda3/lib/python3.11/site-packages (2.1.4)
Requirement already satisfied: numpy<2,>=1.23.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (1.26.4)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3.post1)
Requirement already satisfied: tzdata>=2022.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3)
Requirement already satisfied: six>=1.5 in /opt/anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
(base) admin@Admins-MacBook-Pro-2 python-venv % source myenv/bin/activate
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip3 install pandas
Collecting pandas
  Obtaining dependency information for pandas from https://files.pythonhosted.org/packages/c1/fa/7ac648108144a095b4fb6aa3de1954689f7af60a14cf25583f4960ecb878/pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl.metadata (91 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 1.5 MB/s eta 0:00:00
Collecting numpy>=1.23.2 (from pandas)
  Obtaining dependency information for numpy>=1.23.2 from https://files.pythonhosted.org/packages/60/e7/0e07379944aa8afb49a556a2b54587b828eb41dc9adc56fb7615b678ca53/numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 2.7 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2 (from pandas)
  Obtaining dependency information for python-dateutil>=2.8.2 from https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Obtaining dependency information for pytz>=2020.1 from https://files.pythonhosted.org/packages/81/c4/34e93fe5f5429d7570ec1fa436f1986fb1f00c3e0f43a589fe2bbcd22c3f/pytz-2025.2-py2.py3-none-any.whl.metadata
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Obtaining dependency information for tzdata>=2022.7 from https://files.pythonhosted.org/packages/5c/23/c7abc0ca0a1526a0774eca151daeb8de62ec457e77262b66b359c3c7679e/tzdata-2025.2-py2.py3-none-any.whl.metadata
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Obtaining dependency information for six>=1.5 from https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl.metadata
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 6.8 MB/s eta 0:00:00
Downloading numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl (21.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.3/21.3 MB 6.7 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 6.9 MB/s eta 0:00:00
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 8.6 MB/s eta 0:00:00
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 7.3 MB/s eta 0:00:00
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-2.3.4 pandas-2.3.3 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip3 install pandas==1.4.4
Collecting pandas==1.4.4
  Downloading pandas-1.4.4.tar.gz (4.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 9.4 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.21.0 in ./myenv/lib/python3.11/site-packages (from pandas==1.4.4) (2.3.4)
Requirement already satisfied: python-dateutil>=2.8.1 in ./myenv/lib/python3.11/site-packages (from pandas==1.4.4) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./myenv/lib/python3.11/site-packages (from pandas==1.4.4) (2025.2)
Requirement already satisfied: six>=1.5 in ./myenv/lib/python3.11/site-packages (from python-dateutil>=2.8.1->pandas==1.4.4) (1.17.0)
Building wheels for collected packages: pandas
  Building wheel for pandas (pyproject.toml) ... done
  Created wheel for pandas: filename=pandas-1.4.4-cp311-cp311-macosx_10_9_x86_64.whl size=10568873 sha256=e81db116e6928368a01b1996a1298aa2059b797119a23da05f0df547635500ab
  Stored in directory: /Users/admin/Library/Caches/pip/wheels/56/ff/8e/5497c17f51e61a95c9cf4c58914222f311ca968796ee52d430
Successfully built pandas
Installing collected packages: pandas
  Attempting uninstall: pandas
    Found existing installation: pandas 2.3.3
    Uninstalling pandas-2.3.3:
      Successfully uninstalled pandas-2.3.3
Successfully installed pandas-1.4.4

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % 
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/__init__.py", line 15, in <module>
    from pandas.compat.numpy import (
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/numpy/__init__.py", line 4, in <module>
    from pandas.util.version import Version
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/__init__.py", line 1, in <module>
    from pandas.util._decorators import (  # noqa:F401
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/_decorators.py", line 14, in <module>
    from pandas._libs.properties import cache_readonly  # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/_libs/__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
  File "pandas/_libs/interval.pyx", line 1, in init pandas._libs.interval
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
>>> pd.__version__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined. Did you mean: 'id'?
>>> import pandas as pd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/__init__.py", line 15, in <module>
    from pandas.compat.numpy import (
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/numpy/__init__.py", line 4, in <module>
    from pandas.util.version import Version
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/__init__.py", line 1, in <module>
    from pandas.util._decorators import (  # noqa:F401
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/_decorators.py", line 14, in <module>
    from pandas._libs.properties import cache_readonly  # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/_libs/__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
  File "pandas/_libs/interval.pyx", line 1, in init pandas._libs.interval
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
>>> import pandas as id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/__init__.py", line 15, in <module>
    from pandas.compat.numpy import (
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/compat/numpy/__init__.py", line 4, in <module>
    from pandas.util.version import Version
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/__init__.py", line 1, in <module>
    from pandas.util._decorators import (  # noqa:F401
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/util/_decorators.py", line 14, in <module>
    from pandas._libs.properties import cache_readonly  # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/admin/Desktop/python/python-venv/myenv/lib/python3.11/site-packages/pandas/_libs/__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
  File "pandas/_libs/interval.pyx", line 1, in init pandas._libs.interval
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
>>> exit()
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % deactivate 
(base) admin@Admins-MacBook-Pro-2 python-venv % python3 
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> pd.__version__
'2.1.4'
>>> exit()
(base) admin@Admins-MacBook-Pro-2 python-venv % python3 -m venv pandas1-5
(base) admin@Admins-MacBook-Pro-2 python-venv % source pandas1-5/bin/activate
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % python3
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install pandas
Collecting pandas
  Obtaining dependency information for pandas from https://files.pythonhosted.org/packages/c1/fa/7ac648108144a095b4fb6aa3de1954689f7af60a14cf25583f4960ecb878/pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Using cached pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl.metadata (91 kB)
Collecting numpy>=1.23.2 (from pandas)
  Obtaining dependency information for numpy>=1.23.2 from https://files.pythonhosted.org/packages/60/e7/0e07379944aa8afb49a556a2b54587b828eb41dc9adc56fb7615b678ca53/numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Using cached numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl.metadata (62 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Obtaining dependency information for python-dateutil>=2.8.2 from https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Obtaining dependency information for pytz>=2020.1 from https://files.pythonhosted.org/packages/81/c4/34e93fe5f5429d7570ec1fa436f1986fb1f00c3e0f43a589fe2bbcd22c3f/pytz-2025.2-py2.py3-none-any.whl.metadata
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Obtaining dependency information for tzdata>=2022.7 from https://files.pythonhosted.org/packages/5c/23/c7abc0ca0a1526a0774eca151daeb8de62ec457e77262b66b359c3c7679e/tzdata-2025.2-py2.py3-none-any.whl.metadata
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Obtaining dependency information for six>=1.5 from https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl.metadata
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Using cached pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl (11.6 MB)
Using cached numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl (21.3 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-2.3.4 pandas-2.3.3 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install pandas==1.5
Collecting pandas==1.5
  Obtaining dependency information for pandas==1.5 from https://files.pythonhosted.org/packages/86/56/1166f3d36fda4e16f4d7296207fae1fa5c01352b32e9c480e1ed360b180e/pandas-1.5.0-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading pandas-1.5.0-cp311-cp311-macosx_10_9_x86_64.whl.metadata (11 kB)
Requirement already satisfied: python-dateutil>=2.8.1 in ./pandas1-5/lib/python3.11/site-packages (from pandas==1.5) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./pandas1-5/lib/python3.11/site-packages (from pandas==1.5) (2025.2)
Requirement already satisfied: numpy>=1.21.0 in ./pandas1-5/lib/python3.11/site-packages (from pandas==1.5) (2.3.4)
Requirement already satisfied: six>=1.5 in ./pandas1-5/lib/python3.11/site-packages (from python-dateutil>=2.8.1->pandas==1.5) (1.17.0)
Downloading pandas-1.5.0-cp311-cp311-macosx_10_9_x86_64.whl (11.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.9/11.9 MB 1.5 MB/s eta 0:00:00
Installing collected packages: pandas
  Attempting uninstall: pandas
    Found existing installation: pandas 2.3.3
    Uninstalling pandas-2.3.3:
      Successfully uninstalled pandas-2.3.3
Successfully installed pandas-1.5.0

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev  # pyright: ignore # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/compat/__init__.py", line 18, in <module>
    from pandas.compat.numpy import (
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/compat/numpy/__init__.py", line 4, in <module>
    from pandas.util.version import Version
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/util/__init__.py", line 2, in <module>
    from pandas.util._decorators import (  # noqa:F401
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/util/_decorators.py", line 14, in <module>
    from pandas._libs.properties import cache_readonly
  File "/Users/admin/Desktop/python/python-venv/pandas1-5/lib/python3.11/site-packages/pandas/_libs/__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
  File "pandas/_libs/interval.pyx", line 1, in init pandas._libs.interval
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
>>> pd.__version__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined. Did you mean: 'id'?
>>> yes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yes' is not defined
>>> exit()
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % deactivate
(base) admin@Admins-MacBook-Pro-2 python-venv % python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> __version__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '__version__' is not defined
>>> pd.__version__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined. Did you mean: 'id'?
>>> import pandas as pd
>>> pd.__version__
'2.1.4'
>>> exit()
(base) admin@Admins-MacBook-Pro-2 python-venv % source myenv/bin/activate
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % deactivate
(base) admin@Admins-MacBook-Pro-2 python-venv % source pandas1-5/bin/activate
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % touch main.py
(pandas1-5) (base) admin@Admins-MacBook-Pro-2 python-venv % deactivate
(base) admin@Admins-MacBook-Pro-2 python-venv % python main.py
2.1.4
(base) admin@Admins-MacBook-Pro-2 python-venv % python3 main.py
2.1.4
(base) admin@Admins-MacBook-Pro-2 python-venv % source myenv/bin/activate
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % main.py
zsh: command not found: main.py
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install dateutils
Collecting dateutils
  Obtaining dependency information for dateutils from https://files.pythonhosted.org/packages/1e/23/cbac954194e5132448cfec0148be1318baac99e68ed597b3d7ff4ae5c182/dateutils-0.6.12-py2.py3-none-any.whl.metadata
  Downloading dateutils-0.6.12-py2.py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: python-dateutil in ./myenv/lib/python3.11/site-packages (from dateutils) (2.9.0.post0)
Requirement already satisfied: pytz in ./myenv/lib/python3.11/site-packages (from dateutils) (2025.2)
Requirement already satisfied: six>=1.5 in ./myenv/lib/python3.11/site-packages (from python-dateutil->dateutils) (1.17.0)
Downloading dateutils-0.6.12-py2.py3-none-any.whl (5.7 kB)
Installing collected packages: dateutils
Successfully installed dateutils-0.6.12

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install lxml
Collecting lxml
  Obtaining dependency information for lxml from https://files.pythonhosted.org/packages/28/66/1ced58f12e804644426b85d0bb8a4478ca77bc1761455da310505f1a3526/lxml-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading lxml-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl.metadata (3.6 kB)
Downloading lxml-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 8.9 MB/s eta 0:00:00
Installing collected packages: lxml
Successfully installed lxml-6.0.2

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install pyopenxl
ERROR: Could not find a version that satisfies the requirement pyopenxl (from versions: none)
ERROR: No matching distribution found for pyopenxl

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install openxl
ERROR: Could not find a version that satisfies the requirement openxl (from versions: none)
ERROR: No matching distribution found for openxl

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip install openpyxl
Collecting openpyxl
  Obtaining dependency information for openpyxl from https://files.pythonhosted.org/packages/c0/da/977ded879c29cbd04de313843e76868e6e13408a94ed6b987245dc7c8506/openpyxl-3.1.5-py2.py3-none-any.whl.metadata
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting et-xmlfile (from openpyxl)
  Obtaining dependency information for et-xmlfile from https://files.pythonhosted.org/packages/c1/8b/5fe2cc11fee489817272089c4203e679c63b570a5aaeb18d852ae3cbba6a/et_xmlfile-2.0.0-py3-none-any.whl.metadata
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.9/250.9 kB 2.7 MB/s eta 0:00:00
Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-2.0.0 openpyxl-3.1.5

[notice] A new release of pip is available: 23.2.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip freeze > requirements.txt
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip freeze
dateutils==0.6.12
et_xmlfile==2.0.0
lxml==6.0.2
numpy==2.3.4
openpyxl==3.1.5
pandas==1.4.4
python-dateutil==2.9.0.post0
pytz==2025.2
six==1.17.0
tzdata==2025.2
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % pip freeze > requirements.txt
(myenv) (base) admin@Admins-MacBook-Pro-2 python-venv % 
