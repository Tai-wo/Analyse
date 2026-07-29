import { Link } from "react-router-dom";
import {
    Upload,
    BrainCircuit,
    FolderOpen,
    BarChart3
} from "lucide-react";

import "../css/quickActions.css";

function QuickActions() {

    const actions = [

        {
            title: "Upload Dataset",
            icon: <Upload size={32} />,
            path: "/upload"
        },

        {
            title: "AI Analysis",
            icon: <BrainCircuit size={32} />,
            path: "/features"
        },

        {
            title: "Workspace",
            icon: <FolderOpen size={32} />,
            path: "/datasets"
        },

        {
            title: "Results",
            icon: <BarChart3 size={32} />,
            path: "/results"
        }

    ];

    return (

        <div className="quickGrid">

            {

                actions.map((item, index) => (

                    <Link

                        to={item.path}

                        className="quickCard"

                        key={index}

                    >

                        <div className="quickIcon">

                            {item.icon}

                        </div>

                        <h3>{item.title}</h3>

                    </Link>

                ))

            }

        </div>

    );

}

export default QuickActions;