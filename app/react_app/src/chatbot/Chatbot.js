import React from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import '../App.css';


class MessageList extends React.Component {

  componentDidMount() {
    this.scrollToBottom();
  }

  componentDidUpdate() {
    this.scrollToBottom();
  }

  scrollToBottom() {
    this.el.scrollIntoView({ behavior: 'smooth' });
  }

  render() {
    return (      
        <div className="message-list" style={{width: 500, height: '50vh', overflow: 'scroll'}}>                 
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
            <div ref={el => { this.el = el; }} />
        </div>
    )
  }
}


class MyChatbot extends React.Component{

    constructor(props) {
      super(props);
      this.state = {messages: [], text: "", pause_ui: false};      
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {

              // Force send first message
              if (this.state.messages.length == 0) {
                const data = this.state.pipeline[0].data;
                this.setState({text: data['force_human_message']}, function() {
                  this.sendMessage();
                });
              }

            });
        });
    }

    render() {
        if (this.state.pipeline === undefined) return <p>Loading...</p>;
        const data = this.state.pipeline[0].data;
        console.log(data['force_human_message']);
        return (
          <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'column'}}>            
              <p style = {{marginBottom: 20}}>Chat Window</p>
              <MessageList messages={this.state.messages} />
              <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', flexDirection: 'row'}}>
                <TextField id="outlined-basic" placeholder="Type message here..." label="Type message here..." value={this.state.text} onChange={this.textChanged} style={{marginTop: 40, width: 390}} />
                <Button onClick={this.sendMessage} variant="contained" color="primary" style={{marginTop: 40, marginLeft: 15}}>Send</Button>               
              </div>
              <p style = {{marginTop: 40, color: '#b8b8b8'}}>{data['instruction']}</p>
            </div>
          );
    }

    textChanged = (e) => {
      this.setState({ text: e.target.value });
    }

    sendMessage = () => {

      console.log(this.state.text);

      if (this.state.pause_ui == true || this.state.text.length < 2) return;

      //TODO: disable UI
      this.setState({'pause_ui': true})

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
          this.setState({'pause_ui': false})
        })

      }); 
    }

    popComponent = (chatbot, options) => {
      this.props.advance();
    }
}

export default MyChatbot;