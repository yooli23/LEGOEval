import React from 'react';
import axios from 'axios';

import * as Surveys from "survey-react";
import "survey-react/modern.css";
import "./Survey.css";

class Survey extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data);
        })
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;
        const data = this.state.pipeline[0].data;
        let json = {};
        if (data.hasOwnProperty("questions")) {
            json = {title: data.title, showProgressBar: "top", questions: []}
            for (var i = 0; i < data.questions.length; i++) {
                json.questions.push(this.parseQuestion(JSON.parse(data.questions[i])));
            }
        }
        Surveys.StylesManager.applyTheme("modern");
        let model = new Surveys.Model(json);
        return (
          <Surveys.Survey model={model} onUpdateQuestionCssClasses={this.customizeTheme} onComplete={this.popComponent}/>
        );
    }

    parseQuestion(question) {
        let parsed;
        switch (question["type"]){
            case "radiogroup":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], colCount: question["colCount"],
                        choices: question["choices"]};
                break;
            case "checkbox":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], colCount: question["colCount"],
                        hasNone: question["hasNone"], choices: question["choices"]};
                break;
            case "text":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], placeHolder: question["placeHolder"],
                        autoComplete: question["autoComplete"]};
                break;
            case "rating":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        minRateDescription: question["minRateDescription"],
                        maxRateDescription: question["maxRateDescription"]};
                break;
            case "comment":
                parsed = { type: question["type"], name: question["name"], title: question["title"]};
                break;
            case "matrix":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        columns: question["columns"], rows: question["rows"]};
                break;
            default:
                parsed = {};
        }
        return parsed;
    }

    customizeTheme = (survey, options) => {
        var classes = options.cssClasses;

            classes.mainRoot += " sv_qstn";
            classes.root = "sq-root";
            classes.title += " sq-title";
            classes.item += " sq-item";

            if (options.question.isRequired) {
                classes.title += " sq-title-required";
            }

            switch (options.question.getType()) {
                case "radiogroup":
                    classes.root += " sq-root-rg";
                    break;
                case "checkbox":
                    classes.root += " sq-root-cb";
                    break;
                case "text":
                    classes.root += " sq-root-text";
                    break;
                case "rating":
                    classes.root += " sq-root-rating";
                    break;
                case "comment":
                    classes.root += " sq-root-comment";
                    break;
                case "matrix":
                    classes.root += " sq-root-matrix";
                    break;
                default:
            }
    }

    popComponent = (survey, options) => {
        const url = window.location.href.split('?')[0];

        const data = this.state.pipeline[0].data;

        var surveyTitleStr = data.title;
        var surveyData = JSON.stringify(survey.data);

        var updateVal = {};
        updateVal['instruction'] = 'advance';
        updateVal[surveyTitleStr] = surveyData;

        axios.post(url+ "/update", Object.assign({}, this.state, updateVal)).then(res => {
            if(this.props._callBackFun){
                this.props._callBackFun(res);
            }
            this.setState(res.data);
            this.props.advance();
        })
        window.scrollTo(0,0)
    }

}

export default Survey;