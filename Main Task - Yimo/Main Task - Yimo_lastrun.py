#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on July 19, 2023, at 18:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import time
import sys
from psychopy import visual,event,core
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
#from pylab import *
#import logging

timer = core.Clock()
total_score = 0
feedback_txt = 0
logged = 0

Videoshowstart = 0
Videoshowstop = 0

flag_6040 = False
flag_5743 = False
flag_5446 = False
flag_5149 = False




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = "Rewa's Exp"  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'Task': ["1 - without skip", "2 - with skip"],
    'Dot Ratio': ["60:40, 57:43", "57:43, 54:46", "54:46, 51:49"],
    'Deadline': ["2.5s, 2.0s", "2.0s, 1.5s", "1.5s, 1.0s"],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expInfo['Task'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\AOE\\Desktop\\Rewa\\Rewa Exp-20230711T012626Z-002\\Rewa Exp\\Main Task - Yimo\\Main Task - Yimo_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "General_instructions" ---
text_g = visual.TextStim(win=win, name='text_g',
    text='Welcome to the experiment!\n \nIn this experiment, you will be asked to do two tasks (480 tials in total).\nThe intention of the both tasks is to choose the dominant color (the most presented color) in a patch of Red and Green dots, within different deadlines.\nA specific explanation is given prior to each task.\n \nGood luck!\n \nStart by pressing SPACE.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_task1" ---
text = visual.TextStim(win=win, name='text',
    text='Here is the instruction for the first task.\n \nYou do this task by pressing the "right arrow" (for RIGHT circle) and "left arrow" (for LEFT circle).\n \nYou will receive feedback on your performance using points. Once you reach a total score of 150 points, the task is over. Each time you can earn 1 point for a correct answer. You lose 2 points for an incorrect or too late answer.\n \nIn between, your total score will be given regularly. \n \nNow press SPACE to start.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code
if str(expInfo['Dot Ratio']) == '60:40, 57:43':
    flag_6040 = True
    flag_5743 = True
elif  str(expInfo['Dot Ratio']) == '57:43, 54:46':
    flag_5743 = True
    flag_5446 = True
elif  str(expInfo['Dot Ratio']) == '54:46, 51:49':
    flag_5446 = True
    flag_5149 = True
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_task2" ---
text_11 = visual.TextStim(win=win, name='text_11',
    text='Here is the instruction for the second task.\n \nThis task is same as Task1.\n \nYou do this task by pressing the "right arrow" (for RIGHT circle) and "left arrow" (for LEFT circle).\nIf you could not decide your choice, you can press "SPACE" (for SKIP).\n \nOnce you reach a total score of 150 points, the task is over. Each time you can earn 1 point for a correct answer. You lose 2 points for an incorrect or too late answer.\nIf you skip the trial, you will not lose any point.\n\nNow press SPACE to start.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "Fixation_1" ---
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot_1" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
circle_4 = visual.Polygon(
    win=win, name='circle_4',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Right_2 = visual.ShapeStim(
    win=win, name='Right_2',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
Left_2 = visual.ShapeStim(
    win=win, name='Left_2',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "Dots_Show_6040" ---
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.255, 0.255)[0], height=(0.255, 0.255)[1],
    ori=45.0, pos=(0.1275, 0.1275), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
    opacity=None, depth=-1.0, interpolate=True)
movie = visual.MovieStim(
    win, name='movie',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)
circle = visual.Polygon(
    win=win, name='circle',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
dots_60 = visual.DotStim(
    win=win, name='dots_60',
    nDots=60, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
dots_40 = visual.DotStim(
    win=win, name='dots_40',
    nDots=40, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-5.0)
response = keyboard.Keyboard()
Right = visual.ShapeStim(
    win=win, name='Right',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
Left = visual.ShapeStim(
    win=win, name='Left',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-8.0, interpolate=True)
key_skip = keyboard.Keyboard()

# --- Initialize components for Routine "feedback_1" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation_2" ---
fix_3 = visual.TextStim(win=win, name='fix_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot_2" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
circle_6 = visual.Polygon(
    win=win, name='circle_6',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fix_6 = visual.TextStim(win=win, name='fix_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Right_6 = visual.ShapeStim(
    win=win, name='Right_6',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
Left_6 = visual.ShapeStim(
    win=win, name='Left_6',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "Dots_Show_5743" ---
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.255, 0.255)[0], height=(0.255, 0.255)[1],
    ori=45.0, pos=(0.1275, 0.1275), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
    opacity=None, depth=-1.0, interpolate=True)
movie_2 = visual.MovieStim(
    win, name='movie_2',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)
circle_2 = visual.Polygon(
    win=win, name='circle_2',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
dots_43 = visual.DotStim(
    win=win, name='dots_43',
    nDots=43, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
dots_57 = visual.DotStim(
    win=win, name='dots_57',
    nDots=57, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-5.0)
response_2 = keyboard.Keyboard()
Right_3 = visual.ShapeStim(
    win=win, name='Right_3',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
Left_3 = visual.ShapeStim(
    win=win, name='Left_3',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-8.0, interpolate=True)
key_skip_2 = keyboard.Keyboard()

# --- Initialize components for Routine "feedback_2" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation_3" ---
fix_4 = visual.TextStim(win=win, name='fix_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot_3" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
circle_7 = visual.Polygon(
    win=win, name='circle_7',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fix_7 = visual.TextStim(win=win, name='fix_7',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Right_7 = visual.ShapeStim(
    win=win, name='Right_7',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
Left_7 = visual.ShapeStim(
    win=win, name='Left_7',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "Dot_Show_5446" ---
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.255, 0.255)[0], height=(0.255, 0.255)[1],
    ori=45.0, pos=(0.1275, 0.1275), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
    opacity=None, depth=-1.0, interpolate=True)
movie_3 = visual.MovieStim(
    win, name='movie_3',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)
circle_3 = visual.Polygon(
    win=win, name='circle_3',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
dots_46 = visual.DotStim(
    win=win, name='dots_46',
    nDots=46, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
dots_54 = visual.DotStim(
    win=win, name='dots_54',
    nDots=54, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-5.0)
response_3 = keyboard.Keyboard()
Left_4 = visual.ShapeStim(
    win=win, name='Left_4',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
Right_4 = visual.ShapeStim(
    win=win, name='Right_4',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-8.0, interpolate=True)
key_skip_3 = keyboard.Keyboard()

# --- Initialize components for Routine "feedback_3" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation_4" ---
fix_5 = visual.TextStim(win=win, name='fix_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot_4" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
circle_8 = visual.Polygon(
    win=win, name='circle_8',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fix_8 = visual.TextStim(win=win, name='fix_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Right_8 = visual.ShapeStim(
    win=win, name='Right_8',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
Left_8 = visual.ShapeStim(
    win=win, name='Left_8',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "Dots_Show_5149" ---
movie_4 = visual.MovieStim(
    win, name='movie_4',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-1
)
circle_5 = visual.Polygon(
    win=win, name='circle_5',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
dots_49 = visual.DotStim(
    win=win, name='dots_49',
    nDots=49, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-3.0)
dots_51 = visual.DotStim(
    win=win, name='dots_51',
    nDots=51, dotSize=10.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.58, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
response_4 = keyboard.Keyboard()
Left_5 = visual.ShapeStim(
    win=win, name='Left_5',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
Right_5 = visual.ShapeStim(
    win=win, name='Right_5',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
key_skip_4 = keyboard.Keyboard()

# --- Initialize components for Routine "feedback_4" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "score" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=total_score,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Your total score is: ',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press Spacebar to continue',
    font='Arial',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "End" ---
text_10 = visual.TextStim(win=win, name='text_10',
    text='It is the end of the experiment.\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "General_instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
General_instructionsComponents = [text_g, key_resp_4]
for thisComponent in General_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "General_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_g* updates
    
    # if text_g is starting this frame...
    if text_g.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_g.frameNStart = frameN  # exact frame index
        text_g.tStart = t  # local t and not account for scr refresh
        text_g.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_g, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_g.status = STARTED
        text_g.setAutoDraw(True)
    
    # if text_g is active this frame...
    if text_g.status == STARTED:
        # update params
        pass
    
    # *key_resp_4* updates
    waitOnFlip = False
    
    # if key_resp_4 is starting this frame...
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        # update status
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in General_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "General_instructions" ---
for thisComponent in General_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "General_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_task1" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code
if str(expInfo['Task']) == "2 - with skip":
    continueRoutine = False
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instructions_task1Components = [text, key_resp_2]
for thisComponent in Instructions_task1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_task1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    # Run 'Each Frame' code from code
    if key_resp_2.keys == "space":
        continueRoutine = False
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_task1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_task1" ---
for thisComponent in Instructions_task1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instructions_task1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_task2" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_21
if str(expInfo['Task']) == "1 - without skip":
    continueRoutine = False
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions_task2Components = [text_11, key_resp_3]
for thisComponent in Instructions_task2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_task2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    
    # if text_11 is starting this frame...
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_11.status = STARTED
        text_11.setAutoDraw(True)
    
    # if text_11 is active this frame...
    if text_11.status == STARTED:
        # update params
        pass
    # Run 'Each Frame' code from code_21
    if key_resp_3.keys == "space":
        continueRoutine = False
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_task2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_task2" ---
for thisComponent in Instructions_task2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_task2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=15.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_6040 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("Rewa_Sequence_" + expInfo['Deadline'] + ".xlsx"),
        seed=None, name='trials_6040')
    thisExp.addLoop(trials_6040)  # add the loop to the experiment
    thisTrial_6040 = trials_6040.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6040.rgb)
    if thisTrial_6040 != None:
        for paramName in thisTrial_6040:
            exec('{} = thisTrial_6040[paramName]'.format(paramName))
    
    for thisTrial_6040 in trials_6040:
        currentLoop = trials_6040
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6040.rgb)
        if thisTrial_6040 != None:
            for paramName in thisTrial_6040:
                exec('{} = thisTrial_6040[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        if total_score > 149:
            trials.finished = True
            break
            
        if flag_6040 == False:
            continueRoutine = False
            trials_6040.finished = True
            break
            
        # keep track of which components have finished
        Fixation_1Components = [fix]
        for thisComponent in Fixation_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            
            # if fix is starting this frame...
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix.status = STARTED
                fix.setAutoDraw(True)
            
            # if fix is active this frame...
            if fix.status == STARTED:
                # update params
                pass
            
            # if fix is stopping this frame...
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    # update status
                    fix.status = FINISHED
                    fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_1" ---
        for thisComponent in Fixation_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(screenshot)
        # Run 'Begin Routine' code from code_14
        if flag_6040 == False:
            continueRoutine = False
        # keep track of which components have finished
        screenshot_1Components = [image, circle_4, fix_2, Right_2, Left_2]
        for thisComponent in screenshot_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "screenshot_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # *circle_4* updates
            
            # if circle_4 is starting this frame...
            if circle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_4.frameNStart = frameN  # exact frame index
                circle_4.tStart = t  # local t and not account for scr refresh
                circle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_4.status = STARTED
                circle_4.setAutoDraw(True)
            
            # if circle_4 is active this frame...
            if circle_4.status == STARTED:
                # update params
                pass
            
            # if circle_4 is stopping this frame...
            if circle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_4.tStop = t  # not accounting for scr refresh
                    circle_4.frameNStop = frameN  # exact frame index
                    # update status
                    circle_4.status = FINISHED
                    circle_4.setAutoDraw(False)
            
            # *fix_2* updates
            
            # if fix_2 is starting this frame...
            if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_2.frameNStart = frameN  # exact frame index
                fix_2.tStart = t  # local t and not account for scr refresh
                fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_2.status = STARTED
                fix_2.setAutoDraw(True)
            
            # if fix_2 is active this frame...
            if fix_2.status == STARTED:
                # update params
                pass
            
            # if fix_2 is stopping this frame...
            if fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_2.tStop = t  # not accounting for scr refresh
                    fix_2.frameNStop = frameN  # exact frame index
                    # update status
                    fix_2.status = FINISHED
                    fix_2.setAutoDraw(False)
            
            # *Right_2* updates
            
            # if Right_2 is starting this frame...
            if Right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_2.frameNStart = frameN  # exact frame index
                Right_2.tStart = t  # local t and not account for scr refresh
                Right_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_2.status = STARTED
                Right_2.setAutoDraw(True)
            
            # if Right_2 is active this frame...
            if Right_2.status == STARTED:
                # update params
                pass
            
            # if Right_2 is stopping this frame...
            if Right_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Right_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Right_2.tStop = t  # not accounting for scr refresh
                    Right_2.frameNStop = frameN  # exact frame index
                    # update status
                    Right_2.status = FINISHED
                    Right_2.setAutoDraw(False)
            
            # *Left_2* updates
            
            # if Left_2 is starting this frame...
            if Left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_2.frameNStart = frameN  # exact frame index
                Left_2.tStart = t  # local t and not account for scr refresh
                Left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_2.status = STARTED
                Left_2.setAutoDraw(True)
            
            # if Left_2 is active this frame...
            if Left_2.status == STARTED:
                # update params
                pass
            
            # if Left_2 is stopping this frame...
            if Left_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Left_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Left_2.tStop = t  # not accounting for scr refresh
                    Left_2.frameNStop = frameN  # exact frame index
                    # update status
                    Left_2.status = FINISHED
                    Left_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in screenshot_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot_1" ---
        for thisComponent in screenshot_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dots_Show_6040" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        
        # Get the value of a parameter from the loop
        #correct_answer = current_trial['correct']
        #print('correct_answer',correct_answer)
        
        
        if flag_6040 == False:
            continueRoutine = False
            
        # Get the duration of each loop
        #Dotsshowstart=timer.getTime()
        
        
        
        
        movie.setMovie(Countdown)
        dots_60.setColor(color1, colorSpace='rgb')
        dots_60.refreshDots()
        dots_40.setColor(color2, colorSpace='rgb')
        dots_40.refreshDots()
        response.keys = []
        response.rt = []
        _response_allKeys = []
        key_skip.keys = []
        key_skip.rt = []
        _key_skip_allKeys = []
        # keep track of which components have finished
        Dots_Show_6040Components = [polygon, movie, circle, dots_60, dots_40, response, Right, Left, key_skip]
        for thisComponent in Dots_Show_6040Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Dots_Show_6040" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            
            #if response.keys == str(correct_answer) or response.keys == correct_answer:
            #     response.corr = 1
            #     continueRoutine = False
            #elif len(response.keys)>1:
            #    response.corr = -2
            #    continueRoutine = False
            
            if len(response.keys)>1:
                continueRoutine = False
            
            if str(expInfo['Task']) == "2 - with skip":
                if key_skip.keys == "space":
                    continueRoutine = False
                    
            if movie.status == STARTED and logged == 0:
                Videoshowstart=timer.getTime()
                logged = 1
            
            
            
            
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                pass
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # *movie* updates
            
            # if movie is starting this frame...
            if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie.frameNStart = frameN  # exact frame index
                movie.tStart = t  # local t and not account for scr refresh
                movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie.status = STARTED
                movie.setAutoDraw(True)
                movie.play()
            if movie.isFinished:  # force-end the routine
                continueRoutine = False
            
            # *circle* updates
            
            # if circle is starting this frame...
            if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle.status = STARTED
                circle.setAutoDraw(True)
            
            # if circle is active this frame...
            if circle.status == STARTED:
                # update params
                pass
            
            # *dots_60* updates
            
            # if dots_60 is starting this frame...
            if dots_60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_60.frameNStart = frameN  # exact frame index
                dots_60.tStart = t  # local t and not account for scr refresh
                dots_60.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_60, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_60.status = STARTED
                dots_60.setAutoDraw(True)
            
            # if dots_60 is active this frame...
            if dots_60.status == STARTED:
                # update params
                pass
            
            # *dots_40* updates
            
            # if dots_40 is starting this frame...
            if dots_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_40.frameNStart = frameN  # exact frame index
                dots_40.tStart = t  # local t and not account for scr refresh
                dots_40.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_40, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_40.status = STARTED
                dots_40.setAutoDraw(True)
            
            # if dots_40 is active this frame...
            if dots_40.status == STARTED:
                # update params
                pass
            
            # *response* updates
            waitOnFlip = False
            
            # if response is starting this frame...
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                # update status
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['right','left'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(correct)) or (response.keys == correct):
                        response.corr = 1
                    else:
                        response.corr = 0
            
            # *Right* updates
            
            # if Right is starting this frame...
            if Right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right.frameNStart = frameN  # exact frame index
                Right.tStart = t  # local t and not account for scr refresh
                Right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right.status = STARTED
                Right.setAutoDraw(True)
            
            # if Right is active this frame...
            if Right.status == STARTED:
                # update params
                pass
            
            # *Left* updates
            
            # if Left is starting this frame...
            if Left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left.frameNStart = frameN  # exact frame index
                Left.tStart = t  # local t and not account for scr refresh
                Left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left.status = STARTED
                Left.setAutoDraw(True)
            
            # if Left is active this frame...
            if Left.status == STARTED:
                # update params
                pass
            
            # *key_skip* updates
            waitOnFlip = False
            
            # if key_skip is starting this frame...
            if key_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_skip.frameNStart = frameN  # exact frame index
                key_skip.tStart = t  # local t and not account for scr refresh
                key_skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_skip, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_skip.status == STARTED and not waitOnFlip:
                theseKeys = key_skip.getKeys(keyList=['space'], waitRelease=False)
                _key_skip_allKeys.extend(theseKeys)
                if len(_key_skip_allKeys):
                    key_skip.keys = _key_skip_allKeys[-1].name  # just the last key pressed
                    key_skip.rt = _key_skip_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Dots_Show_6040Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dots_Show_6040" ---
        for thisComponent in Dots_Show_6040Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_2
        #DotsshowRT = timer.getTime()-Dotsshowstart
        Videoshowstop=timer.getTime()
        VideoshowRT=Videoshowstop- Videoshowstart
        
        #thisExp.addData('DotsshowRT', DotsshowRT)
        thisExp.addData('Videoshowstart', Videoshowstart)
        thisExp.addData('Videoshowstop', Videoshowstop)
        thisExp.addData('VideoshowRT', VideoshowRT)
        
        logged = 0
        
        
        # For Feedback Page
        if flag_6040 == True:
            if key_skip.keys=="space":
                feedback_txt = 'Skipped 0'
                current_score = 0
            elif response.keys is None or len(response.keys) < 1:
                feedback_txt = 'Too late -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
            elif response.corr == 1:
                feedback_txt = 'Correct +1'
                feedback_col = [1.000,1.000,1.000]
                total_score += 1
                current_score = 1
            elif response.corr == 0:
                feedback_txt = 'Incorrect -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
        movie.stop()
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_6040 (TrialHandler)
        trials_6040.addData('response.keys',response.keys)
        trials_6040.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            trials_6040.addData('response.rt', response.rt)
        # check responses
        if key_skip.keys in ['', [], None]:  # No response was made
            key_skip.keys = None
        trials_6040.addData('key_skip.keys',key_skip.keys)
        if key_skip.keys != None:  # we had a response
            trials_6040.addData('key_skip.rt', key_skip.rt)
        # the Routine "Dots_Show_6040" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_3.setText(feedback_txt)
        # Run 'Begin Routine' code from code_4
        if flag_6040 == False:
            continueRoutine = False
        # keep track of which components have finished
        feedback_1Components = [text_3]
        for thisComponent in feedback_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_1" ---
        for thisComponent in feedback_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_4
        thisExp.addData('total_score', total_score)
        thisExp.addData('Dot_ratio', '60:40')
        thisExp.addData('current_score', current_score)
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_6040'
    
    # get names of stimulus parameters
    if trials_6040.trialList in ([], [None], None):
        params = []
    else:
        params = trials_6040.trialList[0].keys()
    # save data for this loop
    trials_6040.saveAsText(filename + 'trials_6040.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_5743 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("Rewa_Sequence_" + expInfo['Deadline'] + ".xlsx"),
        seed=None, name='trials_5743')
    thisExp.addLoop(trials_5743)  # add the loop to the experiment
    thisTrial_5743 = trials_5743.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5743.rgb)
    if thisTrial_5743 != None:
        for paramName in thisTrial_5743:
            exec('{} = thisTrial_5743[paramName]'.format(paramName))
    
    for thisTrial_5743 in trials_5743:
        currentLoop = trials_5743
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5743.rgb)
        if thisTrial_5743 != None:
            for paramName in thisTrial_5743:
                exec('{} = thisTrial_5743[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_11
        if total_score > 149:
            trials.finished = True
            break
        
        if flag_5743 == False:
            continueRoutine = False
            trials_5743.finished = True
            break
        # keep track of which components have finished
        Fixation_2Components = [fix_3]
        for thisComponent in Fixation_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_3* updates
            
            # if fix_3 is starting this frame...
            if fix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_3.frameNStart = frameN  # exact frame index
                fix_3.tStart = t  # local t and not account for scr refresh
                fix_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_3.status = STARTED
                fix_3.setAutoDraw(True)
            
            # if fix_3 is active this frame...
            if fix_3.status == STARTED:
                # update params
                pass
            
            # if fix_3 is stopping this frame...
            if fix_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_3.tStop = t  # not accounting for scr refresh
                    fix_3.frameNStop = frameN  # exact frame index
                    # update status
                    fix_3.status = FINISHED
                    fix_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_2" ---
        for thisComponent in Fixation_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        image_2.setImage(screenshot)
        # Run 'Begin Routine' code from code_15
        if flag_5743 == False:
            continueRoutine = False
        # keep track of which components have finished
        screenshot_2Components = [image_2, circle_6, fix_6, Right_6, Left_6]
        for thisComponent in screenshot_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "screenshot_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # if image_2 is stopping this frame...
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    # update status
                    image_2.status = FINISHED
                    image_2.setAutoDraw(False)
            
            # *circle_6* updates
            
            # if circle_6 is starting this frame...
            if circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_6.frameNStart = frameN  # exact frame index
                circle_6.tStart = t  # local t and not account for scr refresh
                circle_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_6.status = STARTED
                circle_6.setAutoDraw(True)
            
            # if circle_6 is active this frame...
            if circle_6.status == STARTED:
                # update params
                pass
            
            # if circle_6 is stopping this frame...
            if circle_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_6.tStop = t  # not accounting for scr refresh
                    circle_6.frameNStop = frameN  # exact frame index
                    # update status
                    circle_6.status = FINISHED
                    circle_6.setAutoDraw(False)
            
            # *fix_6* updates
            
            # if fix_6 is starting this frame...
            if fix_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_6.frameNStart = frameN  # exact frame index
                fix_6.tStart = t  # local t and not account for scr refresh
                fix_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_6.status = STARTED
                fix_6.setAutoDraw(True)
            
            # if fix_6 is active this frame...
            if fix_6.status == STARTED:
                # update params
                pass
            
            # if fix_6 is stopping this frame...
            if fix_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_6.tStop = t  # not accounting for scr refresh
                    fix_6.frameNStop = frameN  # exact frame index
                    # update status
                    fix_6.status = FINISHED
                    fix_6.setAutoDraw(False)
            
            # *Right_6* updates
            
            # if Right_6 is starting this frame...
            if Right_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_6.frameNStart = frameN  # exact frame index
                Right_6.tStart = t  # local t and not account for scr refresh
                Right_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_6.status = STARTED
                Right_6.setAutoDraw(True)
            
            # if Right_6 is active this frame...
            if Right_6.status == STARTED:
                # update params
                pass
            
            # if Right_6 is stopping this frame...
            if Right_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Right_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Right_6.tStop = t  # not accounting for scr refresh
                    Right_6.frameNStop = frameN  # exact frame index
                    # update status
                    Right_6.status = FINISHED
                    Right_6.setAutoDraw(False)
            
            # *Left_6* updates
            
            # if Left_6 is starting this frame...
            if Left_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_6.frameNStart = frameN  # exact frame index
                Left_6.tStart = t  # local t and not account for scr refresh
                Left_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_6.status = STARTED
                Left_6.setAutoDraw(True)
            
            # if Left_6 is active this frame...
            if Left_6.status == STARTED:
                # update params
                pass
            
            # if Left_6 is stopping this frame...
            if Left_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Left_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Left_6.tStop = t  # not accounting for scr refresh
                    Left_6.frameNStop = frameN  # exact frame index
                    # update status
                    Left_6.status = FINISHED
                    Left_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in screenshot_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot_2" ---
        for thisComponent in screenshot_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dots_Show_5743" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_5
        
        # Get the value of a parameter from the loop
        #correct_answer = current_trial['correct']
        #print('correct_answer',correct_answer)
        
        if flag_5743 == False:
            continueRoutine = False
            
        # Get the duration of each loop
        Dotsshowstart=timer.getTime()
        movie_2.setMovie(Countdown)
        dots_43.setColor(color2, colorSpace='rgb')
        dots_43.refreshDots()
        dots_57.setColor(color1, colorSpace='rgb')
        dots_57.refreshDots()
        response_2.keys = []
        response_2.rt = []
        _response_2_allKeys = []
        key_skip_2.keys = []
        key_skip_2.rt = []
        _key_skip_2_allKeys = []
        # keep track of which components have finished
        Dots_Show_5743Components = [polygon_2, movie_2, circle_2, dots_43, dots_57, response_2, Right_3, Left_3, key_skip_2]
        for thisComponent in Dots_Show_5743Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Dots_Show_5743" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_5
            
            #if response.keys == str(correct_answer) or response.keys == correct_answer:
            #     response.corr = 1
            #     continueRoutine = False
            #elif len(response.keys)>1:
            #    response.corr = -2
            #    continueRoutine = False
            
            if len(response_2.keys)>1:
                continueRoutine = False
                
            if str(expInfo['Task']) == "2 - with skip":
                if key_skip_2.keys == "space":
                    continueRoutine = False
            
            if movie_2.status == STARTED and logged == 0:
                Videoshowstart=timer.getTime()
                logged = 1
            
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                pass
            
            # if polygon_2 is stopping this frame...
            if polygon_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_2.tStop = t  # not accounting for scr refresh
                    polygon_2.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_2.status = FINISHED
                    polygon_2.setAutoDraw(False)
            
            # *movie_2* updates
            
            # if movie_2 is starting this frame...
            if movie_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_2.frameNStart = frameN  # exact frame index
                movie_2.tStart = t  # local t and not account for scr refresh
                movie_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie_2.status = STARTED
                movie_2.setAutoDraw(True)
                movie_2.play()
            if movie_2.isFinished:  # force-end the routine
                continueRoutine = False
            
            # *circle_2* updates
            
            # if circle_2 is starting this frame...
            if circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_2.frameNStart = frameN  # exact frame index
                circle_2.tStart = t  # local t and not account for scr refresh
                circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_2.status = STARTED
                circle_2.setAutoDraw(True)
            
            # if circle_2 is active this frame...
            if circle_2.status == STARTED:
                # update params
                pass
            
            # *dots_43* updates
            
            # if dots_43 is starting this frame...
            if dots_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_43.frameNStart = frameN  # exact frame index
                dots_43.tStart = t  # local t and not account for scr refresh
                dots_43.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_43, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_43.status = STARTED
                dots_43.setAutoDraw(True)
            
            # if dots_43 is active this frame...
            if dots_43.status == STARTED:
                # update params
                pass
            
            # *dots_57* updates
            
            # if dots_57 is starting this frame...
            if dots_57.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_57.frameNStart = frameN  # exact frame index
                dots_57.tStart = t  # local t and not account for scr refresh
                dots_57.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_57, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_57.status = STARTED
                dots_57.setAutoDraw(True)
            
            # if dots_57 is active this frame...
            if dots_57.status == STARTED:
                # update params
                pass
            
            # *response_2* updates
            waitOnFlip = False
            
            # if response_2 is starting this frame...
            if response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_2.frameNStart = frameN  # exact frame index
                response_2.tStart = t  # local t and not account for scr refresh
                response_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                response_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response_2.status == STARTED and not waitOnFlip:
                theseKeys = response_2.getKeys(keyList=['right','left'], waitRelease=False)
                _response_2_allKeys.extend(theseKeys)
                if len(_response_2_allKeys):
                    response_2.keys = _response_2_allKeys[-1].name  # just the last key pressed
                    response_2.rt = _response_2_allKeys[-1].rt
                    # was this correct?
                    if (response_2.keys == str(correct)) or (response_2.keys == correct):
                        response_2.corr = 1
                    else:
                        response_2.corr = 0
            
            # *Right_3* updates
            
            # if Right_3 is starting this frame...
            if Right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_3.frameNStart = frameN  # exact frame index
                Right_3.tStart = t  # local t and not account for scr refresh
                Right_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_3.status = STARTED
                Right_3.setAutoDraw(True)
            
            # if Right_3 is active this frame...
            if Right_3.status == STARTED:
                # update params
                pass
            
            # *Left_3* updates
            
            # if Left_3 is starting this frame...
            if Left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_3.frameNStart = frameN  # exact frame index
                Left_3.tStart = t  # local t and not account for scr refresh
                Left_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Left_3.started')
                # update status
                Left_3.status = STARTED
                Left_3.setAutoDraw(True)
            
            # if Left_3 is active this frame...
            if Left_3.status == STARTED:
                # update params
                pass
            
            # *key_skip_2* updates
            waitOnFlip = False
            
            # if key_skip_2 is starting this frame...
            if key_skip_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_skip_2.frameNStart = frameN  # exact frame index
                key_skip_2.tStart = t  # local t and not account for scr refresh
                key_skip_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_skip_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_skip_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_skip_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_skip_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_skip_2.status == STARTED and not waitOnFlip:
                theseKeys = key_skip_2.getKeys(keyList=['space'], waitRelease=False)
                _key_skip_2_allKeys.extend(theseKeys)
                if len(_key_skip_2_allKeys):
                    key_skip_2.keys = _key_skip_2_allKeys[-1].name  # just the last key pressed
                    key_skip_2.rt = _key_skip_2_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Dots_Show_5743Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dots_Show_5743" ---
        for thisComponent in Dots_Show_5743Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_5
        #DotsshowRT = timer.getTime()-Dotsshowstart
        Videoshowstop=timer.getTime()
        VideoshowRT=Videoshowstop- Videoshowstart
        
        #thisExp.addData('DotsshowRT', DotsshowRT)
        thisExp.addData('Videoshowstart', Videoshowstart)
        thisExp.addData('Videoshowstop', Videoshowstop)
        thisExp.addData('VideoshowRT', VideoshowRT)
        
        logged = 0
        
        # For Feedback Page
        if flag_5743 == True:
            if key_skip_2.keys=="space":
                feedback_txt = 'Skipped 0'
                current_score = 0
        
            elif response_2.keys is None or len(response_2.keys) < 1:
                feedback_txt = 'Too late -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
            elif response_2.corr == 1:
                feedback_txt = 'Correct +1'
                feedback_col = [1.000,1.000,1.000]
                total_score += 1
                current_score = 1
            elif response_2.corr == 0:
                feedback_txt = 'Incorrect -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
        movie_2.stop()
        # check responses
        if response_2.keys in ['', [], None]:  # No response was made
            response_2.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               response_2.corr = 1;  # correct non-response
            else:
               response_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_5743 (TrialHandler)
        trials_5743.addData('response_2.keys',response_2.keys)
        trials_5743.addData('response_2.corr', response_2.corr)
        if response_2.keys != None:  # we had a response
            trials_5743.addData('response_2.rt', response_2.rt)
        # check responses
        if key_skip_2.keys in ['', [], None]:  # No response was made
            key_skip_2.keys = None
        trials_5743.addData('key_skip_2.keys',key_skip_2.keys)
        if key_skip_2.keys != None:  # we had a response
            trials_5743.addData('key_skip_2.rt', key_skip_2.rt)
        # the Routine "Dots_Show_5743" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_6.setText(feedback_txt)
        # Run 'Begin Routine' code from code_16
        if flag_5743 == False:
            continueRoutine = False
        # keep track of which components have finished
        feedback_2Components = [text_6]
        for thisComponent in feedback_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # if text_6 is stopping this frame...
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    # update status
                    text_6.status = FINISHED
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_2" ---
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_16
        thisExp.addData('total_score', total_score)
        thisExp.addData('Dot_ratio', '57:43')
        thisExp.addData('current_score', current_score)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_5743'
    
    # get names of stimulus parameters
    if trials_5743.trialList in ([], [None], None):
        params = []
    else:
        params = trials_5743.trialList[0].keys()
    # save data for this loop
    trials_5743.saveAsText(filename + 'trials_5743.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_5446 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("Rewa_Sequence_" + expInfo['Deadline'] + ".xlsx"),
        seed=None, name='trials_5446')
    thisExp.addLoop(trials_5446)  # add the loop to the experiment
    thisTrial_5446 = trials_5446.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5446.rgb)
    if thisTrial_5446 != None:
        for paramName in thisTrial_5446:
            exec('{} = thisTrial_5446[paramName]'.format(paramName))
    
    for thisTrial_5446 in trials_5446:
        currentLoop = trials_5446
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5446.rgb)
        if thisTrial_5446 != None:
            for paramName in thisTrial_5446:
                exec('{} = thisTrial_5446[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        if total_score > 149:
            trials.finished = True
            break
        
        if flag_5446 == False:
            continueRoutine = False
            trials_5446.finished = True
            break
        # keep track of which components have finished
        Fixation_3Components = [fix_4]
        for thisComponent in Fixation_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_4* updates
            
            # if fix_4 is starting this frame...
            if fix_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_4.frameNStart = frameN  # exact frame index
                fix_4.tStart = t  # local t and not account for scr refresh
                fix_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_4.status = STARTED
                fix_4.setAutoDraw(True)
            
            # if fix_4 is active this frame...
            if fix_4.status == STARTED:
                # update params
                pass
            
            # if fix_4 is stopping this frame...
            if fix_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_4.tStop = t  # not accounting for scr refresh
                    fix_4.frameNStop = frameN  # exact frame index
                    # update status
                    fix_4.status = FINISHED
                    fix_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_3" ---
        for thisComponent in Fixation_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        image_3.setImage(screenshot)
        # Run 'Begin Routine' code from code_17
        if flag_5446 == False:
            continueRoutine = False
        # keep track of which components have finished
        screenshot_3Components = [image_3, circle_7, fix_7, Right_7, Left_7]
        for thisComponent in screenshot_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "screenshot_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # if image_3 is stopping this frame...
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    # update status
                    image_3.status = FINISHED
                    image_3.setAutoDraw(False)
            
            # *circle_7* updates
            
            # if circle_7 is starting this frame...
            if circle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_7.frameNStart = frameN  # exact frame index
                circle_7.tStart = t  # local t and not account for scr refresh
                circle_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_7.status = STARTED
                circle_7.setAutoDraw(True)
            
            # if circle_7 is active this frame...
            if circle_7.status == STARTED:
                # update params
                pass
            
            # if circle_7 is stopping this frame...
            if circle_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_7.tStop = t  # not accounting for scr refresh
                    circle_7.frameNStop = frameN  # exact frame index
                    # update status
                    circle_7.status = FINISHED
                    circle_7.setAutoDraw(False)
            
            # *fix_7* updates
            
            # if fix_7 is starting this frame...
            if fix_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_7.frameNStart = frameN  # exact frame index
                fix_7.tStart = t  # local t and not account for scr refresh
                fix_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_7.status = STARTED
                fix_7.setAutoDraw(True)
            
            # if fix_7 is active this frame...
            if fix_7.status == STARTED:
                # update params
                pass
            
            # if fix_7 is stopping this frame...
            if fix_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_7.tStop = t  # not accounting for scr refresh
                    fix_7.frameNStop = frameN  # exact frame index
                    # update status
                    fix_7.status = FINISHED
                    fix_7.setAutoDraw(False)
            
            # *Right_7* updates
            
            # if Right_7 is starting this frame...
            if Right_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_7.frameNStart = frameN  # exact frame index
                Right_7.tStart = t  # local t and not account for scr refresh
                Right_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_7.status = STARTED
                Right_7.setAutoDraw(True)
            
            # if Right_7 is active this frame...
            if Right_7.status == STARTED:
                # update params
                pass
            
            # if Right_7 is stopping this frame...
            if Right_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Right_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Right_7.tStop = t  # not accounting for scr refresh
                    Right_7.frameNStop = frameN  # exact frame index
                    # update status
                    Right_7.status = FINISHED
                    Right_7.setAutoDraw(False)
            
            # *Left_7* updates
            
            # if Left_7 is starting this frame...
            if Left_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_7.frameNStart = frameN  # exact frame index
                Left_7.tStart = t  # local t and not account for scr refresh
                Left_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_7.status = STARTED
                Left_7.setAutoDraw(True)
            
            # if Left_7 is active this frame...
            if Left_7.status == STARTED:
                # update params
                pass
            
            # if Left_7 is stopping this frame...
            if Left_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Left_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Left_7.tStop = t  # not accounting for scr refresh
                    Left_7.frameNStop = frameN  # exact frame index
                    # update status
                    Left_7.status = FINISHED
                    Left_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in screenshot_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot_3" ---
        for thisComponent in screenshot_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dot_Show_5446" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        
        # Get the value of a parameter from the loop
        #correct_answer = current_trial['correct']
        #print('correct_answer',correct_answer)
        
        if flag_5446 == False:
            continueRoutine = False
            
        # Get the duration of each loop
        Dotsshowstart=timer.getTime()
        movie_3.setMovie(Countdown)
        dots_46.setColor(color2, colorSpace='rgb')
        dots_46.refreshDots()
        dots_54.setColor(color1, colorSpace='rgb')
        dots_54.refreshDots()
        response_3.keys = []
        response_3.rt = []
        _response_3_allKeys = []
        key_skip_3.keys = []
        key_skip_3.rt = []
        _key_skip_3_allKeys = []
        # keep track of which components have finished
        Dot_Show_5446Components = [polygon_3, movie_3, circle_3, dots_46, dots_54, response_3, Left_4, Right_4, key_skip_3]
        for thisComponent in Dot_Show_5446Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Dot_Show_5446" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_6
            
            #if response.keys == str(correct_answer) or response.keys == correct_answer:
            #     response.corr = 1
            #     continueRoutine = False
            #elif len(response.keys)>1:
            #    response.corr = -2
            #    continueRoutine = False
            
            if len(response_3.keys)>1:
                continueRoutine = False
            
            if str(expInfo['Task']) == "2 - with skip":
                if key_skip_3.keys == "space":
                    continueRoutine = False
            
            if movie_3.status == STARTED and logged == 0:
                Videoshowstart=timer.getTime()
                logged = 1
            
            
            # *polygon_3* updates
            
            # if polygon_3 is starting this frame...
            if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.tStart = t  # local t and not account for scr refresh
                polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_3.status = STARTED
                polygon_3.setAutoDraw(True)
            
            # if polygon_3 is active this frame...
            if polygon_3.status == STARTED:
                # update params
                pass
            
            # if polygon_3 is stopping this frame...
            if polygon_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_3.tStop = t  # not accounting for scr refresh
                    polygon_3.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_3.status = FINISHED
                    polygon_3.setAutoDraw(False)
            
            # *movie_3* updates
            
            # if movie_3 is starting this frame...
            if movie_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_3.frameNStart = frameN  # exact frame index
                movie_3.tStart = t  # local t and not account for scr refresh
                movie_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie_3.status = STARTED
                movie_3.setAutoDraw(True)
                movie_3.play()
            if movie_3.isFinished:  # force-end the routine
                continueRoutine = False
            
            # *circle_3* updates
            
            # if circle_3 is starting this frame...
            if circle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_3.frameNStart = frameN  # exact frame index
                circle_3.tStart = t  # local t and not account for scr refresh
                circle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_3.status = STARTED
                circle_3.setAutoDraw(True)
            
            # if circle_3 is active this frame...
            if circle_3.status == STARTED:
                # update params
                pass
            
            # *dots_46* updates
            
            # if dots_46 is starting this frame...
            if dots_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_46.frameNStart = frameN  # exact frame index
                dots_46.tStart = t  # local t and not account for scr refresh
                dots_46.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_46, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_46.status = STARTED
                dots_46.setAutoDraw(True)
            
            # if dots_46 is active this frame...
            if dots_46.status == STARTED:
                # update params
                pass
            
            # *dots_54* updates
            
            # if dots_54 is starting this frame...
            if dots_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_54.frameNStart = frameN  # exact frame index
                dots_54.tStart = t  # local t and not account for scr refresh
                dots_54.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_54, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_54.status = STARTED
                dots_54.setAutoDraw(True)
            
            # if dots_54 is active this frame...
            if dots_54.status == STARTED:
                # update params
                pass
            
            # *response_3* updates
            waitOnFlip = False
            
            # if response_3 is starting this frame...
            if response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_3.frameNStart = frameN  # exact frame index
                response_3.tStart = t  # local t and not account for scr refresh
                response_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                response_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response_3.status == STARTED and not waitOnFlip:
                theseKeys = response_3.getKeys(keyList=['right','left'], waitRelease=False)
                _response_3_allKeys.extend(theseKeys)
                if len(_response_3_allKeys):
                    response_3.keys = _response_3_allKeys[-1].name  # just the last key pressed
                    response_3.rt = _response_3_allKeys[-1].rt
                    # was this correct?
                    if (response_3.keys == str(correct)) or (response_3.keys == correct):
                        response_3.corr = 1
                    else:
                        response_3.corr = 0
            
            # *Left_4* updates
            
            # if Left_4 is starting this frame...
            if Left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_4.frameNStart = frameN  # exact frame index
                Left_4.tStart = t  # local t and not account for scr refresh
                Left_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_4.status = STARTED
                Left_4.setAutoDraw(True)
            
            # if Left_4 is active this frame...
            if Left_4.status == STARTED:
                # update params
                pass
            
            # *Right_4* updates
            
            # if Right_4 is starting this frame...
            if Right_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_4.frameNStart = frameN  # exact frame index
                Right_4.tStart = t  # local t and not account for scr refresh
                Right_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_4.status = STARTED
                Right_4.setAutoDraw(True)
            
            # if Right_4 is active this frame...
            if Right_4.status == STARTED:
                # update params
                pass
            
            # *key_skip_3* updates
            waitOnFlip = False
            
            # if key_skip_3 is starting this frame...
            if key_skip_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_skip_3.frameNStart = frameN  # exact frame index
                key_skip_3.tStart = t  # local t and not account for scr refresh
                key_skip_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_skip_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_skip_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_skip_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_skip_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_skip_3.status == STARTED and not waitOnFlip:
                theseKeys = key_skip_3.getKeys(keyList=['space'], waitRelease=False)
                _key_skip_3_allKeys.extend(theseKeys)
                if len(_key_skip_3_allKeys):
                    key_skip_3.keys = _key_skip_3_allKeys[-1].name  # just the last key pressed
                    key_skip_3.rt = _key_skip_3_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Dot_Show_5446Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dot_Show_5446" ---
        for thisComponent in Dot_Show_5446Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_6
        #DotsshowRT = timer.getTime()-Dotsshowstart
        Videoshowstop=timer.getTime()
        VideoshowRT=Videoshowstop- Videoshowstart
        
        #thisExp.addData('DotsshowRT', DotsshowRT)
        thisExp.addData('Videoshowstart', Videoshowstart)
        thisExp.addData('Videoshowstop', Videoshowstop)
        thisExp.addData('VideoshowRT', VideoshowRT)
        
        logged = 0
        
        # For Feedback Page
        if flag_5446 == True:
            if key_skip_3.keys=="space":
                feedback_txt = 'Skipped 0'
                current_score = 0
            elif response_3.keys is None or len(response_3.keys) < 1:
                feedback_txt = 'Too late -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
            elif response_3.corr == 1:
                feedback_txt = 'Correct +1'
                feedback_col = [1.000,1.000,1.000]
                total_score += 1
                current_score = 1
            elif response_3.corr == 0:
                feedback_txt = 'Incorrect -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
        movie_3.stop()
        # check responses
        if response_3.keys in ['', [], None]:  # No response was made
            response_3.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               response_3.corr = 1;  # correct non-response
            else:
               response_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_5446 (TrialHandler)
        trials_5446.addData('response_3.keys',response_3.keys)
        trials_5446.addData('response_3.corr', response_3.corr)
        if response_3.keys != None:  # we had a response
            trials_5446.addData('response_3.rt', response_3.rt)
        # check responses
        if key_skip_3.keys in ['', [], None]:  # No response was made
            key_skip_3.keys = None
        trials_5446.addData('key_skip_3.keys',key_skip_3.keys)
        if key_skip_3.keys != None:  # we had a response
            trials_5446.addData('key_skip_3.rt', key_skip_3.rt)
        # the Routine "Dot_Show_5446" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_7.setText(feedback_txt)
        # Run 'Begin Routine' code from code_18
        if flag_5446 == False:
            continueRoutine = False
        # keep track of which components have finished
        feedback_3Components = [text_7]
        for thisComponent in feedback_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            
            # if text_7 is starting this frame...
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_7.status = STARTED
                text_7.setAutoDraw(True)
            
            # if text_7 is active this frame...
            if text_7.status == STARTED:
                # update params
                pass
            
            # if text_7 is stopping this frame...
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    # update status
                    text_7.status = FINISHED
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_3" ---
        for thisComponent in feedback_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_18
        thisExp.addData('total_score', total_score)
        thisExp.addData('Dot_ratio', '54:46')
        thisExp.addData('current_score', current_score)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_5446'
    
    # get names of stimulus parameters
    if trials_5446.trialList in ([], [None], None):
        params = []
    else:
        params = trials_5446.trialList[0].keys()
    # save data for this loop
    trials_5446.saveAsText(filename + 'trials_5446.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_5149 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("Rewa_Sequence_" + expInfo['Deadline'] + ".xlsx"),
        seed=None, name='trials_5149')
    thisExp.addLoop(trials_5149)  # add the loop to the experiment
    thisTrial_5149 = trials_5149.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5149.rgb)
    if thisTrial_5149 != None:
        for paramName in thisTrial_5149:
            exec('{} = thisTrial_5149[paramName]'.format(paramName))
    
    for thisTrial_5149 in trials_5149:
        currentLoop = trials_5149
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5149.rgb)
        if thisTrial_5149 != None:
            for paramName in thisTrial_5149:
                exec('{} = thisTrial_5149[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_13
        if total_score > 149:
            trials.finished = True
            break
        
        if flag_5149 == False:
            continueRoutine = False
            trials_5149.finished = True
            break
        # keep track of which components have finished
        Fixation_4Components = [fix_5]
        for thisComponent in Fixation_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_5* updates
            
            # if fix_5 is starting this frame...
            if fix_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_5.frameNStart = frameN  # exact frame index
                fix_5.tStart = t  # local t and not account for scr refresh
                fix_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_5.status = STARTED
                fix_5.setAutoDraw(True)
            
            # if fix_5 is active this frame...
            if fix_5.status == STARTED:
                # update params
                pass
            
            # if fix_5 is stopping this frame...
            if fix_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_5.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_5.tStop = t  # not accounting for scr refresh
                    fix_5.frameNStop = frameN  # exact frame index
                    # update status
                    fix_5.status = FINISHED
                    fix_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_4" ---
        for thisComponent in Fixation_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        image_4.setImage(screenshot)
        # Run 'Begin Routine' code from code_19
        if flag_5149 == False:
            continueRoutine = False
        # keep track of which components have finished
        screenshot_4Components = [image_4, circle_8, fix_8, Right_8, Left_8]
        for thisComponent in screenshot_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "screenshot_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # if image_4 is stopping this frame...
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    # update status
                    image_4.status = FINISHED
                    image_4.setAutoDraw(False)
            
            # *circle_8* updates
            
            # if circle_8 is starting this frame...
            if circle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_8.frameNStart = frameN  # exact frame index
                circle_8.tStart = t  # local t and not account for scr refresh
                circle_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_8.status = STARTED
                circle_8.setAutoDraw(True)
            
            # if circle_8 is active this frame...
            if circle_8.status == STARTED:
                # update params
                pass
            
            # if circle_8 is stopping this frame...
            if circle_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_8.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_8.tStop = t  # not accounting for scr refresh
                    circle_8.frameNStop = frameN  # exact frame index
                    # update status
                    circle_8.status = FINISHED
                    circle_8.setAutoDraw(False)
            
            # *fix_8* updates
            
            # if fix_8 is starting this frame...
            if fix_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_8.frameNStart = frameN  # exact frame index
                fix_8.tStart = t  # local t and not account for scr refresh
                fix_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix_8.status = STARTED
                fix_8.setAutoDraw(True)
            
            # if fix_8 is active this frame...
            if fix_8.status == STARTED:
                # update params
                pass
            
            # if fix_8 is stopping this frame...
            if fix_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_8.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_8.tStop = t  # not accounting for scr refresh
                    fix_8.frameNStop = frameN  # exact frame index
                    # update status
                    fix_8.status = FINISHED
                    fix_8.setAutoDraw(False)
            
            # *Right_8* updates
            
            # if Right_8 is starting this frame...
            if Right_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_8.frameNStart = frameN  # exact frame index
                Right_8.tStart = t  # local t and not account for scr refresh
                Right_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_8.status = STARTED
                Right_8.setAutoDraw(True)
            
            # if Right_8 is active this frame...
            if Right_8.status == STARTED:
                # update params
                pass
            
            # if Right_8 is stopping this frame...
            if Right_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Right_8.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Right_8.tStop = t  # not accounting for scr refresh
                    Right_8.frameNStop = frameN  # exact frame index
                    # update status
                    Right_8.status = FINISHED
                    Right_8.setAutoDraw(False)
            
            # *Left_8* updates
            
            # if Left_8 is starting this frame...
            if Left_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_8.frameNStart = frameN  # exact frame index
                Left_8.tStart = t  # local t and not account for scr refresh
                Left_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_8.status = STARTED
                Left_8.setAutoDraw(True)
            
            # if Left_8 is active this frame...
            if Left_8.status == STARTED:
                # update params
                pass
            
            # if Left_8 is stopping this frame...
            if Left_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Left_8.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Left_8.tStop = t  # not accounting for scr refresh
                    Left_8.frameNStop = frameN  # exact frame index
                    # update status
                    Left_8.status = FINISHED
                    Left_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in screenshot_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot_4" ---
        for thisComponent in screenshot_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dots_Show_5149" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_9
        
        # Get the value of a parameter from the loop
        #correct_answer = current_trial['correct']
        #print('correct_answer',correct_answer)
        
        if flag_5149 == False:
            continueRoutine = False
            
        # Get the duration of each loop
        Dotsshowstart=timer.getTime()
        movie_4.setMovie(Countdown)
        dots_49.setColor(color2, colorSpace='rgb')
        dots_49.refreshDots()
        dots_51.setColor(color1, colorSpace='rgb')
        dots_51.refreshDots()
        response_4.keys = []
        response_4.rt = []
        _response_4_allKeys = []
        key_skip_4.keys = []
        key_skip_4.rt = []
        _key_skip_4_allKeys = []
        # keep track of which components have finished
        Dots_Show_5149Components = [movie_4, circle_5, dots_49, dots_51, response_4, Left_5, Right_5, key_skip_4]
        for thisComponent in Dots_Show_5149Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Dots_Show_5149" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_9
            
            #if response.keys == str(correct_answer) or response.keys == correct_answer:
            #     response.corr = 1
            #     continueRoutine = False
            #elif len(response.keys)>1:
            #    response.corr = -2
            #    continueRoutine = False
            
            if len(response_4.keys)>1:
                continueRoutine = False
                
            if str(expInfo['Task']) == "2 - with skip":
                if key_skip_4.keys == "space":
                    continueRoutine = False
            
            if movie_4.status == STARTED and logged == 0:
                Videoshowstart=timer.getTime()
                logged = 1
            
            
            # *movie_4* updates
            
            # if movie_4 is starting this frame...
            if movie_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_4.frameNStart = frameN  # exact frame index
                movie_4.tStart = t  # local t and not account for scr refresh
                movie_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie_4.status = STARTED
                movie_4.setAutoDraw(True)
                movie_4.play()
            if movie_4.isFinished:  # force-end the routine
                continueRoutine = False
            
            # *circle_5* updates
            
            # if circle_5 is starting this frame...
            if circle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_5.frameNStart = frameN  # exact frame index
                circle_5.tStart = t  # local t and not account for scr refresh
                circle_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                circle_5.status = STARTED
                circle_5.setAutoDraw(True)
            
            # if circle_5 is active this frame...
            if circle_5.status == STARTED:
                # update params
                pass
            
            # *dots_49* updates
            
            # if dots_49 is starting this frame...
            if dots_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_49.frameNStart = frameN  # exact frame index
                dots_49.tStart = t  # local t and not account for scr refresh
                dots_49.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_49, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_49.status = STARTED
                dots_49.setAutoDraw(True)
            
            # if dots_49 is active this frame...
            if dots_49.status == STARTED:
                # update params
                pass
            
            # *dots_51* updates
            
            # if dots_51 is starting this frame...
            if dots_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dots_51.frameNStart = frameN  # exact frame index
                dots_51.tStart = t  # local t and not account for scr refresh
                dots_51.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dots_51, 'tStartRefresh')  # time at next scr refresh
                # update status
                dots_51.status = STARTED
                dots_51.setAutoDraw(True)
            
            # if dots_51 is active this frame...
            if dots_51.status == STARTED:
                # update params
                pass
            
            # *response_4* updates
            waitOnFlip = False
            
            # if response_4 is starting this frame...
            if response_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_4.frameNStart = frameN  # exact frame index
                response_4.tStart = t  # local t and not account for scr refresh
                response_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                response_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response_4.status == STARTED and not waitOnFlip:
                theseKeys = response_4.getKeys(keyList=['right','left'], waitRelease=False)
                _response_4_allKeys.extend(theseKeys)
                if len(_response_4_allKeys):
                    response_4.keys = _response_4_allKeys[-1].name  # just the last key pressed
                    response_4.rt = _response_4_allKeys[-1].rt
                    # was this correct?
                    if (response_4.keys == str(correct)) or (response_4.keys == correct):
                        response_4.corr = 1
                    else:
                        response_4.corr = 0
            
            # *Left_5* updates
            
            # if Left_5 is starting this frame...
            if Left_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_5.frameNStart = frameN  # exact frame index
                Left_5.tStart = t  # local t and not account for scr refresh
                Left_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                Left_5.status = STARTED
                Left_5.setAutoDraw(True)
            
            # if Left_5 is active this frame...
            if Left_5.status == STARTED:
                # update params
                pass
            
            # *Right_5* updates
            
            # if Right_5 is starting this frame...
            if Right_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_5.frameNStart = frameN  # exact frame index
                Right_5.tStart = t  # local t and not account for scr refresh
                Right_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                Right_5.status = STARTED
                Right_5.setAutoDraw(True)
            
            # if Right_5 is active this frame...
            if Right_5.status == STARTED:
                # update params
                pass
            
            # *key_skip_4* updates
            waitOnFlip = False
            
            # if key_skip_4 is starting this frame...
            if key_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_skip_4.frameNStart = frameN  # exact frame index
                key_skip_4.tStart = t  # local t and not account for scr refresh
                key_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_skip_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_skip_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_skip_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_skip_4.status == STARTED and not waitOnFlip:
                theseKeys = key_skip_4.getKeys(keyList=['space'], waitRelease=False)
                _key_skip_4_allKeys.extend(theseKeys)
                if len(_key_skip_4_allKeys):
                    key_skip_4.keys = _key_skip_4_allKeys[-1].name  # just the last key pressed
                    key_skip_4.rt = _key_skip_4_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Dots_Show_5149Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dots_Show_5149" ---
        for thisComponent in Dots_Show_5149Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_9
        #DotsshowRT = timer.getTime()-Dotsshowstart
        Videoshowstop=timer.getTime()
        VideoshowRT=Videoshowstop- Videoshowstart
        
        #thisExp.addData('DotsshowRT', DotsshowRT)
        thisExp.addData('Videoshowstart', Videoshowstart)
        thisExp.addData('Videoshowstop', Videoshowstop)
        thisExp.addData('VideoshowRT', VideoshowRT)
        
        logged = 0
        
        # For Feedback Page
        if flag_5149 == True:
            if key_skip_4.keys=="space":
                feedback_txt = 'Skipped 0'
                current_score = 0
            elif response_4.keys is None or len(response_4.keys) < 1:
                feedback_txt = 'Too late -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
            elif response_4.corr == 1:
                feedback_txt = 'Correct +1'
                feedback_col = [1.000,1.000,1.000]
                total_score += 1
                current_score = 1
            elif response_4.corr == 0:
                feedback_txt = 'Incorrect -2'
                feedback_col = [0.404,-1.000,-1.000]
                total_score -= 2
                current_score = -2
        
        movie_4.stop()
        # check responses
        if response_4.keys in ['', [], None]:  # No response was made
            response_4.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               response_4.corr = 1;  # correct non-response
            else:
               response_4.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_5149 (TrialHandler)
        trials_5149.addData('response_4.keys',response_4.keys)
        trials_5149.addData('response_4.corr', response_4.corr)
        if response_4.keys != None:  # we had a response
            trials_5149.addData('response_4.rt', response_4.rt)
        # check responses
        if key_skip_4.keys in ['', [], None]:  # No response was made
            key_skip_4.keys = None
        trials_5149.addData('key_skip_4.keys',key_skip_4.keys)
        if key_skip_4.keys != None:  # we had a response
            trials_5149.addData('key_skip_4.rt', key_skip_4.rt)
        # the Routine "Dots_Show_5149" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_8.setText(feedback_txt)
        # Run 'Begin Routine' code from code_20
        if flag_5149 == False:
            continueRoutine = False
        # keep track of which components have finished
        feedback_4Components = [text_8]
        for thisComponent in feedback_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # if text_8 is stopping this frame...
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    # update status
                    text_8.status = FINISHED
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_4" ---
        for thisComponent in feedback_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_20
        thisExp.addData('total_score', total_score)
        thisExp.addData('Dot_ratio', '51:49')
        thisExp.addData('current_score', current_score)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_5149'
    
    # get names of stimulus parameters
    if trials_5149.trialList in ([], [None], None):
        params = []
    else:
        params = trials_5149.trialList[0].keys()
    # save data for this loop
    trials_5149.saveAsText(filename + 'trials_5149.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "score" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    scoreComponents = [text_2, text_5, key_resp, text_9]
    for thisComponent in scoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_8
        text_2.text = str(total_score)
        
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score" ---
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "score" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 15.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "End" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_10]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    
    # if text_10 is starting this frame...
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_10.started')
        # update status
        text_10.status = STARTED
        text_10.setAutoDraw(True)
    
    # if text_10 is active this frame...
    if text_10.status == STARTED:
        # update params
        pass
    
    # if text_10 is stopping this frame...
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.stopped')
            # update status
            text_10.status = FINISHED
            text_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
