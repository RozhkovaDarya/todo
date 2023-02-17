import React from 'react';
//import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import UserList from './components/User';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors')
      .then(response => {
        const authors = response.data
          this.setState(
          {
            'authors': authors
          }
        )
      }).catch(error => console.log(error))
  }

  render () {
    return (
      <div>
        <UserList users={this.state.users} />
      </div>
    )
  }
}

export default App;
