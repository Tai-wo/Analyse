import MainLayout from "../layouts/MainLayout";
import "../css/workspace.css";

import {
    FolderOpen,
    BrainCircuit,
    Database,
    FileSpreadsheet,
    Sparkles,
    Play
} from "lucide-react";

function Workspace(){

    return(

        <MainLayout>

            <div className="workspace-page">

                <div className="pageHeader">

                    <h1>Workspace</h1>

                    <p>
                        Manage your current AI analysis workspace.
                    </p>

                </div>

                <div className="workspaceHero">

                    <FolderOpen size={70}/>

                    <div>

                        <h2>Sales Dashboard Workspace</h2>

                        <p>
                            Dataset connected successfully and ready for analysis.
                        </p>

                    </div>

                </div>

                <div className="workspaceGrid">

                    <div className="workspaceCard">

                        <Database size={45}/>

                        <h3>Dataset</h3>

                        <p>Sales.xlsx</p>

                    </div>

                    <div className="workspaceCard">

                        <FileSpreadsheet size={45}/>

                        <h3>Rows</h3>

                        <p>5,240</p>

                    </div>

                    <div className="workspaceCard">

                        <Sparkles size={45}/>

                        <h3>AI Status</h3>

                        <p>Ready</p>

                    </div>

                    <div className="workspaceCard">

                        <BrainCircuit size={45}/>

                        <h3>Suggestions</h3>

                        <p>12 Available</p>

                    </div>

                </div>

                <button className="workspaceButton">

                    <Play size={20}/>

                    Start AI Analysis

                </button>

            </div>

        </MainLayout>

    )

}

export default Workspace;