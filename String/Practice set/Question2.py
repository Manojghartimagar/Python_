#write a program to fill in a letter template given below with name and date 
letter ='''dear </Name/>,
             you are selected!
          </Date/>'''
print((letter.replace("</Name/>","Manoj")).replace("</Date/>","2026-02-04"))