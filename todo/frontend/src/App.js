import React from 'react'
import UserList from './components/User.js'
import NotesList from './components/Notes.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import axios from 'axios'
import LoginForm from './components/Auth.js'


const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'user': [],
      'notes': []
    }
  }

  load_data() {
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        this.setState({users: response.data})
      }).catch(error => console.log(error))
    
    axios.get('http://127.0.0.1:8000/api/notes/')
      .then(response => {
        this.setState({notes: response.data})
      }).catch(error => console.log(error))
    }
    
    componentDidMount() {
      this.load_data()
    }

  render() {
    return (
      <div className="App">
        <BrowserRouter>
        <nav>
          <ul>
            <li>
              <Link to='/'>Users</Link>
            </li>
            <li>
              <Link to='/notes'>Notes</Link>
            </li>
            <li>
              <Link to='/login'>Login</Link>
            </li>
          </ul>
        </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList items={this.state.user} />} />
            <Route exact path='/notes' component={() => <NotesList items={this.state.notes} />} />
            <Route path="/user/:id">
              <UserList items={this.state.notes} />
            </Route>
            <Redirect from='/users' to='/' />
            <Route component={NotFound404} />
          </Switch>          
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
