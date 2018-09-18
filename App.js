/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View} from 'react-native';
import { AppRegistry, TextInput } from 'react-native';

// const instructions = Platform.select({
//   ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
//   android:
//     'Double tap R on your keyboard to reload,\n' +
//     'Shake or press menu button for dev menu',
// });

// type Props = {};
export default class App extends Component{
  constructor(props) {
    super(props);
    this.state = { text: 'Placeholder placeholder' };
  }
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Jenkins</Text>
        <TextInput 
          style={{height: 40, width:300,  borderColor: 'gray', borderWidth: 1}}
          onChangeText={(text) => this.setState({text})}
          value = {this.state.text}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,

    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  title: {
    fontSize: 20,
    textAlign: 'center',
    margin: 35,
  },
});
