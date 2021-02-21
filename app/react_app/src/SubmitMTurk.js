import React from 'react';
import axios from 'axios';


class SubmitMTurk extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        this.setState({complete: false});
        // const url = window.location.href;            
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
                // this.submitTask();
                this.setState({complete: true});
                this.notifyBackendToCompleteTask();
            });            
        })      
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;        
        return (
            <div>
                <form name="mturk_form" method="post" id="mturk_form" action="https://workersandbox.mturk.com/mturk/externalSubmit">
                <input type="hidden" value={this.state.mturk.assignment_id} name="assignmentId" id={this.state.mturk.assignment_id}/>
                <input type="hidden" value='foo' name="bar"/>
                <input type="submit"/>
                </form>

                <form name="mturk_form2" method="post" id="mturk_form2" action="workersandbox.mturk.com/mturk/externalSubmit">
                <input type="hidden" value={this.state.mturk.assignment_id} name="assignmentId" id={this.state.mturk.assignment_id}/>
                <input type="hidden" value='foo' name="bar"/>
                <input type="submit"/>
                </form>

                <form name="mturk_form3" method="post" id="mturk_form3" action="/mturk/externalSubmit">
                <input type="hidden" value={this.state.mturk.assignment_id} name="assignmentId" id={this.state.mturk.assignment_id}/>
                <input type="hidden" value='foo' name="bar"/>
                <input type="submit"/>
                </form>

                <form name="mturk_form4" method="post" id="mturk_form4" action="mturk/externalSubmit">
                <input type="hidden" value={this.state.mturk.assignment_id} name="assignmentId" id={this.state.mturk.assignment_id}/>
                <input type="hidden" value='foo' name="bar"/>
                <input type="submit"/>
                </form>                                

            </div>
        );     
    }   

    notifyBackendToCompleteTask = () => {
        console.log("trying to notify backend");
        // const url = window.location.href;           
        const url = window.location.href.split('?')[0]; 
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'mark_complete'})).then(res => {            
            this.setState(res.data);            
        })
    }
}


export default SubmitMTurk;