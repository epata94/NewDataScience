'''
r"""OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)
'''


# 1. os 모듈의 파일과 디렉터리 관련 함수
import os
# 현재 작업 디렉터리 경로
os.getcwd() # 'D:\\Pywork\\workspace'
# 작업 디렉터리 변경
os.chdir('chapter08')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08'

# 현재 작업 디렉터리 목록
os.listdir('.') # list 반환 - ['.project', '.pydevproject', 'data', 'example', 'lecture']

# 디렉터리 생성
os.mkdir('test')
os.listdir('.') # ['.project', '.pydevproject', 'data', 'example', 'lecture', 'test']

# 디렉터리 이동
os.chdir('test')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08\\test'

# 여러 디렉터리 생성
os.makedirs('test2/test3')
os.listdir('.') # ['test2']

# 디렉터리 이동
os.chdir('test2')
os.listdir('.') # ['test3']

# 디렉터리 삭제
os.rmdir('test3')
os.listdir('.') # []

# 상위 디렉터리 이동
os.chdir('../..')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08'

# 여러 개의 디렉터리 삭제
os.removedirs('test/test2')
os.listdir('.') # ['.project', '.pydevproject', 'data', 'example', 'lecture']


# 2. os.path 모듈의 파일 경로 관련 함수
import os.path # windows 파일 경로를 조작하는 모듈

dir(os.path)
'''
['abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
'''
os.getcwd() # 'D:\\Pywork\\workspace'
os.chdir('chapter08')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08'

os.path.abspath('lecture/step01_try_except.py')
#'D:\\Pywork\\workspace\\chapter08\\lecture\\step01_try_except.py'
os.path.dirname('lecture/step01_try_except.py')
#'lecture'
os.path.exists('D:\\Pywork\\workspace') # True

os.path.isfile('lecture/step01_try_except.py') # True
os.path.isdir('lecture') # True

os.path.split("c:\\test\\test1.txt") # ('c:\\test', 'test1.txt')
os.path.join('c:\\test', 'test1.txt') # 'c:\\test\\test1.txt'

os.path.getsize('lecture/step01_try_except.py') # 1883 byte

# 3. glob 모듈의 파일 경로 관련 함수
import glob
help(glob)
#  glob - Filename globbing utility.
'''
NAME
    glob - Filename globbing utility.
FUNCTIONS
    escape(pathname)
        Escape all special characters.
    
    glob(pathname, *, recursive=False)
        Return a list of paths matching a pathname pattern.
        
        The pattern may contain simple shell-style wildcards a la
        fnmatch. However, unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns.
        
        If recursive is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.
    
    iglob(pathname, *, recursive=False)
        Return an iterator which yields the paths matching a pathname pattern.
        
        The pattern may contain simple shell-style wildcards a la
        fnmatch. However, unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns.
        
        If recursive is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.
DATA
    __all__ = ['glob', 'iglob', 'escape']
FILE
    c:\python37\lib\glob.py
'''
print(dir(glob))
'''
'escape', 'fnmatch', 'glob', 'glob0', 'glob1', 'has_magic', 'iglob', 'magic_check', 'magic_check_bytes', 'os', 're']
'''

glob.escape()

'''
유니스 셀이 사용하는 규칙에 따라 지정된 패턴과 일치하는 모든 경로명을 찾는다.
결과는 무순서로 반환된다.
*, ?, []로 표시되는 문자 범위는 올바르게 일치한다.
리터럴 일치를 위해서는 대괄호 안에 메타문자를 넣는다. 예를 들면 '[?]'는 '?'
문자와 일치한다.

glob.glob(pathname, *, recursive=False) :
경로 지정을 포함하는 문자열인 pathname에 일치하는 경로 이름의 비어있을 수 있는 리스트를 반환한다.
pathname은 절대경로와 상대경로를 지정할 수 있다.

glob.iglob(pathname, *, recursive=False)
glob()과 같은 값을 산출하지만 이터레이터를 반환한다.

glob.escape(pathname)
모든 특수문자(*, ?, [])를 이스케이프 처리한다. 특수문자가 들어있을 수 있는 임의의 
리터럴 문자열을 일치시키려는 경우에 유용하다. 
 '''

glob.glob('./[0-9].*')
#['./10.test', './20.gif']
glob.glob('*.exe')
#[test.exe, 10.exe, a.exe, 1.exe]
glob.glob('?.exe')
#[a.exe, 1.exe]
glob.glob('*.txt', recursive=True)
#[2.txt, 1.txt]

