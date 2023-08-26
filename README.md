# pyJukeBox
## Overview
This is a Python script that helps the user to download songs and transfer them to their mobile phone via email. If a user has a certain playlist on Spotify that they would like to download offline the script can automatically fetch all the songs directly and share them with the user.

## Technologies Used
For this project, I have used YouTube API, Spotify API and some Python libraries such as Pytube, SMTPlib, JSON and email. I have used email.MIMEBASE to load songs to the email.

## How to use
After downloading all the files of the code in a directory user can run the command **python3 main.py**. If the user wants to download only one song then they can simply write the name of the song on the terminal and the email ID in which they want to get the song. But if they want to download songs from their custom playlist they have to write **spotify** in the terminal and then their Spotify user ID and their email ID.

## Challenges Faced and How I overcame them
+ I was trying to get the URL of the song video on YouTube by using Beautiful Soup 4 but unfortunately, it was not working. Later on, I realised that I should give some time for the js to properly load and then get the link. However, I found a much better legal fix for this problem in YouTube API.
+ When I was planning the project I used the Bluetooth library in Python to transfer the songs, The code that I wrote was able to make a Bluetooth connection automatically if the name of the device was given but when I tried sharing songs it was not coming in proper mp3 format in my mobile phone.
Then when I looked up online they said that I needed some protocol to deal with properly receiving the songs on the  mobile phone side. I then thought of sharing the songs on email and implemented it as it was much simpler and the user could access their email with devices.
+ The songs are also downloaded locally on the same directory but even if the user has already downloaded that song the code was downloading it again so I created a JSON file to store the songs that the user has already downloaded and send them directly rather than by downloading it again.
+ Mid-way through the project the Pytube library stopped working after searching online I got to know that YouTube had changed its URL format due to which the HTML parser of Pytube was not working to fix that I downloaded a GitHub fork which resolved that issue  however I would like to add that Pytube library was later updated to resolve this issue.

## Future Improvements
+ The user currently gives commands directly to the terminal however, we can implement a user-friendly GUI for the user to interact using Tkinter.
+ Or we can make a full stack application which will have python(Django) running on the backend with the same logic and Front-end providing an immersive user-interface to the user.
