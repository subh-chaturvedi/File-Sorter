# File-Sorter
A python program to sort all files in a directory into appropriate sub-directories.
- Fully compatible with Linux based OS, for Windows follow special instructions.

## **Directions to install and run:**
  1. Run the install.sh shell script to install the required files to the HOME directory.
  2. Alternatively all the files in the bin folder can be copied to a folder in the home directory.
  3. Optionally, the .desktop file in the bin folder can be placed in the appropriate folder to make the program appear in the applications menu.
  4. Run the launch.sh shell script.
  5. Input the path to the folder which is to be sorted.
  6. Thats it, the folder will be sorted.
  
## **Directions to add more filtering conditions:**
  1. Run the adder.py python script.
  2. Input the extension that is to be filtered and the group it has to be sorted into.\
  For example:\
     If I have to sort all "*.dll" files into the DynamicLinkLibrary folder,
     I will input .dll as extension and DynamicLinkLibrary as the group.

## **For Windows:**
  1. Replace all forward slashes in the python code with double backward slashes.
  2. Run the program using Sortergui.py
  3. Enter all paths with **DOUBLE BACKSLASHES**.
  
