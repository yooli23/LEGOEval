// ActionProvider starter code
class ActionProvider {
  constructor(createChatBotMessage, setStateFunc, createClientMessage) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
    this.createClientMessage = createClientMessage;
  }

  /**
   *
   * @param messageIn is the user input message
   * @param chatHistory is an array of objects recording the entire chat history. Each object
   *        has an attribute "message" storing user's input/ bot's response and "type" for identity
   *        as either bot or user. The elements with odd indices belong to the bot, while those with
   *        even indices belong to the user.
   */

  respond = (messageIn, chatHistory) => {
    console.log(chatHistory);
    // TODO: Chatbot simply repeats user's input now for test purpose
    const messageOut = messageIn;
    const response = this.createChatBotMessage(messageOut);
    this.updateChatbotState(response);
  };

  /**
   * This method updates the chat history
   */
  updateChatbotState = (message) => {
    this.setState((prevState) => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  };

}

export default ActionProvider;
