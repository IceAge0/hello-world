from cx_Freeze import setup,Executable
executables=[
			Executable('J:/yh/py/2020.12-2021.1/zakura.py')
			]

setup(
	name="zakura2",
	version="0.1",
	description="sample cxfreeze script",
	executables=executables
	)

