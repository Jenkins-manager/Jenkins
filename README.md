# Jenkins
[![Build Status](https://travis-ci.org/Jenkins-manager/Jenkins.svg?branch=master)](https://travis-ci.org/Jenkins-manager/Jenkins)

## Dependencies

- Python 3
- Django
- Pip
- Pytest
- React Native

## Installation

### **Development**

If you wish to contribute to this project, in addition to the requirements listed above you will need to follow the steps listed below. First enter the following sequence of commands in your terminal:
```
export DJANGO_SETTINGS_MODULE=jenkinsServer.settings
git clone https://github.com/Jenkins-manager/Jenkins.git
cd Jenkins
npm install
npm install -g react-native-cli
sudo pip install -r requirements.txt
python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.3.0-py3-none-any.whl
```
#### Database setup
To configure the data set run the following command from the command line:
```
Server jackbranch$ python add_database_data.py
```


#### To start the server

```
python manage.py runserver
```
to view front end react on ios ensure x-code is installed, if not visit the Apple Store to download in another terminal
```
cd path/Jenkins/Server
```
```
react-native run-ios
```
when mock iPhone appears, open evgie app enjoy

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

## Adding questions

To add a new question, navigate to the *Jenkins/Server* directory, then run the following command in your console:
```
python q_and_a_script.py
```
Once this is excecuted you will be greeted with the script menu, which provides these simple instructions:
```
This is the runner for adding questions and answers to the application
Please read the included instructions for more infomation, this can be doneby entering HELP! at any time, press QQQ to close the script at any time
Enter a question to begin:
```

### Note
If you wish to add a two word keyword to the database (recommended to avoid keyword clashes) please replace the space character with '_', for example 'key word' would become 'key_word'.

### Credits
Team members: [Marcus Kerr](https://github.com/MarcusKerr), [Jack Branch](https://github.com/pliantmeerkat), [Daniel den Hartog](https://github.com/velvetsnowman), [Kirtiman Singh](https://github.com/kirtimansingh93), [Cui Li Lim](https://github.com/limcuili)  

[Trello board](https://trello.com/b/jnnwcT3C/jenkins).
