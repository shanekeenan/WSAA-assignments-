# Assignment 04 from Topic 05 Authentication

# Author: Shane Keenan 
# date: 01/05/2024 
# status: complete 

'''
Assignment description: 
Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name. 
The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
I do not need to see your keys (see lab2, to follow)
Handup: Push the program as assignment04-github.py to assignments repository.
Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.
'''

import requests
import json
from config import apikeys as cfg
from github import Github

# fine-grained token stored in config.py file.  
apikey = cfg["githubkey"]

g = Github(apikey)
repo = g.get_repo("shanekeenan/aprivateone")
#print(repo.clone_url)


#list the repos in my Github account

#for repo in g.get_user().get_repos():
 #   print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))

# find the url for the file "test.txt "
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# access the contents of the text file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

# count the number of times Andrew appears in the text 
count = 0
for char in contentOfFile.split(): # split the text into individual words
    if char == 'Andrew':
        count += 1
print(f"File contains {count} instances of the name Andrew")


# Replace Andrew with Shane 
mod_contentOfFile = contentOfFile.replace('Andrew', 'Shane')


# commit and push to repo 
gitHubResponse=repo.update_file(fileInfo.path,"Andrew has been updated to Shane",mod_contentOfFile,fileInfo.sha)
print (gitHubResponse)
print (f"These have now been replace with the name Shane")
