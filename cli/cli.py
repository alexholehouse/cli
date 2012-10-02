# Collection of tools for easy command line interface

import os
import sys


#--------------------------------------------------------
class CommandlineInterfaceError(BaseException):
    pass



#--------------------------------------------------------
# Print a row of $character, the width of the terminal,
# or print width*offset.
#
# If offset is 0 or less, or greater than 1 it is ignored
#
def print_terminal_line(character, offset=1):
    rows, columns = os.popen('stty size', 'r').read().split()
    if (offset <= 1 and offset > 0):
        print character * int(float(columns) * float(offset))
        
    else:
        print character * int(columns)

        
def print_in_middle(message, border=" "):
    rows, columns = os.popen('stty size', 'r').read().split()
    length_of_message = len(message)
    offset  = 1 + length_of_message%2
    print border + " " * int((float(columns)/2-(float(length_of_message)/2))) + message + " " * int(float(columns)/2-(float(length_of_message)/2)-offset) + border
    



#--------------------------------------------------------
# Asks if the user wants to continue or not. $default can 
# be "N" or "Y" to specifiy if the default behavour is
# true or false

#
def yes_or_no(message, default="N"):
    

    if (default == "N"):
        try:
            input_command = raw_input(message + " [y/N]: ")
        except KeyboardInterrupt:
            input_command = "n"
            
        if(input_command == "y" or input_command == "Y"):
            return True
        else:
            return False

    elif (default == "Y"):
        try:
            input_command = raw_input(message + " [Y/n]: ")
        except KeyboardInterrupt:
            input_command = "n"
        
        if(input_command == "n" or input_command == "N"):
            return False
        else:
            return True

    else:
        error_message = "ERROR in cli.yes_or_no() - invalid default specified: '" + default + "'"
        raise CommandlineInterfaceError(error_message);


def clear_screen():
    os.system('clear')

def error_and_quit(message):
    print "[FATAL ERROR] " + message
    print "Exiting ungracefully...\n"
    exit(1)

def error_and_continue(message):
    print "[ERROR] " + message
    

def warning_and_continue(message):
    print "[WARNING] " + message




#--------------------------------------------------------
# Sometimes you need a cat
#
def print_cat():
    
    print "\
                  ;,_            ,\n\
                 _uP~'b          d'u,\n\
                dP'   'b       ,d'  'o\n\
               d'    , `b     d''    'b\n\
              l] [    ' `l,  d'       lb\n\
              Ol ?     '  'b`'=uoqo,_  'l\n\
            ,dBb 'b        'b,    `'~~TObup,_\n\
          ,d' (db.`'         ''     'tbc,_ `~'Yuu,_\n\
        .d' l`T'  '=                      ~     `''Yu,\n\
      ,dO` gP,                           `u,   b,_  'b7\n\
     d?' ,d' l,                           `'b,_ `~b  '1\n\
   ,8i' dl   `l                 ,ggQOV',dbgq,._'  `l  lb\n\
  .df' (O,    '             ,ggQY'~  , @@@@@d'bd~  `b '1\n\
 .df'   `'           -=@QgpOY''     (b  @@@@P db    `Lp'b,\n\
.d(                  _               'ko '=d_,Q`  ,_  '  'b,\n\
Ql         .         `'qo,._          'tQo,_`''bo ;tb,    `'b,\n\
qQ         |L           ~'QQQgggc,_.,dObc,opooO  `'~~';.   __,7,\n\
qp         t\io,_           `~'TOOggQV''''        _,dg,_ =PIQHib.\n\
`qp        `Q['tQQQo,_                          ,pl{QOP''   7AFR`\n\
  `         `tb  '''tQQQg,_             p' 'b   `       .;-.`Vl'\n\
             'Yb      `'tQOOo,__    _,edb    ` .__   /`/'|  |b;=;.__\n\
                           `'tQQQOOOOP''`'\QV;qQObob'`-._`\_~~-._\n\
                                ''''    ._        /   | |oP'\_   ~\ ~\_~\n\
                                        `~'\ic,qggddOOP'|  |  ~\   `\~-._\n\
                                          ,qP`'''|'   | `\ `;   `\   `\n\
                               _        _,p'     |    |   `\`;    |    |\n\
                                      'boo,._dP'       `\_  `\    `\|   `\   ;\n\
                                      `'7tY~'            `\  `\    `|_   |\n\
                                                               `~\  |\n\
"
