## Introduction

This repository contains the source codes for the course MACHINE LEARNING of the  Electrical and Computer Engineering
Master from the Engineering Institute of Universidade do Algarve, Portugal. 

## Setup your platform
### Requirements
I suggest you the use a virtual environment. To install requirements in your environment run `pip install -r requirements.txt`

###  jupyter
if using jupyter, make sure you have it installed [(https://jupyter.org)](https://jupyter.org/index.html) and it is in your path. 
Then you should be able to start an instance by running:
- start.sh in Linux or start.bat in Windows.
- jupyter-notebook on a terminal

Note: make sure you activated your environment (e.g., activate dhml)

#### jupyter extensions
##### Linux 

1. to activate the jupyter extensions  
* install -  jupyter_contrib_nbextensions
	`> pip3 install jupyter_contrib_nbextensions`
    (make sure you do not 'sudo' it!)

* enable extensions configurator
 	`> jupyter nbextensions_configurator enable --user`

* E.g., to activate TOC in the notebooks, go to the Nbextensions tab and activate the "table of contents"

* install jupyter themes
    > `pip3 install jupyterthemes`
    
    and the set the theme (look at https://github.com/dunovank/jupyter-themes). 
    > `jt -t grade3 -fs 95 -tfs 11 -nfs 115 -cellw 95% -T -nf exosans -f droidmono -altmd -altout -N`
  
    or

    > `jt -t monokai -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T -nf exosans -f droidmono -altmd -altout -N`


    or ...

##### Windows 10

to active the jupyter extensions  

* install -  jupyter_contrib_nbextensions: 
 [ver https://github.com/ipython-contrib/jupyter_contrib_nbextensions]

	* open powershel from file explorer
	  - > `conda install -c conda-forge jupyter_contrib_nbextensions`
        
	  or
      
      - >  `pip install jupyter_contrib_nbextensions`
      
	* enable extensions configurator
	 	> `jupyter nbextensions_configurator enable --user`

	* To activate TOC in the notebooks, go to the Nbextensions tab and activate the "table of contents"


## Syllabus


1. Python Programming
	1. Procedural programming
	1. Object-oriented programming
	1. Parallelism ( multi-threaded and multi-process)
1. Machine learning algorithms
	1. Supervised versus unsupervised learning
	1. Selection and evaluation of models
	1. Linear regression	
	1. Logistic regression
	1. Vector machines support
	1. Clustering
	1. Decision trees and forests
	1. Neuronal networks
    
## Clone this repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. 
If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You'll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you'd like to and then click **Clone**.
4. Open the directory you just created to see your repository's files.

# Contacts

- Pedro Cardoso
- pcardoso(a)ualg.pt
- [homepage](http://w3.ualg.pt/~pcardoso)


![ISE](https://bytebucket.org/pcardoso/dhml/raw/040bc0a569ba6c8483f422e210374e53382cf77a/utils/ise.jpg) ![ISE](https://bytebucket.org/pcardoso/dhml/raw/040bc0a569ba6c8483f422e210374e53382cf77a/utils/ise2.jpg) ![FARO](https://bytebucket.org/pcardoso/dhml/raw/040bc0a569ba6c8483f422e210374e53382cf77a/utils/faro.jpg)
