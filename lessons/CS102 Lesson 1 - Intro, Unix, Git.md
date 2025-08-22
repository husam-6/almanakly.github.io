First class after labor day, probably 14-15 classes

Lets do no exams, projects and quizzes. Base heavily off Hongs notes, but read the book and write your notes here. Come up with your own assignments and use GitHub classroom (look up tutorials, setup assignments, test autograde)
## Intro
- Name, Major, Year
	- What do you hope to get out of this class?
	- "Sock, sock, shoe shoe" or "sock, shoe, sock, shoe."
- How many of you have coded before? What languages?
## Course Website & Syllabus

\<TK\>
## Computers and Software 
- a machine that manipulates information by following instructions (software) and is made up of physical components (hardware)
## Programming Language
- This is how you interact with the computer and give it instructions 
- This can be high or low level 
- Computers only understand 0s and 1s at the lowest level (machine code)
	- Assembly Language is a step up from this, abstraction but its still low level. Think of it as like a bunch of mnemonic macros for machine code instructions 
	- C / C++ are high level languages (although C is still considered low since it proivdes direct memory access + management)
		- Portable, powerful instructions, easier to maintain and write
	- Python / Javascript are even 'higher' up the chain 
		- These are *interpreted* languages
## Compiled Languages vs Interpreted
- What is a compiler? 
	- A compiler reads in your code and translates it to machine code. This makes a compiled language very fast and efficient
	- C, C++ are compiled (there are others too of course, Go, Rust, etc) 
- What is an interpreted language 
	- Code is executed line by line by an *interpreter*. This translates AND runs the code one at a time
	- Python, Javascript
		- Java is sort of half compiled half interpreted. Code is compiled into *bytecode* and executed by the JVM
## UNIX
- Unix is a family of operating systems which have become the base of Linux, Mac OS, Android, and others 
- You can develop in a Unix environment in a couple different ways 
	- Unix machine -> linux computer (all the computers in the labs are Linux)
	- MacOS -> OS Terminal. Pre-installed, click cmd + space and search for Terminal to find it 
	- WSL / Ubuntu -> Windows. This is a Unix environment you can install on windows which will let you dev in the same environment
### Commands 
- There are tons of commands that you should get familiar with over time. I don't know them all nor could I teach them all. But we can go over a bunch of common examples. Google is your best friend with these, there are tons of resources for every one! 

- `man \<cmd\>`
	- if you ever forget the way to use a command, this will open up the *man page* for it.
	- "man ls"
- `ls \<file or directory\>`
	- list the files in the provided destiation 
	- Many args you can pass to do different things 
	- ls -la -> long list all files including ones with period at the start
- `cd \<directory\>`
	- This and ls are your bread and butter. Use it to navigate your file system via the command line! 
- `mkdir \<name\>
	- create a directory 
- `pwd
	- path to your current directory 
- `touch \<file name\>
	- create an empty file 
- `mv \<file1\> \<file2\>
	- Move a file to a new destination. 
	- Can also be used to rename a file 
- `cp \<file1\> \<file2\>
	- Copy a file
- rm \<file\>
	- remove a file 
- `grep 
	- SUPER SUPER USEFUL!! 
	- grep -rnH "pattern" \<directory\>
- `diff \<file1\> \<file2\>
	- diff two files
- `chmod \<permissions\>  \<file\>
	- Change mode
	- chmod 777 file will usually suffice for anything you need if youre lazy
## Git and GitHub
- Git is a framework which powers all of the software world. It's open source and has many major benfits
- Version Control 
	- When you write software, you are always writing in iterations. Things break, you fix them, different things break, you fix them.
	- Oftentimes YOU will break things and introduce bugs! 
	- Git let's you save a snapshot of the changes you make. You can navigate back and forth between changes and change state to a version that was working when things are not working properly!
- Collaboration
	- Software teams are usually large and will have multiple people working in the same repository or package 
	- Git gives you a framework for *branching* and working in different states without impacting each others work 
- Durability 
	- It's not an uncommon problem to lose things you have locally. Think of photos, files, music, etc on your phone, computer, ipads, etc etc 
	- Git is the way you backup things so that they are *durable* and you don't lose them
### What is Github?
- GitHub is the microsoft platform that uses Git 
- It's free to use and you can use this to store your code, manage it, and collaborate with your classmates 
- I would *HIGHLY* recommend you learn how to use Git and use it for the rest of your college career. Store major projects, even assignments and notes!
- Set up and connect GitHub on your machine, there are many docs: https://docs.github.com/en/get-started/git-basics/set-up-git
### Commands 
- Git is a framework - there is a CLI you should learn 
- git status 
	- This tells you the state of your changes. What files did you modify? What files did you add which were not tracked previously? 
- git add \<file\>
	- Add a file to be tracked. When you make changes this stages it to be saved 
- git commit -m "Message"
	- This commits your staged changes. A commit is a unit of changes that you can mush together
- There are many more commands, these are the major ones you should learn 
## Editors and Shell Scripts 
- An editor is where you can write code 
- You can write code just about anywhere (though not everywhere is recommended)
	- vim
	- emacs
	- notepad++
	- VSCode, IntelliJ, PyCharm, Eclipse and many other IDE's
- vim or emacs are the basics, and you should be able to use one in the case when you can't install one of the others
### vim Quick Guide
- `vim filename` -- to start editing a file with vim
- `ESC :w` -- write/save the file
- `ESC i` -- insert before the character
- `ESC a` -- insert after the character
- `ESC :q` -- quit vim
- `ESC :q!` -- quit vim and override unsaved changes
- `ESC :wq` -- save and quit vim
### Bash / Shell Scripts
- Think of this as a script which will execute Unix commands you specify. 
- Very useful for certain tasks
```
#!/bin/bash

mkdir new_folder
cd new_folder
touch new_file.txt
ls
```

- First line is called a 'shebang' and it specifies the interpreter you want to use
```
chmod 777 unix_commands.sh
./unix_commands.sh
```
## Programming in C
- We mentioned you need a specific environment to dev
	- You need to be able to run `gcc`. 
- Set up Ubuntu for Windows WSL [here](https://learn.microsoft.com/en-us/windows/wsl/install).
- Set up gcc for Windows WSL [here](https://learnubuntu.com/install-gcc/).
```
sudo apt-get update
sudo apt install gcc
```    
- Mac - Run `gcc` and install XCode
### Parts of a Program 
- When you write a program there are core parts which you should get familiar. We will explore much of these in detail over time 
- Variables & functions
	- Functions are a sequence of statements to execute together
- When you are finished, you need to compile the code which results in an executable file
## Hello World!
- The starter program for every programmer, for every language
- Print a statement to the terminal!
```
vim hello.c
```

```
#include <stdio.h>

int main() {
	printf("Hello world!\n");
	return 0;
}
```

Run with 
```
gcc hello.c
./a.out
```
## Create a Repo, Save your work
- This is how we will submit homework and I will grade your assignments 
- On github.com create a repo, initialize with a README. 
- Clone it on your local 
```
git clone \<copied ssh link\>
```
### Branching
- I mentioned a valuable tool is collaboration. Branching lets you create a separate workspace in the same repo to save and develop. 
- Then later you can merge into main!
```
git checkout -b helloBranch
```
- This creates a new branch, you can save your work and push it here, without touching the main branch 
```
git add hello.c
git commit -m "first commit"
git push origin helloBranch
```
- Create a PR by navigating to GitHub page now for your repo
- Have it reviewed and merge into mainline!
## Textbook 
Textbooks are not required for the course, but they may be useful to have. These two are the two I reference.
- [The C Programming Language, 2nd Edition - Brian W. Kernighan & Dennis M. Ritchie](https://amzn.to/2LovuOa)
- [Python Programming for the Absolute Beginner, 3rd Edition - Mihael Dawson](https://amzn.to/2LkVOIU)
I also reference notes from Professor Hong who has great github.io: https://hong3cooper.github.io/
## Homework
\<TK\>