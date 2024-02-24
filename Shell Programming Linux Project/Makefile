CC = gcc
CFLAGS = -Wall -std=c99

all: children processes

children: children.c
        $(CC) $(CFLAGS) -o $@ $<

processes: processes.c
        $(CC) $(CFLAGS) -o $@ $<

clean:
        rm -f children processes
