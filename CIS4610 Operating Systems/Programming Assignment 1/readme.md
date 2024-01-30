Operating Systems

Programming Project #1 Total Points: 25

1. Write a program in Java which creates producer and consumer threads. The
producer should “produce” by setting the elements of an array of integers to
FULL. The consumer should “consume” by setting the elements of an array of
integers to EMPTY.

Make sure you properly handle the following situations:
• A producer (consumer) producing (consuming) past the end (beginning) of the
buffer
• A producer writing to an array element that is not EMPTY and a consumer
reading (i.e. setting the array element to EMPTY) from an array element that is
not FULL.
• Use wait() and notify() to avoid errors producing and consuming and to ensure
thread synchronization.

Include your program, along with screenshots showing it run correctly for each of the
following cases:
When the buffer is full, and Producer is waiting
When the buffer is empty, and Consumer is waiting
Something in between where the buffer is partially full.

17 points

3. Write a program in C which functions as a DOS command interpreter. DOS uses
the commands cd, dir, type, del, ren, and copy to do the same functions as the
UNIX commands cd, ls, cat, rm, mv, and cp. Your program loops continuously,
allowing the user to type in DOS commands, which are stored in the variables
command, arg1 and arg2. The command should be considered by a case
statement, which executes an appropriate UNIX command, depending on which
DOS command has been given. The program should echo the following
instruction to the user: Type Ctrl-C to exit.
Include your program, along with output showing it run correctly as follows:
For the interpreter:

For commands like cp you can ignore flags like -r and just provide the arguments.
For error checking you can tell the user you have entered too many or too few
arguments. You do not need to correct the number of arguments the user enters.
File path names need not allow whitespace chars.
You should provide screen shots of the effect of each of the commands before and
after the execution of each command. You can use pwd to show the pathname before
and after the command is executed.
