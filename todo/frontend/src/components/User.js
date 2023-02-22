import React from 'react'


const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
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
