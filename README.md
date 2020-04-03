# Purpose
The purpose of this is to:
  A) Give me a project to work on
  B) Provide a simple static site generator using python
# Installation
Currently I do not have a PyPI package setup BUT you can install it from the following commands
`git clone https://github.com/RhinoCodes/Ebuilder-Ultra.git`
`cd Ebuilder-Ultra && pip install setup.py`
* Note: I am not a pro at packaging stuff so be aware that the following commands may not work. 
   | If so feel free to start a Pull Request
 # Simple Usage
 This is only a SIMPLE example for more tutorials/how to's visit the wiki in the near future.
 ```
 from ebuilder.ebuilder_core import *
 
 index = newpage('index')
 title = header(index, "Hello GitHub!")
 title.center()
 title.color('gray')
 index.commit()
 ```
 
 This example would create a .html file with a <h1> tag, centered and gray.
  
```
from ebuilder.ebuilder_core import EbuilderTextComponent as etc
  
header_two = etc("h2")
```
Note that if you only import EbuilderTextComponent you wont be able to 
access the other functions of Ebuilder Ultra, like making a new page, it is shown here
because it is the most efficient way.

# Advice Welcome
Feel free to dig through the source code, you'll see that EbuilderTextComponent 
has a bit of a weird implementation....
