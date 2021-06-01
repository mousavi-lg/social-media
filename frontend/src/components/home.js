import React from "react";


const Home = () => {
    return (
        <div className="h-screen bg-gradient-to-r from-green-400 to-blue-500 flex flex-col">
            <h1 className="text-3xl text-white text-center">Hello</h1>
            <a href="/login">
                <button className="p-3 bg-indigo-600 w-auto h-auto text-xl text-center text-black ">Login</button>
            </a>
        </div>
    );
}


export default Home;