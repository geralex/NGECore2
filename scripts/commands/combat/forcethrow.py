import sys

def setup(core, actor, target, command):
	core.buffService.addBuffToCreature(target, 'fs_force_throw')
	return
	
def preRun(core, actor, target, command):
	return

def run(core, actor, target, commandString):
	return