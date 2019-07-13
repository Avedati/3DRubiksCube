#!/usr/bin/env python

""" main.py: A 3D Rubik's Cube designed in Python using PyOpenGL. Written shortly after it's 2D counterpart. """

__author__  = "the-inhuman-account"
__version__ = "0.0.2"

import pygame, sys, time, os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import randint
white = (1, 1, 1)
light_blue = (0, 1, 1)
blue = (0, 0, 1)
green = (0, 1, 0)
red = (1, 0, 0)
purple = (1, 0, 1)
pygame.init()
 
#just for reference
#white = 1
#light blue = 2
#blue = 3
#green = 4
#purple = 5
#red = 6
 
solution = []
 
front = [
1,
1,
1,
1,
1,
1,
1,
1,
1
]
 
back = [
2,
2,
2,
2,
2,
2,
2,
2,
2
]
 
left = [
3,
3,
3,
3,
3,
3,
3,
3,
3
]
 
right = [
4,
4,
4,
4,
4,
4,
4,
4,
4
]
 
top = [
5,
5,
5,
5,
5,
5,
5,
5,
5
]
 
bot = [
6,
6,
6,
6,
6,
6,
6,
6,
6
]
 
verts = (
(0.9, -0.9, -0.9),#node[0]
(0.9, 0.9, -0.9),#node[1]
(-0.9, 0.9, -0.9),#node[2]
(-0.9, -0.9, -0.9),#node[3]
(0.9, -0.9, 0.9),#node[4]
(0.9, 0.9, 0.9),#node[5]
(-0.9, -0.9, 0.9),#node[6]
(-0.9, 0.9, 0.9),#node[7]
)
edges = (
(0, 1),
(0, 3),
(0, 4),
(2, 1),
(2, 3),
(2, 7),
(6, 3),
(6, 4),
(6, 7),
(5, 1),
(5, 4),
(5, 7),
)
 
front_edges = []
back_edges = []
left_edges = []
right_edges = []
top_edges = []
bot_edges = []
# 3
#0 1
# 2
front_corners = []
back_corners = []
left_corners = []
right_corners = []
top_corners = []
bot_corners = []
 
#0 1
#
#2 3
 
def move_face(side_edges, side_corners, selftype):
    #moving edges
    if selftype == 'ni':
        Mylist = []
        Mylist.append(side_edges[0])
        Mylist.append(side_edges[2])
        Mylist.append(side_edges[1])
        Mylist.append(side_edges[3])
        side_edges[0], side_edges[2], side_edges[1], side_edges[3] = Mylist[3], Mylist[0], Mylist[1], Mylist[2]
        #moving corners
        My_new_list = []
        My_new_list.append(side_corners[0])
        My_new_list.append(side_corners[2])
        My_new_list.append(side_corners[3])
        My_new_list.append(side_corners[1])
        side_corners[0], side_corners[2], side_corners[3], side_corners[1] = My_new_list[1], My_new_list[2], My_new_list[3], My_new_list[0]
    else:
        Mylist = []
        Mylist.append(side_edges[0])
        Mylist.append(side_edges[2])
        Mylist.append(side_edges[1])
        Mylist.append(side_edges[3])
        side_edges[0], side_edges[2], side_edges[1], side_edges[3] = Mylist[1], Mylist[2], Mylist[3], Mylist[0]
        #moving corners
        My_new_list = []
        My_new_list.append(side_corners[0])
        My_new_list.append(side_corners[2])
        My_new_list.append(side_corners[3])
        My_new_list.append(side_corners[1])
        side_corners[0], side_corners[2], side_corners[3], side_corners[1] = My_new_list[1], My_new_list[2], My_new_list[3], My_new_list[0]
 
def f():
    #moving edges
    move_face(front_edges, front_corners, 'i')
    f_l1 = []
    f_l1.append(top_edges[3])
    f_l1.append(right_edges[1])
    f_l1.append(bot_edges[3])
    f_l1.append(left_edges[1])
    top_edges[3], right_edges[1], bot_edges[3], left_edges[1] = f_l1[3], f_l1[0], f_l1[1], f_l1[2]
    #moving corners
    Mylist = []
    Mylist.append(top_corners[2])
    Mylist.append(top_corners[3])
    Mylist.append(right_corners[1])
    Mylist.append(right_corners[3])
    Mylist.append(bot_corners[2])
    Mylist.append(bot_corners[3])
    Mylist.append(left_corners[1])
    Mylist.append(left_corners[3])
    top_corners[2], top_corners[3], right_corners[1], right_corners[3], bot_corners[2], bot_corners[3], left_corners[1], left_corners[3] = Mylist[6], Mylist[7], Mylist[0], Mylist[1], Mylist[2], Mylist[3], Mylist[4], Mylist[5]
    solution.append('fi')
def b():
    move_face(back_edges, back_corners, 'ni')
    b_l1 = []
    b_l1.append(top_edges[2])
    b_l1.append(right_edges[0])
    b_l1.append(bot_edges[2])
    b_l1.append(left_edges[0])
    top_edges[2], right_edges[0], bot_edges[2], left_edges[0] = b_l1[1], b_l1[2], b_l1[3], b_l1[0]
    #moving corners
    Mylist = []
    Mylist.append(top_corners[0])
    Mylist.append(top_corners[1])
    Mylist.append(right_corners[0])
    Mylist.append(right_corners[2])
    Mylist.append(bot_corners[0])
    Mylist.append(bot_corners[1])
    Mylist.append(left_corners[0])
    Mylist.append(left_corners[2])
    top_corners[0], top_corners[1], right_corners[0], right_corners[2], bot_corners[0], bot_corners[1], left_corners[0], left_corners[2] = Mylist[2], Mylist[3], Mylist[4], Mylist[5], Mylist[6], Mylist[7], Mylist[0], Mylist[1]
    solution.append('bi')
def l():
    move_face(left_edges, left_corners, 'i')
    l_l1 = []
    l_l1.append(front_edges[0])
    l_l1.append(top_edges[0])
    l_l1.append(back_edges[0])
    l_l1.append(bot_edges[0])
    front_edges[0], top_edges[0], back_edges[0], bot_edges[0] = l_l1[1], l_l1[2], l_l1[3], l_l1[0]
    #moving corners
    Mylist = []
    Mylist.append(front_corners[0])
    Mylist.append(front_corners[2])
    Mylist.append(top_corners[0])
    Mylist.append(top_corners[2])
    Mylist.append(back_corners[0])
    Mylist.append(back_corners[2])
    Mylist.append(bot_corners[0])
    Mylist.append(bot_corners[2])
    front_corners[0], front_corners[2], top_corners[0], top_corners[2], back_corners[0], back_corners[2], bot_corners[0], bot_corners[2] = Mylist[2], Mylist[3], Mylist[4], Mylist[5], Mylist[6], Mylist[7], Mylist[0], Mylist[1]
    solution.append('li')
def r():
    move_face(right_edges, right_corners, 'ni')
    r_l1 = []
    r_l1.append(front_edges[1])
    r_l1.append(top_edges[1])
    r_l1.append(back_edges[1])
    r_l1.append(bot_edges[1])
    front_edges[1], top_edges[1], back_edges[1], bot_edges[1] = r_l1[3], r_l1[0], r_l1[1], r_l1[2]
    #moving corners
    Mylist = []
    Mylist.append(front_corners[1])
    Mylist.append(front_corners[3])
    Mylist.append(top_corners[1])
    Mylist.append(top_corners[3])
    Mylist.append(back_corners[1])
    Mylist.append(back_corners[3])
    Mylist.append(bot_corners[1])
    Mylist.append(bot_corners[3])
    front_corners[1], front_corners[3], top_corners[1], top_corners[3], back_corners[1], back_corners[3], bot_corners[1], bot_corners[3] = Mylist[6], Mylist[7], Mylist[0], Mylist[1], Mylist[2], Mylist[3], Mylist[4], Mylist[5]
    solution.append('ri')
def u():
    move_face(top_edges, top_corners, 'i')
    u_l1 = []
    u_l1.append(front_edges[3])
    u_l1.append(left_edges[3])
    u_l1.append(back_edges[3])
    u_l1.append(right_edges[3])
    front_edges[3], left_edges[3], back_edges[3], right_edges[3] = u_l1[3], u_l1[0], u_l1[1], u_l1[2]
    #moving corners
    Mylist = []
    Mylist.append(front_corners[0])
    Mylist.append(front_corners[1])
    Mylist.append(left_corners[0])
    Mylist.append(left_corners[1])
    Mylist.append(back_corners[0])
    Mylist.append(back_corners[1])
    Mylist.append(right_corners[0])
    Mylist.append(right_corners[1])
    front_corners[0], front_corners[1], left_corners[0], left_corners[1], back_corners[0], back_corners[1], right_corners[0], right_corners[1] = Mylist[6], Mylist[7], Mylist[0], Mylist[1], Mylist[2], Mylist[3], Mylist[4], Mylist[5]
    solution.append('ui')
def d():
    move_face(bot_edges, bot_corners, 'ni')
    d_l1 = []
    d_l1.append(front_edges[2])
    d_l1.append(left_edges[2])
    d_l1.append(back_edges[2])
    d_l1.append(right_edges[2])
    front_edges[2], left_edges[2], back_edges[2], right_edges[2] = d_l1[1], d_l1[2], d_l1[3], d_l1[0]
    #moving corners
    Mylist = []
    Mylist.append(front_corners[3])
    Mylist.append(front_corners[2])
    Mylist.append(left_corners[3])
    Mylist.append(left_corners[2])
    Mylist.append(back_corners[3])
    Mylist.append(back_corners[2])
    Mylist.append(right_corners[3])
    Mylist.append(right_corners[2])
    front_corners[3], front_corners[2], left_corners[3], left_corners[2], back_corners[3], back_corners[2], right_corners[3], right_corners[2] = Mylist[2], Mylist[3], Mylist[4], Mylist[5], Mylist[6], Mylist[7], Mylist[0], Mylist[1]
    solution.append('di')
 
 
def scramble():
    luck = randint(1, 300)
    for i in range(0, luck):
        luck1 = randint(1, 6)
        if luck1 == 1:
            f()
        elif luck1 == 2:
            b()
        elif luck1 == 3:
            l()
        elif luck1 == 4:
            r()
        elif luck1 == 5:
            u()
        elif luck1 == 6:
            d() 
 
def fast_solution():
    myRange = int(len(solution))
    for i in range(myRange):
        if solution[i - 1] == 'fi':
            for tres in range(3):
                f()
        elif solution[i - 1] == 'bi':
            for tres in range(3):
                b()
        elif solution[i - 1] == 'li':
            for tres in range(3):
                l()
        elif solution[i - 1] == 'ri':
            for tres in range(3):
                r()
        elif solution[i - 1] == 'ui':
            for tres in range(3):
                u()
        elif solution[i - 1] == 'di':
            for tres in range(3):
                d()
 
def slow_solution():
    myRange = int(len(solution))
    for i in range(myRange):
        if solution[i - 1] == 'fi':
            for tres in range(3):
                f()
            time.sleep(0.5)
        elif solution[i - 1] == 'bi':
            for tres in range(3):
                b()
            time.sleep(0.5)
        elif solution[i - 1] == 'li':
            for tres in range(3):
                l()
            time.sleep(0.5)
        elif solution[i - 1] == 'ri':
            for tres in range(3):
                r()
            time.sleep(0.5)
        elif solution[i - 1] == 'ui':
            for tres in range(3):
                u()
            time.sleep(0.5)
        elif solution[i - 1] == 'di':
            for tres in range(3):
                d()
            time.sleep(0.5)
 
def isColor_edges(List, List2, pos1, pos2, pos3, pos4):
    if List[pos1] == 1:
        List2.append(white)
    if List[pos1] == 2:
        List2.append(light_blue)
    if List[pos1] == 3:
        List2.append(blue)
    if List[pos1] == 4:
        List2.append(green)
    if List[pos1] == 5:
        List2.append(purple)
    if List[pos1] == 6:
        List2.append(red)
    if List[pos2] == 1:
        List2.append(white)
    if List[pos2] == 2:
        List2.append(light_blue)
    if List[pos2] == 3:
        List2.append(blue)
    if List[pos2] == 4:
        List2.append(green)
    if List[pos2] == 5:
        List2.append(purple)
    if List[pos2] == 6:
        List2.append(red)
    if List[pos3] == 1:
        List2.append(white)
    if List[pos3] == 2:
        List2.append(light_blue)
    if List[pos3] == 3:
        List2.append(blue)
    if List[pos3] == 4:
        List2.append(green)
    if List[pos3] == 5:
        List2.append(purple)
    if List[pos3] == 6:
        List2.append(red)
    if List[pos4] == 1:
        List2.append(white)
    if List[pos4] == 2:
        List2.append(light_blue)
    if List[pos4] == 3:
        List2.append(blue)
    if List[pos4] == 4:
        List2.append(green)
    if List[pos4] == 5:
        List2.append(purple)
    if List[pos4] == 6:
        List2.append(red)
 
def isColor_corners(side, side2, pos1, pos2, pos3, pos4):
    if side[pos1] == 1:
        side2.append(white)
    if side[pos1] == 2:
        side2.append(light_blue)
    if side[pos1] == 3:
        side2.append(blue)
    if side[pos1] == 4:
        side2.append(green)
    if side[pos1] == 5:
        side2.append(purple)
    if side[pos1] == 6:
        side2.append(red)
    if side[pos2] == 1:
        side2.append(white)
    if side[pos2] == 2:
        side2.append(light_blue)
    if side[pos2] == 3:
        side2.append(blue)
    if side[pos2] == 4:
        side2.append(green)
    if side[pos2] == 5:
        side2.append(purple)
    if side[pos2] == 6:
        side2.append(red)
    if side[pos3] == 1:
        side2.append(white)
    if side[pos3] == 2:
        side2.append(light_blue)
    if side[pos3] == 3:
        side2.append(blue)
    if side[pos3] == 4:
        side2.append(green)
    if side[pos3] == 5:
        side2.append(purple)
    if side[pos3] == 6:
        side2.append(red)
    if side[pos4] == 1:
        side2.append(white)
    if side[pos4] == 2:
        side2.append(light_blue)
    if side[pos4] == 3:
        side2.append(blue)
    if side[pos4] == 4:
        side2.append(green)
    if side[pos4] == 5:
        side2.append(purple)
    if side[pos4] == 6:
        side2.append(red)
 
def t(x, y, z):
    glTranslatef(x, y, z)
 
def draw(p1, p2, p3, p4, color):
    glBegin(GL_QUADS)
    glColor3fv(color) 
    glVertex3fv(p1)
    glVertex3fv(p2)
    glVertex3fv(p3)
    glVertex3fv(p4)
    glEnd()
 
def centers():
    #top center
    draw((0.3, -0.9, -0.3), (-0.3, -0.9, -0.3), (-0.3, -0.9, 0.3), (0.3, -0.9, 0.3), (1, 0, 1))
    #bottom center
    draw((0.3, 0.9, -0.3), (-0.3, 0.9, -0.3), (-0.3, 0.9, 0.3), (0.3, 0.9, 0.3), (1, 0, 0))
    #front center
    draw((0.3, 0.3, 0.9), (-0.3, 0.3, 0.9), (-0.3, -0.3, 0.9), (0.3, -0.3, 0.9), (1, 1, 1))
    #back center
    draw((0.3, 0.3, -0.9), (0.3, -0.3, -0.9), (-0.3, -0.3, -0.9), (-0.3, 0.3, -0.9), (0, 1, 1))
    #left center
    draw((-0.9, -0.3, 0.3), (-0.9, -0.3, -0.3), (-0.9, 0.3, -0.3), (-0.9, 0.3, 0.3), (0, 0, 1))
    #right center
    draw((0.9, -0.3, 0.3), (0.9, -0.3, -0.3), (0.9, 0.3, -0.3), (0.9, 0.3, 0.3), (0, 1, 0))
 
def draw_edges():
    isColor_edges(front, front_edges, 3, 5, 7, 1)
    #draw front edges
    #***
    #!**
    #***
    draw((-0.3, 0.3, 0.9), (-0.9, 0.3, 0.9), (-0.9, -0.3, 0.9), (-0.3, -0.3, 0.9), front_edges[0])
    #***
    #**!
    #***
    draw((0.3, 0.3, 0.9), (0.9, 0.3, 0.9), (0.9, -0.3, 0.9), (0.3, -0.3, 0.9), front_edges[1])
    #***
    #***
    #*!*
    draw((0.3, -0.3, 0.9), (-0.3, -0.3, 0.9), (-0.3, -0.9, 0.9), (0.3, -0.9, 0.9), front_edges[2])
    #*!*
    #***
    #***
    draw((0.3, 0.3, 0.9), (-0.3, 0.3, 0.9), (-0.3, 0.9, 0.9), (0.3, 0.9, 0.9), front_edges[3])
    isColor_edges(back, back_edges, 3, 5, 7, 1)
    #draw back edges
    #***
    #!**
    #***
    draw((-0.9, -0.3, -0.9), (-0.9, 0.3, -0.9), (-0.3, 0.3, -0.9), (-0.3, -0.3, -0.9), back_edges[0])
    #***
    #**!
    #***
    draw((0.9, -0.3, -0.9), (0.9, 0.3, -0.9), (0.3, 0.3, -0.9), (0.3, -0.3, -0.9), back_edges[1])
    #***
    #***
    #*!*
    draw((-0.3, -0.9, -0.9), (0.3, -0.9, -0.9), (0.3, -0.3, -0.9), (-0.3, -0.3, -0.9), back_edges[2])
    #*!*
    #***
    #***
    draw((-0.3, 0.9, -0.9), (0.3, 0.9, -0.9), (0.3, 0.3, -0.9), (-0.3, 0.3, -0.9), back_edges[3])
    isColor_edges(left, left_edges, 3, 5, 7, 1)
    #draw left edges
    #***
    #!**
    #***
    draw((-0.9, -0.3, -0.3), (-0.9, -0.3, -0.9), (-0.9, 0.3, -0.9), (-0.9, 0.3, -0.3), left_edges[0])
    #***
    #**!
    #***
    draw((-0.9, -0.3, 0.9), (-0.9, -0.3, 0.3), (-0.9, 0.3, 0.3), (-0.9, 0.3, 0.9), left_edges[1])
    #***
    #***
    #*!*
    draw((-0.9, -0.9, 0.3), (-0.9, -0.9, -0.3), (-0.9, 0.9, -0.3), (-0.9, 0.9, 0.3), left_edges[2])
    #*!*
    #***
    #***
    draw((-0.9, 0.3, 0.3), (-0.9, 0.3, -0.3),(-0.9, 0.9, -0.3), (-0.9, 0.9, 0.3), left_edges[3])
    isColor_edges(right, right_edges, 3, 5, 7, 1)
    #draw right edges
    #***
    #!**
    #***
    draw((0.9, -0.3, -0.3), (0.9, -0.3, -0.9), (0.9, 0.3, -0.9), (0.9, 0.3, -0.3), right_edges[0])
    #***
    #**!
    #***
    draw((0.9, -0.3, 0.9), (0.9, -0.3, 0.3), (0.9, 0.3, 0.3), (0.9, 0.3, 0.9), right_edges[1])
    #***
    #***
    #*!*
    draw((0.9, -0.9, 0.3), (0.9, -0.9, -0.3), (0.9, 0.9, -0.3), (0.9, 0.9, 0.3), right_edges[2])
    #*!*
    #***
    #***
    draw((0.9, 0.3, 0.3), (0.9, 0.3, -0.3),(0.9, 0.9, -0.3), (0.9, 0.9, 0.3), right_edges[3])
    isColor_edges(top, top_edges, 3, 5, 7, 1)
    #draw top edges
    #***
    #!**
    #***
    draw((-0.9, 0.9, -0.3), (-0.9, 0.9, 0.3), (-0.3, 0.9, 0.3), (-0.3, 0.9, -0.3), top_edges[0])
    #***
    #**!
    #***
    draw((0.9, 0.9, -0.3), (0.9, 0.9, 0.3), (0.3, 0.9, 0.3), (0.3, 0.9, -0.3), top_edges[1])
    #***
    #***
    #*!*
    draw((-0.3, 0.9, -0.9), (-0.3, 0.9, -0.3), (0.3, 0.9, -0.3), (0.3, 0.9, -0.9), top_edges[2])
    #*!*
    #***
    #***
    draw((-0.3, 0.9, 0.9), (-0.3, 0.9, 0.3), (0.3, 0.9, 0.3), (0.3, 0.9, 0.9), top_edges[3])
    isColor_edges(bot, bot_edges, 3, 5, 7, 1)
    #draw bottom edges
    #***
    #!**
    #***
    draw((-0.9, -0.9, -0.3), (-0.9, -0.9, 0.3), (-0.3, -0.9, 0.3), (-0.3, -0.9, -0.3), bot_edges[0])
    #***
    #**!
    #***
    draw((0.9, -0.9, -0.3), (0.9, -0.9, 0.3), (0.3, -0.9, 0.3), (0.3, -0.9, -0.3), bot_edges[1])
    #***
    #***
    #*!*
    draw((-0.3, -0.9, -0.9), (-0.3, -0.9, -0.3), (0.3, -0.9, -0.3), (0.3, -0.9, -0.9), bot_edges[2])
    #*!*
    #***
    #***
    draw((-0.3, -0.9, 0.9), (-0.3, -0.9, 0.3), (0.3, -0.9, 0.3), (0.3, -0.9, 0.9), bot_edges[3])
 
def draw_corners():
    isColor_corners(front, front_corners, 0, 2, 6, 8)
    #draw front corners 
    #! *
    #
    #* *
    draw((-0.9, 0.9, 0.9), (-0.3, 0.9, 0.9), (-0.3, 0.3, 0.9), (-0.9, 0.3, 0.9), front_corners[0])
    #* !
    #
    #* *
    draw((0.9, 0.9, 0.9), (0.3, 0.9, 0.9), (0.3, 0.3, 0.9), (0.9, 0.3, 0.9), front_corners[1])
    #* *
    #
    #! *
    draw((-0.9, -0.9, 0.9), (-0.3, -0.9, 0.9), (-0.3, -0.3, 0.9), (-0.9, -0.3, 0.9), front_corners[2])
    #* *
    #
    #* !
    draw((0.9, -0.9, 0.9), (0.3, -0.9, 0.9), (0.3, -0.3, 0.9), (0.9, -0.3, 0.9), front_corners[3])
    isColor_corners(back, back_corners, 0, 2, 6, 8)
    #draw back corners
    #! *
    #
    #* *
    draw((-0.9, 0.9, -0.9), (-0.3, 0.9, -0.9), (-0.3, 0.3, -0.9), (-0.9, 0.3, -0.9), back_corners[0])
    #* !
    #
    #* *
    draw((0.9, 0.9, -0.9), (0.3, 0.9, -0.9), (0.3, 0.3, -0.9), (0.9, 0.3, -0.9), back_corners[1])
    #* *
    #
    #! *
    draw((-0.9, -0.9, -0.9), (-0.3, -0.9, -0.9), (-0.3, -0.3, -0.9), (-0.9, -0.3, -0.9), back_corners[2])
    #* *
    #
    #* !
    draw((0.9, -0.9, -0.9), (0.3, -0.9, -0.9), (0.3, -0.3, -0.9), (0.9, -0.3, -0.9), back_corners[3])
    isColor_corners(left, left_corners, 0, 2, 6, 8)
    #draw left corners
    draw((-0.9, 0.9, -0.3), (-0.9, 0.9, -0.9), (-0.9, 0.3, -0.9), (-0.9, 0.3, -0.3), left_corners[0])
    draw((-0.9, 0.9, 0.3), (-0.9, 0.9, 0.9), (-0.9, 0.3, 0.9), (-0.9, 0.3, 0.3), left_corners[1])
    draw((-0.9, -0.9, -0.3), (-0.9, -0.9, -0.9), (-0.9, -0.3, -0.9), (-0.9, -0.3, -0.3), left_corners[2])
    draw((-0.9, -0.9, 0.3), (-0.9, -0.9, 0.9), (-0.9, -0.3, 0.9), (-0.9, -0.3, 0.3), left_corners[3])
    isColor_corners(right, right_corners, 0, 2, 6, 8)
    #draw right corners
    draw((0.9, 0.9, -0.3), (0.9, 0.9, -0.9), (0.9, 0.3, -0.9), (0.9, 0.3, -0.3), right_corners[0])
    draw((0.9, 0.9, 0.3), (0.9, 0.9, 0.9), (0.9, 0.3, 0.9), (0.9, 0.3, 0.3), right_corners[1])
    draw((0.9, -0.9, -0.3), (0.9, -0.9, -0.9), (0.9, -0.3, -0.9), (0.9, -0.3, -0.3), right_corners[2])
    draw((0.9, -0.9, 0.3), (0.9, -0.9, 0.9), (0.9, -0.3, 0.9), (0.9, -0.3, 0.3), right_corners[3])
    isColor_corners(top, top_corners, 0, 2, 6, 8)
    #draw top corners
    draw((-0.9, 0.9, -0.9), (-0.3, 0.9, -0.9), (-0.3, 0.9, -0.3), (-0.9, 0.9, -0.3), top_corners[0])
    draw((0.9, 0.9, -0.9), (0.3, 0.9, -0.9), (0.3, 0.9, -0.3), (0.9, 0.9, -0.3), top_corners[1])
    draw((-0.9, 0.9, 0.9), (-0.3, 0.9, 0.9), (-0.3, 0.9, 0.3), (-0.9, 0.9, 0.3), top_corners[2])
    draw((0.9, 0.9, 0.9), (0.3, 0.9, 0.9), (0.3, 0.9, 0.3), (0.9, 0.9, 0.3), top_corners[3])
    isColor_corners(bot, bot_corners, 0, 2, 6, 8)
    #draw bottom corners
    draw((-0.9, -0.9, -0.9), (-0.3, -0.9, -0.9), (-0.3, -0.9, -0.3), (-0.9, -0.9, -0.3), bot_corners[0])
    draw((0.9, -0.9, -0.9), (0.3, -0.9, -0.9), (0.3, -0.9, -0.3), (0.9, -0.9, -0.3), bot_corners[1])
    draw((-0.9, -0.9, 0.9), (-0.3, -0.9, 0.9), (-0.3, -0.9, 0.3), (-0.9, -0.9, 0.3), bot_corners[2])
    draw((0.9, -0.9, 0.9), (0.3, -0.9, 0.9), (0.3, -0.9, 0.3), (0.9, -0.9, 0.3), bot_corners[3])
 
 
def lt():
    glRotatef(2, 0, 3, 0)
 
def rt():
    glRotatef(2, 0, -3, 0)
 
def fd():
    glRotatef(2, 3, 0, 0)
 
def dn():
    glRotatef(2, -3, 0, 0)
 
def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verts[vertex])
    glEnd()
static = True
I = False
os.system('clear')
def main(static, I):
    cubex = 800
    cubey = 600
    lft = False
    rght = False
    tp = False
    dwn = False
    cube_display = pygame.display.set_mode((cubex, cubey), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Rubik's cube")
    gluPerspective(45, (cubex / cubey), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)
    while True:
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and static == True:
                static = False
            elif event.type == pygame.KEYDOWN and static == False:
                if event.key == pygame.K_LEFT and not lft:
                    lft = True
                elif event.key == pygame.K_RIGHT and not rght:
                    rght = True
                elif event.key == pygame.K_UP and not tp:
                    tp = True
                elif event.key == pygame.K_DOWN and not dwn:
                    dwn = True
                elif event.key == pygame.K_SPACE:
                    lft = False
                    rght = False
                    tp = False
                    dwn = False
                elif event.key == pygame.K_f and not I:
                    f()
                elif event.key == pygame.K_b and not I:
                    b()
                elif event.key == pygame.K_l and not I:
                    l()
                elif event.key == pygame.K_r and not I:
                    r()
                elif event.key == pygame.K_u and not I:
                    u()
                elif event.key == pygame.K_d and not I:
                    d()
                elif event.key == pygame.K_f and I:
                    f()
                    f()
                    f()
                elif event.key == pygame.K_b and I:
                    b()
                    b()
                    b()
                elif event.key == pygame.K_l and I:
                    l()
                    l()
                    l()
                elif event.key == pygame.K_r and I:
                    r()
                    r()
                    r()
                elif event.key == pygame.K_u and I:
                    u()
                    u()
                    u()
                elif event.key == pygame.K_d and I:
                    d()
                    d()
                    d()
                elif event.key == pygame.K_i and not I:
                    I = True
                elif event.key == pygame.K_i and I:
                    I = False
                elif event.key == pygame.K_1:
                    scramble()
                elif event.key == pygame.K_2:
                    fast_solution()
                elif event.key == pygame.K_3:
                    slow_solution()
                elif event.key == pygame.K_4:
                    for i in range(9):
                        global front, back, left, right, top, down
                        front.pop()
                        back.pop()
                        left.pop()
                        right.pop()
                        top.pop()
                        bot.pop()
                        front.insert(0, 1)
                        back.insert(0, 2)
                        left.insert(0, 3)
                        right.insert(0, 4)
                        top.insert(0, 5)
                        bot.insert(0, 6)
        if lft:
            lt()
        if rght:
            rt()
        if tp:
            fd()
        if dwn:
            dn()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        cube()
        centers()
        draw_corners()
        draw_edges()
        glDisable(GL_DEPTH_TEST)
        pygame.display.flip()
        pygame.time.wait(10)
main(static, I)
