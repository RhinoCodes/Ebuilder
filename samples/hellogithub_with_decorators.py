from ebuilder.ebuilder_decorators import *

@page
def index():
    title = header(index, "Hello Github!")
    title.font("-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif")
    title.center()
    title.color("gray")
    subtitle = header_two(index, "By RhinoCodes")
    subtitle.font("-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif")
    subtitle.center()
    index.commit()

# This and hellogithub_with_core.py both generate the same content except this one closes out the html file for you