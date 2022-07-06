# AIPAA Front-end

This is the repository for _[AIPAA](https://aipaa.ir)_ services client. I mostly write for TTS service, but you can make a PR for other services they provided.

## How to use

- Go to [AIPAA](https://aipaa.ir) website and create an account.
- Go to your console and create a new set of credentials (In the website, it's written as _اعتبارنامه‌ها_)
- Clone this repository, copy and rename `main.py` file to your project's root directory (let's assume you renamed the file to `aipaa.py`):

    ```python
    from aipaa import AipaaFrontend

    aipaa = AipaaFrontend(YOUR_CLIENT_ID, YOUR_CLIENT_SECRET)
    ```
- Then, you need to authenticate. It's easy as Pie:

    ```python
    aipaa.authenticate()
    ```

_NOTE_: There is no need to store the result in any variable. It's been handled internally. 

- Now, you can use features implemented in the library. For now, Only TTS is available.

## Code sample

```python
from aipaa import AipaaFrontend

aipaa = AipaaFrontend(YOUR_CLIENT_ID, YOUR_CLIENT_SECRET)
aipaa.authenticate()
aipaa.say("سلام دوست عزیزم")
```

## Important notes

- I wrote this library as a part of my personal _smart assistant_ project. This is why I only made it for TTS systems.
- I am only responsible for __THIS__ library and codes contained in __THIS__ repository, since my code is a third-party application on top of AIPAA's API and service. 
- The code in this repository is open source and you can use it under the _MIT License_. But AIPAA's core service isn't and I'm not responsible for that. Please mind this while making a new issue.

## TODO

- [ ] Making a Python library for this project
- [ ] Exploring API and add more features to the TTS functionallity. 