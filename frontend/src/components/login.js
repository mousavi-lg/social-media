import React, { Component } from "react";
import axios from "axios";
import swal from "sweetalert";


class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: ""
        }
        this.Submit = this.Submit.bind(this)
    }
    Submit() {
        axios.post('http://127.0.0.1:8000/api/auth/login/', {
            username : this.state.username,
            password : this.state.password
        })
        .catch(function (error) {
            if (error.response) {
                swal({
                    text: error.response.data.message,
                    icon: "error"
                });
            }
        })
        .then(
            function(response) {
                if (response) {
                    swal({
                        text: response.data.message,
                        icon: "success"
                    })
                    .then((value) => {
                        window.location = "/"
                    })
                }
            }
        )
    }

    handleChange = (event) => {
        const target = event.target
        const value = target.value
        const name = target.name
        this.setState(
            {
                [name]:value
            }
        )
    }

    render() {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-green-500 via-indigo-300 to-green-500">
                <div className="bg-white p-16 rounded-xl shadow-2xl w-2/3 border-4 border-collapse border-gray-500">
                    <h2 className="text-3xl font-bold font-serif mb-10 text-purple-900">Login here</h2>
                    <div className="space-y-5">
                        <div>
                            <label className="block mb-2 font-bold font-serif text-purple-900">Username</label>
                            <input
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-blue-400"
                                type="text"
                                name="username"
                                placeholder="username"
                                value={this.state.username}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div>
                            <label className="block mb-1 font-bold font-serif text-purple-900">Password</label>
                            <input
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-purple-500"
                                type="password"
                                name="password"
                                placeholder="password"
                                value={this.state.password}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div className="flex items-center">
                            <label className="ml-1 font-serif text-purple-900 text-lg">If you don't have any account <a href="/register" className="font-extrabold underline">create an account here</a>.</label>
                        </div>
                        <button
                            className="block w-full p-4 font-semibold text-2xl font-sans rounded text-gray-800 bg-gradient-to-r from-indigo-400 via-green-500 to-indigo-400 hover:from-yellow-400 hover:to-pink-500"
                            onClick={this.Submit} 
                        >
                            Login
                        </button>
                    </div>
                </div>
            </div>
        );
    }
}


export default Login;

