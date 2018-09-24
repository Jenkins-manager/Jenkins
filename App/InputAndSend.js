import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { AppRegistry, TextInput } from 'react-native';
import { Button } from 'react-native';

class InputAndSend extends Component {
  render() {
    return (
      <View style={styles.input}>
          <TextInput
            style={{
              flex:1,
              height: 35,
              borderColor: 'gray',
              borderWidth: 1
            }}
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
  input: {
    flexDirection: 'row',
    position: 'absolute',
    bottom: 10
  }
});