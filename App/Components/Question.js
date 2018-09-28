import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';


class Question extends Component {
  render() {
    return(
      <View style={styles.questionBox}>
        <Text style={styles.questionText}>{this.props.question.text}</Text>
      </View>
    );
  }
}

export default Question;

const styles = StyleSheet.create({
  questionBox: {
    padding: 8,
    borderRadius: 8,
    backgroundColor: '#34b7f1',
    position: 'relative',
    right: -120,
    margin: 2, 
    maxWidth: 300
  },
  questionText: {
    color: '#fff',
  }
});
