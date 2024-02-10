# parking-eye-registration

## Introduction

Depending on what gym you go to, the car park would give some set amount of time permitted to park. However, individuals would need to scan a QR code at the gym to get more parking hours and avoid a fine.

This repository aims to help the user save time, no need to worry about car parking by enabling a scheduled run at low cost, or even free, allow the user to not worry about parking fines (and the stress of dealing with Parking Eye and/or POPLA) and therefore focus on their workout.

I also hold no responsibility to the actions of what other users do such as spamming registrations, this sole purpose is to automate *my own schedule*

## Usage
1. Go to the gym (the gym group). Scan QR code and copy the unique link that looks like `iamparking.at/QRCode?id={}`
2. Use the URL in point 1, put this into the environment variables with key `parking-url`
3. Put your car registration with no whitespaces in between in your environment variables with key `reg-plate`
4. Deploy main.py on some kind of server with python 3.11 and python-dotenv with points 2 and 3 applied
5. Set your schedule, ideally randomised on between some minutes of what time you usually go to gym
## To do

1. Create a docker file for app
2. Create mobile app
