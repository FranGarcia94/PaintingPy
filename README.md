# PaintingPy

[![Python_version](https://img.shields.io/badge/Python-v3.10.2-blueviolet?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3102/)
![](https://custom-icon-badges.herokuapp.com/github/license/FranGarcia94/PaintingPy?logo=law)
![](https://badge-size.herokuapp.com/FranGarcia94/PaintingPy/main/paintingpy.py)

![Tkinter](https://img.shields.io/badge/Tkinter-orange?style=flat)
![Canvas](https://img.shields.io/badge/Canvas-red?style=flat)
![Pillow](https://img.shields.io/badge/Pillow-gray?style=flat)
![Paint](https://img.shields.io/badge/Paint-green?style=flat)

<p align = "center">
<a href="https://www.flaticon.es/iconos-gratis/panel-solar"><img src="https://user-images.githubusercontent.com/107102754/186997276-59004b6d-0738-4ca2-a28a-8189a8299411.png" width=370/></a>
</p>
<p align = "center">
<b>Simple GUI to paint with Python</b>
</p>

# Introduction

This GUI has been developed in Python and is based on Tkinter and Canvas to create a simple but interesting drawing experience, especially in a didactic way. The interface is as follows:

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/186999742-fa7f41c2-c1dc-40e4-8699-dcc79f25133f.png" width=695/>
</p>

The interface elements are intuitive and share some properties, they are:
- One click
- Drag mouse

Circle, Square, Star and Random Brush also allow Fill or Hollow mode and outline color. The Polygon mode does not allow the brush thickness, but it is possible to use it as a continuous drawing brush.

Here is an example using the different elements:

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187006552-815e0208-c4b0-41f3-aa86-0c3f894060e5.jpg" width=695/>
</p>

Let's see the different components.

# Tools
##  0. Brush Thickness

It's a slider that represents the size of the shapes. You can change both the minimum and maximum value, in this case it is [0, 60] and the figures shown below have the following sizes [10, 25, 40, 60]. 
Don't forget that the figures show one-click shapes but you can drag and use them like a brush.

## 1. Circle Brush

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187001072-9fd1818f-730d-455d-b350-ef8b0f7a1dcc.jpg" width=695/>
</p>

## 2. Square Brush

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187001110-b4fd249d-502e-4e9d-aaf1-11ea62fda10e.jpg" width=695/>
</p>

## 3. Line Brush
<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187001139-4f27dd48-2d51-40a0-ae1b-1f64c43e8bb7.jpg" width=695/>
</p>

Here it is possible to change the direction of the line by exchanging x1 with x2 in this part of the code.

```python
  x1, y1 = ( event.x - scaleVar.get() ), ( event.y - scaleVar.get() )
  x2, y2 = ( event.x + scaleVar.get() ), ( event.y + scaleVar.get() )

  w.create_line(x1, y1, x2, y2, fill = color[1])
  draw.line([x1, y1, x2, y2], fill=color[0],  width=scaleVar.get())
  
```

## 4. Polygon

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187001182-7a07d226-e8ea-462b-a56f-f197c431891a.jpg" width=695/>
</p>

As you can see in this image (made by my little brother, unless you think it's not too bad in which case I made it :satisfied:), it is possible to use this tool as a continuous brush or to make open or closed polygons.

## 5. Star Brush

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187001229-ae6bc836-7c65-4355-865b-3eefa0213663.jpg" width=695/>
</p>

It should be noted that this tool is not a default attribute of canvas (Like circle, line, polygon or rectangle), It is a succession of lines created by manually entered points (depending on the position on the screen), so you can create your own figure and add it as a brush.

For a star as shown, the points are as follows:

```python
        x1, y1 = (event.x - scaleVar.get()), (event.y)
        x2, y2 = (event.x - scaleVar.get()//4), (event.y - scaleVar.get()//4)
        x3, y3 = (event.x), (event.y - scaleVar.get())
        x4, y4 = (event.x + scaleVar.get()//4), (event.y - scaleVar.get()//4)
        x5, y5 = (event.x + scaleVar.get()), (event.y)
        x6, y6 = (event.x + scaleVar.get()//4), (event.y + scaleVar.get()//4)
        x7, y7 = (event.x), (event.y + scaleVar.get())
        x8, y8 = (event.x - scaleVar.get()//4), (event.y + scaleVar.get()//4)

        points = [x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8]
        
```

## 6. Random

<p align = "center">
<img src="https://user-images.githubusercontent.com/107102754/187003099-d890cf3f-4389-42a7-8406-67f259f1f587.gif" width=695/>
</p>

This is a special function that creates random circles or squares that move and collide with the edges of the interface.

In the same way as in the other modes you can use one-click to create the shapes, or use drag. Anyway, it is possible to modify the size of the brush, the colors and the filling or not.


| One-Click | Drag |
| -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187003575-6981281c-cd98-4c9f-a099-4022399ca2e7.gif" width="425"/> | <img src="https://user-images.githubusercontent.com/107102754/187004018-f9793e67-64da-44c6-8cfc-56492bde0ea1.gif" width="425"/>|

# Save and Clear

Finally, with these buttons we can save the drawing and clean the screen respectively.

Here it's necessary to clarify that to save the drawing, it is done through `Pillow` library creating a copy in memory of everything we do in `Canvas`, that is why the result of the saved image may be slightly different from what we see.


| Intro | Circle |
| -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187005730-8141dacf-00de-4ca1-9997-1c9e46915404.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187005693-d2172d96-e6e3-4706-97dd-92501ae0471b.png" width="450"/> |

| Square | Lines |
| -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187005924-7dd96897-80e2-4238-a556-3404a65200f2.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187005805-ced5c1b9-3d08-492f-9f0a-166dd19b1d4a.png" width="450"/> |

| Polygon | Star |
| -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187005817-b5643ca8-e4bf-4cdc-afa3-64a2a897ddca.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187005985-0a56fc90-d4ef-40fa-b7dc-fd435fe7a586.png" width="450"/> |

As we can see, the saved images are practically the same. However, with the `Lines` tool the difference is more obvious due to the differences with this statement in the two libraries.

### Exception

Regarding saving the image, there is one important exception.

If we use the random mode, the image that will be saved is the movement of the object or objects that appear on the screen and not the position of the elements when the button is pressed.

I have done this in order to create interesting and different figures and patterns since the direction and speed of the figures in this mode is random.

Here is a sample of some of these images:

| Random 1 | Random 2 | Random 3 |
| -- | -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187007288-6b549e8b-6086-4096-8190-30c63ba52d3b.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187007313-78379b80-d45a-489e-adc1-6b5dd44a1a52.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187007324-1fcf775b-83b5-45fe-90c3-7fa02197d4b7.png" width="450"/> |

| Random 4 | Random 5 | Random 6 |
| -- | -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/187007334-11da3d57-eb20-45ab-9953-c7edfc3840ef.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187007345-306c0967-aefe-4d5c-b783-bb02083bb9bf.png" width="450"/> | <img src="https://user-images.githubusercontent.com/107102754/187007354-0a36b221-2cd0-4641-b344-6d16f7703d92.png" width="450"/> |




