# MapReduce

About the project: The project is to develop a map-reduce solution. In our project we are trying to find out map – reduce solution for maximum number of sales for genre and platform. Our dataset is a subset of Video games data. The data set consist of name,platform,year,genre,publisher,nasales,eusales,jpsales,othersales,globalsales,criticScore,criticCount,userScore,userCount,developer and rating.

Getting Started : In order to see the code the following steps need to be followed

Prerequisites

The prerequisite is to have a VMware , Python installed and running in laptop.

Link to download VMWare

Download and install from https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0

or

Download and install VirtualBox from https://www.virtualbox.org/wiki/Downloads

Link to download Python 2.6 version

https://www.python.org/download/releases/2.6.6/

Create the Virtual Machine:

###Installion of VMWare Download the VMWare from above link and then install by these steps Create a new Virtual machine: Create a new virtual machine by pressing the ‘New’ button: Choose a name, use ‘Type’: ‘Linux’: Press Next Select memory size for the VM. (2048 MB) Press Next Select ‘Use an existing virtual hard drive file’’, click the button to browse to the directory you unzipped the provided VM image and press ‘Create’. Select the machine and click ‘Play virtual machine’ Start the VM!

**Data Source**
https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings

* *duplicate input dataset is in the "Kalyan/VideoGames.txt" and "anoop/VideoGames.txt"*

**Download the Video Games dataset and convert .xlsx to tab delimited .txt file by just following these steps below**
1. open downloaded Video_Games_Sales_as_at_22_Dec_2016.xlsx file
2. select **save as** option
3. enter new file name and type **Text (Tab delimited) (*.txt)** option

**How to run the solution**

After installing VMWare put the mapper, reducer and .txt dataset into a folder and follow the commands given below in order to put these files into HDFS and run the solution to get the output

In code, to see local mapper.py & reducer.py, type:

$ ls

To execute (anoop replace **Kalyan** with **anoop**)

$ cd Kalyan

Put a copy of VideoGames.txt into HDFS myinput directory.

$ hadoop fs -ls

$ hadoop fs -put VideoGames.txt

$ hadoop fs -ls

$ hadoop fs -tail VideoGames.txt

$ hadoop fs -mkdir myinput

$ hadoop fs -put VideoGames.txt myinput

Verify myinput/VideoGames.txt is in HDFS.

$ hadoop fs -ls myinput

To Run MR

hs mapper.py reducer.py myinput joboutput

Review the output in HDFS

$ hadoop fs -ls

$ hadoop fs -ls joboutput

*To get results out of Hadoop, use get:* (for anoop replace **results.txt** with **intermediateResults.txt**)

$ hadoop fs -get joboutput/part-00000 results.txt

*Check for a local copy with ls:*

$ ls

*kalyan Result*

mapper.py reducer.py results.txt

*Anoop Results*

mapper.py reducer.py intermediateResults.txt

$ sort -nrk 2,2 results.txt completeOutput.txt (for anoop replace **completeOutput.txt** with **completeResults.txt**)

$ ls

*kalyan Result*

mapper.py reducer.py results.txt completeOutput.txt

*Anoop Results*

mapper.py reducer.py intermediateResults.txt completeResults.txt


*completeOutput.txt and completeResults.txt will have the results from our map reduce problem*

**Final Results**

*Graph for maximum number of sales for genre* 
![alt tag](https://github.com/KairamkondaKalyanDass/Video-games-MapReduce/blob/master/images/Kalyan%20results.JPG)

*Graph for maximum number of sales for genre* 
![alt tag](https://github.com/KairamkondaKalyanDass/Video-games-MapReduce/blob/master/images/Anoop%20results.JPG)
