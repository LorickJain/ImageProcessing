import PIL
import numpy
import scipy
import os
import sys
import math

from PIL import Image
from scipy import ndimage
from scipy.ndimage import filters # for chiru :image manipulation
from numpy import array
from scipy import fftpack

def splitrgb():
	im = Image.open('input.jpg')

	pix=list(im.getdata())

	r=[(x[0],0,0) for x in pix ]
	g=[(0,x[1],0) for x in pix ]
	b=[(0,0,x[2]) for x in pix ]

	imr = Image.new(im.mode,im.size)
	img = Image.new(im.mode,im.size)
	imb = Image.new(im.mode,im.size)

	imr.putdata(r)
	img.putdata(g)
	imb.putdata(b)
	imr.save("Outr.jpg")
	img.save("Outg.jpg")
	imb.save("Outb.jpg")

def weirdmerge():
	im = Image.open('input.jpg')
	pix=list(im.getdata())
	pen = Image.open('input.png')
	penpix=list(pen.getdata())
	for i in range(len(penpix)):
		pix[i]=penpix[i]
	
	merge = Image.new(im.mode,im.size)
	merge.putdata(pix)
	merge.save("merge.jpg")

def flat(im):
	pix=list(im.getdata())

	flat=[(x[0]-x[0]%100,x[1]-x[1]%100,x[2]-x[2]%100) for x in pix ]
	
	f=Image.new(im.mode,im.size)
	f.putdata(flat)
	return f

def outline():
	im = Image.open('input.jpg')
	im=flat(im)
	pix=list(im.getdata())
	out=[(pix[x][0]-pix[x-1][0],pix[x][1]-pix[x-1][1],pix[x][2]-pix[x-1][2]) for x in range(1,len(pix)) ]
	f=Image.new(im.mode,im.size)
	f.putdata(out)
	#f=flat(f)
	f.save("flat.jpg")
	
def colourfilter():
	im = Image.open('input.jpg')

	pix=list(im.getdata())
	print "Enter r%"
	rpc=int(input())
	print "Enter g%"
	gpc=int(input())
	print "Enter b%"
	bpc=int(input())	
	
	alter=[(x[0]*rpc/100,x[1]*gpc/100,x[2]*bpc/100) for x in pix ]
	f=Image.new(im.mode,im.size)
	f.putdata(alter)
	f.save("colourfilter.jpg")

def redsharp():
	im = Image.open('input.jpg')
	pix=list(im.getdata())
	out=[(pix[x-x%10][0],pix[x-x%10][1],pix[x-x%10][2]) for x in range(len(pix)) ]
	f=Image.new(im.mode,im.size)
	f.putdata(out)
	#f=flat(f)
	f.save("reducesharp.jpg")

def fourier():
	im = Image.open('input.jpg')

	blurred = ndimage.gaussian_filter(im, sigma=3)
	very = ndimage.gaussian_filter(im, sigma=5)
	veryvery = ndimage.gaussian_filter(im, sigma=40)
	veryvery=Image.fromarray(veryvery, 'RGB')
	blurred=Image.fromarray(blurred, 'RGB')
	very=Image.fromarray(very, 'RGB')
	blurred.save("blurred.jpg")
	very.save("very-blurred.jpg")
	veryvery.save("very-very-blurred.jpg")
	
def glow():
	im = Image.open('input.jpg')

	pix=list(im.getdata())

	r=[(x[0],0,0) for x in pix ]
	g=[(0,x[1],0) for x in pix ]
	b=[(0,0,x[2]) for x in pix ]

	imr = Image.new(im.mode,im.size)
	#img = Image.new(im.mode,im.size)
	#imb = Image.new(im.mode,im.size)

	imr.putdata(r)
	#img.putdata(g)
	#imb.putdata(b)
	imr = ndimage.gaussian_filter(imr, sigma=5)
	imr=Image.fromarray(imr, 'RGB')
	new=list(imr.getdata())
	newlist=[(new[i][0],g[i][1],b[i][2]) for i in range(len(new))]
	f=Image.new(im.mode,im.size)
	f.putdata(newlist)
	f.save("glow.jpg")

#glow()
def color_filter():
	alter=[]
	im = Image.open('input.jpg')
	pix=list(im.getdata())
	y = len(pix)
	print "Enter r%"
	rpc = int(input())
	print "Enter g%"
	gpc = int(input())
	print "Enter b%"
	bpc = int(input())
	for i in range(y/3):
		alter.append((pix[i][0]*rpc/100, pix[i][1], pix[i][2]))
	for i in range(y/3, (2*y/3)):
		alter.append((pix[i][0], pix[i][1]*gpc/100, pix[i][2]))
	for i in range((2*y)/3, y):
		alter.append((pix[i][0], pix[i][1], pix[i][2]*bpc/100))
	f=Image.new(im.mode,im.size)
	f.putdata(alter)
	f.save("3color.jpg")
		
def goldoutline():
	im = Image.open('input.jpg')
	pix=list(im.getdata())
	alter=[(180,120,x[2]) for x in pix]
	f=Image.new(im.mode,im.size)
	f.putdata(alter)
	f.save("goldoutline.jpg")
def gold():
	im = Image.open('input.jpg')
	pix=list(im.getdata())
	alter=[(max(x[0],255-x[0]),max(x[1],255-x[1]),x[2]) for x in pix]
	f=Image.new(im.mode,im.size)
	f.putdata(alter)
	f.save("gold.jpg")
goldoutline()
