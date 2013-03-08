# Makefile for C++ Programming on Windows


################################################################################
# test.debug.makefile
# test.vcxproj
# D:\GoogleCode\test\test
################################################################################
# stdafx.cpp
# test.cpp
################################################################################


PROGRAM = test


CPP = cl.exe

CPPSOURCES = stdafx.cpp test.cpp

CPPOBJECTS = $(CPPSOURCES:.cpp=.obj)

CPPFLAGS = /D "WIN32"	\
	/D "_DEBUG"	\
	/D "_CONSOLE"	\
	\
	/MDd	\
	/analyze-	\
	/I "D:\Lordol2Lib\library\STLport-5.2.1\stlport"	\
	/I "D:\Lordol2Lib\library\mysql 5.0\include"	\
	/I "D:\Lordol2Lib\library\boost_1_48_0"	\
	/I "D:\Lordol2Lib\library\libcurl-7.19.3-win32-ssl-msvc\include"	\
	\
	/Zc:forScope	\
	/Fo	\
	/EHsc	\
	/nologo	\
	/errorReport:queue	\
	/WX-	\
	/Od	\
	/Gd	\
	/Oy-	\
	/GS	\
	/Gm-	\
	/W3	\
	/Fa	\
	/Zc:wchar_t	\
	/fp:precise

LINKFLAGS = /SUBSYSTEM:CONSOLE	\
	/DYNAMICBASE	\
	/NOLOGO	\
	/NXCOMPAT	\
	/INCREMENTAL:NO	\
	/DEBUG	\
	/MACHINE:X86	\
	/MANIFEST	\
	/TLBID:1	\
	/ERRORREPORT:QUEUE	\
	/MANIFESTUAC:uiAccess='false'	\
	/ALLOWISOLATION	\
	/MANIFESTUAC:level='asInvoker'	\
	"kernel32.lib"	\
	"user32.lib"	\
	"gdi32.lib"	\
	"winspool.lib"	\
	"comdlg32.lib"	\
	"advapi32.lib"	\
	"shell32.lib"	\
	"ole32.lib"	\
	"oleaut32.lib"	\
	"uuid.lib"	\
	"odbc32.lib"	\
	"odbccp32.lib"	\
	/LIBPATH:"D:\Lordol2Lib\library\STLport-5.2.1\lib"	\
	/LIBPATH:"D:\Lordol2Lib\library\mysql 5.0\lib\debug"	\
	/LIBPATH:"D:\Lordol2Lib\library\libcurl-7.19.3-win32-ssl-msvc\lib\Debug"	\
	\
	



all: $(PROGRAM)


$(PROGRAM): $(CPPOBJECTS)
	link.exe /out:$(PROGRAM) \stdafx.obj \test.obj $(LINKFLAGS)


stdafx.obj: stdafx.cpp
	$(CPP) $(CPPFLAGS) /c stdafx.cpp

test.obj: test.cpp
	$(CPP) $(CPPFLAGS) /c test.cpp




clean:
	del $(CPPOBJECTS) $(PROGRAM)


run:
	$(PROGRAM)

