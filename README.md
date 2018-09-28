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
```
python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.3.0-py3-none-any.whl
```

```
cd Server
```

* This adds the settings to your path
```
export DJANGO_SETTINGS_MODULE=jenkinsServer.settings
```
* To start the server

```
python manage.py runserver
```
* to view front end react on ios

* ensure x-code is installed, if not visit the Apple Store to download

* in another terminal
```
cd path/Jenkins/Server
```
```
react-native run-ios
```
* when mock iPhone appears, open evgie app

* enjoy

*This is our 2-week final project for Makers; 17 Sept 2018 - 28 Sept 2018*  

## Testing

The unit testing for this project is done in [Pytest](https://docs.pytest.org/en/latest/) to run the testing suite simply
```
cd path/Jenkins/Server
```
```
python -m pytest tests
```
you should then see an output like the one below:

    ==================47 passed in 4.56 seconds==================


Team members: [Marcus Kerr](https://github.com/MarcusKerr), [Jack Branch](https://github.com/pliantmeerkat), [Daniel den Hartog](https://github.com/velvetsnowman), [Kirtiman Singh](https://github.com/kirtimansingh93), [Cui Li Lim](https://github.com/limcuili)  

[Trello board](https://trello.com/b/jnnwcT3C/jenkins).
