# youtube-watch-history-parser
Program to extract history from youtube watch history HTML file, and write the links and video titles into a new CSV file

## Steps to use

- Get your youtube watch history from Google Takeout. You will receive a zip file containing the watch_history.html file (at the path: Takeout/Youtube and YouTube Music/history/).
- Place that html file into this downloaded repository.
- Install the required packages (as mentioned in requirements.txt).
- Run the following shell command to create a new CSV file with name yt-history.csv (or any other name of your choosing) containing the extracted links and titles:

```sh
python parse-html-watch-history.py watch-history.html yt-history.csv
```

**NOTE:** If you have installed the packages into a virtual environment, then instead of 'python' you might have to use './Scripts/python.exe'