import {
    LayoutDashboard,
    Upload,
    Database,
    FolderOpen,
    Sparkles,
    BarChart3,
    History,
    Settings,
    LogOut,
    HardDrive,
    UserCircle2
} from "lucide-react";

import { NavLink } from "react-router-dom";

import "../css/sidebar.css";

function Sidebar() {

    const menu = [

        {
            name: "Dashboard",
            icon: <LayoutDashboard size={20}/>,
            path: "/dashboard"
        },

        {
            name: "Upload",
            icon: <Upload size={20}/>,
            path: "/upload"
        },

        {
            name: "Datasets",
            icon: <Database size={20}/>,
            path: "/datasets"
        },

        {
            name: "Workspace",
            icon: <FolderOpen size={20}/>,
            path: "/workspace/1"
        },

        {
            name: "Features",
            icon: <Sparkles size={20}/>,
            path: "/features"
        },

        {
            name: "Results",
            icon: <BarChart3 size={20}/>,
            path: "/results"
        },

        {
            name: "History",
            icon: <History size={20}/>,
            path: "/history"
        },

        {
            name: "Settings",
            icon: <Settings size={20}/>,
            path: "/settings"
        }

    ];

    return (

        <aside className="sidebar">

            <div>

                <div className="logo">

                    <div className="logoIcon">

                        A

                    </div>

                    <div>

                        <h2>Analyse</h2>

                        <span>AI Analytics Platform</span>

                    </div>

                </div>

                <nav>

                    {

                        menu.map((item)=>(

                            <NavLink

                                key={item.name}

                                to={item.path}

                                className={({isActive})=>

                                    isActive

                                    ?

                                    "menu active"

                                    :

                                    "menu"

                                }

                            >

                                {item.icon}

                                <span>

                                    {item.name}

                                </span>

                            </NavLink>

                        ))

                    }

                </nav>

            </div>

            <div>

                <div className="storageCard">

                    <HardDrive size={28}/>

                    <h4>

                        Storage

                    </h4>

                    <div className="progress">

                        <div className="progressFill"></div>

                    </div>

                    <small>

                        2.8 GB / 10 GB Used

                    </small>

                </div>

                <div className="profileCard">

                    <UserCircle2 size={45}/>

                    <div>

                        <h4>

                            Taiwo

                        </h4>

                        <small>

                            Premium User

                        </small>

                    </div>

                </div>

                <button className="logout">

                    <LogOut size={18}/>

                    Logout

                </button>

            </div>

        </aside>

    );

}

export default Sidebar;