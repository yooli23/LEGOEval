This chatbot is built using react-chatbot-kit.

It consists of three components, a config, a message parser, and an action provider.

The config allows one to set "initialMessages" as well as other properties of the bot.

The message parser controls what happens when the user sends a message.
One can implement the "parse()" method to perform actions on the message received from the user.
Currently, this method will pass the user message as well as the entire dialogue history to the "respond" method of the action provider and thus invoke a bot response. 

The action provider is in charge of what actions the bot is going to perform.
Within the constructor, the action provider is given the createChatBotMessage to generate a response and createClientMessage to mimic a user's input in the chat box.

For more information on react-chatbot-kit, please refer to https://fredrikoseberg.github.io/react-chatbot-kit-docs/