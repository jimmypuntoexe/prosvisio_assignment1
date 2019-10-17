# 2019 assignment1

### DEVELOPERS
*Balducci Gianmaria 807141*

*Guidi Alessandro 808865*

### TARGET
Target is to set up a CI/CD pipeline to automate the entire development process and use the Gitlab CI/CD infrastructure to implement it


### APPLICATION
The application manages the sale of cinema tickets, through a database of several cinema in the area.

In this mode,it's possibile reserve tickets for cinema to watch your favorite film.

For the database,we used MySql,instead the application is was written using *Python*,  which used his library *mysql.connector* as interface.  

The database is made of four table:
*  Cinema: contains the information related to cinema(**Id**,Nome,Città)
*  Film: contains the movie information that you can see(**Id**,Titolo,Regista)
*  Clienti: contains the information of customer who have buy a tickets(**CF**,Nome,Cognome,Età)
*  Biglietto: contains tickets information of the chosen show(Posto,Fila,Sala,**DataTime**)

