import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


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
                this.notifyBackendToCompleteTask();
            });            
        })      
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;
        return (
            <form name="mturk_form" method="post" id="mturk_form" action={this.state.mturk.end_point}>
                <input type="hidden" value={this.state.mturk.assignment_id} name="assignmentId" id={this.state.mturk.assignment_id}/>
                <input type="hidden" value='foo' name="bar"/>
                <input type="hidden" value={this.state.mturk.end_point} name = "end_point"/>
                <Button type="submit" variant="contained" color="primary">Click here to finish task</Button>
            </form>
        );     
    }

    notifyBackendToCompleteTask = () => {        
        const url = window.location.href.split('?')[0]; 
        axios.post(url+ "/update",
        Object.assign({}, this.state, {instruction: 'mark_complete', complete: true})).then(res => {            
            this.setState(res.data);            
        })
    }
}


export default SubmitMTurk;