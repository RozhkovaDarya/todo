import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  
  componentDidMount() {
    const users = [
      {
        'email': 'dima@mail.ru',
        'first_name': 'Dima',
        'last_name': 'Ivanov',
        'birthday_year': 1980
      },
      {
        'email': 'masha@mail.ru',
        'first_name': 'Masha',
        'last_name': 'Smirnova',
        'birthday_year': 1991
      },
      {
        'email': 'ignat@mail.ru',
        'first_name': 'Ignat',
        'last_name': 'Nosov',
        'birthday_year': 1975
      },
    ]
    this.setState(
      {
        'users': users
      }
    )
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
