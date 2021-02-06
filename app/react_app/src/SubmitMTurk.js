import React from 'react';
import axios from 'axios';


class SubmitMTurk extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        this.setState({complete: false});
        const url = window.location.href;            
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
                this.submitTask();
            });            
        })      
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;        
        if (this.state.complete == true) {
            return <p>Submitting your task, please be patient...</p>;        
        }else{
            return <p>Task Complete!</p>;
        }        
    }    

    submitTask = () => {
        if (this.state.pipeline == undefined) {console.log("Error submitting task!"); return;}

        axios.post(this.state.mturk.sandbox_end_point, {assignmentId: this.state.mturk.assignment_id, foo: 'bar'}).then(res => {
            this.setState({complete: true});
            console.log(res);
            this.notifyBackendToCompleteTask();
        }).catch( (error) => {
            // handle error
            console.log(error);
        });

        axios.post(this.state.mturk.production_end_point, {assignmentId: this.state.mturk.assignment_id, foo: 'bar'}).then(res => {            
            console.log(res);
            this.setState({complete: true});
            this.notifyBackendToCompleteTask();
        }).catch( (error) => {
            // handle error
            console.log(error);
        });
    }

    notifyBackendToCompleteTask = () => {
        console.log("trying to notify backend");
        const url = window.location.href;            
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'mark_complete'})).then(res => {            
            this.setState(res.data);            
        })
    }
}


export default SubmitMTurk;