#!/usr/bin/python

from fractions import gcd
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import math
import random

class MSGenerator:

	def __init__(self, width, height, offset="", scale="", bgcolor=(0,0,0), fgcolor = (255,0,0)):

		self.w = width
		self.h = height + 1
		
		self.r = offset if isinstance(offset, int) or isinstance(offset, float) else random.randint(0, 100) + 1
		self.s = scale if isinstance(scale, int) else int(scale) if isinstance(scale, float) else int(min(w,h) / (gcd(w,h) / 2))
			
		self.bgc = bgcolor
		self.fgc = fgcolor
		
		self.sq = [
			[                                                           ],
			[ (0,0),    (0,-0.5), (0.5,0)                               ],
			[ (0.5,0),  (1,-0.5), (1,0)                                 ],
			[ (0,0),    (0,-0.5), (1,-0.5), (1,0)                       ],
			[ (0.5,-1), (1,-1),   (1,-0.5)                              ],
			[ (0,0),    (0,-0.5), (0.5,-1), (1,-1),   (1,-0.5), (0.5,0) ],
			[ (0.5,-1), (1,-1),   (1,0),    (0.5,0)                     ],
			[ (0,0),    (0,-0.5), (0.5,-1), (1,-1),   (1,0)             ],
			[ (0,-0.5), (0,-1),   (0.5,-1)                              ],
			[ (0,0),    (0,-1),   (0.5,-1), (0.5,0)                     ],
			[ (0,-0.5), (0,-1),   (0.5,-1), (1,-0.5), (1,0),   (0.5,0)  ],
			[ (0,0),    (0,-1),   (0.5,-1), (1,-0.5), (1,0)             ],
			[ (0,-0.5), (0,-1),   (1,-1),   (1,-0.5)                    ],
			[ (0,0),    (0,-1),   (1,-1),   (1,-0.5), (0.5,0)           ],
			[ (0,-0.5), (0,-1),   (1,-1),   (1,0),    (0.5,0)           ],
			[ (0,0),    (0,-1),   (1,-1),   (1,0)                       ]
		]

	def printInfo(self):
		print ("Width      : {0}".format(self.w))
		print ("Height     : {0}".format(self.h))
		print ("Offset (r) : {0}".format(self.r))
		print ("Scale      : {0}".format(self.s))

	def getValue(self, x, y):
		return (int(self.s * math.sin((y * self.r)*180) - self.s * math.cos((x * self.r)*180)))  % 2
	
	def buildSegment(self, x, y, draw):
		v1 = self.getValue(x,y)
		v2 = self.getValue(x+self.s,y)
		v3 = self.getValue(x+self.s,y-self.s)
		v4 = self.getValue(x,y-self.s)
		
		c = v1 + v2 * 2 + v3 * 4 + v4 * 8
		
		if c > 0:
			tb = []
			for coord in self.sq[c]:
				x2,y2 = coord
				tb.append((int(x2 * self.s) + x, int(y2 * self.s) + y))
			draw.polygon((tb),fill=self.fgc)
		
	def buildImage(self):
		image = Image.new("RGB", (self.w, self.h))
		draw = ImageDraw.Draw(image)
		ImageDraw.floodfill(image, xy=(0,0), value=self.bgc)

		for x in range(0,self.w,self.s):
			for y in range(self.s,self.h,self.s):
				self.buildSegment(x, y, draw)
				
		return image
