Marching Squares Generator
==========================

Create interesting and at the same time simple
images with only few lines of code.


Installation
------------

Simply download MarchingSquares.py and put it in your project folder.

Usage
-----

To import generator:

```python
from MarchingSquares import MSGenerator
```

Before usage you need to create instance of it.
Syntax of the constructor:

```python
MSGenerator(width, height, offset = "auto", scale = "auto", bgcolor = (0,0,0), fgcolor = (255,0,0))
```

Here are methods from generator:

- `getValue(x, y)` - Get value for vertex
- `buildSegment(x, y, draw)` - Draw segment at (x, y) based on 
vertex values using ImageDraw object from PIL
- `buildImage()` - Creating image
- `printInfo()` - Print width, height, offset and scale. Usefull when values are
calculated


Examples
--------

![Offset 9](/examples/9.png)
![Offset 59](/examples/59.png)
![Offset 35](/examples/35.png)
![Offset 6](/examples/6.png)
![Offset 86](/examples/86.png)
