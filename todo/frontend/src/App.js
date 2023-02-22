import React from 'react'
import UserList from './components/User.js'
import NotesList from './components/Notes.js'
import {HashRouter, Route, Link} from 'react-router-dom'


class App extends React.Component {
  constructor(props) {
    super(props)
    const user1 = {id: 1, name: 'Петр', birthday_year: 1980}
    const user2 = {id: 2, name: 'Марина', birthday_year: 1999}
    const users = [user1, user2]
    const notes1 = {id: 1, name: 'Алые паруса', author: user1}
    const notes2 = {id: 2, name: 'Золотая цепь', author: user2}
    const notes3 = {id: 3, name: 'Пиковая дама', author: user2}
    const notes4 = {id: 4, name: 'Руслан и Людмила', author: user2}
    const notes = [notes1, notes2, notes3, notes4]
    this.state = {
      'user': users,
      'notes': notes
    }
  }
  
  render() {
    return (
      <div className="App">
        <HashRouter>
        <nav>
          <ul>
            <li>
              <Link to='/'>Users</Link>
            </li>
            <li>
              <Link to='/books'>Notes</Link>
            </li>
          </ul>
        </nav>
          <Route exact path='/' component={() => <UserList items={this.state.user} />} />
          <Route exact path='/notes' component={() => <NotesList items={this.state.notes} />} />
        </HashRouter>
      </div>
    )
  }
}

export default App;
