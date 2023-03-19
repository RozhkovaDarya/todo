import React from 'react'


const NotesItem = ({item, deleteNotes}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.name}</td>
            <td><button onClick={()=>deleteNotes(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const NotesList = ({items, deleteNotes}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUHTOR</th>
                <th></th>
            </tr>
            {items.map((item) => <NotesItem item={item} deleteNotes={deleteNotes} />)}
        </table>
    )
}


export default NotesList
