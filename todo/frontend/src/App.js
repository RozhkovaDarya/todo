import React from 'react'
import UserList from './components/User.js'
import NotesList from './components/Notes.js'
import UserNotes from './components/UserNotes.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import axios from 'axios'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie'


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
      'notes': [],
      'token': ''
    }
  }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token})
  }
  
  is_authenticated() {
    return this.state.token != ''
  }
  
  logout() {
    this.set_token('')
  }
  
  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token})
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }
  
  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
  if (this.is_authenticated())
    {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }
  
  load_data() {
    
    const headers = this.get_headers()
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
      this.get_token_from_storage()
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
              {
                this.is_authenticated() ? 
                <button onClick={()=>this.logout()}>Logout</button> : 
                <Link to='/login'>Login</Link>
              }
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
            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
          </Switch>          
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
