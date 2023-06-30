# ACADEMIC TOOLKIT

# What is this code about?
The academic toolkit provides students and academic researchers with tools that aid in any form of report or academic writing. 
This project was written in Python 3. 

# Python version?
3.11.4 (As of June 30 2023)

# How to execute and run the Academic Toolkit? 
In the terminal, simply input: python toolkit.py 

# Motivation behind this project? 
* Initial motivation was to automate the removal of intext references from text to obtain a pure word count immediately (for reports and assignments)
* I decided that there were additional features that I wanted to use when I was writing academic reports or university assessments 
* The first and second main feature that I want to add was to automate the proecess of producing references for any source (in Harvard style with The University of Adelaide's guidelines)
* Following this, I then wanted to have the option to convert text to speech in order to hear how any text sounds when it is read aloud (e.g., for speeches or for checking grammer and punctuation in text)
* Finaly, I also wanted to implement a feature to allow for converstion from speech to text in order to get transcripts for videos such as lectures or podcasts

# What are the features of the Academic Toolkit? 
* Word count can be accurately calculated for any text
* The intext referencing within text can be automatically and instantly removed to obtain the pure text form (without intext) and the pure word count (without intext)
* All 54 possible reference types can be automatically generated from simple user input (in Harvard style via The University of Adelaide)
* Convert text into speech which is saved within a .mp3 file (user may hear how their text sounds read aloud)
* Convert speech to text (any words spoken within .media files can be extracted and provided in text form (25mb max limit))

# References used for this code: 
* https://platform.openai.com/docs/api-reference/chat (OpenAI's Whisper AI model was used for speech to text (via OpenAI's API))
* https://www.geeksforgeeks.org/convert-text-speech-python/ (Google's gTTS (Text-To-Speech) tool was used for text to speech)
* https://www.adelaide.edu.au/library/ua/media/4063/library-qrg-harvard-referencing.pdf (54 reference types were used from The University of Adelaide's Harvard referencing guide)