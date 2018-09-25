import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';

class InputAndSend extends Component {
  render() {
    return (
      <View style={styles.inputAndSendContainer}>
          <TextInput
            style={styles.input}
          />
          <Button
            title='Send'
            onPress={() => this.sendQuestion()}
          />
        </View>
    )
  }
}
export default InputAndSend;

const styles = StyleSheet.create({
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