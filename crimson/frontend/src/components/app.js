// import React, { Component } from "react";
// import { render } from "react-dom";

// export default class App extends Component {
//     constructor(props) {
//         super(props);
//     }
//     render() {
//         return (<h1>Testing React Code</h1>)
//     }
// }

// const appDiv = document.getElementById("app");
// render(<App/>, appDiv);

import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage.js";

export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <HomePage />
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);