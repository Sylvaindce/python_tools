
CYTHON 			= 	/usr/bin/cython3
CYTHON_ARGS 	= 	--embed
CYTHON_OBJ 		= 	$(SRC:.py=.c)

GCC				= 	/usr/bin/gcc
GCC_INCLUDE 	= 	-Wall -Os -I/usr/include/python3.6m
GCC_ARGS		= 	-lpython3.6m -lpthread -lm -lutil -ldl

RM				= 	rm -f

SRC 			= 	hello.py
NAME			= 	hello_exec


all:				exec_cython exec_gcc

exec_cython:
					$(CYTHON) $(CYTHON_ARGS) -o $(CYTHON_OBJ) $(SRC)

exec_gcc:
					$(GCC) $(GCC_INCLUDE) -o $(NAME) $(CYTHON_OBJ) $(GCC_ARGS)

clean:
					$(RM) $(CYTHON_OBJ)

fclean:				clean
					$(RM) $(NAME)

re:					fclean all

.PHONY:				all clean fclean re
