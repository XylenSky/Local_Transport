#  Information Driver

 For finding the weather at a place or share files.

## Installation

Standered installation and implementation of django and static file sharing.
You can use the following command to start and then copy the file content from the repository.

```bash
django-admin startproject interaction
django-admin startapp core
```

## Usage


* This project is about the uploading the single or multiple file on the server and share the files present on the server including new ones.
<img src='Screenshot 2022-08-15 at 9.22.10 PM.png' width = '800' img>

* This project's homepages tells about the weather at any place which is implemented by searching the querry on the search engine then scrapping the information from the page and show it on the page.
<img src='Screenshot 2022-08-15 at 9.19.36 PM.png' height = '500' img>

* It can be well used in the local area network where we need to send the files from just one computer to another computer or cellphone to computer but we don't want to make any changes in our computer settings because that also left some thoughts left in our mind about security.

## Features
* In this project it is insured that anyone cannot upload the file without having a key for accessing the server.
* Key changes after every successful attempt.
* Maximum no of files to be uploaded and size of the individual file can also be controlled.
* Used CSRF token to avoid cross-site-request-forgery attacks.
## How to use
* Open the upload page.
* A Key will be printed each time on terminal when a request get's validated. Then that key can be used to share or upload more files on the server.
