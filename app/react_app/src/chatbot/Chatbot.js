import React from "react";
import Chatbot from "react-chatbot-kit";

import config from "./chatbotConfig";
import MessageParser from "./MessageParser";
// import ActionProvider from "./ActionProvider";
import axios from "axios";
import Button from "@material-ui/core/Button";




class MessageList extends React.Component {
  render() {
    return (
      <ul className="message-list">                 
        {this.props.messages.map(message => {
          return (
           <li key={message.id}>
             <div>
               {message.senderId}
             </div>
             <div>
               {message.text}
             </div>
           </li>
         )
       })}
     </ul>
    )
  }
}





class MyChatbot extends React.Component{

    constructor(props) {
      super(props);
      this.state = {messages: [], text: ""};      
    }

    componentDidMount() {
        const url = window.location.href;
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
              // pass
            });         
        })
    }

    render() {
        if (this.state.pipeline === undefined) return <p>Loading...</p>;
        const data = this.state.pipeline[0].data;
        return (
            <div>
              <MessageList messages={this.state.messages} />
              <input type="text" placeholder="add a new todo..." value={this.state.text} onChange={this.textChanged} />
              <Button onClick={this.sendMessage}>Send</Button> 
            </div>
          );
    }

    textChanged = (e) => {
      this.setState({ text: e.target.value });
    }

    sendMessage = () => {

      //TODO: disable UI

      // Update the user's message
      var data = this.state.messages;
      data.push({id: this.state.messages.length, senderId: "You", text: this.state.text});
      this.setState({messages: data}, function() {

        // Send to backend, update data
        var title = this.state.pipeline[0].data.identifier;
        var updateVal = {};
        updateVal[title] = this.state.messages;
        updateVal['instruction'] = 'request_message';
        const url = window.location.href.split('?')[0];
        axios.post(url+ "/update", Object.assign({}, this.state, updateVal)).then(res => {        
          this.setState(res.data, function() { this.popComponent(); });

          //TODO: enable UI
        })

      }); 
    }

    popComponent = (chatbot, options) => {
      this.props.advance();
    }
}

export default MyChatbot;