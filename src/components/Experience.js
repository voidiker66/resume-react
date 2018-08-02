import React from 'react';
import Background from './Background';

const API_URL = "http://localhost:5000/api/work/";

export default class Experience extends React.Component {

  constructor() {
    super();
   
    this.state = {
        work: [],
        company: [],
    };
  }

componentDidMount() {
  fetch(API_URL + this.props.match.params.work_id)
  .then(results => {
    return results.json();
  }).then(data=> {
    this.setState({
      work: data
  })
    });
  fetch("http://localhost:5000/api/company")
  .then(r => {
    return r.json();
  }).then(d => {
    
    this.setState({
      company: d.objects
    })
  });
}

  render() {
    return (
    	<div>
      <Background/>
        <h1>{this.state.company.map((c, index) => {
          if (c.company_db_id === this.state.work.work_company) {
            this.state.company = c;
            return c.company_name;
          }
        })}</h1>
        <h3>{this.state.work.work_job_title}</h3>
        <p dangerouslySetInnerHTML={{ __html: this.state.work.work_description}}></p>
		  </div>
    );
  }
}