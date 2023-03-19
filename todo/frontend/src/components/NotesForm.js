import React from 'react'


class NotesForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', user: props.user[0].id}
    }
    
    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    
    handleSubmit(event) {
        this.props.createNotes(this.state.name, this.state.user)
        event.preventDefault()
    }
    
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="login">name</label>
                    <input type="text" className="form-control" name="name"
                        value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>
            
            <div className="form-group">
                <label for="author">user</label>
                
                <select name="author" className='form-control' onChange={(event)=>this.handleChange(event)}>
                    {this.props.users.map((item)=><option value={item.id}>{item.name}</option>)}
                </select>
            
            </div>
            <input type="submit" className="btn btn-primary" value="Save" />
        </form>
        );
    }
}

export default NotesForm
