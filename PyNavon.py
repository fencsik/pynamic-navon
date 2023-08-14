#!/usr/bin/env python

import numpy as np
from numpy import sqrt
from math import floor
from psychopy import core, visual
from psychopy.hardware import keyboard

# set up Navon letters

class PynamicNavon:
    localHeight = .02
    localWidth = .015
    globalHeight = .25 # originally .2
    globalWidth = .2 # originally .15
    nY = 9
    localHeight = globalHeight/nY

    def __init__(self, win):
        self.letters = dict()
        let = list('ACDEFHLMNOTVX')
        self.xy = dict()
        for l in let:
            exec('self.xy[\'{}\'] = self._Generate{}()'.format(l, l))
        max_length = 0
        for k, pos in self.xy.items():
            if pos.shape[0] > max_length:
                max_length = pos.shape[0]
        self.max_length = max_length
        self.letters = sorted(self.xy)
        self._CreateComponents(win, max_length)

    def _CreateComponents(self, win, max_length):
        self.local_component_stim = []
        for i in range(self.max_length):
            self.local_component_stim.append(visual.TextBox2(
                win=win, name='local%02d' % i,
                text='+', pos=[0, 0],
                font='Arial', letterHeight=self.localHeight,
                alignment='center', bold=True,
                color='red', opacity=1,
                autoDraw=False))

    def GetLetters(self):
        return self.letters

    def Draw(self, letter, local_letter, color=None, center=(0, 0)):
        if not letter in self.xy:
            raise RuntimeError('requested letter "{}" not implemented'.format(letter))
        if len(local_letter) > 1:
            local_letter = local_letter[0]
        if len(center) != 2:
            # ignore center if it doesn't make sense
            center = (0, 0)
        pos = self.xy[letter]
        pos -= center
        for i in range(pos.shape[0]):
            self.local_component_stim[i].setPos(pos[i])
            self.local_component_stim[i].setText(local_letter)
            if color != None:
                self.local_component_stim[i].setColor(color)
            self.local_component_stim[i].draw()

    def Print(self):
        for k, v in self.xy.items():
            print(k, v)
        print('max length = {}'.format(self.max_length))
        print('letters = ', sorted(self.xy))

    def _GenerateA(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        xy = []
        for i in range(0,nY):
            xy.append([(1 + i - nY) / 2 / (nY - 1) * gw, (i - nY / 2) / nY * gh])
        for i in range(0,nY-1):
            xy.append([-(1 + i - nY) / 2 / (nY - 1) * gw, (i - nY / 2) / nY * gh])
        for i in range(int(nY/3),nY-int(nY/3)):
            xy.append([(.5 + i - nY / 2) / (nY - 3) * gw, -gh / 6])
        return(np.array(xy))

    def _GenerateC(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        xy = []
        for i in range(nY):
            xy.append([
                -sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
                (i - nY / 2) / nY * gh])
        for i in range(1, int(nY / 3)):
            xy.append([
                sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
                (i - nY / 2) / nY * gh])
        for i in range(int(2 * nY / 3), nY - 1):
            xy.append([
                sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
                (i - nY / 2) / nY * gh])
        i = .25
        xy.append([
            sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
            (i - nY / 2) / nY * gh])
        xy.append([
            -sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
            (i - nY / 2) / nY * gh])
        xy.append([
            sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
            -(1 + i - nY / 2) / nY * gh])
        xy.append([
            -sqrt(.25 - ((.5 + i - nY / 2) / (nY - 1))**2) * gw,
            -(1 + i - nY / 2) / nY * gh])
        return(np.array(xy))

    def _GenerateD(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,floor(nY/2)):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,gh/2-lh])
        for i in range(1,floor(nY/2)):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-gh/2])
        for i in range(0,nY):
            xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        i = .25
        xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,-(1+i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateE(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,gh/2-lh])
        for i in range(1,nY-1):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-lh/2])
        for i in range(1,nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-gh/2])
        return(np.array(xy))

    def _GenerateF(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,gh/2-lh])
        for i in range(1,nY-2):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-lh/2])
        return(np.array(xy))

    def _GenerateH(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,nY-1):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-lh/2])
        for i in range(nY):
            xy.append([gw/2,(i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateL(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,-gh/2])
        return(np.array(xy))

    def _GenerateM(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2-gw/2/nY,(i-nY/2)/nY*gh])
        for i in range(0,nY-1):
            xy.append([i/2/(nY-1)*gw,(i-nY/2)/nY*gh])
        for i in range(1,nY-1):
            xy.append([-i/2/(nY-1)*gw,(i-nY/2)/nY*gh])
        for i in range(nY):
            xy.append([gw/2+gw/2/nY,(i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateN(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([-gw/2,(i-nY/2)/nY*gh])
        for i in range(1,nY-1):
            xy.append([-(.5+i-nY/2)/(nY-1)*gw,(i-nY/2)/nY*gh])
        for i in range(nY):
            xy.append([gw/2,(i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateO(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(0,nY):
            xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        for i in range(nY-1):
            xy.append([-sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        i = .25
        xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        xy.append([-sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,(i-nY/2)/nY*gh])
        xy.append([sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,-(1+i-nY/2)/nY*gh])
        xy.append([-sqrt(.25-((.5+i-nY/2)/(nY-1))**2)*gw,-(1+i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateT(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,gh/2-lh])
        for i in range(nY-1):
            xy.append([0,(i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateV(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(0,nY):
            xy.append([i/2/(nY-1)*gw,(i-nY/2)/nY*gh])
        for i in range(1,nY):
            xy.append([-i/2/(nY-1)*gw,(i-nY/2)/nY*gh])
        return(np.array(xy))

    def _GenerateX(self):
        nY = self.nY
        gw = self.globalWidth
        gh = self.globalHeight
        lh = self.localHeight
        xy = []
        for i in range(0,nY):
            xy.append([-(.5+i-nY/2)/(nY-1)*gw,(i-nY/2)/nY*gh])
        for i in range(0,nY):
            xy.append([(.5+i-nY/2)/(nY-1)*gw,(i-nY/2)/nY*gh])
        return(np.array(xy))

screen_size = (1792, 1120)
win = visual.Window(
    size=screen_size, fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='Default', color=[0, 0, 0], colorSpace='rgb',
    backgroundImage=None, backgroundFit=None,
    blendMode='avg', useFBO=True,
    units='height')
win.mouseVisible = False
keyboard = keyboard.Keyboard()
letters = PynamicNavon(win)
x = letters.GetLetters()
y = x.copy()
np.random.shuffle(y)
for i in range(len(x)):
    win.clearBuffer()
    letters.Draw(x[i], y[i], 'white')
    win.flip()
    keys = keyboard.waitKeys()
    if keys[0].name in ('q', 'Q', 'escape'):
        core.quit()
win.close()
core.quit()
