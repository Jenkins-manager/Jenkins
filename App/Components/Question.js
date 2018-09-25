import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';


class Question extends Component {
  render() {
    return(
      <View style={styles.questionBox}>
        {/* <Text>{this.props.question.text}</Text> */}
        <Text style={styles.questionText}>This is a question</Text>
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
    margin: 2
  },
  questionText: {
    color: '#fff',
  }
});
