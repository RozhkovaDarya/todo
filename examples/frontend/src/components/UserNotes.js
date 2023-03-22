import React from 'react'
import { useParams } from 'react-router-dom'


const NotesItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.user.name}</td>
        </tr>
    )
}


const NotesList = ({items}) => {
    
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.user.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>USER</th>
            </tr>
            {filtered_items.map((item) => <NotesItem item={item} />)}
        </table>
    )
}

export default NotesList
