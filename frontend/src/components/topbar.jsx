import "../css/topbar.css";

import {
    Search,
    Bell,
    MoonStar,
    Sparkles,
    UserCircle2
} from "lucide-react";

function Topbar() {

    return (

        <header className="topbar">

            <div className="searchBox">

                <Search size={18} />

                <input
                    type="text"
                    placeholder="Search datasets, workspaces, AI tools..."
                />

            </div>

            <div className="topActions">

                <button className="aiButton">

                    <Sparkles size={18} />

                    AI Assistant

                </button>

                <button className="iconButton">

                    <Bell size={20}/>

                </button>

                <button className="iconButton">

                    <MoonStar size={20}/>

                </button>

                <div className="profile">

                    <UserCircle2 size={40}/>

                    <div>

                        <h4>Taiwo</h4>

                        <small>Premium User</small>

                    </div>

                </div>

            </div>

        </header>

    );

}

export default Topbar;