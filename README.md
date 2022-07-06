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