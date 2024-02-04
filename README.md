# DontSneakThroughMyPc!

Simple program that sends your mobile phone a notification (and other devices, as long as they have the app installed) once your computer has been booted up.

Will send another message every 5 minutes as long as the app is not closed.

## API Reference

#### Get your PushBullet API Key

```http
  https://www.pushbullet.com/#settings/account
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your PushBullet API key |

## Installation

Download the files in the repository

Python file doesn't need to be executed, and .bat file shall be put inside an autorun folder.

Change the code accordingly to your specifications.


```bash
Python file:
  api_key = "InsertYourAPIKeyHere"
```
```bash
Batch file:
  python "ExactPathToPythonFileWithQuotationMarks"
```
    
## Actually using the program

1. Put the program inside of an autorun folder
##### In my case, I'll be using "shell:startup" by pressing Windows + R and typing it there.

```bash
  Windows + R 
  shell:startup
  Copy the batch file (with the installation already completed)
```


## Demo

You can find an example [here](https://ibb.co/6g2xpJd)
