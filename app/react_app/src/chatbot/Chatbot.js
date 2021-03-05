import React from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import '../App.css';


class MessageList extends React.Component {
  render() {
    return (      
        <div className="message-list" style={{width: 500}}>                 
            {this.props.messages.map(message => {
                return (
                  <div class="bubbleWrapper">
                    <div class={"You" == message.senderId ? "inlineContainer own" : "inlineContainer"}>
                      <div className={"You" != message.senderId ?"otherBubble other" : "ownBubble own"}>{message.text}</div>
                    </div>
                    <span className={"You" != message.senderId ?"other" : "own"}>{message.senderId}</span>
                  </div>
                )
              })
            }
      </div>
    )
  }
}


class MyChatbot extends React.Component{

    constructor(props) {
      super(props);
      this.state = {messages: [], text: ""};      
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0];
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
          <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'column'}}>
            <p style = {{marginBottom: 20}}>Please send messages until the task will automatically end.</p>
              <MessageList messages={this.state.messages} />
              <input type="text" placeholder="Type message here..." value={this.state.text} onChange={this.textChanged} style={{marginTop: 40}} />
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
      data.push(
        {id: this.state.messages.length, senderId: "You", text: this.state.text}
      );

      this.setState({messages: data, text: ""}, function() {

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