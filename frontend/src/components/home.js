import React, { Component } from "react";


class Home extends Component {
    render(){
        return(
        <div className="h-screen bg-gradient-to-r from-green-400 to-blue-500 flex flex-col">
            <div className="px-16 py-20 mt-12 ml-auto mr-auto
            text-3xl cursor-text font-serif text-left align-text-bottom  
            rounded-2xl shadow-2xl w-4/6 h-auto border-4 border-collapse
            border-gray-500 bg-green-50">
                <h1 className="text-center text-4xl -mt-9 mb-16">Welcome to your site!</h1>
                <div className="mt-4">
                    This website is a social media site. If you are intrested to learn more about the
                    constructor or contact with managers <a className="underline" href="/about_us">Click Here</a>.
                </div>
                <div className="mt-4">
                    If you want to know more, how this site has been created please check out my github
                    channel right now if you like it make sure you followed my github channel.
                </div>
                <div className="mt-4">
                    If you have a suggestions or a stick share with us by mailbox and help us
                    to make this site more comfortable and better.
                </div>
                <div className="mt-4">
                    Befor creating your account, I'll be glad if you read the <a href="/terms" className="underline">Terms and Privacy</a>.
                </div>
                <div className="mt-4">
                    If you have created an account please login to your
                account or if you don't have, create your special account now!
                </div>
                <div className="mt-4 mb-8">
                    I hope you'll enjoy this site, have a nice moment!
                </div>
                <hr />
                <div className="-mb-10">
                    <button className="mt-9 text-2xl p-3 mr-4 rounded-xl border-none animate-bounce hover:shadow-2xl
                    hover:bg-green-500 bg-blue-400"><a href="/register">Create your account</a></button>
                    <button className="mt-9 text-2xl p-3 ml-24 rounded-xl border-none animate-bounce hover:shadow-2xl
                    hover:bg-green-500 bg-blue-400"><a href="/login">Login</a></button>
                    <button className="mt-9 text-2xl p-3 ml-24 rounded-xl border-none animate-bounce hover:shadow-2xl
                    hover:bg-green-500 bg-blue-400"><a href="/mailbox">Mailbox</a></button>
                    <button className="mt-9 text-2xl p-3 ml-24 rounded-xl border-none animate-bounce hover:shadow-2xl
                    hover:bg-green-500 bg-blue-400"><a href="https://github.com/mousavi-lg">My github channel</a></button>
                </div>
            </div>
        </div>
        );
    }
}


export default Home;