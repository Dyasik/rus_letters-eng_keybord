# -*- coding: utf-8 -*-

from subprocess import run
from sys import platform

_dict = {
	'а': 'A',
	'б': '6',
	'в': 'B',
	'г': 'r',
	'д': 'g',
	'е': 'E',
	'ё': 'E',
	'ж': '>|<',
	'з': '3',
	'и': 'u',
	'й': 'u',
	'к': 'K',
	'л': '/\\',
	'м': 'M',
	'н': 'H',
	'о': 'O',
	'п': 'II',
	'р': 'P',
	'с': 'C',
	'т': 'T',
	'у': 'y',
	'ф': 'qp',
	'х': 'X',
	'ц': 'LL',
	'ч': '4',
	'ш': 'LL|',
	'щ': 'LLL',
	'ъ': '\'b',
	'ы': 'b|',
	'ь': 'b',
	'э': '-)',
	'ю': '|-0',
	'я': '9|'
}

while True:
	inp = input('Enter russian text (just press Enter to exit):\n')
	if (not len(inp)):
		break	

	res = list()
	for s in inp:
		let = _dict.get(s.lower(), False)
		res.append(let if let else s)

	res = ''.join(res)
	print(res)

	try:
		command = str()
		if platform == 'win32' or platform == 'cygwin':
			# windows
			command = 'clip'
		elif platform == 'linux':
			# linux
			command = 'xclip'
		elif platform == 'darwin':
			# mac
			command = 'pbcopy'

		run([command], input=res, encoding='utf-8').check_returncode()
	except Exception as e:
		print('Error during copying to clipboard: {0}'.format(e))
	else:
		print('Copied to clipboard!\n')
