// MessageParser starter code
class MessageParser {
  constructor(actionProvider, state) {
    this.actionProvider = actionProvider;
    this.state = state;
  }

  parse(message) {
    // Feel free to preprocess input message here
    this.actionProvider.respond(message, this.state.messages);
  }
}

export default MessageParser;