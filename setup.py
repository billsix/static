from setuptools import setup, Extension


setup (name = 'static',
       version = '0.0.1',
       description = 'An implementation of static local variables, as familiar from C',
       author = 'William Emerison Six',
       author_email = 'billsix@gmail.com',
       url = 'https://github.com/billsix/static',
       keywords = "static",
       license = "MIT",
       packages=['static'],
       package_dir={'static': 'src/static'},
       classifiers=[
           "Development Status :: 3 - Alpha",
           "Topic :: Utilities",
           "License :: OSI Approved :: MIT License",
       ],
       long_description = '''
Static local variables are variables local to a function, which upon
first application, assign a value to the variable.  The value bound
by the variable persists after the function application completes,
so the state is preserved across muliple applications of the function.
''')
