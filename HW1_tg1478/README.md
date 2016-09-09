# PUI 2016 HW 1.  

# Assignment 1: Finish Lab 1

For this assignment I worked with Ben Miller (bsmiller25). First, I forked Ben's repo "githubtest_bm2393," then cloned the fork onto my computer. I modified Ben's file "myfirstfile.txt," then submitted a pull request to add the changes to his original file. 

Ben later merged the pull request and committed my changes to his original file. Ben also performed the same actions on my repository "gittest_tg1478."


## Assignment 2: Set up your environment: 


1. I created a directory on compute called PUI2016_tg1478.
2. I created an environmental variable on compute called PUI2016, that returns the full path to the directory PUI2016_tg1478.

If I run the command 
	```
	echo $PUI2016
	```
the full path to the directory is returned. 


3. I created an alias so that typing
 	```
	pui2016 
	```
takes me to the PUI2016_tg1478 diretory. 

4. Screenshot of my .bashrc

![Screenshot 1 Assignment 2: my .bashrc](HW1_SS1.png)

5. After typing this series of commands on the terminal:	
	```
	pwd
	pui2016
	pwd
	```
I am successfully navigated back to the PUI2016_tg1478 directory. 

![Screenshot 2 Assignment 2: my succesfull commands using $PUI2016 and the pui2016 alias](HW2_SS1.png)


7. Once your environment is set up, go to github online and CREATE A NEW GITHUB REPO CALLED PUI2016_\<netID> ( this for me would be PUI2016_fb55: https://github.com/fedhere/PUI2016_fb55 ). Follow the github directions to create a repository on the command line on your local machine (https://help.github.com/articles/creating-a-new-repository/).  Notice that in this case you are working in the reverse order compared to the lab: you create the first instance of the repository on the remote server (on the web) and then you create a local repo to link to it on your machine. Follow the steps indicated by github to create the repo, a README.md file, and to link the online and the local repos. 

8. Inside the repository create a directory HW1_\<netid>

9. Inside this directory add a README.md file: edit the copy on your machine to have it describe what you did to set up your enviroment and upload the screenshots I directed you to take above, so that they are displayed in your README.md (like in the image below). The README.md is a “markdown” file. To see what the syntax to upload an image in a markdown file, or in general to format the text, you can look at this markdown and if you look at the raw file (by clicking the Raw button on the top right) you can see the syntax. 
Remember that you also need to upload the images in your remote directory for them to be displayed in your README! just like any file you add them by git add and git commit, git push.

NOTE: after you modify your .bashrc or .bash_profile you will have to rerun it:
	```
	source .bashrc 
	```
for the new set up to be incorporated in your environment. However, every new bash terminal you open will automatically read the .bashrc/.bash_profile and know about your new alias/env variables

### GRADING: 
We will grade you based on the README.md file you create in the github directory as described above. The README.mdfile **has to be your own!** While you can work in groups this must be written by you in your own words, to show you know what is going on. The screen shots need to show the appropriate lines in the .bashrc and that running the commands as requested takes you to the right directory.



## Assignment 3 - Extra Credit. 

##This may be hard, but figuring it out will greatly help you get the most out of the next several lectures. We keep track of your EC assignments and they will help your final grade. This homework is a notebook: this is the standard format of the homeworks in the future. To get full points your notebook must
## - be rendered (e.g. plots must be visible) so that we see what you intended to turn in
## - run: the TA must be able to download your notebook and run it without error. Failing to run will cost you 25% of the Assignment grade! 

1. Go to the PUI2015 directory you created in Assignment 1 and set up as a repo in Assignment 2.
2. Download the nontebook https://github.com/fedhere/PUI2016_fb55/blob/master/HW1_fb55/HW1_3_fb55.ipynb
. To do so click on Raw on the top right of the notebook. 
Now you have 2 choices: you can copy and paste the entire RAW Jupyter notebook (which is  a JSON file) onto a new file on your own machine (name the file HW1_3_<netID>.ipynb) or you can use the <i>wget</i> command on the terminal: typing 
	```
	wget https://raw.githubusercontent.com/fedhere/PUI2016_fb55/master/HW1_fb55/HW1_3_fb55.ipynb
	```
will save a version of the notebook in the directory where you were when you typed the command. wget, which stands for web get, downloads any files, or even entire directories, from a web URL. You must change the name of the notebook to HW1_3_\<netID>.ipynb

3. Fill in the code cells that I left empty following the directions. Run the check cells, which will help you to know that the cells you filled in were filled in correctly (you want to see the same output I saw, which is in the redered version of the notebook).

4. Once the notebook is done and rendered (you see the plots at the end of it) “stage it” so that git can track it: just follow the procedure in the lab assignment and use 
	```
	git add 
	git commit -m '<your message here>'
	```
5. Link the current directory to your new github repo (which you created in assignment 2) if you have not done so yet, (PUI2016_\<netID> on your github account, just like in the lab assignment you will need to use use 
 	```
	git remote add origin 
	git push -u  <url> 
	```
using the URL of your new repo.

6. Push the notebook into the github repo and check that it renders ok. Remember to check that it runs ok as well: before you commit open a new instance of Jupyter notebook (or restart your kernel!) and run through the notebook cell by cell to assure that there are no problems








## References: 
- markdown syntax - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet, http://daringfireball.net/projects/markdown/syntax
- basic bash commands - http://www.tldp.org/LDP/abs/html/basic.html
- environment setup - http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html#sect_03_01_02
- additional references were provided in the class slides.

Text Editors. 

#### -m

remember to add the -m “my commit message” when you commit to github, otherwise github will automatically open a text editor for you to type your message in , and then you have to deal with it. If github opened a text editor it is either emacs or vi, depending on your setup. If you are using emacs or vi, either because github opened them or to edit files, this is how you save your work and exit:

#### emacs 

Save: Ctrl+x Ctrl+s
Exit: Ctrl+x Ctrl+c
(if your emacs is running on the terminal you have to use these shortcuts, if it is running in its own X window you can use the dropdown menu)

#### vim (vi)

Save: esc :w
Exit: esc :q


## Key Concepts: 

- falsifiability and law of parsimony
- types of scientific questions
- reproducible research
- PEP8 and style standards 

- work with github 
- basic bash commands
- understand how to setup your environment
- creating and checking into github a Jupyter notebook

