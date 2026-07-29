import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    Mail,
    Lock,
    ArrowRight,
    BrainCircuit,
    Database,
    FileSpreadsheet,
    BarChart3
} from "lucide-react";

import "../css/login.css";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = (e) => {

        e.preventDefault();

        navigate("/dashboard");

    };

    return (

        <div className="loginPage">

            <div className="loginBlob loginBlob1"></div>
            <div className="loginBlob loginBlob2"></div>
            <div className="loginBlob loginBlob3"></div>

            <div className="loginLeft">

                <div className="loginBrand">

                    <div className="loginLogo">

                        A

                    </div>

                    <div>

                        <h1>Analyse</h1>

                        <span>

                            AI Powered Analytics Platform

                        </span>

                    </div>

                </div>

                <div className="loginHero">

                    <h2>

                        Transform your spreadsheets into intelligent insights.

                    </h2>

                    <p>

                        Upload Excel or CSV files and let AI clean,
                        analyze, visualize and generate reports automatically.

                    </p>

                </div>

                <div className="loginFeatures">

                    <div className="loginFeature">

                        <FileSpreadsheet size={22}/>

                        <span>Excel Intelligence</span>

                    </div>

                    <div className="loginFeature">

                        <Database size={22}/>

                        <span>SQL Generator</span>

                    </div>

                    <div className="loginFeature">

                        <BrainCircuit size={22}/>

                        <span>Python AI Analysis</span>

                    </div>

                    <div className="loginFeature">

                        <BarChart3 size={22}/>

                        <span>Tableau Dashboard Builder</span>

                    </div>

                </div>

            </div>

            <div className="loginRight">

                <form
                    className="loginCard"
                    onSubmit={handleLogin}
                >

                    <h2>

                        Welcome Back 👋

                    </h2>

                    <p>

                        Sign in to continue to Analyse.

                    </p>

                    <div className="loginInput">

                        <Mail size={20}/>

                        <input

                            type="email"

                            placeholder="Email Address"

                            value={email}

                            onChange={(e)=>setEmail(e.target.value)}

                            required

                        />

                    </div>

                    <div className="loginInput">

                        <Lock size={20}/>

                        <input

                            type="password"

                            placeholder="Password"

                            value={password}

                            onChange={(e)=>setPassword(e.target.value)}

                            required

                        />

                    </div>

                    <div className="loginOptions">

                        <label>

                            <input type="checkbox"/>

                            Remember Me

                        </label>

                        <a href="#">

                            Forgot Password?

                        </a>

                    </div>

                    <button
                        type="submit"
                        className="loginButton"
                    >

                        Login

                        <ArrowRight size={18}/>

                    </button>

                    <div className="loginDivider">

                        OR

                    </div>

                    <button
                        type="button"
                        className="googleButton"
                    >

                        Continue with Google

                    </button>

                </form>

            </div>

        </div>

    );

}

export default Login;