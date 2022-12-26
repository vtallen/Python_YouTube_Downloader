import os.path
from os import path
import time
import ytdownloader.downloader as dl


def cls():
    print("""































































   """)

def main():  # type: () -> None
    home = os.path.expanduser("~")
    os.chdir(home)

    if not path.exists("Downloads"):
        os.mkdir("Downloads")
        os.chdir("Downloads")
    else:
        os.chdir("Downloads")

    if not path.exists("YTDownloader"):
        os.mkdir('YTDownloader')
        os.chdir('YTDownloader')
    else:
        os.chdir("YTDownloader")

    rootPath = os.getcwd()

    runProgram = True

    commandMenu = """
    ==========================================
    Welcome to Youtube Downloader!
    Commands:
    0 - Quit
    1 - Download individual videos
    2 - Download a playlist
    ==========================================
    """

    seperatorText = "=========================================="

    userChoice = ""
    inputFormat = "video"
    inputURL = ""
    URLArray = []

    runValidationLoop = True

    while runProgram == True:
        print(commandMenu)
        userChoice = input(">> ")

        if userChoice == "0":
            runProgram = False
        elif userChoice == "1":
            while runValidationLoop == True:
                inputFormat = input("Output format (audio/video) >> ")
                if inputFormat.lower() == "audio" or inputFormat.lower() == "video":
                    runValidationLoop = False
                else:
                    print(">> Output format not recognized!")
                    time.sleep(1)
                    cls()
                    print(commandMenu)

            runValidationLoop = True

            inputURL = input("Video URL(s) (Use commas to separate links)>> ")
            inputURL = inputURL.strip()

            URLArray = inputURL.split(',')

            URLArray = [x.strip() for x in URLArray]

            loopNum = 0
            createPath = True

            for video in URLArray:
                if createPath == True:
                    dl.download(URLArray[loopNum], createPath, downloadType=inputFormat, downloadPath=rootPath)
                    createPath = False
                else:
                    dl.download(URLArray[loopNum], createPath, downloadType=inputFormat, downloadPath=rootPath)
                loopNum += 1

            loopNum = 0
            createPath = True

            input(">> Download complete, press Enter to continue...")

        elif userChoice == "2":
            while runValidationLoop == True:
                inputFormat = input("Output format (audio/video) >> ")
                if inputFormat.lower() == "audio" or inputFormat.lower() == "video":
                    runValidationLoop = False
                else:
                    print(">> Output format not recognized!")
                    time.sleep(1)
                    cls()
                    print(commandMenu)

            runValidationLoop = True

            inputURL = input("Playlist URL >> ")
            inputURL = inputURL.strip()

            print(seperatorText)
            try:
                dl.download_playlist(inputURL, downloadType=inputFormat, downloadPath=rootPath)
            except:
                print("An error has occurred while trying to download the playlist. Was your URL valid?")
                input(">> Press Enter to continue...")
                cls()

            input(">> Download complete, press Enter to continue...")
        else:
            print(">> Command does not exist")
            input(">> Press Enter to continue...")
            cls()


if __name__ == "__main__":
    main()
