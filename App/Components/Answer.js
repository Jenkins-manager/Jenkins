import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';


class Answer extends Component {
  render() {
    return(
      <View style={styles.answerBox}>
          <Text>{this.props.answer}</Text>
      </View>
    );
  }
}

export default Answer;

const styles = StyleSheet.create({
  answerBox: {
    padding: 8,
    borderRadius: 8,
    backgroundColor: '#ece5dd',
    position: 'relative',
    left: -120,
    margin: 2
  }
});