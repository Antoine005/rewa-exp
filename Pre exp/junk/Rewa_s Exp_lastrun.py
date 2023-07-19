﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on July 11, 2023, at 16:00
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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = "Rewa's Exp"  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\AOE\\Desktop\\Rewa\\Rewa Exp-20230711T012626Z-002\\Rewa Exp\\Rewa_s Exp_lastrun.py',
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

# --- Initialize components for Routine "Instructions" ---
text = visual.TextStim(win=win, name='text',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation" ---
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot" ---
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
    nDots=60, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
dots_40 = visual.DotStim(
    win=win, name='dots_40',
    nDots=10, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
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

# --- Initialize components for Routine "feedback_1" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Fixation" ---
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot" ---
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

# --- Initialize components for Routine "Dots_show_5743" ---
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.255, 0.255)[0], height=(0.255, 0.255)[1],
    ori=45.0, pos=(0.1275, 0.1275), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
    opacity=None, depth=0.0, interpolate=True)
movie_2 = visual.MovieStim(
    win, name='movie_2',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-1
)
circle_2 = visual.Polygon(
    win=win, name='circle_2',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
red_dots_2 = visual.DotStim(
    win=win, name='red_dots_2',
    nDots=43, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-3.0)
green_dots_2 = visual.DotStim(
    win=win, name='green_dots_2',
    nDots=57, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
key_resp_2 = keyboard.Keyboard()
Right_3 = visual.ShapeStim(
    win=win, name='Right_3',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
Left_3 = visual.ShapeStim(
    win=win, name='Left_3',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "feedback_1" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Fixation" ---
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "screenshot" ---
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

# --- Initialize components for Routine "Dot_show_5446" ---
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.255, 0.255)[0], height=(0.255, 0.255)[1],
    ori=45.0, pos=(0.1275, 0.1275), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
    opacity=None, depth=0.0, interpolate=True)
movie_3 = visual.MovieStim(
    win, name='movie_3',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.92, 1.08), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-1
)
circle_3 = visual.Polygon(
    win=win, name='circle_3',
    edges=500, size=(0.6, 0.6),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
red_dots_3 = visual.DotStim(
    win=win, name='red_dots_3',
    nDots=43, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-3.0)
green_dots_3 = visual.DotStim(
    win=win, name='green_dots_3',
    nDots=57, dotSize=15.0,
    speed=0.0, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=0.5, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=-1.0,
    color='white', colorSpace='rgb', opacity=None,
    depth=-4.0)
key_resp_3 = keyboard.Keyboard()
Left_4 = visual.ShapeStim(
    win=win, name='Left_4',units='pix', 
    size=(150,150), vertices='circle',
    ori=0.0, pos=(-550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
Right_4 = visual.ShapeStim(
    win=win, name='Right_4',units='pix', 
    size=(150, 150), vertices='circle',
    ori=0.0, pos=(550, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "feedback_1" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "score" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=total_score,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = [text]
for thisComponent in InstructionsComponents:
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

# --- Run Routine "Instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
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
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    
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
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=18.0, method='random', 
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
    trials_6040 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rewa_Sequence.xlsx'),
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
        
        # --- Prepare to start Routine "Fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = [fix]
        for thisComponent in FixationComponents:
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
        
        # --- Run Routine "Fixation" ---
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
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(screenshot)
        # keep track of which components have finished
        screenshotComponents = [image, circle_4, fix_2, Right_2, Left_2]
        for thisComponent in screenshotComponents:
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
        
        # --- Run Routine "screenshot" ---
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
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
            for thisComponent in screenshotComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot" ---
        for thisComponent in screenshotComponents:
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
        current_trial = trials_6040.trialList[trials_6040.thisN]
        
        # Get the value of a parameter from the loop
        correct_answer = current_trial['correct']
        print('correct_answer',correct_answer)
        
        # Get the duration of each loop
        Dotsshowstart=timer.getTime()
        movie.setMovie(Countdown)
        dots_60.setColor(color1, colorSpace='rgb')
        dots_60.refreshDots()
        dots_40.setColor(color2, colorSpace='rgb')
        dots_40.refreshDots()
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        Dots_Show_6040Components = [polygon, movie, circle, dots_60, dots_40, response, Right, Left]
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
            
            if response.keys == str(correct_answer) or response.keys == correct_answer:
                 response.corr = 1
                 continueRoutine = False
            elif len(response.keys)>1:
                response.corr = -2
                continueRoutine = False
            
            #if response.corr == 1
            print('response.corr',response.corr)
            
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
        DotsshowRT = timer.getTime()-Dotsshowstart
        thisExp.addData('DotsshowRT', DotsshowRT)
        movie.stop()
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trials_6040.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials_6040.addData('response.rt', response.rt)
        # the Routine "Dots_Show_6040" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        print('response.keys',response.keys)
        print('response.corr',response.corr)
        if response.keys is None or len(response.keys) < 1:
            feedback_txt = 'Too late -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        elif response.corr == 1:
            feedback_txt = 'Correct +1'
            feedback_col = [1.000,1.000,1.000]
            total_score += 1
        elif response.corr == -2:
            feedback_txt = 'Incorrect -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        
        #feedback_end = 1
        
        text_3.setText(feedback_txt)
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_6040'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_5743 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rewa_Sequence.xlsx'),
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
        
        # --- Prepare to start Routine "Fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = [fix]
        for thisComponent in FixationComponents:
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
        
        # --- Run Routine "Fixation" ---
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
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(screenshot)
        # keep track of which components have finished
        screenshotComponents = [image, circle_4, fix_2, Right_2, Left_2]
        for thisComponent in screenshotComponents:
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
        
        # --- Run Routine "screenshot" ---
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
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
            for thisComponent in screenshotComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot" ---
        for thisComponent in screenshotComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dots_show_5743" ---
        continueRoutine = True
        # update component parameters for each repeat
        movie_2.setMovie(Countdown)
        red_dots_2.setColor(color2, colorSpace='rgb')
        red_dots_2.refreshDots()
        green_dots_2.setColor(color1, colorSpace='rgb')
        green_dots_2.refreshDots()
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        Dots_show_5743Components = [polygon_2, movie_2, circle_2, red_dots_2, green_dots_2, key_resp_2, Right_3, Left_3]
        for thisComponent in Dots_show_5743Components:
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
        
        # --- Run Routine "Dots_show_5743" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            
            # *red_dots_2* updates
            
            # if red_dots_2 is starting this frame...
            if red_dots_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_dots_2.frameNStart = frameN  # exact frame index
                red_dots_2.tStart = t  # local t and not account for scr refresh
                red_dots_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_dots_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_dots_2.status = STARTED
                red_dots_2.setAutoDraw(True)
            
            # if red_dots_2 is active this frame...
            if red_dots_2.status == STARTED:
                # update params
                pass
            
            # *green_dots_2* updates
            
            # if green_dots_2 is starting this frame...
            if green_dots_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_dots_2.frameNStart = frameN  # exact frame index
                green_dots_2.tStart = t  # local t and not account for scr refresh
                green_dots_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_dots_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                green_dots_2.status = STARTED
                green_dots_2.setAutoDraw(True)
            
            # if green_dots_2 is active this frame...
            if green_dots_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in Dots_show_5743Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dots_show_5743" ---
        for thisComponent in Dots_show_5743Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        movie_2.stop()
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials_5743.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_5743.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "Dots_show_5743" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        print('response.keys',response.keys)
        print('response.corr',response.corr)
        if response.keys is None or len(response.keys) < 1:
            feedback_txt = 'Too late -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        elif response.corr == 1:
            feedback_txt = 'Correct +1'
            feedback_col = [1.000,1.000,1.000]
            total_score += 1
        elif response.corr == -2:
            feedback_txt = 'Incorrect -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        
        #feedback_end = 1
        
        text_3.setText(feedback_txt)
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_5743'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_5446 = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # --- Prepare to start Routine "Fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = [fix]
        for thisComponent in FixationComponents:
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
        
        # --- Run Routine "Fixation" ---
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
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "screenshot" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(screenshot)
        # keep track of which components have finished
        screenshotComponents = [image, circle_4, fix_2, Right_2, Left_2]
        for thisComponent in screenshotComponents:
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
        
        # --- Run Routine "screenshot" ---
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
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
            for thisComponent in screenshotComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screenshot" ---
        for thisComponent in screenshotComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Dot_show_5446" ---
        continueRoutine = True
        # update component parameters for each repeat
        movie_3.setMovie(Countdown)
        red_dots_3.setColor(color2, colorSpace='rgb')
        red_dots_3.refreshDots()
        green_dots_3.setColor(color1, colorSpace='rgb')
        green_dots_3.refreshDots()
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        Dot_show_5446Components = [polygon_3, movie_3, circle_3, red_dots_3, green_dots_3, key_resp_3, Left_4, Right_4]
        for thisComponent in Dot_show_5446Components:
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
        
        # --- Run Routine "Dot_show_5446" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            
            # *red_dots_3* updates
            
            # if red_dots_3 is starting this frame...
            if red_dots_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_dots_3.frameNStart = frameN  # exact frame index
                red_dots_3.tStart = t  # local t and not account for scr refresh
                red_dots_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_dots_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_dots_3.status = STARTED
                red_dots_3.setAutoDraw(True)
            
            # if red_dots_3 is active this frame...
            if red_dots_3.status == STARTED:
                # update params
                pass
            
            # *green_dots_3* updates
            
            # if green_dots_3 is starting this frame...
            if green_dots_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_dots_3.frameNStart = frameN  # exact frame index
                green_dots_3.tStart = t  # local t and not account for scr refresh
                green_dots_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_dots_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                green_dots_3.status = STARTED
                green_dots_3.setAutoDraw(True)
            
            # if green_dots_3 is active this frame...
            if green_dots_3.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in Dot_show_5446Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Dot_show_5446" ---
        for thisComponent in Dot_show_5446Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        movie_3.stop()
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_5446.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_5446.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "Dot_show_5446" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        print('response.keys',response.keys)
        print('response.corr',response.corr)
        if response.keys is None or len(response.keys) < 1:
            feedback_txt = 'Too late -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        elif response.corr == 1:
            feedback_txt = 'Correct +1'
            feedback_col = [1.000,1.000,1.000]
            total_score += 1
        elif response.corr == -2:
            feedback_txt = 'Incorrect -2'
            feedback_col = [0.404,-1.000,-1.000]
            total_score -= 2
        
        #feedback_end = 1
        
        text_3.setText(feedback_txt)
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trials_5446'
    
    
    # --- Prepare to start Routine "score" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    scoreComponents = [text_2]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
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
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 18.0 repeats of 'trials'


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
