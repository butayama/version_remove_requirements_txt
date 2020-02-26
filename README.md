# version_remove_requirements_txt
removes all Version Numbers from a requirements.txt file and stores a requirements_old file

**Example**

requirements.txt becomes requirements_old.txt.
If requirements_old.txt already exists, overwrite or new filename could be entered.

alabaster==0.7.12  
alembic==1.3.3  
ansimarkup==1.4.0  
attrs==19.3.0  
Babel==2.8.0  
....

requirements.txt will be overwritten with:

alabaster  
alembic  
ansimarkup  
attrs  
Babel  
....
