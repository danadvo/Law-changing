# Law-changing
### Written in Python , using XML.etree, XML.dom libraries
***This project was done as part of Digital Humanities election course***

As part of collaboration with the department of Justice in Israel, we are thinking about switching legal documents and documenting method to digital.
In this project I wrote a program that gets as input:

1. XML document that represents legal law (example in 'law.xml')
2. XML document that represents some change of this law (exapmle in 'change.xml')

The program applies the changes on the original law.
Possible changes:
1. Delete law 
2. Add law (or section)
3. Change part of the law (adding content, removing part of the sentence etc.)
4. Change title of law

#### <ins> Running the project: </ins>
To run the project, replace the files named 'law.xml', 'change.xml' with your law and change files (should fit the structure of dtd files).
Then in the cmd run:
<PATH-OF-MAIN-FILE> <NAME-OF-LAW-FILE> <NAME-OF-CHANGE-FILE>
The output will appear in the 'law' file.
