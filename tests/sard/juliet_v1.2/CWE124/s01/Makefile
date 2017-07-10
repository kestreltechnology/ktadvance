CC=gcc
CPP=g++
DEBUG=-g
CFLAGS=-c
LFLAGS=-pthread

INCLUDES=-I ../../../testcasesupport

MAIN=main_linux.c
MAIN_OBJECT=$(MAIN:.c=.o)

C_SUPPORT_PATH=
C_SUPPORT_FILES=$(C_SUPPORT_PATH)io.c $(C_SUPPORT_PATH)std_thread.c
C_SUPPORT_OBJECTS=io.o std_thread.o

# only grab the .c files without "w32" or "wchar_t" in the name
C_SOURCES=$(filter-out $(wildcard x*w32*.c) $(wildcard x*wchar_t*.c),$(wildcard x*.c))
C_OBJECTS=$(C_SOURCES:.c=.o)

# only grab the .cpp files without "w32" or "wchar_t" in the name
CPP_SOURCES=$(filter-out $(wildcard CWE*w32*.cpp) $(wildcard CWE*wchar_t*.cpp),$(wildcard CWE*.cpp))
CPP_OBJECTS=$(CPP_SOURCES:.cpp=.o)

OBJECTS=$(MAIN_OBJECT) $(C_OBJECTS) $(C_SUPPORT_OBJECTS)
# TARGET is the only line in this file specific to the CWE
TARGET=CWE124_s01

all: $(TARGET)

$(TARGET) : $(OBJECTS)
	$(CPP) $(LFLAGS) $(OBJECTS) -o $(TARGET)

$(C_OBJECTS) : $(C_SOURCES)
	$(CC) $(CFLAGS) $(INCLUDES) $(@:.o=.c) -o $@

$(CPP_OBJECTS) : $(CPP_SOURCES)
	$(CC) $(CFLAGS) $(INCLUDES) $(@:.o=.cpp) -o $@

$(C_SUPPORT_OBJECTS) : $(C_SUPPORT_FILES)
	$(CC) $(CFLAGS) $(INCLUDES) $(C_SUPPORT_PATH)$(@:.o=.c) -o $@

$(MAIN_OBJECT) : $(MAIN)
	$(CC) $(CFLAGS) $(INCLUDES) $(MAIN) -o $@

clean:
	rm -rf *.o $(TARGET)
