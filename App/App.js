import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';
import InputAndSend from './Components/InputAndSend';
import Question from './Components/Question';
import Answer from './Components/Answer';

export default class App extends React.Component {
  constructor() {
    super();

    this.state = { 
      text: '', 
      questions: [] 
    };
  }
  
  // sendQuestion() {
  //   fetch('http://localhost:8000/send_question/',
  //     {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify({
  //         body: this.state.text,
  //       }),
  //       }).then(function(result) {
  //         if(!result.ok) {
  //           throw Error('Bad data input')
  //         }
  //       }).then(function(result){
  //           console.log(result)
  //       }).catch(function(error) {
  //           alert(error)
  //     })
  // }

  sQ() {
    const {questions, text} = this.state;
    questions.push({text});
    this.setState({questions})
  }



  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Jenkins</Text>
        {/* <Question />
        <Answer /> */}
        {
          this.state.questions.map((question, i) => {
            return (
              <Question key={i} question={question}/>
            )
          })
        }
        <View style={styles.inputAndSendContainer}>
          <TextInput
            style={styles.input}
            onChangeText={(text) => this.setState({text})}
          />
          <Button
            title='Send'
            onPress={() => this.sQ()}
          />
        </View>
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
  inputAndSendContainer: {
    flexDirection: 'row',
    position: 'absolute',
    bottom: 10
  },
  input: {
    flex:1,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 8
  }
});
