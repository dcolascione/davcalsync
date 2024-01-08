from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('davcalsync', base=base)
]

setup(name='davcalsync',
      version = '1.0',
      description = 'Yet another calendar sync tool',
      options = {'build_exe': build_options},
      executables = executables)
