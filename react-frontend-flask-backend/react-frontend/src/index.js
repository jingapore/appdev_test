import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import ReactDOM from 'react-dom';
import axios from "axios";

class Create extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bookID: "",
            bookTitle: "",
            bookAuthor: ""
        };
    }

    handleInputChange = e => {
        this.setState({
            [e.target.name]: e.target.value, //e.target.name should be an item. but why is it in square brackets? because that is used to indicate that a variable is passed, and to use the variable's value as the key
        });
    };

    handleSubmit = e => {
        e.preventDefault();
        const { bookID, bookTitle, bookAuthor } = this.state; //{} represent destructuring assignment
        const book = {
            bookID,
            bookTitle,
            bookAuthor,
        };

        axios
            .post("http://localhost:5000/api/create", book)
            .then((response) => {console.log("Book Created"); console.log(response);})
            .catch(err => {
                console.error(err);
            });
    };
    render() {
        if (this.state.hasCreatedBook) {
            return <Redirect to = "http://localhost:5000/hello"/>;
        }
        return (
            <div>
                <br />
                <div className="container">
                    <form onSubmit={this.handleSubmit}>
                        <div style={{ width: "30%" }} className="form-group">
                            <input
                                type="text"
                                className="form-control"
                                name="bookID"
                                placeholder="Book ID"
                                onChange={this.handleInputChange}
                            />
                        </div>
                        <br />
                        <div stype={{ width: "30%" }} className="form-group">
                            <input
                                type="text"
                                className="form-control"
                                name="bookTitle"
                                placeholder="Book Title"
                                onChange={this.handleInputChange}
                            />
                        </div>
                        <br />
                        <div type={{ width: "30%" }} className="form-group">
                            <input
                                type="text"
                                className="form-control"
                                name="bookAuthor"
                                placeholder="Book Author"
                                onChange={this.handleInputChange}
                            />
                        </div>
                        <br />
                        <div style={{ width: "30%" }}>
                            <button className="btn btn-success" type="submit">
                                Create
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

ReactDOM.render(

    <Create />, 
    document.getElementById('root')
);
