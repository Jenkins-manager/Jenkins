import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';
import InputAndSend from './Components/InputAndSend';
import Question from './Components/Question';
import Answer from './Components/Answer';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      text: '', 
      questions: [] 
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

  sQ() {
    const {questions, text} = this.state;
    questions.push({text});
    this.setState({questions})
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Jenkins</Text>
        <Question />
        <Answer />
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
  answerBox: {
    padding: 8,
    borderRadius: 8,
    backgroundColor: '#ece5dd',
    position: 'relative',
    left: -120,
    margin: 2
  }
});
