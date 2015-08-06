from scene import *
from random import *
import time
import sys
class Particle(object):
    def __init__(self, wh):
        self.w = wh.w
        self.h = wh.h
        self.x = randint(0, self.w)
        self.y = randint(0, self.h)
        self.vx = randint(-10, 20)
        self.vy = randint(-10, 20)
        self.colour = Color(random(), random(), random())

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98
        self.vy *= 0.98
        if self.x > self.w:
            self.x = self.w
            self.vx *= -1
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.y > self.h:
            self.y = self.h
            self.vy *= -1
        if self.y < 0:
            self.y = 0
            self.vy *= -1
    def draw(self):
        fill(*self.colour)
        rect(self.x, self.y, 8, 8)

class Intro(Scene):
    def setup(self):
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))
    def draw(self):
        background(0.00, 0.05, 0.20)
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())

        s = 47 if self.size.w > 100 else 7
        text('Welcome to\n  Jitter Tap\n\n\n', 'Futura', s, *self.bounds.center().as_tuple())
        t = 100 if self.size.w > 100 else 7
        text('\n🔴', 'Futura', t, *self.bounds.center().as_tuple())
        s = 27 if self.size.w > 100 else 7
        text('\n\n\n\n\n\n\n\n\n\n\n\nBy: Adedayo Ogunnoiki', 'Futura', s, *self.bounds.center().as_tuple())

    def touch_ended(self, touch):
        run(Help1())

import motion, scene
use_motion = True

class Help1(Scene):
    def setup(self):
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))

    def draw(self):
        background(0.00, 0.05, 0.20)
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())

        s = 35 if self.size.w > 100 else 7
        text('You will have to\nclick the button\na 100 times as\nquickly as possible.\nThen your time\nand the speed\nat which you\nwere clicking will\nbe displayed.', 'Futura', s, *self.bounds.center().as_tuple())

    def touch_ended(self, touch):
        run(Help2())

class Help2(Scene):
    def setup(self):
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))

    def draw(self):
        background(0.00, 0.05, 0.20)
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())

        s = 45 if self.size.w > 100 else 7
        text('Also, you can\nclick the ❎\nat the top\nright of the\nscreen to exit.', 'Futura', s, *self.bounds.center().as_tuple())

    def touch_ended(self, touch):
        run(JitterClick())

import time
from scene import *
from PIL import Image
class JitterClick(Scene):
    def __init__(self):
        self.start_time = 0
        self.finish_time = 0
        self.clicks = 0

    def setup(self):
        self.button = Button(Rect(self.size.w/2-100, self.size.h/2-140, 200, 200))
        self.button.background = Color(0,0.05,0.2)
        self.button.stroke = Color(0,0.05,0.2)
        self.button.image = 'Red_Circle'
        self.button.action = self.add_clicks
        self.add_layer(self.button)
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))

    def add_clicks( self):
        self.clicks += 1
        if self.clicks == 1:
            self.start_time = time.time()

    def draw(self):
        background(0,0.05,0.2)
        self.button.background = Color(0,0.05,0.2)
        self.button.draw()
        text('Taps: %i' % self.clicks, x=self.size.w/2, y=self.size.h/3.8*3, font_size=57)
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())
        if self.clicks == 100:
            self.finish_time = time.time()
            run(desp(self.clicks, self.finish_time - self.start_time))

class desp(Scene):
    def __init__(self, xclicks, duration):
        self.xclicks = xclicks
        self.duration = duration
        self.duration =  "%.3f" % self.duration
        self.speed = duration/xclicks
        self.speed =  "%.3f" % self.speed

    def setup(self):
        self.show_instructions = True
        self.p_size = 64 if self.size.w > 700 else 32
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))

    def draw(self):
        background(0, 0.05, 0.2)
        text('\n\n\n\n\n\nIt took you \n{} seconds \nto tap {} \ntimes. You were\ntapping at \n{} taps a\nsecond.'.format(self.duration, self.xclicks, self.speed), x=self.size.w/2, y=self.size.h/3.8*3, font_size=42)
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())

    def touch_ended(self, touch):
        run(restart())

class restart(Scene):
    def setup(self):
        self.button = Button(Rect(self.size.w/2-80, self.size.h/2--45, 150, 150), 'Restart')
        self.button.background = Color(0,0.05,0.2)
        self.button.stroke = Color(0,0.05,0.2)
        self.button.image = 'Blue_Circle'
        self.button.action = self.add_clicks
        self.add_layer(self.button)
        self.particles = []
        for p in xrange(200):
            self.particles.append(Particle(self.size))

    def add_clicks( sender):
        run(JitterClick())

    def draw(self):
        background(0,0.05,0.2)
        self.button.background = Color(0,0.05,0.2)
        self.button.draw()
        s = 45 if self.size.w > 100 else 7
        tint(255,255,255)
        text('\n\n\nOr you can\nclick the ❎\nat the top\nright of the\nscreen to exit.', 'Futura', s, *self.bounds.center().as_tuple())
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = Color(random(), random(), random())

run(Intro())

