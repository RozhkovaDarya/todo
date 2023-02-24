import React from 'react'
import {Link} from 'react-router-dom'


const UserItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`user/${item.id}`}>{item.id}</Link></td>
            <td>{item.name}</td>
            <td>{item.birthday_year}</td>
        </tr>
    )
}
    

const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>BIRTHDAY_YEAR</th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}


export default UserList
