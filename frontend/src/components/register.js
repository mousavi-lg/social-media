import React, { Component } from "react";


class Register extends Component {
    constructor(props){
        super(props)
        this.state = {
            username:"",
            password:"",
            re_password:"",
            email:""
        }
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    async postdata(username, password, re_password, email){
        let result = await fetch(
            'http://localhost:8000/api/auth/register',
            {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(
                    {
                        "username":username,
                        "password":password,
                        "re_password":re_password,
                        "email":email
                    }
                )
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


    handleSubmit(event){
        this.postdata(this.state.username, this.state.password, this.state.re_password, this.state.email)
        event.preventDefualt()
        this.setState(
            {
                username : "",
                password : "",
                re_password : "",
                email : ""
            }
        )
    }
    render(){
        return(
            <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-yellow-500 via-red-500 to-pink-500">
                <div className="bg-white p-16 rounded-xl shadow-2xl w-2/3 border-4 border-collapse border-gray-500">
                    <h2 className="text-3xl font-bold font-serif mb-10 text-red-900">Create Your Account</h2>
                    <div className="space-y-5">
                        <div>
                            <label className="block mb-2 font-bold font-serif text-red-900">Username</label>
                            <input 
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-yellow-300"
                                type="text"
                                name="username"
                                placeholder="username"
                                value={this.state.name}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div>
                            <label className="block mb-1 font-bold font-serif text-red-900">Password</label>
                            <input 
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-yellow-500"
                                type="password"
                                name="password"
                                placeholder="password"
                                value={this.state.name}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div>
                            <label className="block mb-1 font-bold font-serif text-red-900">Enter password again</label>
                            <input 
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-pink-400"
                                type="password"
                                name="re_password"
                                placeholder="re_password"
                                value={this.state.name}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div>
                            <label className="block mb-1 font-bold font-serif text-red-900">Email</label>
                            <input 
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-pink-600"
                                type="email"
                                name="email"
                                placeholder="email"
                                value={this.state.name}
                                onChange={this.handleChange}
                            />
                        </div>
                        <div>
                            <label className="block mb-1 font-bold font-serif text-red-900">Phone number</label>
                            <input 
                                className="w-full border-2 border-gray-300 p-3 rounded outline-none focus:border-red-700"
                                type="tel"
                                name="phone-number"
                                placeholder="Phone number" 
                            />
                        </div>
                        <div className="flex items-center">
                            <input 
                                className="w-4 h-5"
                                type="checkbox"
                            />
                            <label className="ml-3 font-serif text-red-900 text-lg">I agree with <a href="/terms" className="font-extrabold underline">terms and privacy</a>.</label>
                        </div>
                        <button
                            className="block w-full p-4 text-2xl font-sans rounded text-black bg-gradient-to-r from-yellow-400 to-pink-500 hover:from-green-700 hover:to-blue-500"
                            onClick={this.handleSubmit}
                        >
                            Sign Up
                        </button>
                    </div>
                </div>
            </div>
        );
    }
}

export default Register;