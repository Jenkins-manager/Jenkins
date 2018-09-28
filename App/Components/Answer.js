import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';


class Answer extends Component {
  render() {
    return(
      <View style={styles.answerBox}>
          {/* <Text style={styles.answerBox}>There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..</Text> */}
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
    // left: -20,
    margin: 3,
    position: 'relative',
    
  }
});