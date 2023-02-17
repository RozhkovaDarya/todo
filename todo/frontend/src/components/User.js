import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.email}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>
    )
}


const UserList = ({user}) => {
    return (
        <table>
            <th>
                Email
            </th>
            <th>
                First_name
            </th>
            <th>
                Last_name
            </th>
            <th>
                Birthday_year
            </th>
            {user.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList
