#!/usr/bin/env python3

from os import makedirs, path
from jinja2 import FileSystemLoader, Environment

module = ("%02d" % int(input('Module number: ')))

exos = int(input('Number of exos: '))

file_loader = FileSystemLoader(path.join(path.dirname(path.realpath(__file__)), 'templates'))

env = Environment(loader=file_loader)

makefileTemplate = env.get_template('Makefile.jinja2')
mainTemplate = env.get_template('main.cpp.jinja2')
gitignoreTemplate = env.get_template('.gitignore.jinja2')

makedirs('module' + module, exist_ok=True)

gitignoreOutput = gitignoreTemplate.render()
gitignoreFile = open(path.join('module' + module, '.gitignore'), "w+")
gitignoreFile.write(gitignoreOutput)

for i in range(0, exos):
	exo = ("%02d" % i)

	exoPath = path.join('module' + module, 'ex' + exo)

	makedirs(exoPath, exist_ok=True)

	makefileOutput = makefileTemplate.render(exoNbr=exo)
	makefile = open(path.join(exoPath, 'Makefile'), "w+")
	makefile.write(makefileOutput)

	mainOutput = mainTemplate.render()
	mainFile = open(path.join(exoPath, 'main.cpp'), "w+")
	mainFile.write(mainOutput)
