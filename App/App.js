import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';
import Question from './Components/Question';
import Answer from './Components/Answer';

export default class App extends React.Component {
  constructor() {
    super();

    this.state = { 
      text: '', 
      questions: [],
      answers: []
    };
  }

  sendQuestion() {
    const {questions, text, answers} = this.state;
    questions.push({text});
    this.setState({questions});
    // this.setState({answer: '400'});
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
            alert(result)
            throw Error('Bad data input')
          }
          return result.json();
        }).then(function(answerJson){
          answers.push({answerJson});
          console.log(answers)
        }).catch(function(error) {
          alert(error);
        });
  }

  render() {
    return (
      <View style={styles.container}>
      <Text style={styles.title}>Jenkins</Text>
        {
          this.state.questions.map((question, i) => {
            return [
              <Question key={i} question={question}/>,
              <Answer key={i+1} answer={this.state.answers[i]}/>
            ]
          })
        }
        {/* {
          this.state.answers.map((answer, i) => {
            return (<Answer key={i} answer={answer}/>)
          })
        } */}
        <View style={styles.inputAndSendContainer}>
          <TextInput
            style={styles.inputBox}
            onChangeText={(text) => this.setState({text})}
          />
          <Button
            title='Send'
            onPress={() => this.sendQuestion()}
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
  inputBox: {
    flex:1,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 8
  }
});
