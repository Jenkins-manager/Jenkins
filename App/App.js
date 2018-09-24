import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
// import { AppRegistry, TextInput } from 'react-native';
// import { Button } from 'react-native';
import InputAndSend from './InputAndSend';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      text: '' 
    };
  }
  
  sendQuestion() {
    fetch('http://localhost:8000/send_question/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          body: this.state.text,
        }),
        }).then(function(result) {
          if(!result.ok) {
            throw Error('Bad data input')
          }
        }).then(function(result){
            console.log(result)
        }).catch(function(error) {
            alert(error)
      })
  } 

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Jenkins</Text>
        <InputAndSend />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    padding: 10,
  },
  title: {
    fontSize: 20,
    textAlign: 'center',
    margin: 25,
  },
  input: {
    flexDirection: 'row',
    position: 'absolute',
    bottom: 10
  }
});
