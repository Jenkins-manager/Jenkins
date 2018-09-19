import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';

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
        {/* <Text>Changes you make will automatically reload.</Text>
        <Text>Shake your phone to open the developer menu.</Text> */}
        <TextInput 
          style={{height: 40, width:300,  borderColor: 'gray', borderWidth: 1}}
          onChangeText={(text) => this.setState({text})}
          value = {this.state.text}
        />
        <Button 
        onPress={() => this.sendQuestion()}
        title='Send' />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    textAlign: 'center',
    margin: 35,
  }
});
