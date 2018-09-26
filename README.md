# Jenkins
[![Build Status](https://travis-ci.org/Jenkins-manager/Jenkins.svg?branch=master)](https://travis-ci.org/Jenkins-manager/Jenkins)

## Dependencies

- Python 3
- Django
- Pip
- Pytest
- React Native

## Installation

### Development

If you wish to contribute to this project, in addition to the requirements listed above you will need to follow the steps listed below.
    - export DJANGO_SETTINGS_MODULE=jenkinsServer.settings (this adds the settings to your path)
```
git clone https://github.com/Jenkins-manager/Jenkins.git
```

```
cd Jenkins
```
```
npm install
npm install -g react-native-cli
```
```
sudo pip install -r requirements.txt
```
* to start server

```
cd Server
```

```
python manage.py runserver
```
* to view front end react on ios
```
ensure x-code is installed
```
```
react-native run-ios
```
* when mock iphone appears, open evgie app


*This is our 2-week final project for Makers; 17 Sept 2018 - 28 Sept 2018*  

## Testing

The unit testing for this project is done in [Pytest](https://docs.pytest.org/en/latest/) to run the testing suite simply navigate to the **Server** directory, then run the following command :
    python -m pytest tests

you should then see an output like the one below:

    ==================2 passed in 0.03 seconds==================


Team members: [Marcus Kerr](https://github.com/MarcusKerr), [Jack Branch](https://github.com/pliantmeerkat), [Daniel den Hartog](https://github.com/velvetsnowman), [Kirtiman Singh](https://github.com/kirtimansingh93), [Cui Li Lim](https://github.com/limcuili)  

[Trello board](https://trello.com/b/jnnwcT3C/jenkins).

