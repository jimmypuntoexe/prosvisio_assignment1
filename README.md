# 2019 assignment1

### DEVELOPERS
*Balducci Gianmaria 807141*

*Guidi Alessandro 808865*

Repository: https://gitlab.com/jiimmy.exe/2019_assignment1_balducci_guidi/

### TARGET
Target is to set up a CI/CD pipeline to automate the entire development process and use the Gitlab CI/CD infrastructure to implement it


### APPLICATION
The application manages the sale of cinema tickets, through a database of several cinema in the area.

In this way,it's possibile reserve tickets for cinema to watch your favorite film.

For the database,we used MySql,instead the application is was written using *Python*,  which used his library *mysql.connector* as interface.  

The database is made of four table:
*  Cinema: contains the information related to cinema(**Id**,Nome,Città)
*  Film: contains the movie information that you can see(**Id**,Titolo,Regista)
*  Cliente: contains the information of customer who have buy a tickets(**CF**,Nome,Cognome,Età)
*  Biglietto: contains tickets information of the chosen show(Posto,Fila,Sala,**DataTime**)

## DevOps

# Container
We use Docker for the containerization.
The application uses two docker images:
 * Application: python 3.7
 * Database: mysql 5.7

 
# Continuous Integration and Continuous Deployment CI/CD
We exploit the CI/CD tool provide by GitLab for create the pipeline.
The pipeline have two stages:
  * build: create application's docker and build a runnable instace of application.Then push it in the repository.
  * verify: analize code for programming errors, helps enforcing a coding standard,
  sniffs for code smells and offers simple refactoring suggestions.
  For this purpose we used Pylint.
  * test-unit: in this stage we test the application using the library "unittest" imported in the script "test.py"
  * release: Create a tag target-image that refers to source_image that is the latest and upload the repository
            


           
