from setuptools import setup

setup(name="UV_convert",  #unique global name for package
      version = "0.1",
      description = "a small package to convert wind U/V itterables into Magnitude/Theta",
      author="Skye Leake",
      packages=["UV_convert"],  #the name of the folder containing .py file and the .py file
      install_requires=['numpy'],
      zip_safe=False)  #false - package cannot run directly from a .zip file
