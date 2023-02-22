import React from 'react'


const NotesItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.name}</td>
        </tr>
    )
}


const NotesList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUHTOR</th>
            </tr>
            {items.map((item) => <NotesItem item={item} />)}
        </table>
    )
}


export default NotesList
