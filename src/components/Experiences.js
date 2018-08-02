import React from 'react';
import { Link } from "react-router-dom";
import Pagination from './pagination';
import {Col} from 'react-bootstrap';
// import ParkSuggestions from "./ParkSuggestions";
import Background from './Background';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';

//<ParkSuggestions results={this.state.parks} />

const API_URL = "http://localhost:5000/api/work";

export default class Experiences extends React.Component{   

  constructor() {
    super();
    //button click for each item
    this.handleClick = this.handleClick.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
    this.toggle = this.toggle.bind(this);
    this.select = this.select.bind(this);

      // an example array of 30 items to be paged
    
    this.state = {
        work: [],
        allWork: [],
        company: [],
        pageOfItems: [],
        dropdownOpen: false,
        sortValue: 1,
        sortText: "Database ID Asc"
    };
    
    // bind function in constructor instead of render 
    this.onChangePage = this.onChangePage.bind(this);
}
componentDidMount() {
  fetch(API_URL)
  .then(results => {
    return results.json();
  }).then(data=> {
    this.setState({
      allWork: data.objects,
      work: data.objects
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
  console.log(this.state.company);
}

toggle() {
    this.setState(prevState => ({
      dropdownOpen: !prevState.dropdownOpen
    }));
  }

async sortResults() {
  function byNameAsc(a, b) {
    return a.work_company > b.work_company;
  }
  function byNameDesc(a, b) {
    return a.work_company < b.work_company;
  }

  console.log(this.state.sortValue);
  var obj = [...this.state.work];

  if (this.state.sortValue === 1) {
    await obj.sort(byNameAsc);
  }
  else if (this.state.sortValue === 2) {
    await obj.sort(byNameDesc);
  }
  else {
    await obj.sort(byNameAsc);
  }
  this.state.work = obj;
}

//handle button click 
handleClick() {
  this.setState(prevState => ({
    isToggleOn: !prevState.isToggleOn
  }));
}


  handleKeyPress(event) {
  if(event.key === 'Enter'){
    this.setState({
      query: this.search.value
    });
    this.getInfo()
  }
  else {
    this.setState({
      query: this.search.value
    }, () => {
      if (this.state.query && this.state.query.length > 1) {
        // this.showDropdown()
        if (this.state.query.length % 2 === 0) {
          this.getInfo()
        }
      } else if (!this.state.query) {
        // this.hideDropdown()
      }
    });
  }
}

async select(event) {
  console.log(event.target.innerText);
  console.log(event.target.value);
  await this.setState({
    dropdownOpen: !this.state.dropdownOpen,
    sortValue: parseInt(event.target.value, 10),
    sortText: event.target.innerText
  });
  await this.sortResults();
  await this.handleClick();
  this.toggle();
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
  const project =this.state.pageOfItems.map(item =>
    <Link to={"/work/"+item.work_db_id}>
    <Col key ={item.work_db_id} xs={6} md={4}>

      <div className="card grid" style={cardStyle}>
        <h3 className='experience-card card-name important'>{this.state.company.map((c, index) => {
          if (c.company_db_id === item.work_company) {
            return (c.company_name);
          }
        })}</h3>
        <p className='card-name'>{item.work_job_title}</p>
        <span className='card-name'>{item.work_start}{item.work_end ? ' - ' + item.work_end : ''}</span>
      </div>
    </Col>
    </Link>
    );
    return (
        <div>
        <Background/>
      <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggle} onChange={this.handleChange} value={this.sortValue}>
        <DropdownToggle caret>
          Filter ({this.state.sortText})
        </DropdownToggle> 
        <DropdownMenu>
          <DropdownItem value="1" onClick={this.select}>Database ID Asc</DropdownItem>
          <DropdownItem divider />
          <DropdownItem value="2" onClick={this.select}>Database ID Desc</DropdownItem>
          <DropdownItem divider />
        </DropdownMenu>
      </Dropdown>
            <div className="container">
                <div className="text-center">
                    <h1 id='events'>Work Experience</h1>
                    {project}
                    <Pagination items={this.state.work} onChangePage={this.onChangePage}/>
                </div>
            </div>
            <hr />
        </div>
    );
}

}



  