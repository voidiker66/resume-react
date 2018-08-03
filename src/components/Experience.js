import React from 'react';
import { Link } from "react-router-dom";
import Pagination from './pagination';
import {Col} from 'react-bootstrap';
import Background from './Background';

const API_URL = "http://localhost:5000/api/work/";

export default class Experience extends React.Component {

  constructor() {
    super();

    this.onChangePage = this.onChangePage.bind(this);
   
    this.state = {
        work: [],
        company: [],
        project: [],
        pageOfItems: []
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
  .then(re => {
    return re.json();
  }).then(da => {
    
    this.setState({
      company: da.objects
    })
  });
  fetch("http://localhost:5000/api/project?q={\"filters\":[{\"name\":\"project_work\",\"op\":\"eq\",\"val\":" + this.props.match.params.work_id + "}]}")
  .then(r => {
    return r.json();
  }).then(d => {
    this.setState({
      project: d.objects
    })
  }); 
}

onChangePage(pageOfItems) {
    // update state with new page of items
    this.setState({ pageOfItems: pageOfItems });
}

  render() {
    var cardStyle = {
    display: 'block',
    transitionDuration: '0.3s',
    height: '15vw',
    overflow: 'hidden'
  }
  const projectItems =this.state.pageOfItems.map(item =>
    <Link to={"/project/"+item.project_db_id}>
    <Col key ={item.project_db_id} xs={6} md={4}>

      <div className="card grid" style={cardStyle}>
        <h3 className='card-name important'><b>{item.project_name}</b></h3>
        <p className='card-name'>{item.project_languages}</p>
          <p className='card-name' dangerouslySetInnerHTML={{ __html: item.project_description}}></p>
      </div>
    </Col>
    </Link>
    );
    return (
    	<div>
      <Background/>

        <h3>{this.state.work.work_job_title}</h3>
        <p dangerouslySetInnerHTML={{ __html: this.state.work.work_description}}></p>
        {projectItems}
        <Pagination items={this.state.project} onChangePage={this.onChangePage}/>
		  </div>
    );
  }
}