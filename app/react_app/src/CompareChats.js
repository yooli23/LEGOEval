import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


/*
Initial:
- an identifer
- chatbotA
- chatbotB
- text

Set:
- compare_bot_a
- compare_bot_b

inst:
- load_comparison
*/


class MessageList extends React.Component {
    render() {
      return (      
          <div className="message-list" style={{width: 500}}>                 
              {this.props.messages.map(message => {
                  return (
                    <div class="bubbleWrapper">
                      <div class={"bot_a" == message.senderId ? "inlineContainer own" : "inlineContainer"}>
                        <div className={"bot_a" != message.senderId ?"otherBubble other" : "ownBubble own"}>{message.text}</div>
                      </div>
                    </div>
                  )
                })
              }
        </div>
      )
    }
  }


class CompareChats extends React.Component {

    constructor(props) {
      super(props);
      this.state = {compare_bot_a: [], compare_bot_b: [], compare_bot_preference: ""}; 
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0]; 
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
                axios.post(url+ "/update", Object.assign({}, this.state, {instruction: 'load_comparison'})).then(result => {            
                    this.setState(result.data);     
                });
            });
        })      
    }

    render() {
      if (this.state.pipeline == undefined) return <p>Loading...</p>;      
      const data = this.state.pipeline[0].data;
      return (
        <div>
            <p style = {{marginBottom: 20}}>{data.text}</p>
        
            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'row'}}>
                <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'column'}}>            
                    <MessageList messages={this.state.compare_bot_a} />
                    {this.props.showButtons ? <Button onClick={this.chooseConvoA} variant="contained" color="primary">Choose This Conversation</Button> : null}
                </div>

                <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'column'}}>            
                    <MessageList messages={this.state.compare_bot_b} />                    
                    {this.props.showButtons ? <Button onClick={this.chooseConvoB} variant="contained" color="primary">Choose This Conversation</Button> : null}
                </div>
            </div>
        </div>
      );
    }   
    
    chooseConvoA = () => {
        const data = this.state.pipeline[0].data;
        this.setState({compare_bot_preference: data.chatbotA}, function() {
            this.popComponent();
        });
    }

    chooseConvoB = () => {
        const data = this.state.pipeline[0].data;
        this.setState({compare_bot_preference: data.chatbotB}, function() {
            this.popComponent();
        });
    }    

    popComponent = () => {    
        var title = this.state.pipeline[0].data.identifier;
        var updateVal = {};
        updateVal[title] = this.state.compare_bot_preference;
        updateVal['instruction'] = 'advance';
        const url = window.location.href.split('?')[0];
        axios.post(url+ "/update", Object.assign({}, this.state, updateVal)).then(res => {        
          this.setState(res.data, function() { 
                this.props.advance();
            });
        })
    }
}


export default CompareChats;