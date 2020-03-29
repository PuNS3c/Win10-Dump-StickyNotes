# Win10-Dump-StickyNotes
Dump sticky notes content with python script

> Note: This was tested on windows 10 Build 18363


### How does it work? 
`Microsoft.Notes.exe` use sqlite db to store the notes. You can see the handle in ProcessExplorer. 
Reading it is as simple as `SELECT * FROM Note`, and viewing the content. 
This is what the script does.

### How to run?
Download the `.py` file, and run.
